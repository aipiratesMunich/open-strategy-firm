# fm-01-hub-business-case on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (12/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States question, outputs, and decision threshold (NPV>0 at 9%) before building | yes | README.md: 'Question: Should Kestrel invest in a cross-dock hub in the south region? Threshold: NPV at the 9% hurdle rate above zero...' followed by 'Answer in numbers' and 'Decided by' before the detailed build sections (inputs, line items, checks). |
| Separates inputs, calculations, outputs; no bare numbers in formulas except 0/1 or documented conversions | yes | inputs.csv, calc.csv, outputs.csv are distinct files; spec.json formulas use named drivers e.g. 'parcels * saving_per_parcel', 'pick(t, 0, ramp_2027, 1)', '-investment * pick(t, 1, 0)' — only 0/1 literals appear. |
| Base NPV within EUR 3.1-3.4m and payback in 2030/year 4 | yes | outputs.csv: npv base = 3.2302410504; payback_period base = 2030. |
| Tornado ranking with saving per parcel first, parcels routed second | yes | sensitivity.csv: rank 1 saving_per_parcel, rank 2 full_run_rate_parcels. |
| Break-even values given for saving per parcel (~0.42-0.43) and parcels (~3.8-3.9m), both flagged inside range | yes | sensitivity.csv: saving_per_parcel break_even 0.4249869616 (yes); full_run_rate_parcels break_even 3.8635178329 (yes). |
| In-range break-even surfaced in headline/decided-by line, not just appendix | yes | README 'Decided by' line: 'both break-even inside the evidence range'; also stated in chat response headline and board memo. |
| Down case is coherent competitor-hub story (fewer parcels, lower saving, higher investment), NPV negative | yes | spec.json scenario_stories.down: 'Competitor opens a rival hub nearby... low-end volume... low-end saving... high-end investment'; outputs.csv npv down = -4.626210314. |
| Checks block plus two outputs recomputed by hand with both numbers recorded | yes | checks.csv present; README Spot test: 'NPV: model EUR 3.230m, by hand EUR 3.230m... Payback: model 2030... by hand... ≈ 3.8 years.' |
| 60% ramp listed as flagged assumption | yes | README Flags: 'Drivers flagged as assumptions (no source or source starts with "assumption"): ramp_2027'. |
| 'What the deck should say' sentences carry model version | yes | Each bullet ends with '(model v01)', e.g. 'Base case clears the CFO's hurdle... (model v01).' |
| Must not present NPV without range/scenarios | yes | All NPV mentions include base/down/up, e.g. 'NPV (9% hurdle...): base +3.23, down -4.63, up +8.33.' |
| Must not add terminal value/tax without flagging departure | yes | README: 'No terminal value and no tax, per the agreed screening convention' — explicitly flags this as the agreed convention rather than silently adding them. |

## Transcript

## Turn 1

**User:** Build the business case for the Kestrel south hub from these inputs. Board needs NPV, payback and what decides the answer. (Attached in the working directory: fm-01-input.md.)

Built the business case and model, with the board's three questions answered directly.

**NPV (9% hurdle, 2027–2034, EUR m):** base **+3.23**, down **-4.63**, up **+8.33**. IRR 21%, **payback ~3.8 years** (within 2030).

**What decides the answer:** the saving per routed parcel and the hub's routed volume are the two drivers that matter — both break even *inside* the quoted evidence ranges (EUR 0.425/parcel vs. quoted low of 0.40; 3.86m parcels vs. quoted low of 3.8m). These are exactly the two levers the planning team flagged a competitor response would pull together, plus a costlier fit-out. Modelled as one combined scenario (not three independent lows), that single story flips NPV to **-4.63m** — a decisive reversal, not a rounding risk. Fixed cost, investment size, discount rate, and the 2027 ramp assumption are not decisive on their own.

Delivered:
- `model/` — inputs.csv, spec.json, calc.csv, outputs.csv, checks.csv (master check: OK), sensitivity.csv, model.xlsx (live formulas), and README.md with the full handover (question, answer, spot-test by hand, tornado, scenarios, known weaknesses, what the deck should say).
- `kestrel-south-hub-board-memo.md` — a one-page board memo stating the recommendation, the numbers, what decides it, and a concrete next step (ask the planning team what it already knows about competitor hub plans, before the board commits EUR 6.0m).

