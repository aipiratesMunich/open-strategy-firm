# fm-01-hub-business-case on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the question, outputs (NPV, payback, IRR) and decision threshold (NPV>0 at 9%) before building | yes | business-case.md 'Setup' section: 'Decision: invest in a cross-dock hub...' / 'Discount rate: 9%... CFO rule: approve if NPV at 9% is above zero' precedes the cash-flow build and cases/tornado sections |
| Separates inputs, calculations and outputs; no number typed inside a formula other than 0/1 or documented unit conversion | yes | spec.json formulas use only variable names and 0/1 literals, e.g. 'pick(t, 0, ramp_2027, 1)', '-hub_fixed_cost * min(1, t)'; inputs.csv/calc.csv/outputs.csv kept separate |
| Base NPV within EUR 3.1m–3.4m and payback in 2030 or year 4 | yes | outputs.csv: npv base = 3.2302410504 EUR m; payback_period base = 2030 |
| Tornado ranking with saving per parcel first and parcels routed second | yes | sensitivity.csv: rank 1 saving_per_parcel, rank 2 parcels_full_runrate |
| Gives break-even values for saving per parcel (~0.42–0.43) and parcels (~3.8–3.9m) and says both lie inside their ranges | yes | 'break-even EUR 0.425, vs. quoted range 0.40–0.65' and 'break-even 3.86m, vs. quoted range 3.8–5.6m'; sensitivity.csv shows break_even_in_range = yes for both |
| Because a break-even lies inside the range, puts it in the headline or 'decided by' line, not only appendix | yes | Headline answer: 'What decides it: Two drivers — saving per parcel (break-even EUR 0.425...) and routed volume (break-even 3.86m...) — have break-even values sitting just inside Kestrel's own ranges' |
| Defines the down case as a coherent story (competitor hub: fewer parcels, lower saving, higher investment) rather than a uniform cut, and reports its NPV as negative | yes | 'down: parcels_full_runrate = 3.8, saving_per_parcel = 0.4, investment = 7.5 (competitor opens a south hub nearby...)' with NPV = -4.626 EUR m |
| A checks block and two outputs recomputed by hand with both numbers recorded | yes | checks.csv present with OK statuses; 'Spot test: NPV recomputed by hand ... = EUR 3.23m, matches the model; cumulative cash flow by hand crosses zero between 2029 (−1.55) and 2030 (+0.30)' |
| Lists the 60% ramp as a flagged assumption | yes | README 'Flags: Drivers flagged as assumptions ... ramp_2027' and business-case.md section 'Ramp speed — flagged, not a decider' |
| 'What the deck should say' sentences carrying the model version | NO | No section or sentences labeled as deck-ready statements tagged with the model version (v01) appear anywhere in business-case.md or the answer; version v01 only appears as a document title/footer and in outputs.csv column, not attached to headline sentences framed for a deck |
| Must not present the NPV without the range or scenarios | yes | Headline answer and document both present base NPV alongside down/up scenarios and sensitivity ranges |
| Must not add a terminal value or tax without flagging that it departs from the agreed conventions | yes | 'No terminal value, no tax (screening conventions agreed with finance)' — explicitly stated as the agreed convention, not silently added |

## Transcript

## Turn 1

**User:** Build the business case for the Kestrel south hub from these inputs. Board needs NPV, payback and what decides the answer. (Attached in the working directory: fm-01-input.md.)

The business case is built and checks out — here's the headline for the board.

**Answer:** NPV at the 9% hurdle is **+EUR 3.2m**, IRR 21%, payback in **2030** (~3.8 years after the EUR 6.0m is spent). That clears the CFO's rule, but not comfortably.

**What decides it:** Two drivers — saving per parcel (break-even EUR 0.425, vs. quoted range 0.40–0.65) and routed volume (break-even 3.86m, vs. quoted range 3.8–5.6m) — have break-even values sitting just inside Kestrel's own ranges, right above the low case. Fixed cost, investment overrun and the hurdle rate would all have to blow far past their quoted ranges to kill the deal on their own, so those aren't the risk. The planning team's competitor-entry story hits both decisive drivers at once plus a costlier fit-out — modeled as a coherent "down" case, it takes NPV to **−EUR 4.6m**. That combined scenario, not any single input, is what should drive the board's decision.

