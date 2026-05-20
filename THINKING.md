1.Who is using this?

    The salesperson at a cycle showroom is a non‑technical user who configures cycles 10–20 times a day.

    

    2. What makes this tricky?

Time‑sensitive pricing introduces three edge cases:

    Price overlaps or gaps:

        Two price entries for the same part might partially overlap (e.g., both valid on 2016‑12‑01), or there might be a gap with no defined price on the query date.

    Current‑price handling:

        A part’s latest price has no valid_until (still current). The engine must pick this entry if the given date is on or after valid_from.

    Future price on a past date:

        A price entry starts on 2017‑01‑01, but the salesperson asks for 2016‑12‑15. The correct price is the one active on that 2016‑12‑15, not the future one.



        3.My Plan
Parts and prices:

    Each part has a name, a component (e.g., "frame"), and a list of price_history entries (each with valid_from, valid_until, price).

Time‑sensitive pricing:

    For a given part and date, filter price entries where date >= valid_from and valid_until is null or date <= valid_until, then pick the latest one.

Output:

    The engine returns the total price plus a map of component → subtotal so the UI can show a breakdown like in the example.




    ## Data Model

Core entities:

- **Part**
  - id          : str
  - name        : str
  - component   : str (e.g., "frame", "handlebar_brakes", "seating", "wheels", "chain_assembly")
  - price_history : List[PriceEntry]

- **PriceEntry**
  - valid_from  : date (YYYY-MM-DD)
  - valid_until : date | null (null = still current)
  - price       : float (INR)

- **CycleConfiguration**
  - date        : date (for which price is queried)
  - part_ids    : List[str]

Relations:
- Each Component (e.g., "wheels") has many Parts (e.g., rim, tyre, tube, spokes).
- Each Part has many PriceEntries (price over time).
- A CycleConfiguration points to a list of Part IDs and a date.

Design choice for time‑sensitive pricing:
- I store a list of price ranges per part (every `PriceEntry` has `valid_from` and `valid_until`) instead of a single price.
- This lets me support:
  - Historical quotes (any date in the past).
  - Future price changes (up to a new `valid_from`).
  - “Current” price (null `valid_until`).
- On lookup, for a given date I pick the most recent entry that covers that date.