Recommendation in the memo: approve conditional on that competitor-intelligence checkpoint, rather than an unconditional approval — the base case clears the hurdle, but the one risk the planning team already named is big enough to flip it.


## Files in work dir after run

- fm-01-input.md
- kestrel-south-hub-board-memo.md
- model/README.md
- model/calc.csv
- model/checks.csv
- model/inputs.csv
- model/model.xlsx
- model/outputs.csv
- model/sensitivity.csv
- model/spec.json

## File written by the run: kestrel-south-hub-board-memo.md

**Subject: Base case clears the 9% hurdle (NPV +EUR 3.2m), but the business case is not robust to the one risk the planning team already flagged**

To: the Board. We recommend approving the EUR 6.0m south hub investment only alongside a named checkpoint on competitor hub plans, not as an unconditional approval. On the numbers alone the base case passes the CFO's rule — NPV at 9% is positive — but a single, specific, already-identified risk flips it to a loss of similar size. Please decide at the next board meeting whether to (a) approve outright, (b) approve with the checkpoint below, or (c) commission the evidence first.

**The numbers (model v01, 2026-10-14):**
- **NPV at 9%: EUR +3.2m** base case (down case EUR -4.6m; up case EUR +8.3m).
- **IRR: 21%. Payback: about 3.8 years** from the start of 2027 (within 2030, the fourth operating year).
- Built from 5.0m parcels/year at full run-rate (60% ramp in 2027), a EUR 0.55 saving per routed parcel, EUR 0.9m/year fixed operating cost, and the EUR 6.0m fit-out, discounted over the hub's eight-year life with no terminal value and no tax, per the agreed screening convention.

**What decides the answer:**
1. Two drivers — the saving per routed parcel and the volume routed through the hub — carry almost all the uncertainty, and both break even *inside* the evidence range already on file, not safely outside it: the saving only needs to fall to EUR 0.425/parcel (the quoted low case is EUR 0.40) and volume only needs to fall to 3.86m parcels (the quoted low case is 3.8m) for NPV to turn negative.
2. These are exactly the two levers the planning team's own note says move together if a competitor opens a rival hub nearby — plus a costlier, accelerated fit-out. Modelled as one combined scenario rather than three separate low draws, that story alone produces NPV EUR -4.6m: a decisive flip, not a marginal one.
3. By contrast, the hub's fixed cost, the investment amount and the discount rate would each have to move far outside their quoted ranges to change the answer on their own, and the 2027 ramp assumption barely moves NPV at all. The case is not fragile in general — it is fragile to this one specific, named risk.

**Risk and what would change the answer:** Kestrel has no current evidence on whether or when a competitor would open a south-region hub. If the board wants a number before committing EUR 6.0m, the cheapest test is to ask the planning/network team for whatever competitor-intelligence or site-leasing signals they already track for the south region, rather than commissioning new research. We recommend that as the pre-commitment check, with a go/no-go built around it rather than silence.

**Next steps:** planning team to report what it knows on competitor hub plans in the south region by the next board cycle; finance to hold the EUR 6.0m within the capital plan pending that input; board to confirm the 9% hurdle rate and the no-terminal-value convention still stand before sign-off.

Sources: 2025 network flow data and planning-team ramp assumption (south region); Network simulation v4 (saving per parcel, fuel-price low/high); site lease offer and 14-FTE staffing plan (fixed cost); two supplier quotes, September 2026 (investment); Group finance (hurdle rate). Full model, inputs, checks, sensitivity table and spreadsheet: `model/README.md`, `model/inputs.csv`, `model/sensitivity.csv`, `model/model.xlsx` (v01).


## File written by the run: model/README.md

# Model: Kestrel south hub cross-dock business case, v01, 2026-10-14