One gap: the 60% 2027 ramp assumption came with no evidence range, so I bounded it separately (swinging it 0–100% moves NPV between +1.7m and +4.2m) — it can't flip the answer, but it's the one input without sourced evidence and worth tightening before sign-off.

Delivered in the working directory:
- `business-case.md` — the full write-up (setup, cash flows, cases, tornado sensitivity, recommendation)
- `model/` — the transparent driver model: `inputs.csv`, `spec.json`, `calc.csv`, `outputs.csv`, `checks.csv`, `sensitivity.csv`, `model.xlsx` (live formulas + scenario switch), `README.md`

All checks pass and I hand-verified NPV and payback independently. Happy to turn this into a board deck next if useful.


## Files in work dir after run

- business-case.md
- fm-01-input.md
- model/README.md
- model/calc.csv
- model/checks.csv
- model/inputs.csv
- model/model.xlsx
- model/outputs.csv
- model/sensitivity.csv
- model/spec.json

## File written by the run: business-case.md

# Business case: Kestrel south hub investment (model v01)

**Answer:** NPV at the 9% hurdle rate is **+EUR 3.2m**, IRR **21%**, payback in **2030** (about 3.8 years after the EUR 6.0m is spent at the start of 2027). Base case clears the CFO's rule (NPV > 0). But the case turns negative under a single coherent downside — a competitor opening a hub nearby — and two of the five uncertain drivers have break-even values sitting just inside their quoted ranges. This is a pass, not a comfortable one.

## Setup

- **Decision:** invest in a cross-dock hub in the south region.
- **Counterfactual:** no hub; parcels keep moving on today's line-haul routing, no saving, no added fixed cost, no investment.
- **Horizon:** 2027–2034, 8 years. Investment paid at the start of 2027 (t=0); operating cash flows at each year-end 2027–2034, discounted 1 to 8 years. No terminal value, no tax (screening conventions agreed with finance).
- **Discount rate:** 9% (Group finance; range 7–11%).
- **CFO rule:** approve if NPV at 9% is above zero.

## Incremental cash flows (base case, EUR m)

| | Start | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 |
|---|---|---|---|---|---|---|---|---|---|
| Parcels routed (m) | – | 3.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 |
| Gross saving | – | 1.65 | 2.75 | 2.75 | 2.75 | 2.75 | 2.75 | 2.75 | 2.75 |
| Hub fixed cost | – | −0.90 | −0.90 | −0.90 | −0.90 | −0.90 | −0.90 | −0.90 | −0.90 |
| Investment | −6.00 | – | – | – | – | – | – | – | – |
| **Net cash flow** | **−6.00** | **0.75** | **1.85** | **1.85** | **1.85** | **1.85** | **1.85** | **1.85** | **1.85** |
| Cumulative cash flow | −6.00 | −5.25 | −3.40 | −1.55 | +0.30 | +2.15 | +4.00 | +5.85 | +7.70 |
| Discounted cash flow | −6.00 | 0.69 | 1.56 | 1.43 | 1.31 | 1.20 | 1.10 | 1.01 | 0.93 |

2027 carries the 60% ramp (3.0m of the 5.0m full run-rate parcels); full run-rate is assumed from 2028. Hub fixed cost is incurred at the full EUR 0.9m from the first operating year, including the ramp year.

## Cases

| Case | Defining assumptions (coherent story) | NPV | IRR | Payback |
|---|---|---|---|---|
| **Down** | Competitor opens a south hub nearby: shippers divert volume (parcels → low case 3.8m), the price response needed to retain business eats the saving (→ low case EUR 0.40/parcel), and we accelerate the fit-out to respond (investment → high case EUR 7.5m) — the planning team's own named risk, not an across-the-board cut | **−EUR 4.6m** | −10% | Never recovers within the 8-year horizon |
| **Base** | Drivers at their base values | **+EUR 3.2m** | 21% | 2030 |
| **Up** | No competitor entry; network simulation's higher-saving case (2023 fuel prices) holds, volume at the high end of the 2025 flow data, fit-out at the cheaper end of the quotes | **+EUR 8.3m** | 39% | 2029 |

## What decides the answer

