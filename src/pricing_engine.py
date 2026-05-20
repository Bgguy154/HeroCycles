# src/pricing_engine.py

from datetime import date
from typing import List, Dict, Any
import json


def load_parts_data(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_price_for_date(
    price_history: List[Dict], query_date: date
) -> float:
    candidates = []
    for entry in price_history:
        valid_from = date.fromisoformat(entry["valid_from"])
        valid_until = (
            date.fromisoformat(entry["valid_until"])
            if entry["valid_until"]
            else None
        )

        # Check if entry covers query_date
        if valid_from <= query_date:
            if valid_until is None or query_date <= valid_until:
                candidates.append(entry)

    if not candidates:
        raise ValueError(
            f"No price found for date {query_date} in given price_history"
        )

    # Sort by valid_from descending, pick latest
    candidates.sort(
        key=lambda x: date.fromisoformat(x["valid_from"]), reverse=True
    )
    return candidates[0]["price"]


def compute_cycle_price(
    parts: List[Dict], part_ids: List[str], query_date: date
) -> Dict[str, Any]:
    part_map = {p["id"]: p for p in parts}
    component_totals = {
        "frame": 0.0,
        "handlebar_brakes": 0.0,
        "seating": 0.0,
        "wheels": 0.0,
        "chain_assembly": 0.0,
    }

    total = 0.0
    for part_id in part_ids:
        part = part_map.get(part_id)
        if not part:
            raise ValueError(f"Unknown part ID: {part_id}")

        price = find_price_for_date(part["price_history"], query_date)
        component = part["component"]
        component_totals[component] = round(
            component_totals[component] + price, 2
        )
        total += price

    return {
        "date": query_date.isoformat(),
        "parts": part_ids,
        "component_breakdown": component_totals,
        "total": round(total, 2),
    }