**Question:** Should Kestrel invest in a cross-dock hub in the south region? Threshold: NPV at the 9% hurdle rate above zero over the hub's eight-year life (2027-2034).
**Answer in numbers:** NPV base EUR +3.23m (down EUR -4.63m, up EUR +8.33m); IRR base 20.9%; payback base year 2030, about 3.8 years from the start of 2027.
**Decided by:** saving per routed parcel and the volume routed through the hub — both break-even inside their evidence range, and both move together (down) if a competitor opens a rival hub nearby. See "What decides the answer" below.
**Master check:** OK
**Spot test:** NPV: model EUR 3.230m, by hand EUR 3.230m (discounted cash flows -6.00, 0.688, 1.557, 1.429, 1.311, 1.202, 1.103, 1.012, 0.929 summed). Payback: model 2030 (first year cumulative cash >= 0), by hand cumulative cash -6.00 / -5.25 / -3.40 / -1.55 / +0.30 at t=0..4, i.e. 3 + 1.55/1.85 ≈ 3.8 years.

## What decides the answer

Two drivers carry almost all the uncertainty in the tornado below, and their break-even values sit inside the evidence range, not safely outside it:
- **Saving per routed parcel**: NPV turns negative below EUR 0.425/parcel — only EUR 0.03 under the quoted low case (EUR 0.40, itself a 2025-fuel-price simulation, not a hypothetical).
- **Full run-rate volume**: NPV turns negative below 3.86m parcels/year — only 60k parcels under the quoted low case (3.8m).

Both are exactly the two levers the planning team's note says a competitor response would pull **at the same time** (fewer parcels routed, and a price response that erodes the saving), together with a costlier, accelerated fit-out. Modelled as one coherent "down" scenario rather than three independent low draws, it produces NPV EUR -4.63m — a decisive flip, not a marginal one. Hub fixed cost, the investment amount and the discount rate all have break-even values well outside their quoted ranges and do not, on their own, change the answer; the 2027 ramp assumption barely moves NPV at all (it dilutes one year of cash flow, not the structural economics).

## Key outputs

| Output | Unit | base | down | up |
|---|---|---|---|---|
| NPV at hurdle rate | EUR m | 3.23 | -4.626 | 8.33 |
| IRR | per year | 0.2091 | -0.09939 | 0.388 |
| Payback (first period cumulative cash >= 0) | year | 2030 | none | 2029 |
| Parcels routed, 2027 (ramp year) | m parcels | 3 | 2.28 | 3.36 |
| Savings at full run-rate, 2028 | EUR m | 2.75 | 1.52 | 3.64 |