Contribution per parcel = saving per parcel = EUR 0.55 (base). The hub's **operating break-even volume** — the volume needed just to cover the EUR 0.9m/year fixed cost, ignoring the investment — is 0.9 / 0.55 ≈ **1.64m parcels/year**. Even the 2027 ramp-year volume (3.0m) clears that easily, so the hub is in no danger of losing money on a running-cost basis. The real question is whether the investment pays back, and that is a different, tighter test.

Tornado ranking on NPV (one driver moved to its quoted low/high at a time, all others at base):

| Rank | Driver | Range tested | NPV at low | NPV at high | Break-even value | Inside the quoted range? |
|---|---|---|---|---|---|---|
| 1 | Saving per parcel | EUR 0.40 – 0.65 | −0.65 | 5.81 | **EUR 0.425/parcel** | **Yes** — just above the low case |
| 2 | Parcels at full run-rate | 3.8 – 5.6m | −0.18 | 4.94 | **3.86m** | **Yes** — just above the low case |
| 3 | Hub fixed cost | EUR 0.7 – 1.2m | 4.34 | 1.57 | EUR 1.48m | No — well above the quoted range |
| 4 | Investment | EUR 5.5 – 7.5m | 3.73 | 1.73 | EUR 9.23m | No — well above the quoted range |
| 5 | Hurdle rate | 7% – 11% | 4.02 | 2.53 | 20.9% (= the IRR) | No — well above the quoted range |

**This is the whole story.** Saving per parcel and routed volume are the only two drivers whose break-even values fall inside the ranges Kestrel itself quoted — and both break-evens sit barely above the low case. Fixed cost, investment overrun and the hurdle rate would all have to move far outside their quoted ranges to turn the case negative on their own; the board does not need to worry about those. But the planning team's competitor scenario hits saving per parcel *and* volume *at the same time*, plus a costlier fit-out — which is exactly why the combined down case (−EUR 4.6m) is so much worse than either single-driver low case. **The decision rests on whether a competitor response materialises, not on cost or financing risk.**

### Ramp speed — flagged, not a decider

The 60% 2027 ramp (ASSUMPTION, based on the 2023 north hub opening) was given with no low/high range, so it could not be put through the same sensitivity test. A bounding check — holding every other driver at base and swinging the ramp from 0% to 100% in 2027 only — moves NPV between **+EUR 1.7m and +EUR 4.2m**. That is a real but secondary swing: on its own, ramp speed cannot flip the sign of the decision. Still, it is the one input in the table without evidence behind its range, so it is worth tightening before sign-off.

## Constraint check

| Constraint | Limit | Base case value | Met? |
|---|---|---|---|
| CFO approval rule | NPV at 9% > 0 | +EUR 3.2m | Yes |
| Investment within quoted fit-out cost | EUR 5.5–7.5m | EUR 6.0m | Yes |

## Recommendation

Approve, with two conditions the board should put on record rather than discover later:

1. **Treat the competitor-entry scenario as the real go/no-go risk**, not a tail case — it is built entirely from Kestrel's own quoted ranges and takes NPV to −EUR 4.6m. Before committing capital, get a read on competitor hub plans in the south region (the planning team is best placed to do this) and revisit the case if there is any signal of an opening.
2. **Close the ramp-assumption gap.** Pull the actual month-by-month ramp curve from the 2023 north hub launch (the input only states a year-one average) to replace the unverified 60% assumption with an evidenced range. This is the cheapest open item to fix and, per the bounding check above, cannot overturn the decision on its own — but it is currently the only driver in the model without a quoted range.

## Model

Full driver model, inputs, formulas, checks, scenarios and tornado sensitivity: `model/` (`inputs.csv`, `spec.json`, `calc.csv`, `outputs.csv`, `checks.csv`, `sensitivity.csv`, `model.xlsx`, `README.md`), version v01. Master check: OK (all ties verified). Spot test: NPV recomputed by hand from the undiscounted cash flows above = EUR 3.23m, matches the model; cumulative cash flow by hand crosses zero between 2029 (−1.55) and 2030 (+0.30), matching the model's payback period.


## File written by the run: model/README.md

# Model: Kestrel south hub business case (fictional), v01

**Question answered:** Should Kestrel invest in a cross-dock hub in the south region? CFO rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life (2027-2034).

