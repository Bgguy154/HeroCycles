# src/app.py

from datetime import date
import sys
import json
from pricing_engine import compute_cycle_price, load_parts_data


def main():
    parts = load_parts_data("src/data/parts.json")

    if len(sys.argv) != 2:
        print(
            "Usage: python src/app.py <config.json>",
            file=sys.stderr,
        )
        print("Example input.json as shown in the assignment.")
        sys.exit(1)

    config_path = sys.argv[1]
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    query_date = date.fromisoformat(config["date"])
    part_ids = config["parts"]

    result = compute_cycle_price(parts, part_ids, query_date)

    print(f"Cycle Price Breakdown — {config['date']}")
    print("-" * 40)

    pretty_names = {
        "frame": "Frame",
        "handlebar_brakes": "Handle Bar/Brakes",
        "seating": "Seating",
        "wheels": "Wheels",
        "chain_assembly": "Chain Assembly",
    }

    for comp_key, total in result["component_breakdown"].items():
        if total > 0:
            print(f"{pretty_names[comp_key]} : ₹{total:,.0f}")

    print("-" * 40)
    print(f"TOTAL : ₹{result['total']:,.0f}")


if __name__ == "__main__":
    main()