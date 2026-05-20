// ui/script.js

// Hardcoded Hero‑style parts with time‑sensitive prices for demo
const parts = {
  "steel_frame": {
    component: "frame",
    price_history: [
      { valid_from: "2016-01-01", valid_until: "2016-11-30", price: 1100 },
      { valid_from: "2016-12-01", valid_until: null, price: 1200 },
    ],
  },
  "standard_handlebar": {
    component: "handlebar_brakes",
    price_history: [{ valid_from: "2016-01-01", valid_until: null, price: 400 }],
  },
  "v_brakes": {
    component: "handlebar_brakes",
    price_history: [{ valid_from: "2016-01-01", valid_until: null, price: 450 }],
  },
  "basic_saddle": {
    component: "seating",
    price_history: [{ valid_from: "2016-01-01", valid_until: null, price: 400 }],
  },
  "tubeless_tyre": {
    component: "wheels",
    price_history: [
      { valid_from: "2016-01-01", valid_until: "2016-11-30", price: 500 },
      { valid_from: "2016-12-01", valid_until: null, price: 530 },
    ],
  },
  "standard_rim": {
    component: "wheels",
    price_history: [{ valid_from: "2016-01-01", valid_until: null, price: 300 }],
  },
  "tube": {
    component: "wheels",
    price_history: [{ valid_from: "2016-01-01", valid_until: null, price: 150 }],
  },
  "spokes": {
    component: "wheels",
    price_history: [{ valid_from: "2016-01-01", valid_until: null, price: 200 }],
  },
  "4_gear_assembly": {
    component: "chain_assembly",
    price_history: [{ valid_from: "2016-01-01", valid_until: null, price: 950 }],
  },
};

const componentNames = {
  frame: "Frame",
  handlebar_brakes: "Handle Bar/Brakes",
  seating: "Seating",
  wheels: "Wheels",
  chain_assembly: "Chain Assembly",
};

function findPriceForDate(priceHistory, isoDate) {
  const query = new Date(isoDate);
  const candidates = priceHistory.filter((entry) => {
    const from = new Date(entry.valid_from);
    const until = entry.valid_until ? new Date(entry.valid_until) : null;

    if (from > query) return false;
    if (until && query > until) return false;
    return true;
  });

  if (candidates.length === 0) return 0;

  candidates.sort(
    (a, b) => new Date(b.valid_from) - new Date(a.valid_from)
  );
  return candidates[0].price;
}

function computePriceBreakdown(selectedPartIds, dateStr) {
  const componentTotals = {
    frame: 0,
    handlebar_brakes: 0,
    seating: 0,
    wheels: 0,
    chain_assembly: 0,
  };
  let total = 0;

  for (const id of selectedPartIds) {
    const part = parts[id];
    if (!part) continue;

    const price = findPriceForDate(part.price_history, dateStr);
    componentTotals[part.component] += price;
    total += price;
  }

  const lines = [
    `Cycle Price Breakdown — ${dateStr}`,
    "------------------------------------",
  ];

  for (const [key, value] of Object.entries(componentTotals)) {
    if (value > 0) {
      lines.push(`${componentNames[key]} : ₹${value.toFixed(0)}`);
    }
  }

  lines.push("------------------------------------");
  lines.push(`TOTAL : ₹${total.toFixed(0)}`);

  return lines.join("\n");
}

document.getElementById("compute").addEventListener("click", () => {
  const dateStr = document.getElementById("date").value || "2016-12-15";

  const wheels = Array.from(
    document.getElementById("wheels").selectedOptions
  ).map((opt) => opt.value);

  const selected = [
    document.getElementById("frame").value,
    document.getElementById("handlebar_brakes").value,
    document.getElementById("seating").value,
    ...wheels,
    document.getElementById("chain_assembly").value,
  ];

  const breakdownText = computePriceBreakdown(
    selected.filter((id) => id),
    dateStr
  );

  document.getElementById("breakdown").textContent = breakdownText;
});