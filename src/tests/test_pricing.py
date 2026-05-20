# src/tests/test_pricing.py

import unittest
from datetime import date
from src.pricing_engine import find_price_for_date, compute_cycle_price


class TestPricingEngine(unittest.TestCase):
    def test_price_for_single_range(self):
        history = [
            {"valid_from": "2016-01-01", "valid_until": None, "price": 500}
        ]
        price = find_price_for_date(history, date(2016, 6, 1))
        self.assertEqual(price, 500)

    def test_price_with_end_date(self):
        history = [
            {"valid_from": "2016-01-01", "valid_until": "2016-11-30", "price": 500},
            {"valid_from": "2016-12-01", "valid_until": None, "price": 530},
        ]
        price = find_price_for_date(history, date(2016, 12, 15))
        self.assertEqual(price, 530)

        price = find_price_for_date(history, date(2016, 6, 1))
        self.assertEqual(price, 500)

    def test_compute_cycle_price_example(self):
        parts = [
            {
                "id": "steel_frame",
                "component": "frame",
                "price_history": [
                    {"valid_from": "2016-01-01", "valid_until": "2016-11-30", "price": 1100},
                    {"valid_from": "2016-12-01", "valid_until": None, "price": 1200},
                ],
            },
            {
                "id": "basic_saddle",
                "component": "seating",
                "price_history": [
                    {"valid_from": "2016-01-01", "valid_until": None, "price": 400},
                ],
            },
        ]
        result = compute_cycle_price(parts, ["steel_frame", "basic_saddle"], date(2016, 12, 15))
        self.assertEqual(result["component_breakdown"]["frame"], 1200.0)
        self.assertEqual(result["component_breakdown"]["seating"], 400.0)
        self.assertEqual(result["total"], 1600.0)


if __name__ == "__main__":
    unittest.main()