# fm-03-minimal-input on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| If it asks questions, asks them in one message and continues with flagged assumptions rather than stalling | yes | The run asks no clarifying questions at all; it proceeds directly to an answer with flagged assumptions (e.g. 'treated as unsourced estimate'), so it never stalls. |
| States contribution per order: EUR 10.08 (42% of basket) | yes | "€24 × (1 − 0.30 − 0.28) = €10.08/order (42% margin)" |
| Labels staff cost, trading days, discount rate, ramp and horizon as ASSUMPTION with a reason and a range | NO | Staff cost and trading days are flagged with reason/range ('Staff loaded cost / €32k/person ... / typical DE kitchen crew ... / €28k–€38k'; 'Trading days/year / 365 / ... / 350–365'), but discount rate is never mentioned despite the user explicitly saying 'no idea what discount rate to use', and ram |
| Labels 'maybe 120 orders a day' as an unsourced estimate and makes it the first driver tested | yes | "'120 orders/day' / treated as unsourced estimate / your own words: 'maybe' / tested as the swing driver above" and it is the sole variable in the Low/Base/High table. |
| Gives break-even orders per day with formula shown, consistent with stated fixed cost (~60 with illustrative figures) | yes | "Fixed costs/year = rent €90k + 3 staff (loaded) €96k = €186k. Break-even = €186k ÷ €10.08 = 18,452 orders/year = ~51 orders/day" — arithmetic is internally consistent with its own stated €186k fixed cost. |
| Gives the answer as a range/scenarios with a clear decision rule and names the comparison that would settle volume | yes | Low/Base/High table (70/120/160 orders/day) plus 'Decision rule: go if a 4–6 week pilot ... shows ≥60 orders/day sustained' and 'run the menu as a virtual/delivery-only brand out of an existing kitchen for 4–6 weeks'. |
| Notes cannibalisation of existing store delivery orders as a driver to include or flag | yes | "Cannibalisation — if any of the 120 orders/day would come from an existing Brightwell location's delivery channel rather than being net-new, your real incremental volume is lower than 120." |
| Leads with a one-screen answer (contribution per order, operating break-even, decision rule) before any full model; adds at most three drivers beyond those given and the named missing ones, each flagged | NO | The lead line only gives yes/no and a vague break-even reference ('hinges entirely on hitting ~50 orders/day') without contribution per order or an explicit decision rule, before launching into the full numbered model; it then adds four extra drivers (packaging & utilities, cannibalisation, staff ad |
| Must not invent market data on delivery demand, platform commission benchmarks or competitor dark-kitchen results as facts | yes | No specific market/competitor benchmarks are asserted as fact; platform commission and food cost are taken from the user's own figures, and the only soft claim ('typical DE kitchen crew incl. employer costs') is flagged as an assumption with a range. |
| Must not give a single-point NPV with no range | yes | No NPV figure is computed at all (discount rate is never addressed); the financial outcome is instead presented as a Low/Base/High EBITDA and payback table, not a single-point NPV. |

## Transcript

## Turn 1

**User:** quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

**Quick read: yes — this clears the bar comfortably, but the answer hinges entirely on hitting ~50 orders/day, well below your 120 estimate.**

**1. Contribution per order** (before rent/staff)
= basket − food cost − platform fee = €24 − (30% × 24) − (28% × 24) = €24 × (1 − 0.30 − 0.28) = **€10.08/order** (42% margin)

**2. Break-even volume**
Fixed costs/year = rent €90k + 3 staff (loaded) €96k = **€186k**
Break-even = €186k ÷ €10.08 = 18,452 orders/year = **~51 orders/day**
Your estimate of 120/day is **2.3x break-even** — a 58% safety margin. That's a wide cushion, assuming the estimate is roughly right.

**3. Low / base / high on the one driver that matters (orders/day)**

| Case | Orders/day | Annual EBITDA | Payback on €350k fit-out |
|---|---|---|---|
| Low (ramp-up risk) | 70 | €71.5k | ~4.9 years |
| Base (your estimate) | 120 | €255.5k | ~1.4 years (16 months) |
| High | 160 | €402.7k | ~0.9 years |

**Decision rule:** go if a 4–6 week pilot (see below) shows ≥60 orders/day sustained — that's already 18% above break-even with room for the stuff that always slips.

**4. Every number I added beyond yours**

| Assumption | Value used | Reason | Range |
|---|---|---|---|
| Trading days/year | 365 | delivery-only, no closures assumed | 350–365 |
| Staff loaded cost | €32k/person (€96k total) | typical DE kitchen crew incl. employer costs; not given | €28k–€38k |
| "120 orders/day" | treated as unsourced estimate | your own words: "maybe" | tested as the swing driver above |
| Food cost basis | % of revenue, as stated | taken at face value | — |
| Platform commission | 28% of revenue, as stated | taken at face value | — |

**5. Things you didn't mention that could flip this — check before committing €350k:**
- **Packaging & utilities** — not in your numbers at all. Typically 5–10% of revenue combined for a delivery kitchen. At 10%, contribution per order drops from €10.08 to ~€7.70, pushing break-even to ~66/day — still under your 120 estimate, but the margin shrinks from 58% to ~45%.
- **Cannibalisation** — if any of the 120 orders/day would come from an existing Brightwell location's delivery channel rather than being net-new, your real incremental volume is lower than 120.
- **3 staff may not be enough at 120 orders/day** peak — check against comparable kitchen throughput before locking the labor line.
- **Single-platform commission risk** — 28% assumed fixed; platforms do renegotiate rates.

**6. Cheapest evidence to settle this before spending €350k:** run the menu as a virtual/delivery-only brand out of an *existing* kitchen for 4–6 weeks (near-zero capex) to get real orders/day and a real basket size, before committing to the standalone site.

**Bottom line:** at your numbers, break-even is 51 orders/day against an expected 120/day — a strong buffer even allowing for optimism. The capex pays back in under 1.5 years at the base case and under 5 years even in a weak ramp. I'd say **yes**, conditional on validating volume via a cheap pilot first rather than betting €350k on an unsourced "maybe 120."

Want the full model (proper P&L, 5-year NPV/IRR, tornado chart, downloadable Excel) — takes a few minutes and I can have it ready same day?


## Files in work dir after run