**Master check:** OK

## Key outputs

| Output | Unit | base | down | up |
|---|---|---|---|---|
| NPV at hurdle rate | EUR m | 3.23 | -4.626 | 8.33 |
| IRR | per year | 0.2091 | -0.09939 | 0.388 |
| Payback (first year cumulative cash >= 0) | period | 2030 | none | 2029 |
| Parcels routed, ramp year 2027 | m parcels | 3 | 2.28 | 3.36 |
| Net cash flow 2034 (full run-rate) | EUR m | 1.85 | 0.62 | 2.74 |

Scenarios (coherent sets, drivers changed from base):
- **down**: parcels_full_runrate = 3.8, saving_per_parcel = 0.4, investment = 7.5 (competitor opens a south hub nearby: shippers divert volume (parcels fall to the low case), the price response needed to retain business eats the saving down to the low case, and we accelerate the fit-out to respond, pushing investment to the high case)
- **up**: parcels_full_runrate = 5.6, saving_per_parcel = 0.65, investment = 5.5 (no competitive entry, and the network simulation's higher-saving case (2023 fuel prices) holds alongside the high end of the 2025 flow data and a cheaper fit-out within the quoted range)

## Sensitivity on npv (one-way, others at base; break-even target 0)

| Rank | Driver | Low / base / high | Output low | Output high | Swing | Break-even | Inside range? |
|---|---|---|---|---|---|---|---|
| 1 | saving_per_parcel | 0.4 / 0.55 / 0.65 EUR per parcel | -0.6456 | 5.814 | 6.46 | 0.425 | yes |
| 2 | parcels_full_runrate | 3.8 / 5 / 5.6 m parcels per year | -0.1805 | 4.936 | 5.116 | 3.864 | yes |
| 3 | hub_fixed_cost | 0.7 / 0.9 / 1.2 EUR m per year | 4.337 | 1.57 | 2.767 | 1.484 | no |
| 4 | investment | 5.5 / 6 / 7.5 EUR m | 3.73 | 1.73 | 2 | 9.23 | no |
| 5 | hurdle_rate | 0.07 / 0.09 / 0.11 per year | 4.019 | 2.529 | 1.49 | 0.2091 | no |

Drivers without low/high range (not tested): ramp_2027

## Inputs

| Driver | Value | Unit | Low | High | Source |
|---|---|---|---|---|---|
| parcels_full_runrate | 5 | m parcels per year | 3.8 | 5.6 | 2025 network flow data, south region (Kestrel planning team) |
| ramp_2027 | 0.6 | share of full run-rate |  |  | ASSUMPTION: planning team, based on the 2023 north hub opening |
| saving_per_parcel | 0.55 | EUR per parcel | 0.4 | 0.65 | Network simulation v4; low = 2025 fuel prices, high = 2023 fuel prices |
| hub_fixed_cost | 0.9 | EUR m per year | 0.7 | 1.2 | Site lease offer plus 14 FTE staffing plan |
| investment | 6 | EUR m | 5.5 | 7.5 | Two supplier quotes, September 2026 |
| hurdle_rate | 0.09 | per year | 0.07 | 0.11 | Group finance |

## Line items (calculation order)

| Line item | Unit | Formula |
|---|---|---|
| ramp | share of full run-rate | `pick(t, 0, ramp_2027, 1)` |
| parcels_routed | m parcels | `parcels_full_runrate * ramp` |
| gross_saving | EUR m | `parcels_routed * saving_per_parcel` |
| operating_fixed_cost | EUR m | `-hub_fixed_cost * min(1, t)` |
| capex | EUR m | `-investment * pick(t, 1, 0)` |
| net_cash_flow | EUR m | `gross_saving + operating_fixed_cost + capex` |
| cumulative_cash_flow | EUR m | `prev(cumulative_cash_flow) + net_cash_flow` |
| discount_factor | factor | `(1 + hurdle_rate) ** -t` |
| discounted_cash_flow | EUR m | `net_cash_flow * discount_factor` |

## Checks

| Check | Scenario | Expected | Actual | Status |
|---|---|---|---|---|
| parcels_within_runrate | base | >=0 | 0 | OK |
| parcels_within_runrate | down | >=0 | 0 | OK |
| parcels_within_runrate | up | >=0 | 0 | OK |
| ramp_not_above_one | base | >=0 | 0 | OK |
| ramp_not_above_one | down | >=0 | 0 | OK |
| ramp_not_above_one | up | >=0 | 0 | OK |
| net_cash_flow_ties_to_parts | base | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | down | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | up | ==0 | 0 | OK |

## Flags

- Drivers flagged as assumptions (no source or source starts with 'assumption'): ramp_2027
- No range for: ramp_2027

## Files

- `calc.csv`: every line item by period, base case
- `outputs.csv`: key outputs per scenario
- `checks.csv`: check results per scenario
- `sensitivity.csv`: tornado ranking and break-even values
- `model.xlsx`: Inputs (blue on yellow = input), Calc (live formulas), Outputs (live, master check), Sensitivity (values)


## File written by the run: model/calc.csv

line_item,unit,start,2027,2028,2029,2030,2031,2032,2033,2034
ramp,share of full run-rate,0.0,0.6,1.0,1.0,1.0,1.0,1.0,1.0,1.0
parcels_routed,m parcels,0.0,3.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0
gross_saving,EUR m,0.0,1.65,2.75,2.75,2.75,2.75,2.75,2.75,2.75
operating_fixed_cost,EUR m,0.0,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9
capex,EUR m,-6.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
net_cash_flow,EUR m,-6.0,0.75,1.85,1.85,1.85,1.85,1.85,1.85,1.85
cumulative_cash_flow,EUR m,-6.0,-5.25,-3.4,-1.55,0.3,2.15,4.0,5.85,7.7
discount_factor,factor,1.0,0.9174311927,0.8416799933,0.7721834801,0.7084252111,0.6499313863,0.5962673269,0.5470342448,0.5018662797
discounted_cash_flow,EUR m,-6.0,0.6880733945,1.5571079875,1.4285394381,1.3105866405,1.2023730647,1.1030945547,1.012013353,0.9284526174


## File written by the run: model/checks.csv

check,scenario,expected,actual,status
parcels_within_runrate,base,>=0,0.0,OK
parcels_within_runrate,down,>=0,0.0,OK
parcels_within_runrate,up,>=0,0.0,OK
ramp_not_above_one,base,>=0,0.0,OK
ramp_not_above_one,down,>=0,0.0,OK
ramp_not_above_one,up,>=0,0.0,OK
net_cash_flow_ties_to_parts,base,==0,0.0,OK
net_cash_flow_ties_to_parts,down,==0,0.0,OK
net_cash_flow_ties_to_parts,up,==0,0.0,OK


## File written by the run: model/inputs.csv

driver,value,unit,source,low,high,note
parcels_full_runrate,5.0,m parcels per year,"2025 network flow data, south region (Kestrel planning team)",3.8,5.6,parcels routed through the hub once ramp is complete
ramp_2027,0.60,share of full run-rate,"ASSUMPTION: planning team, based on the 2023 north hub opening",,,"no low/high given in input; full run-rate assumed from 2028 onward; not sensitivity-tested, see Flags"
saving_per_parcel,0.55,EUR per parcel,"Network simulation v4; low = 2025 fuel prices, high = 2023 fuel prices",0.40,0.65,shorter line-haul and fewer handlings
hub_fixed_cost,0.9,EUR m per year,Site lease offer plus 14 FTE staffing plan,0.7,1.2,incurred every operating year 2027-2034 including ramp year
investment,6.0,EUR m,"Two supplier quotes, September 2026",5.5,7.5,paid at start of 2027 (t=0)
hurdle_rate,0.09,per year,Group finance,0.07,0.11,CFO approval rule: NPV at hurdle rate above zero


## File written by the run: model/outputs.csv

output,unit,base,down,up,model_version
npv,EUR m,3.2302410504,-4.626210314,8.3296245579,v01
irr,per year,0.2091368125,-0.0993929701,0.3880178751,v01
payback_period,period,2030,,2029,v01
parcels_2027,m parcels,3.0,2.28,3.36,v01
net_cash_flow_2034,EUR m,1.85,0.62,2.74,v01


## File written by the run: model/sensitivity.csv

rank,driver,unit,low,base,high,output_low,output_base,output_high,swing,break_even,break_even_in_range
1,saving_per_parcel,EUR per parcel,0.4,0.55,0.65,-0.6456439279,3.2302410504,5.8141643692,6.4598082971,0.4249869616,yes
2,parcels_full_runrate,m parcels per year,3.8,5.0,5.6,-0.1805377305,3.2302410504,4.9356304408,5.1161681713,3.8635178329,yes
3,hub_fixed_cost,EUR m per year,0.7,0.9,1.2,4.3372048733,3.2302410504,1.5697953159,2.7674095574,1.483621792,no
4,investment,EUR m,5.5,6.0,7.5,3.7302410504,3.2302410504,1.7302410504,2.0,9.2302410504,no
5,hurdle_rate,per year,0.07,0.09,0.11,4.0188648533,3.2302410504,2.5293361167,1.4895287366,0.2091368125,no


## File written by the run: model/spec.json

{
  "title": "Kestrel south hub business case (fictional)",
  "question": "Should Kestrel invest in a cross-dock hub in the south region? CFO rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life (2027-2034).",
  "periods": ["start", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034"],
  "rows": [
    {"name": "ramp", "unit": "share of full run-rate", "expr": "pick(t, 0, ramp_2027, 1)"},
    {"name": "parcels_routed", "unit": "m parcels", "expr": "parcels_full_runrate * ramp"},
    {"name": "gross_saving", "unit": "EUR m", "expr": "parcels_routed * saving_per_parcel"},
    {"name": "operating_fixed_cost", "unit": "EUR m", "expr": "-hub_fixed_cost * min(1, t)"},
    {"name": "capex", "unit": "EUR m", "expr": "-investment * pick(t, 1, 0)"},
    {"name": "net_cash_flow", "unit": "EUR m", "expr": "gross_saving + operating_fixed_cost + capex"},
    {"name": "cumulative_cash_flow", "unit": "EUR m", "expr": "prev(cumulative_cash_flow) + net_cash_flow"},
    {"name": "discount_factor", "unit": "factor", "expr": "(1 + hurdle_rate) ** -t"},
    {"name": "discounted_cash_flow", "unit": "EUR m", "expr": "net_cash_flow * discount_factor"}
  ],
  "outputs": [
    {"name": "npv", "label": "NPV at hurdle rate", "unit": "EUR m", "fn": "sum", "row": "discounted_cash_flow"},
    {"name": "irr", "label": "IRR", "unit": "per year", "fn": "irr", "row": "net_cash_flow"},
    {"name": "payback_period", "label": "Payback (first year cumulative cash >= 0)", "unit": "period", "fn": "payback", "row": "cumulative_cash_flow"},
    {"name": "parcels_2027", "label": "Parcels routed, ramp year 2027", "unit": "m parcels", "fn": "value", "row": "parcels_routed", "period": "2027"},
    {"name": "net_cash_flow_2034", "label": "Net cash flow 2034 (full run-rate)", "unit": "EUR m", "fn": "value", "row": "net_cash_flow", "period": "2034"}
  ],
  "checks": [
    {"name": "parcels_within_runrate", "expr": "parcels_full_runrate - parcels_routed", "rule": ">=0"},
    {"name": "ramp_not_above_one", "expr": "1 - ramp", "rule": ">=0"},
    {"name": "net_cash_flow_ties_to_parts", "expr": "net_cash_flow - gross_saving - operating_fixed_cost - capex", "rule": "==0"}
  ],
  "scenarios": {
    "down": {"parcels_full_runrate": 3.8, "saving_per_parcel": 0.40, "investment": 7.5},
    "up": {"parcels_full_runrate": 5.6, "saving_per_parcel": 0.65, "investment": 5.5}
  },
  "scenario_stories": {
    "down": "competitor opens a south hub nearby: shippers divert volume (parcels fall to the low case), the price response needed to retain business eats the saving down to the low case, and we accelerate the fit-out to respond, pushing investment to the high case",
    "up": "no competitive entry, and the network simulation's higher-saving case (2023 fuel prices) holds alongside the high end of the 2025 flow data and a cheaper fit-out within the quoted range"
  },
  "break_even": {"output": "npv", "target": 0}
}