Scenarios (coherent sets, drivers changed from base):
- **down**: full_run_rate_parcels = 3.8, saving_per_parcel = 0.4, investment = 7.5 (Competitor opens a rival hub nearby: shippers partly switch away (low-end volume), the resulting price response eats part of the per-parcel saving (low-end saving), and fit-out is accelerated and costs more (high-end investment).)
- **up**: full_run_rate_parcels = 5.6, saving_per_parcel = 0.65, investment = 5.5 (Ramp holds and network economics run in Kestrel's favour: volume and per-parcel saving both land at the high end of the evidence range, and the fit-out comes in at the low end of the two supplier quotes.)

## Sensitivity on npv (one-way, others at base; break-even target 0)

| Rank | Driver | Low / base / high | Output low | Output high | Swing | Break-even | Inside range? |
|---|---|---|---|---|---|---|---|
| 1 | saving_per_parcel | 0.4 / 0.55 / 0.65 EUR per parcel | -0.6456 | 5.814 | 6.46 | 0.425 | yes |
| 2 | full_run_rate_parcels | 3.8 / 5 / 5.6 m parcels per year | -0.1805 | 4.936 | 5.116 | 3.864 | yes |
| 3 | hub_fixed_cost | 0.7 / 0.9 / 1.2 EUR m per year | 4.337 | 1.57 | 2.767 | 1.484 | no |
| 4 | investment | 5.5 / 6 / 7.5 EUR m | 3.73 | 1.73 | 2 | 9.23 | no |
| 5 | discount_rate | 0.07 / 0.09 / 0.11 per year | 4.019 | 2.529 | 1.49 | 0.2091 | no |
| 6 | ramp_2027 | 0.45 / 0.6 / 0.75 share of full run-rate | 2.852 | 3.609 | 0.7569 | -0.6804 | no |

## Inputs

| Driver | Value | Unit | Low | High | Source |
|---|---|---|---|---|---|
| full_run_rate_parcels | 5 | m parcels per year | 3.8 | 5.6 | 2025 network flow data, south region (Kestrel planning team) |
| ramp_2027 | 0.6 | share of full run-rate | 0.45 | 0.75 | ASSUMPTION: planning team, based on the 2023 north hub opening |
| saving_per_parcel | 0.55 | EUR per parcel | 0.4 | 0.65 | Network simulation v4; low = 2025 fuel prices, high = 2023 fuel prices |
| hub_fixed_cost | 0.9 | EUR m per year | 0.7 | 1.2 | Site lease offer plus 14 FTE staffing plan |
| investment | 6 | EUR m | 5.5 | 7.5 | Two supplier quotes, September 2026 |
| discount_rate | 0.09 | per year | 0.07 | 0.11 | Group finance hurdle rate |

## Line items (calculation order)

| Line item | Unit | Formula |
|---|---|---|
| ramp | share of full run-rate | `pick(t, 0, ramp_2027, 1)` |
| parcels | m parcels per year | `full_run_rate_parcels * ramp` |
| savings | EUR m | `parcels * saving_per_parcel` |
| fixed_cost | EUR m | `-hub_fixed_cost * min(1, t)` |
| capex | EUR m | `-investment * pick(t, 1, 0)` |
| net_cash_flow | EUR m | `savings + fixed_cost + capex` |
| cumulative_cash_flow | EUR m | `prev(cumulative_cash_flow) + net_cash_flow` |
| discount_factor | factor | `(1 + discount_rate) ** -t` |
| discounted_cash_flow | EUR m | `net_cash_flow * discount_factor` |

## Checks

| Check | Scenario | Expected | Actual | Status |
|---|---|---|---|---|
| savings_ties_to_parcels_times_saving | base | ==0 | 0 | OK |
| savings_ties_to_parcels_times_saving | down | ==0 | 0 | OK |
| savings_ties_to_parcels_times_saving | up | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | base | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | down | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | up | ==0 | 0 | OK |
| parcels_not_above_full_run_rate | base | >=0 | 0 | OK |
| parcels_not_above_full_run_rate | down | >=0 | 0 | OK |
| parcels_not_above_full_run_rate | up | >=0 | 0 | OK |
| fixed_cost_not_positive | base | >=0 | 0 | OK |
| fixed_cost_not_positive | down | >=0 | 0 | OK |
| fixed_cost_not_positive | up | >=0 | 0 | OK |

## Flags

- Drivers flagged as assumptions (no source or source starts with 'assumption'): ramp_2027

## Known weaknesses

- **Ramp beyond 2027 is an assumption, not evidence.** The brief gives a sourced ramp only for 2027 (60%, itself based on one comparable, the 2023 north hub); 100% from 2028 is implied by the brief ("full run-rate") rather than separately evidenced. Sensitivity shows this barely matters to NPV (swing EUR 0.76m) because it only dilutes one year of cash flow — if the ramp instead took two or three years to reach full run-rate, re-run with that path before relying on this result.
- **The competitor scenario is one coherent story, not a probability.** It shows the case flips decisively if that story happens; it does not say how likely the story is. No market data on competitor hub plans was in the brief.
- **No terminal value and no tax**, per the agreed screening convention — this understates NPV if the hub keeps operating past 2034, and overstates it to the extent Kestrel would actually pay tax on these savings.
- **Single-point ramp and fixed-cost timing.** Fixed cost is charged in full from 2027; if the lease and hires phase in, early-year cash flow is slightly better than modelled (a minor effect given fixed cost is not a decisive driver).

## What the deck should say

1. Base case clears the CFO's hurdle: NPV EUR +3.2m at 9%, IRR 21%, payback inside four years (model v01).
2. The case is not robust to its own stated risk: a competitor opening a rival hub — pulling volume, the per-parcel saving, and the fit-out cost all the wrong way at once — flips NPV to EUR -4.6m (model v01).
3. The two drivers that decide this (saving per parcel, break-even EUR 0.425; volume, break-even 3.86m parcels) already break even inside the quoted evidence range, not outside it — so this is a real risk, not a theoretical one, and the board should ask what Kestrel knows today about competitor hub plans in the south region before approving, or set a checkpoint tied to that evidence (model v01).

## Files

- `calc.csv`: every line item by period, base case
- `outputs.csv`: key outputs per scenario
- `checks.csv`: check results per scenario
- `sensitivity.csv`: tornado ranking and break-even values
- `model.xlsx`: Inputs (blue on yellow = input), Calc (live formulas), Outputs (live, master check), Sensitivity (values)


## File written by the run: model/calc.csv

line_item,unit,start,2027,2028,2029,2030,2031,2032,2033,2034
ramp,share of full run-rate,0.0,0.6,1.0,1.0,1.0,1.0,1.0,1.0,1.0
parcels,m parcels per year,0.0,3.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0
savings,EUR m,0.0,1.65,2.75,2.75,2.75,2.75,2.75,2.75,2.75
fixed_cost,EUR m,0.0,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9
capex,EUR m,-6.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
net_cash_flow,EUR m,-6.0,0.75,1.85,1.85,1.85,1.85,1.85,1.85,1.85
cumulative_cash_flow,EUR m,-6.0,-5.25,-3.4,-1.55,0.3,2.15,4.0,5.85,7.7
discount_factor,factor,1.0,0.9174311927,0.8416799933,0.7721834801,0.7084252111,0.6499313863,0.5962673269,0.5470342448,0.5018662797
discounted_cash_flow,EUR m,-6.0,0.6880733945,1.5571079875,1.4285394381,1.3105866405,1.2023730647,1.1030945547,1.012013353,0.9284526174


## File written by the run: model/checks.csv

check,scenario,expected,actual,status
savings_ties_to_parcels_times_saving,base,==0,0.0,OK
savings_ties_to_parcels_times_saving,down,==0,0.0,OK
savings_ties_to_parcels_times_saving,up,==0,0.0,OK
net_cash_flow_ties_to_parts,base,==0,0.0,OK
net_cash_flow_ties_to_parts,down,==0,0.0,OK
net_cash_flow_ties_to_parts,up,==0,0.0,OK
parcels_not_above_full_run_rate,base,>=0,0.0,OK
parcels_not_above_full_run_rate,down,>=0,0.0,OK
parcels_not_above_full_run_rate,up,>=0,0.0,OK
fixed_cost_not_positive,base,>=0,0.0,OK
fixed_cost_not_positive,down,>=0,0.0,OK
fixed_cost_not_positive,up,>=0,0.0,OK


## File written by the run: model/inputs.csv

driver,value,unit,source,low,high,note
full_run_rate_parcels,5.0,m parcels per year,"2025 network flow data, south region (Kestrel planning team)",3.8,5.6,volume routed through the hub once ramp is complete
ramp_2027,0.60,share of full run-rate,"ASSUMPTION: planning team, based on the 2023 north hub opening",0.45,0.75,no numeric range given; widened +/-15pp as the base case rests on one comparable
saving_per_parcel,0.55,EUR per parcel,"Network simulation v4; low = 2025 fuel prices, high = 2023 fuel prices",0.40,0.65,shorter line-haul and fewer handlings
hub_fixed_cost,0.9,EUR m per year,Site lease offer plus 14 FTE staffing plan,0.7,1.2,lease plus staffing
investment,6.0,EUR m,"Two supplier quotes, September 2026",5.5,7.5,"building fit-out and sorter, paid at start of 2027"
discount_rate,0.09,per year,Group finance hurdle rate,0.07,0.11,CFO rule: approve if NPV above zero at this rate


## File written by the run: model/outputs.csv

output,unit,base,down,up,model_version
npv,EUR m,3.2302410504,-4.626210314,8.3296245579,v01
irr,per year,0.2091368125,-0.0993929701,0.3880178751,v01
payback_period,year,2030,,2029,v01
parcels_2027,m parcels,3.0,2.28,3.36,v01
savings_2028,EUR m,2.75,1.52,3.64,v01


## File written by the run: model/sensitivity.csv

rank,driver,unit,low,base,high,output_low,output_base,output_high,swing,break_even,break_even_in_range
1,saving_per_parcel,EUR per parcel,0.4,0.55,0.65,-0.6456439279,3.2302410504,5.8141643692,6.4598082971,0.4249869616,yes
2,full_run_rate_parcels,m parcels per year,3.8,5.0,5.6,-0.1805377305,3.2302410504,4.9356304408,5.1161681713,3.8635178329,yes
3,hub_fixed_cost,EUR m per year,0.7,0.9,1.2,4.3372048733,3.2302410504,1.5697953159,2.7674095574,1.483621792,no
4,investment,EUR m,5.5,6.0,7.5,3.7302410504,3.2302410504,1.7302410504,2.0,9.2302410504,no
5,discount_rate,per year,0.07,0.09,0.11,4.0188648533,3.2302410504,2.5293361167,1.4895287366,0.2091368125,no
6,ramp_2027,share of full run-rate,0.45,0.6,0.75,2.8518006834,3.2302410504,3.6086814173,0.7568807339,-0.680350089,no


## File written by the run: model/spec.json

{
  "title": "Kestrel south hub cross-dock business case",
  "question": "Should Kestrel invest EUR 6.0m in a cross-dock hub in the south region? CFO rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life (2027-2034).",
  "periods": ["start", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034"],
  "rows": [
    {"name": "ramp", "unit": "share of full run-rate", "expr": "pick(t, 0, ramp_2027, 1)"},
    {"name": "parcels", "unit": "m parcels per year", "expr": "full_run_rate_parcels * ramp"},
    {"name": "savings", "unit": "EUR m", "expr": "parcels * saving_per_parcel"},
    {"name": "fixed_cost", "unit": "EUR m", "expr": "-hub_fixed_cost * min(1, t)"},
    {"name": "capex", "unit": "EUR m", "expr": "-investment * pick(t, 1, 0)"},
    {"name": "net_cash_flow", "unit": "EUR m", "expr": "savings + fixed_cost + capex"},
    {"name": "cumulative_cash_flow", "unit": "EUR m", "expr": "prev(cumulative_cash_flow) + net_cash_flow"},
    {"name": "discount_factor", "unit": "factor", "expr": "(1 + discount_rate) ** -t"},
    {"name": "discounted_cash_flow", "unit": "EUR m", "expr": "net_cash_flow * discount_factor"}
  ],
  "outputs": [
    {"name": "npv", "label": "NPV at hurdle rate", "unit": "EUR m", "fn": "sum", "row": "discounted_cash_flow"},
    {"name": "irr", "label": "IRR", "unit": "per year", "fn": "irr", "row": "net_cash_flow"},
    {"name": "payback_period", "label": "Payback (first period cumulative cash >= 0)", "unit": "year", "fn": "payback", "row": "cumulative_cash_flow"},
    {"name": "parcels_2027", "label": "Parcels routed, 2027 (ramp year)", "unit": "m parcels", "fn": "value", "row": "parcels", "period": "2027"},
    {"name": "savings_2028", "label": "Savings at full run-rate, 2028", "unit": "EUR m", "fn": "value", "row": "savings", "period": "2028"}
  ],
  "checks": [
    {"name": "savings_ties_to_parcels_times_saving", "expr": "savings - parcels * saving_per_parcel", "rule": "==0"},
    {"name": "net_cash_flow_ties_to_parts", "expr": "net_cash_flow - savings - fixed_cost - capex", "rule": "==0"},
    {"name": "parcels_not_above_full_run_rate", "expr": "full_run_rate_parcels - parcels", "rule": ">=0"},
    {"name": "fixed_cost_not_positive", "expr": "-fixed_cost", "rule": ">=0"}
  ],
  "scenarios": {
    "down": {"full_run_rate_parcels": 3.8, "saving_per_parcel": 0.40, "investment": 7.5},
    "up": {"full_run_rate_parcels": 5.6, "saving_per_parcel": 0.65, "investment": 5.5}
  },
  "scenario_stories": {
    "down": "Competitor opens a rival hub nearby: shippers partly switch away (low-end volume), the resulting price response eats part of the per-parcel saving (low-end saving), and fit-out is accelerated and costs more (high-end investment).",
    "up": "Ramp holds and network economics run in Kestrel's favour: volume and per-parcel saving both land at the high end of the evidence range, and the fit-out comes in at the low end of the two supplier quotes."
  },
  "break_even": {"output": "npv", "target": 0}
}

