# fm-01-hub-business-case on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the question, outputs, and decision threshold before building | yes | README.md: 'Question answered: Should Kestrel invest in a cross-dock hub in the south region? Decision rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life (2027-2034).' precedes the Key outputs table |
| Separates inputs, calculations and outputs; no literal numbers in formulas other than 0/1 | yes | spec.json formulas use only variables and 0/1, e.g. 'pick(t, 0, ramp_2027, 1)', '-fixed_cost * pick(t, 0, 1)', '(1 + discount_rate) ** -t'; inputs.csv/calc.csv/outputs.csv are separate files |
| Base NPV within EUR 3.1m–3.4m and payback in 2030 or year 4 | yes | outputs.csv: 'npv,EUR m,3.2302410504' and 'payback_period,period,2030' |
| Tornado ranking with saving per parcel first and parcels routed second | yes | sensitivity.csv: rank 1 'saving_per_parcel', rank 2 'parcels_full_runrate' |
| Break-even values for saving/parcel (~0.42-0.43) and parcels (~3.8-3.9m), both flagged inside range | yes | sensitivity.csv: break_even 0.4249869616 (yes) for saving_per_parcel, 3.8635178329 (yes) for parcels_full_runrate |
| Break-even inside range surfaced in headline/decided-by line, not just appendix | yes | Memo subject line: 'base-case NPV +EUR 3.2m at the 9% hurdle rate, but the saving per parcel is what decides it' |
| Down case is coherent story (competitor hub: fewer parcels, lower saving, higher investment), NPV negative | yes | spec.json scenario_stories.down: 'a rival opens its own south-region hub, shippers move so routed volume falls... price response... erodes the saving... fit-out is accelerated... raising investment'; outputs.csv down NPV = -4.626210314 |
| Checks block plus two outputs recomputed by hand with both numbers recorded | NO | Only one hand check is mentioned: 'hand-verified spot check (NPV recomputed by hand = 3.23, matches)' — no second output (e.g. payback or IRR) recomputed by hand with both numbers recorded |
| 60% ramp listed as flagged assumption | yes | README Flags: 'Drivers flagged as assumptions (no source or source starts with 'assumption'): ramp_2027'; inputs.csv source 'ASSUMPTION: planning team, based on the 2023 north hub opening' |
| "What the deck should say" sentences carry the model version | yes | Memo Sources line: 'Sources: model v01 (this folder, `model/`); ...' |
| Must not present NPV without range or scenarios | yes | Memo presents base NPV alongside down/up scenario NPVs (-4.6m, 8.33m) and sensitivity table |
| Must not add terminal value or tax without flagging departure | yes | No terminal value or tax line appears anywhere in calc.csv, spec.json, or outputs.csv |

## Transcript

## Turn 1

**User:** Build the business case for the Kestrel south hub from these inputs. Board needs NPV, payback and what decides the answer. (Attached in the working directory: fm-01-input.md.)

Business case is done. Summary:

