# fm-03-minimal-input on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| If it asks questions, asks them in one message and continues with flagged assumptions rather than stalling | yes | The run asks no clarifying questions at all; it proceeds directly to a quick-read answer and a full set of flagged assumptions instead of stalling. |
| States contribution per order of EUR 10.08 (42%) or a lower figure consistent with an added variable cost, flagged as assumption | yes | 'Variable costs = food 30% + platform 28% + other opex (see below) 8% = 66% ... Contribution/order = €24 × 0.34 = €8.16' with 'Other opex ... ASSUMPTION — nothing in your inputs covers these' flagged in the assumptions table. |
| Labels staff cost, trading days, discount rate, ramp and horizon as ASSUMPTION with a reason and a range | NO | Table row 'Ramp-up / none (flat from day 1) / ASSUMPTION — flagged as a real risk, not modelled / —' gives a reason but explicitly no range (dash), unlike the other rows which all have ranges. |
| Labels 'maybe 120 orders a day' as an unsourced estimate and makes it the first driver tested | yes | 'Orders/day = 120 / — / This is your own rough estimate, unsourced — it's the single biggest swing factor below / tested 90–150' and it is ranked #1 in the sensitivity table: '1 / Orders/day / 90 → 150 ... Swing / €176k'. |
| Gives break-even orders per day with formula shown, consistent with its stated fixed cost | yes | 'Fixed costs = rent €90k + staff €114k = €204k/year' and 'Break-even = €204,000 / €8.16 = 25,000 orders/year ≈ 69 orders/day' — internally consistent with its own stated fixed cost and contribution figure. |
| Gives the answer as a range/scenarios with a clear decision rule and names the comparison that would settle volume | yes | Scenario table uses 90/120/150 orders/day, and recommendation states 'gate the €350k fit-out spend on the pilot: commit only if it shows ≥100 sustained orders/day within 8–12 weeks and the platform commission is contracted at ≤29%,' naming a pilot/platform test as the volume-settling comparison. |
| Notes cannibalisation of existing store delivery orders as a driver to include or flag | yes | 'Whether this cannibalizes any existing Brightwell dine-in or delivery sales nearby.' |
| Leads with a one-screen answer (contribution per order, operating break-even, decision rule) before any full model; adds at most three extra flagged drivers | NO | Contribution (section 1) and break-even (section 2) appear before the scenario table, but the explicit decision rule ('commit only if it shows ≥100 sustained orders/day ... platform commission ... ≤29%') only appears in the final 'Recommendation' line, after the full scenario table, sensitivity rank |
| Must not invent market data on delivery demand, platform commission benchmarks or competitor dark-kitchen results as facts | NO | 'dark kitchens rarely hit full volume from week one; a 3–6 month ramp pushes payback out materially' and marketing spend 'often needed early on' are stated as general industry facts without sourcing or an ASSUMPTION flag on the statement itself. |
| Must not give a single-point NPV with no range | yes | NPV is given across three scenarios: '–€292k' (Down), '+€185k' (Base), '+€730k' (Up) — a range, not a single point. |

## Transcript

## Turn 1

**User:** quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

## Quick read: conditional yes — but the 120 orders/day number hasn't been tested yet, and if it's wrong together with a couple of other things, this loses money

**1. Contribution per order**
Variable costs = food 30% + platform 28% + other opex (see below) 8% = 66% of revenue → contribution margin **34%**
Contribution/order = €24 × 0.34 = **€8.16**

**2. Break-even volume**
Fixed costs = rent €90k + staff €114k = **€204k/year**
Break-even = €204,000 / €8.16 = **25,000 orders/year ≈ 69 orders/day**
Plan is 120/day → **42% margin of safety** if the plan holds. That's a comfortable cushion on volume alone.

**3. Low / base / high case** (coherent stories, not single variables flexed in isolation)

| | Orders/day | Platform take | Staff cost | EBITDA/yr | Payback | NPV @12%, 5yr |
|---|---|---|---|---|---|---|
| **Down** — slow ramp + platform renegotiates + hire at top of range | 90 | 31% | €135k | €16k | ~22 yrs | **–€292k** |
| **Base** — plan holds | 120 | 28% | €114k | €149k | ~28 months | **+€185k** |
| **Up** — strong demand + better platform terms + lean staffing | 150 | 25% | €90k | €300k | ~14 months | **+€730k** |

Base case IRR ≈ 32%, comfortably above a 12% hurdle. But the **down case erases the project** — not because volume drops much (90/day is still above the 69/day break-even on its own), but because volume, take-rate and staff cost deteriorating *together* leaves almost nothing to cover €350k of capex.

**4. Every number I added that you didn't give me**

| Assumption | Value used | Reason | Range |
|---|---|---|---|
| Orders/day = 120 | — | **This is your own rough estimate, unsourced** — it's the single biggest swing factor below | tested 90–150 |
| Trading days/year | 360 | ASSUMPTION — allows for closures/maintenance | 330–365 |
| Staff cost | €38k loaded/head × 3 = €114k | ASSUMPTION — no figure given for kitchen/packing staff | €90k–135k |
| Other opex (utilities, packaging, software, maintenance, insurance) | 8% of revenue | ASSUMPTION — nothing in your inputs covers these, and they're real for a dark kitchen | 5–12% |
| Discount rate | 12% | ASSUMPTION — small single-site F&B capex, platform-dependency risk | 10–15% |
| Horizon | 5 years | ASSUMPTION — no lease term or equipment life given | 3–7 |
| Ramp-up | none (flat from day 1) | ASSUMPTION — flagged as a real risk, not modelled | — |

**5. Sensitivity ranking** (swing in annual EBITDA, each driver alone, others at base)

| Rank | Driver | Low → High | EBITDA low | EBITDA high | Swing |
|---|---|---|---|---|---|
| 1 | Orders/day | 90 → 150 | €60k | €237k | €176k |
| 2 | Avg basket | €20.40 → €27.60 | €96k | €201k | €106k |
| 3 | Platform take-rate | 25% → 31% | €180k | €117k | €62k |

Order volume dominates — and it's the number you're least sure of.

**6. Things you didn't mention that could flip this**
- **Ramp-up time** — dark kitchens rarely hit full volume from week one; a 3–6 month ramp pushes payback out materially and isn't in the model above.
- Platform minimum-order guarantees / exclusivity clauses.
- Marketing/visibility spend to get discovered on the platform (often needed early on, not in food/platform cost).
- Whether this cannibalizes any existing Brightwell dine-in or delivery sales nearby.
- Staff turnover/recruitment cost for a 3-person crew doing unsociable delivery hours.

**Cheapest evidence to settle this before spending €350k:** run a 60–90 day pilot — list as a virtual brand from an existing kitchen if you have one, or a short trial lease — to get a real orders/day number and lock the platform commission in a signed contract, instead of committing capex on an estimate.

**Recommendation:** Go, but gate the €350k fit-out spend on the pilot: commit only if it shows ≥100 sustained orders/day within 8–12 weeks and the platform commission is contracted at ≤29%. Don't sign the lease/fit-out off the 120/day estimate alone — the downside case (volume + take-rate + staff cost all slipping together) loses nearly €300k.

Want the full versioned model (CSV/Excel with live formulas, proper tornado chart, downloadable) instead of this back-of-envelope version — useful if this goes in front of whoever signs off the capex?


## Files in work dir after run


