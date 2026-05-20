# Hero Cycles – Pricing Engine (Fresher Assignment)

A full‑stack pricing engine for Hero Cycles that:
- Computes cycle prices from selected parts.
- Respects time‑sensitive pricing (prices change over time).
- Shows a breakdown by component in the UI.

## Part 1 — Thinking

See `THINKING.md` for:
- User (salesperson) needs and frustrations.
- Three edge cases from time‑sensitive pricing.
- Plan for data model and time handling.
- Data model entities and relations.

## Part 2 — Pricing Engine (2a / 2b)

### Backend (Python)

Requirements:
- Python 3.8+
- `pip install Flask` (optional; HTTP API is bonus)

1. Load the data:
   - `src/data/parts.json` contains all parts and their price histories.

   
2. Run the CLI pricing engine:

   First, create a sample input file:

   ```bash
   cat > example_input.json << 'EOF'
   {
     "date": "2016-12-15",
     "parts": [
       "steel_frame",
       "standard_handlebar",
       "v_brakes",
       "basic_saddle",
       "tubeless_tyre",
       "standard_rim",
       "tube",
       "spokes",
       "4_gear_assembly"
     ]
   }
   EOF
   ```

   Then run:

   ```bash
   python src/app.py example_input.json
   ```

3. Run tests:
   ```bash
   python src/tests/test_pricing.py
   ```

4. (Optional) Run HTTP API:
   ```bash
   python src/api.py
   ```
   Then POST to `http://127.0.0.1:5000/price` with the same JSON structure.

## Part 3 — UI (Option A)

This is a simple web configurator that:
- Lets the user pick parts and a pricing date.
- Shows a real‑time price breakdown using hardcoded prices (no backend connection needed).

### How to run

1. Open `ui/index.html` directly in your browser, or serve it:

   With Python:
   ```bash
   cd ui
   python -m http.server 8000
   # then open http://127.0.0.1:8000
   ```

2. Select parts and a date, then click “Calculate Price”.

## Folder structure

- `THINKING.md`: Part 1 answers and data model.
- `src/`:
  - `pricing_engine.py`: core pricing logic.
  - `app.py`: CLI runner.
  - `api.py`: optional HTTP server.
  - `data/parts.json`: part data.
  - `tests/test_pricing.py`: unit tests.
- `ui/`:
  - `index.html`, `style.css`, `script.js`: web configurator.
- `UI_NOTES.md`: answers to Part 3 UI questions.

Commit history:
- Work incrementally:
  1. `git commit -m "Add THINKING.md and data model plan"`
  2. `git commit -m "Add src/pricing_engine.py and data/parts.json"`
  3. `git commit -m "Add CLI runner and tests"`
  4. `git commit -m "Add UI configurator in ui/"`