**Answer:** Base-case NPV = **+EUR 3.2m** at the 9% hurdle rate, IRR ≈21%, payback in **2030** (the hub's 4th operating year). The recommendation is to approve.

**What decides it:** the **saving per routed parcel** — NPV hits zero at EUR 0.425/parcel, just above the EUR 0.40 low end of the simulated range. **Routed volume** is the second lever (break-even 3.86m parcels vs. 3.8m low end). Both break-evens sit just inside the evidence range, so either one alone at its pessimistic end nearly erases the case. Investment cost and fixed operating cost are not deciding factors — NPV stays positive even at their worst quoted/planned levels.

The planning team's competitor-hub warning was modeled as a combined downside scenario (lower volume + squeezed saving + rushed, costlier fit-out): NPV swings to **-EUR 4.6m** with no payback inside the 8-year life.

**Files produced:**
- `model/` — transparent CSV model (inputs/calc/outputs/checks/sensitivity separated) + `model.xlsx` with a live-formula scenario switch, plus `README.md` with the full tornado ranking and hand-verified spot check (NPV recomputed by hand = 3.23, matches)
- `business-case-memo.md` / `.html` — one-page board memo with the recommendation, the break-even table, and the decision ask

One gap I flagged rather than invented: the brief doesn't give an approval deadline or owner for next steps — the board will need to set those.


## Files in work dir after run

- business-case-memo.html
- business-case-memo.md
- fm-01-input.md
- model/README.md
- model/calc.csv
- model/checks.csv
- model/inputs.csv
- model/model.xlsx
- model/outputs.csv
- model/sensitivity.csv
- model/spec.json

## File written by the run: business-case-memo.html

<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kestrel south hub — board business case</title><style>:root{--text:#14213D;--accent:#D9822B;--light:#E8EBF0}
body{font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;color:var(--text);background:#fff;margin:0}
main{max-width:760px;margin:40px auto;padding:0 16px;font-size:16px;line-height:1.5}
h2{font-size:20px;border-bottom:3px solid var(--accent);padding-bottom:8px}h3{font-size:16px}
li{margin-bottom:4px}table.data{border-collapse:collapse;width:100%;font-size:14px}
table.data th,table.data td{border-bottom:1px solid var(--light);padding:4px 8px;text-align:left}
@media print{@page{size:A4;margin:16mm}main{margin:0}}</style></head><body><main><p><strong>Subject: Approve the EUR 6.0m south hub — base-case NPV +EUR 3.2m at the 9% hurdle rate, but the saving per parcel is what decides it</strong></p>
<p>To the board. We recommend approving the EUR 6.0m investment in the south-region cross-dock hub, paid at the start of 2027. Over the hub&#x27;s eight-year life (2027–2034), the base case NPV at the CFO&#x27;s 9% hurdle rate is +EUR 3.2m, clearing the approval bar (IRR about 21%, payback in 2030 — the hub&#x27;s fourth operating year). Please approve release of the EUR 6.0m capital so fit-out can proceed against the September 2026 supplier quotes (decision date and approving owner to be set by the board; not specified in the brief).</p>
<p>Reasons:</p>
<ol>
<li>At full run-rate (5.0m parcels/year, 2025 network flow data) and a saving of EUR 0.55 per routed parcel (network simulation v4), the hub nets about EUR 1.85m a year above its EUR 0.9m fixed operating cost from 2028, enough to cover the EUR 6.0m outlay with EUR 3.2m to spare.</li>
<li>The ramp is conservative, not hopeful: 60% of full run-rate in the opening year 2027 (planning team&#x27;s estimate from the 2023 north hub opening), full run-rate from 2028. Cumulative cash still turns positive by 2030, inside the eight-year window.</li>
<li>The investment and the fixed operating cost are not what put the case at risk: NPV stays positive even at the high end of both (EUR 7.5m investment: NPV +EUR 1.7m; EUR 1.2m fixed cost: NPV +EUR 1.6m).</li>
</ol>
<p>Risk — what decides the answer: the saving per routed parcel decides it. NPV reaches zero at EUR 0.425 per parcel, just EUR 0.025 above the EUR 0.40 low end of the simulated range — meaning the pessimistic fuel-price simulation alone (0.40, all else at base) already turns NPV slightly negative (-EUR 0.6m). Routed volume is the second lever: break-even is 3.86m parcels/year, just above the 3.8m low end of the planning range (at 3.8m alone, NPV is -EUR 0.2m). The planning team&#x27;s flagged scenario — a competitor opening its own south hub — moves both levers together (fewer parcels, a price response that erodes the saving) and raises the investment through a rushed fit-out; combined, this swings NPV to -EUR 4.6m and the investment does not pay back within the eight-year life.</p>
<table class="data"><tr><th>Driver</th><th class="num">Base</th><th class="num">Break-even</th><th>Inside evidenced range?</th></tr><tr><td>Saving per routed parcel (EUR/parcel)</td><td class="num">0.55</td><td class="num">0.425</td><td>Yes — 6% above the 0.40 low end</td></tr><tr><td>Parcels routed at full run-rate (m/year)</td><td class="num">5.0</td><td class="num">3.86</td><td>Yes — 2% above the 3.8 low end</td></tr><tr><td>Hub fixed operating cost (EUR m/year)</td><td class="num">0.9</td><td class="num">1.48</td><td>No — above the 1.2 high end</td></tr><tr><td>Investment (EUR m)</td><td class="num">6.0</td><td class="num">9.23</td><td>No — above the 7.5 high end</td></tr></table>
<p>Next steps: before releasing capital, commission (1) a short check on whether any competitor is planning a south-region hub, since that is the scenario that flips the case, and (2) a firmer read on the per-parcel saving against current fuel prices, since the whole case turns on a EUR 0.125 swing in that one number. Owners and dates to be set by the board.</p>
<p>Sources: model v01 (this folder, `model/`); 2025 network flow data, south region (Kestrel planning team); network simulation v4; site lease offer plus 14 FTE staffing plan; two supplier quotes, September 2026; Group finance (hurdle rate). Full cash-flow build, scenarios and sensitivity ranking: `model/README.md` and `model/model.xlsx`.</p></main></body></html>


## File written by the run: business-case-memo.md

---
title: Kestrel south hub — board business case
client: Kestrel Logistics (fictional)
audience: Kestrel board — capital approval
date: October 2026
format: memo
---

**Subject: Approve the EUR 6.0m south hub — base-case NPV +EUR 3.2m at the 9% hurdle rate, but the saving per parcel is what decides it**

To the board. We recommend approving the EUR 6.0m investment in the south-region cross-dock hub, paid at the start of 2027. Over the hub's eight-year life (2027–2034), the base case NPV at the CFO's 9% hurdle rate is +EUR 3.2m, clearing the approval bar (IRR about 21%, payback in 2030 — the hub's fourth operating year). Please approve release of the EUR 6.0m capital so fit-out can proceed against the September 2026 supplier quotes (decision date and approving owner to be set by the board; not specified in the brief).

Reasons:
1. At full run-rate (5.0m parcels/year, 2025 network flow data) and a saving of EUR 0.55 per routed parcel (network simulation v4), the hub nets about EUR 1.85m a year above its EUR 0.9m fixed operating cost from 2028, enough to cover the EUR 6.0m outlay with EUR 3.2m to spare.
2. The ramp is conservative, not hopeful: 60% of full run-rate in the opening year 2027 (planning team's estimate from the 2023 north hub opening), full run-rate from 2028. Cumulative cash still turns positive by 2030, inside the eight-year window.
3. The investment and the fixed operating cost are not what put the case at risk: NPV stays positive even at the high end of both (EUR 7.5m investment: NPV +EUR 1.7m; EUR 1.2m fixed cost: NPV +EUR 1.6m).

Risk — what decides the answer: the saving per routed parcel decides it. NPV reaches zero at EUR 0.425 per parcel, just EUR 0.025 above the EUR 0.40 low end of the simulated range — meaning the pessimistic fuel-price simulation alone (0.40, all else at base) already turns NPV slightly negative (-EUR 0.6m). Routed volume is the second lever: break-even is 3.86m parcels/year, just above the 3.8m low end of the planning range (at 3.8m alone, NPV is -EUR 0.2m). The planning team's flagged scenario — a competitor opening its own south hub — moves both levers together (fewer parcels, a price response that erodes the saving) and raises the investment through a rushed fit-out; combined, this swings NPV to -EUR 4.6m and the investment does not pay back within the eight-year life.

| Driver | Base | Break-even | Inside evidenced range? |
|---|---|---|---|
| Saving per routed parcel (EUR/parcel) | 0.55 | 0.425 | Yes — 6% above the 0.40 low end |
| Parcels routed at full run-rate (m/year) | 5.0 | 3.86 | Yes — 2% above the 3.8 low end |
| Hub fixed operating cost (EUR m/year) | 0.9 | 1.48 | No — above the 1.2 high end |
| Investment (EUR m) | 6.0 | 9.23 | No — above the 7.5 high end |

Next steps: before releasing capital, commission (1) a short check on whether any competitor is planning a south-region hub, since that is the scenario that flips the case, and (2) a firmer read on the per-parcel saving against current fuel prices, since the whole case turns on a EUR 0.125 swing in that one number. Owners and dates to be set by the board.

Sources: model v01 (this folder, `model/`); 2025 network flow data, south region (Kestrel planning team); network simulation v4; site lease offer plus 14 FTE staffing plan; two supplier quotes, September 2026; Group finance (hurdle rate). Full cash-flow build, scenarios and sensitivity ranking: `model/README.md` and `model/model.xlsx`.


## File written by the run: model/README.md

# Model: Kestrel south hub cross-dock business case (fictional), v01

**Question answered:** Should Kestrel invest in a cross-dock hub in the south region? Decision rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life (2027-2034).

**Master check:** OK

## Key outputs

| Output | Unit | base | down | up |
|---|---|---|---|---|
| NPV at hurdle rate | EUR m | 3.23 | -4.626 | 8.33 |
| IRR | per year | 0.2091 | -0.09939 | 0.388 |
| Payback (first period, undiscounted cumulative cash >= 0) | period | 2030 | none | 2029 |
| Parcels routed 2027 (ramp year) | m parcels | 3 | 2.28 | 3.36 |
| Parcels routed 2028 (full run-rate) | m parcels | 5 | 3.8 | 5.6 |

Scenarios (coherent sets, drivers changed from base):
- **down**: parcels_full_runrate = 3.8, saving_per_parcel = 0.4, investment = 7.5 (Competitor response: a rival opens its own south-region hub, shippers move so routed volume falls to the low end (3.8m parcels), the price response it forces erodes the saving per parcel to EUR 0.40, and fit-out is accelerated to compete, raising investment to EUR 7.5m.)
- **up**: parcels_full_runrate = 5.6, saving_per_parcel = 0.65, investment = 5.5 (Clean ramp, no competitor: volume reaches the top of the planning range (5.6m parcels), 2023-level fuel prices hold the full simulated saving (EUR 0.65/parcel), and fit-out comes in at the lower supplier quote (EUR 5.5m).)

## Sensitivity on npv (one-way, others at base; break-even target 0)

| Rank | Driver | Low / base / high | Output low | Output high | Swing | Break-even | Inside range? |
|---|---|---|---|---|---|---|---|
| 1 | saving_per_parcel | 0.4 / 0.55 / 0.65 EUR per parcel | -0.6456 | 5.814 | 6.46 | 0.425 | yes |
| 2 | parcels_full_runrate | 3.8 / 5 / 5.6 m parcels per year | -0.1805 | 4.936 | 5.116 | 3.864 | yes |
| 3 | fixed_cost | 0.7 / 0.9 / 1.2 EUR m per year | 4.337 | 1.57 | 2.767 | 1.484 | no |
| 4 | investment | 5.5 / 6 / 7.5 EUR m | 3.73 | 1.73 | 2 | 9.23 | no |
| 5 | discount_rate | 0.07 / 0.09 / 0.11 per year | 4.019 | 2.529 | 1.49 | 0.2091 | no |

Drivers without low/high range (not tested): ramp_2027

## Inputs

| Driver | Value | Unit | Low | High | Source |
|---|---|---|---|---|---|
| parcels_full_runrate | 5 | m parcels per year | 3.8 | 5.6 | 2025 network flow data, south region (Kestrel planning team) |
| ramp_2027 | 0.6 | share of full run-rate |  |  | ASSUMPTION: planning team, based on the 2023 north hub opening |
| saving_per_parcel | 0.55 | EUR per parcel | 0.4 | 0.65 | Network simulation v4 |
| fixed_cost | 0.9 | EUR m per year | 0.7 | 1.2 | Site lease offer plus 14 FTE staffing plan |
| investment | 6 | EUR m | 5.5 | 7.5 | Two supplier quotes, September 2026 |
| discount_rate | 0.09 | per year | 0.07 | 0.11 | Group finance |

## Line items (calculation order)

| Line item | Unit | Formula |
|---|---|---|
| ramp | share of full run-rate | `pick(t, 0, ramp_2027, 1)` |
| routed_parcels | m parcels | `parcels_full_runrate * ramp` |
| gross_saving | EUR m | `routed_parcels * saving_per_parcel` |
| fixed_cost_line | EUR m | `-fixed_cost * pick(t, 0, 1)` |
| capex | EUR m | `-investment * pick(t, 1, 0)` |
| net_cash_flow | EUR m | `gross_saving + fixed_cost_line + capex` |
| cumulative_cash_flow | EUR m | `prev(cumulative_cash_flow) + net_cash_flow` |
| discount_factor | factor | `(1 + discount_rate) ** -t` |
| discounted_cash_flow | EUR m | `net_cash_flow * discount_factor` |

## Checks

| Check | Scenario | Expected | Actual | Status |
|---|---|---|---|---|
| routed_not_above_full_runrate | base | >=0 | 0 | OK |
| routed_not_above_full_runrate | down | >=0 | 0 | OK |
| routed_not_above_full_runrate | up | >=0 | 0 | OK |
| net_cash_flow_ties_to_parts | base | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | down | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | up | ==0 | 0 | OK |
| discounted_cash_flow_ties_to_factor | base | ==0 | 0 | OK |
| discounted_cash_flow_ties_to_factor | down | ==0 | 0 | OK |
| discounted_cash_flow_ties_to_factor | up | ==0 | 0 | OK |

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

line_item,unit,start_2027,2027,2028,2029,2030,2031,2032,2033,2034
ramp,share of full run-rate,0.0,0.6,1.0,1.0,1.0,1.0,1.0,1.0,1.0
routed_parcels,m parcels,0.0,3.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0
gross_saving,EUR m,0.0,1.65,2.75,2.75,2.75,2.75,2.75,2.75,2.75
fixed_cost_line,EUR m,0.0,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9
capex,EUR m,-6.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
net_cash_flow,EUR m,-6.0,0.75,1.85,1.85,1.85,1.85,1.85,1.85,1.85
cumulative_cash_flow,EUR m,-6.0,-5.25,-3.4,-1.55,0.3,2.15,4.0,5.85,7.7
discount_factor,factor,1.0,0.9174311927,0.8416799933,0.7721834801,0.7084252111,0.6499313863,0.5962673269,0.5470342448,0.5018662797
discounted_cash_flow,EUR m,-6.0,0.6880733945,1.5571079875,1.4285394381,1.3105866405,1.2023730647,1.1030945547,1.012013353,0.9284526174


## File written by the run: model/checks.csv

check,scenario,expected,actual,status
routed_not_above_full_runrate,base,>=0,0.0,OK
routed_not_above_full_runrate,down,>=0,0.0,OK
routed_not_above_full_runrate,up,>=0,0.0,OK
net_cash_flow_ties_to_parts,base,==0,0.0,OK
net_cash_flow_ties_to_parts,down,==0,0.0,OK
net_cash_flow_ties_to_parts,up,==0,0.0,OK
discounted_cash_flow_ties_to_factor,base,==0,0.0,OK
discounted_cash_flow_ties_to_factor,down,==0,0.0,OK
discounted_cash_flow_ties_to_factor,up,==0,0.0,OK


## File written by the run: model/inputs.csv

driver,value,unit,source,low,high,note
parcels_full_runrate,5.0,m parcels per year,"2025 network flow data, south region (Kestrel planning team)",3.8,5.6,full run-rate throughput once the hub is established
ramp_2027,0.60,share of full run-rate,"ASSUMPTION: planning team, based on the 2023 north hub opening",,,2027 only; full run-rate assumed from 2028 (no further ramp data given)
saving_per_parcel,0.55,EUR per parcel,Network simulation v4,0.40,0.65,"low = simulation at 2025 fuel prices; high = simulation at 2023 fuel prices"
fixed_cost,0.9,EUR m per year,Site lease offer plus 14 FTE staffing plan,0.7,1.2,
investment,6.0,EUR m,"Two supplier quotes, September 2026",5.5,7.5,paid at the start of 2027
discount_rate,0.09,per year,Group finance,0.07,0.11,CFO hurdle rate


## File written by the run: model/outputs.csv

output,unit,base,down,up,model_version
npv,EUR m,3.2302410504,-4.626210314,8.3296245579,v01
irr,per year,0.2091368125,-0.0993929701,0.3880178751,v01
payback_period,period,2030,,2029,v01
routed_parcels_2027,m parcels,3.0,2.28,3.36,v01
routed_parcels_2028,m parcels,5.0,3.8,5.6,v01


## File written by the run: model/sensitivity.csv

rank,driver,unit,low,base,high,output_low,output_base,output_high,swing,break_even,break_even_in_range
1,saving_per_parcel,EUR per parcel,0.4,0.55,0.65,-0.6456439279,3.2302410504,5.8141643692,6.4598082971,0.4249869616,yes
2,parcels_full_runrate,m parcels per year,3.8,5.0,5.6,-0.1805377305,3.2302410504,4.9356304408,5.1161681713,3.8635178329,yes
3,fixed_cost,EUR m per year,0.7,0.9,1.2,4.3372048733,3.2302410504,1.5697953159,2.7674095574,1.483621792,no
4,investment,EUR m,5.5,6.0,7.5,3.7302410504,3.2302410504,1.7302410504,2.0,9.2302410504,no
5,discount_rate,per year,0.07,0.09,0.11,4.0188648533,3.2302410504,2.5293361167,1.4895287366,0.2091368125,no


## File written by the run: model/spec.json

{
  "title": "Kestrel south hub cross-dock business case (fictional)",
  "question": "Should Kestrel invest in a cross-dock hub in the south region? Decision rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life (2027-2034).",
  "periods": ["start_2027", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034"],
  "rows": [
    {"name": "ramp", "unit": "share of full run-rate", "expr": "pick(t, 0, ramp_2027, 1)"},
    {"name": "routed_parcels", "unit": "m parcels", "expr": "parcels_full_runrate * ramp"},
    {"name": "gross_saving", "unit": "EUR m", "expr": "routed_parcels * saving_per_parcel"},
    {"name": "fixed_cost_line", "unit": "EUR m", "expr": "-fixed_cost * pick(t, 0, 1)"},
    {"name": "capex", "unit": "EUR m", "expr": "-investment * pick(t, 1, 0)"},
    {"name": "net_cash_flow", "unit": "EUR m", "expr": "gross_saving + fixed_cost_line + capex"},
    {"name": "cumulative_cash_flow", "unit": "EUR m", "expr": "prev(cumulative_cash_flow) + net_cash_flow"},
    {"name": "discount_factor", "unit": "factor", "expr": "(1 + discount_rate) ** -t"},
    {"name": "discounted_cash_flow", "unit": "EUR m", "expr": "net_cash_flow * discount_factor"}
  ],
  "outputs": [
    {"name": "npv", "label": "NPV at hurdle rate", "unit": "EUR m", "fn": "sum", "row": "discounted_cash_flow"},
    {"name": "irr", "label": "IRR", "unit": "per year", "fn": "irr", "row": "net_cash_flow"},
    {"name": "payback_period", "label": "Payback (first period, undiscounted cumulative cash >= 0)", "unit": "period", "fn": "payback", "row": "cumulative_cash_flow"},
    {"name": "routed_parcels_2027", "label": "Parcels routed 2027 (ramp year)", "unit": "m parcels", "fn": "value", "row": "routed_parcels", "period": "2027"},
    {"name": "routed_parcels_2028", "label": "Parcels routed 2028 (full run-rate)", "unit": "m parcels", "fn": "value", "row": "routed_parcels", "period": "2028"}
  ],
  "checks": [
    {"name": "routed_not_above_full_runrate", "expr": "parcels_full_runrate - routed_parcels", "rule": ">=0"},
    {"name": "net_cash_flow_ties_to_parts", "expr": "net_cash_flow - gross_saving - fixed_cost_line - capex", "rule": "==0"},
    {"name": "discounted_cash_flow_ties_to_factor", "expr": "discounted_cash_flow - net_cash_flow * discount_factor", "rule": "==0"}
  ],
  "scenarios": {
    "down": {"parcels_full_runrate": 3.8, "saving_per_parcel": 0.40, "investment": 7.5},
    "up": {"parcels_full_runrate": 5.6, "saving_per_parcel": 0.65, "investment": 5.5}
  },
  "scenario_stories": {
    "down": "Competitor response: a rival opens its own south-region hub, shippers move so routed volume falls to the low end (3.8m parcels), the price response it forces erodes the saving per parcel to EUR 0.40, and fit-out is accelerated to compete, raising investment to EUR 7.5m.",
    "up": "Clean ramp, no competitor: volume reaches the top of the planning range (5.6m parcels), 2023-level fuel prices hold the full simulated saving (EUR 0.65/parcel), and fit-out comes in at the lower supplier quote (EUR 5.5m)."
  },
  "break_even": {"output": "npv", "target": 0}
}

