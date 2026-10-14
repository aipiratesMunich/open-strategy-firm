# fm-03-minimal-input on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| If it asks questions, asks them in one message and continues with flagged assumptions rather than stalling | yes | No clarifying questions were asked; the response proceeds directly with a full flagged-assumption analysis instead of stalling. |
| States contribution per order: EUR 10.08 (42% of basket) from the given inputs | yes | '= €10.08 (42% contribution margin)' |
| Labels staff cost, trading days, discount rate, ramp and horizon as ASSUMPTION with a reason and a range | NO | Staff cost and discount rate are explicitly tagged 'ASSUMPTION' with reason and range, but 'Trading days/yr / 350 / typical for delivery-only ops... / 330–365' omits the ASSUMPTION tag, 'Horizon / 5 years, flat volume... / simplification for a quick read / —' has no range, and ramp is never given it |
| Labels 'maybe 120 orders a day' as an unsourced estimate and makes it the first driver tested | yes | '120 orders/day / taken as given / your own estimate, unsourced — tested above as the key risk' listed as the first row, and the whole scenario analysis centers on it. |
| Gives break-even orders per day with the formula shown and consistent with its stated fixed cost | yes | 'Break-even orders/day = fixed cost per day ÷ contribution per order ... ≈ 65 orders/day', arithmetically consistent with its stated €229k fixed cost and €654/day figure. |
| Gives the answer as a range or scenarios with a clear decision rule, and names the comparison that would settle volume | yes | Low/Base/High table (90/120/150 orders/day) with 'Decision rule: go if you have evidence volume will sustain ≥85–90 orders/day...' and 'ask the delivery platform(s) for catchment-level order density/demand data... or run the menu as a virtual brand'. |
| Notes cannibalisation of existing store delivery orders as a driver to include or flag | yes | 'Cannibalization: if Brightwell already sells through this delivery platform from an existing site, some of those 120 orders/day may just be moved, not new.' |
| Leads with a one-screen answer before any full model; adds at most three drivers beyond those given and the named missing ones, each flagged | NO | The opening paragraph is qualitative prose with no contribution/break-even/decision-rule numbers before the full build-up; and beyond the required assumptions it introduces more than three extra drivers (other fixed overhead, kitchen capacity constraint, multi-platform/marketing fees, lease commitme |
| Must not invent market data on delivery demand, platform commission benchmarks or competitor dark-kitchen results as facts | yes | No specific market/competitor figures are asserted as fact; all added figures are presented as flagged assumptions/ranges. |
| Must not give a single-point NPV with no range | yes | 'NPV, 5yr @12%: Low −€286k, Base +€351k, High +€1,024k' — presented as a range across scenarios, not a single point. |

## Transcript

## Turn 1

**User:** quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

## Quick read: dark kitchen go/no-go

**Provisional yes, but don't sign the lease yet** — the economics work comfortably at your assumed volume, but that volume ("maybe 120 orders a day") is the one number nobody has actually measured, and it's also the one number that decides the answer.

### 1. Contribution per order
```
Contribution/order = basket − food cost − platform commission
                    = €24 − (30% × €24) − (28% × €24)
                    = €24 − €7.20 − €6.72
                    = €10.08  (42% contribution margin)
```

### 2. Break-even volume
```
Break-even orders/day = fixed cost per day ÷ contribution per order
Fixed cost/yr (base) = rent €90k + 3 staff €114k + overhead €25k = €229k
Fixed cost/day (÷350 trading days) ≈ €654
Break-even ≈ €654 ÷ €10.08 ≈ 65 orders/day
```
Your estimate of 120/day is ~1.85× break-even — a real margin of safety, *if* 120 is roughly right.

### 3. Low / base / high — driven by order volume + cost creep

| Case | Orders/day | Annual EBITDA | Simple payback (on €350k fit-out) | NPV, 5yr @12% |
|---|---|---|---|---|
| Low | 90, +cost creep (33% food, 30% platform, pricier staff) | ~€18k | ~20 yrs | **−€286k** |
| Base | 120 | ~€194k | ~1.8 yrs | **+€351k** |
| High | 150, slightly better costs | ~€381k | ~0.9 yrs | **+€1,024k** |

**Decision rule:** go if you have evidence volume will sustain ≥85–90 orders/day by month 3–4 of ramp; pause/reconsider if realistic volume looks closer to 70/day — that's close to break-even territory even before ramp-up delay is factored in.

### 4. Every number I added beyond your inputs

| Assumption | Value used | Reason | Range |
|---|---|---|---|
| 120 orders/day | taken as given | **your own estimate, unsourced** — tested above as the key risk, not a fact | 65 (break-even) to 150 |
| Trading days/yr | 350 | typical for delivery-only ops, few closures | 330–365 |
| Staff loaded cost | €38k/head/yr | ASSUMPTION — kitchen/packing staff, incl. employer costs, no location given | €32k–45k |
| Other fixed overhead (utilities, POS, insurance, maintenance) | €25k/yr | ASSUMPTION — not in your inputs at all | €15k–35k |
| Discount rate | 12% | ASSUMPTION — single-unit, platform-dependent delivery concept carries more risk than a mature multi-unit chain (which would be 8–10%); no company WACC given | 10–15% |
| Horizon | 5 years, flat volume (no ramp, no growth, no decline) | simplification for a quick read — a real model should ramp volume up over months 1–6 | — |
| Tax | ignored (pre-tax) | quick read only | — |

### 5. Things you didn't mention that could flip this

- **Ramp-up curve**: you won't do 120 orders/day on day one. A realistic 3–6 month ramp pushes payback out and could flip a marginal case negative — this needs modeling before you commit, not assumed away.
- **Cannibalization**: if Brightwell already sells through this delivery platform from an existing site, some of those 120 orders/day may just be moved, not new.
- **Kitchen capacity with 3 staff**: 120 orders over a service window is roughly 10+/hour at peak — check this is physically doable with 3 people before locking headcount into the model.
- **Multi-platform or marketing fees on top of the 28%** — many platforms charge extra for premium placement/ads, which erodes the 42% contribution margin further.
- **Lease commitment**: if the €90k rent is a multi-year lock-in, that's a bigger risk than the capex itself if volume disappoints.

### 6. Cheapest evidence before you commit €350k
Don't build the kitchen to find out the demand — ask the delivery platform(s) for catchment-level order density/demand data (they usually have this for prospective dark-kitchen sites), or run the menu as a **virtual brand off an existing kitchen** for 4–6 weeks to get a real order-per-day number before signing the lease and fit-out contract. That's a few weeks and near-zero capex versus finding out post-fit-out that real volume is 70, not 120.

---

Want the full model (proper ramp curve, live sensitivity table/tornado, Excel with formulas) before you take this to whoever signs off? I can turn that around within your week.


## Files in work dir after run


