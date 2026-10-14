# cme-01-czech-medical on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/13 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States decision question with minimum bar (EUR 6m, 8% EBIT by 2030, EUR 5m) and kill criteria before analysing | yes | '## Minimum bar agreed by the board' lists 'Revenue at least EUR 6m and EBIT margin at least 8%... Capital: up to EUR 5m... Kill/exit trigger: if the bar is missed by end of 2029' placed before the 'Is the market attractive?' analysis sections |
| Sizes segment top-down (~EUR 31.5m) and bottom-up (~EUR 25.7m) and explains/flags the difference | NO | 'Medical/pharmacy segment ≈ EUR 31.5m/yr... 3-region pharmacy-only pool ≈ EUR 25.65m/yr... Both figures are well above the EUR 6m bar' — the two figures are given but the gap itself (hospitals/labs exclusion vs national/pharmacy scope) is never explained or explicitly flagged as the reason for the d |
| Builds ramp from reps x win rate and arrives at ~EUR 4.0-4.6m revenue in 2030, below EUR 6m bar | yes | '3 reps planned... 40 accounts/rep/year'; table shows 'New adds 120' (3x40) per year, 2030 Revenue 'EUR 4.04m' |
| Computes 2030 EBIT margin below 8% (about 1% to 5%) | yes | 2030 row: 'EUR 0.06m / 1.4%' |
| Models at least one aggressive incumbent reaction using 2024 price-cut evidence and reports effect | yes | 'Modeling the 2024 precedent (incumbent defends share, cutting Kestrel's effective win rate by ~25%...) 2030 accounts = 377, revenue = EUR 3.58m, EBIT = –EUR 0.08m (–2.2% margin)' |
| States the EUR 120k study is sunk and plays no role | NO | No mention of the EUR 120k study cost or sunk-cost treatment anywhere in the answer page; study is referenced only as a data source ('2026 market study (commissioned by Kestrel)') |
| Compares with Austrian alternative per euro of capital and flags it as a management estimate to test | yes | Table row 'EBIT / capital cap / ~17.5% / ~1.1% / ~13.9%' under a column headed 'Kestrel Austria extension (management estimate)' |
| Does not approve the briefed 3-rep plan; answer is do-not-enter/enter-later/conditional with stage gate and says what would make board revisit | yes | 'Enter later, under conditions — do not approve the sales plan as scoped... if either validates, resize to 5 reps and enter; if neither does, do not enter at all'; 'What would change the answer' section lists triggers |
| Compares at least two entry modes on cost, speed, control and exit cost | NO | 'A distributor or partnership mode is not costed in the materials given; directionally it would likely lower the fixed-cost base... at the cost of control, margin capture, and speed... this cannot be quantified without additional data' — only one mode (own depot) is actually costed; no exit-cost com |
| Writes exit criteria and exit cost | NO | 'Kill/exit trigger: if the bar is missed by end of 2029, the board wants a way out (no exit mechanics defined yet — see Open questions)' — exit criteria stated but exit cost explicitly left uncomputed and deferred to a specialist open question |
| Flags that Austrian win rates and prices may not transfer to CZ and names the test | yes | 'the entire ramp rests on one unverified transfer — Austria's 40-accounts/rep/year... would rise with a short local pilot'; 'Price / Unknown CZ price point; model uses the flat EUR 9,500/account planning convention' |
| Must not recommend unconditional entry on strength of EUR 210m headline | yes | Recommendation is 'Enter later, under conditions — do not approve the sales plan as scoped', not unconditional entry |
| Must not invent Czech regulatory requirements, competitor names, or wage levels as facts | yes | 'CZ-specific medical/pharma courier rules... are unknown' listed as open/specialist item rather than asserted fact; no invented competitor names or wage figures beyond those given |

## Transcript

## Turn 1

**User:** Work the Kestrel Czech entry case from the briefing. Quick case, answer page for the board. (Attached in the working directory: cme-01-input.md.)

The 3-rep plan as scoped misses the board's bar: built bottom-up from Kestrel's own Austria account economics (40 accounts/rep/year, 8% churn, 70% variable cost, EUR 9,500/account), it reaches only **EUR 4.0m revenue and 1.4% EBIT margin by 2030** against a EUR 6m / 8% bar — and it's still underwater at the board's own end-2029 checkpoint. That miss holds across downside (incumbent price-reaction precedent) and upside (lower churn) cases, so it's a selling-capacity problem, not a margin problem — fixed-cost leverage means margin recovers fast once revenue nears EUR 6m.

Saved the full answer page to `case-market-entry-kestrel-czech.md`. Headline recommendation: **enter later, under conditions** — don't approve the 3-rep plan; a 5-rep resizing models to EUR 6.0–6.7m / 7.8–10.3% margin (clearing the bar, but only a near-miss under a repeated incumbent reaction), and it should be greenlit only after validating CZ rep productivity and sizing the currently-unsized hospital/lab channel. If neither validates, redirect the capital to the Austria two-region extension already on the table, which is more capital-efficient (~17.5% EBIT/capital-cap vs ~1.1% for the as-scoped Czech plan) though based on a single precedent itself.

Full numbers, scenario tables, assumptions and open questions (including regulatory/labour items for specialists) are in the file.


## Files in work dir after run

- case-market-entry-kestrel-czech.md
- cme-01-input.md

## File written by the run: case-market-entry-kestrel-czech.md

# Market entry: Kestrel Logistics, Czech Republic medical same-day delivery, enter by 2030 board bar?

**Answer:** Enter later, under conditions — do not approve the sales plan as scoped (3 reps from 2027). Built bottom-up from Kestrel's own Austria account economics, that plan reaches only **EUR 3.6–4.2m revenue and –2% to +3% EBIT margin by 2030**, missing the board's EUR 6m / 8% bar in every scenario tested, including the no-incumbent-reaction case. A resized plan (5 reps, same depot) models to **EUR 6.0–6.7m revenue and 7.8–10.3% EBIT margin** — clearing the bar, but only comfortably if the historical incumbent price reaction doesn't repeat against Kestrel specifically. Before the January 2027 board date: validate CZ rep productivity and size the unsized hospital/lab channel; if either validates, resize to 5 reps and enter; if neither does, do not enter at all and redirect capital to the Austria two-region extension already on the table.

**Confidence:** Low-medium, because the entire ramp rests on one unverified transfer — Austria's 40-accounts/rep/year — applied unchanged to a market with an entrenched, price-cutting incumbent; would rise with a short local pilot or interview evidence on CZ-specific win rates.

**Specialists and review:** CZ pharma/medical courier regulation (cold-chain, controlled-substance handling, distribution-practice certification) — legal/regulatory counsel, before the 2027 start. CZ labour law for rep/depot hiring and notice periods — HR/labour counsel, needed to cost the exit criterion below. Recommend a partner-style review of this case before it goes to the board, given how much rests on a single cross-country productivity assumption.

## Minimum bar agreed by the board
- Revenue at least EUR 6m and EBIT margin at least 8% in the Czech business by 2030
- Capital: up to EUR 5m
- Kill/exit trigger: if the bar is missed by end of 2029, the board wants a way out (no exit mechanics defined yet — see Open questions)

## Is the market attractive?

| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Addressable size and growth | Medical/pharmacy segment ≈ EUR 31.5m/yr nationally (EUR 210m B2B same-day × 15%); 3-region pharmacy-only pool ≈ EUR 25.65m/yr (2,700 pharmacies × EUR 9,500). Both figures are well above the EUR 6m bar — size is not the kill factor. | 2026 market study (commissioned by Kestrel) | pass |
| Concentration and incumbents | Two local players hold ~55% of the medical segment. In 2024 the larger incumbent cut price ~12% for 6 months when a new carrier entered — a direct precedent for how Kestrel's own entry would likely be met. | Market study, interviews (single episode, weak evidence) | caution, not an automatic kill, but must be stress-tested (see below) |
| Barriers and regulation | Not covered in the data given. CZ-specific medical/pharma courier rules (cold-chain, controlled substances, GDP-style certification) are unknown. | — | open — specialist input required |

## Can we win?

| Factor | Kestrel (entrant) | Incumbents (combined ~55% share) |
|---|---|---|
| Price | Unknown CZ price point; model uses the flat EUR 9,500/account planning convention, no discounting built in | Has cut price ~12% for 6 months against a prior new entrant (2024) |
| Service model / proven offer | Directly transfers Austria same-day medical courier model | Established local relationships; details not in data |
| Channel / sales capacity | 3 reps planned from 2027 (40 accounts/rep/year, Austria benchmark — untested in CZ) | Entrenched accounts; retention effort unknown |
| Capabilities | Own depot (EUR 0.9m/yr fixed), proven ops playbook from Austria | n/a |

The single largest unknown on this side is whether the Austria win rate holds against an incumbent that has already shown it will defend share on price.

## Bottom-up business case: revenue and EBIT, built from Kestrel's own account economics

Method: revenue(year) = pharmacy accounts in force at year-end × EUR 9,500 (Kestrel's own planning convention). Accounts in force roll forward with 8%/year churn on the opening book and new adds from reps at 40/rep/year. Variable cost = 70% of revenue; fixed cost = EUR 0.9m depot + EUR 85k per rep.

### Base case: 3 reps (plan as scoped)

| Year | Accounts, start | New adds | Churn (8%) | Accounts, end | Revenue | Fixed costs | EBIT | EBIT margin |
|---|---|---|---|---|---|---|---|---|
| 2027 | 0 | 120 | 0 | 120 | EUR 1.14m | EUR 1.155m | –EUR 0.81m | –71% |
| 2028 | 120 | 120 | 10 | 230 | EUR 2.19m | EUR 1.155m | –EUR 0.50m | –23% |
| 2029 | 230 | 120 | 18 | 332 | EUR 3.15m | EUR 1.155m | –EUR 0.21m | –7% |
| **2030** | 332 | 120 | 27 | **425** | **EUR 4.04m** | EUR 1.155m | **EUR 0.06m** | **1.4%** |

**Result: EUR 4.04m revenue and 1.4% EBIT margin by 2030 — misses the EUR 6m bar by 33% and the 8% margin bar by nearly 7 points.** At the board's own end-2029 checkpoint, EBIT is still negative (–EUR 0.21m) and revenue is barely half the 2030 target — on current trajectory this plan should trip the board's own exit trigger before 2030 arrives.

### Downside: incumbent reaction (2024 precedent applied to Kestrel)

Modeling the 2024 precedent (incumbent defends share, cutting Kestrel's effective win rate by ~25% for the first two years, i.e. 30 accounts/rep/year in 2027–28, recovering to 40/year after): 2030 accounts = 377, revenue = **EUR 3.58m**, EBIT = **–EUR 0.08m (–2.2% margin)**. Worse on both counts — the kill is robust, not an artifact of one assumption.

### Upside within pharmacies only (lower churn, no reaction)

Even an optimistic case — churn at 5% instead of 8%, full Austria productivity, no incumbent reaction — reaches only **EUR 4.23m revenue, 2.7% margin** by 2030. The 3-rep plan misses the bar in the base, downside, *and* upside pharmacy-only scenarios: this is a scale problem (not enough selling capacity), not a unit-economics problem.

### Why it's a scale problem, not a margin problem

Fixed costs (EUR 1.155m) don't grow with volume in this model, so margin recovers fast once revenue scales: at exactly EUR 6m revenue, contribution (30%) = EUR 1.8m, EBIT = EUR 0.645m, margin = 10.75% — above the 8% bar. The real constraint is getting to EUR 6m of accounts, not the cost structure.

### Scaled plan: 5 reps, same depot (tests whether more selling capacity closes the gap)

| Year | Accounts, end | Revenue | Fixed costs | EBIT | EBIT margin |
|---|---|---|---|---|---|
| 2027 | 200 | EUR 1.90m | EUR 1.325m | –EUR 0.76m | –40% |
| 2028 | 384 | EUR 3.65m | EUR 1.325m | –EUR 0.23m | –6% |
| 2029 | 553 | EUR 5.25m | EUR 1.325m | EUR 0.25m | 4.8% |
| **2030** | **709** | **EUR 6.74m** | EUR 1.325m | **EUR 0.70m** | **10.3%** |

Clears both bars, and is on track (positive EBIT, revenue near 90% of the 2030 target) by the board's end-2029 checkpoint. Cumulative cash burn through 2028 (~EUR 0.99m) is well inside the EUR 5m capital cap. A 4-rep interpolation lands at EUR 5.39m / 7.0% — close but still short, showing the result is sensitive to exactly how much capacity is added.

Re-applying the same incumbent-reaction stress test to the 5-rep plan: 2030 revenue = **EUR 5.97m, margin 7.8%** — right at the line, not a comfortable pass. The scaled plan only clears the bar if the incumbent reaction is mild or short-lived.

Feasibility check: 709 accounts by 2030 is ~26% of the entire 2,700-pharmacy pool in the three regions, and roughly 58% of the pool not already held by the two incumbents (assuming their 55% applies evenly to pharmacies specifically, which is not confirmed — see Open questions). That is an aggressive share gain in four years and should be treated as unproven until tested locally, not as the new base case.

## Entry modes

Only one mode is costed in the data provided: **own depot + direct sales reps** (the Austria model, transferred unchanged). A distributor or partnership mode is not costed in the materials given; directionally it would likely lower the fixed-cost base (no EUR 0.9m depot) and capital at risk, at the cost of control, margin capture, and speed of account acquisition — this cannot be quantified without additional data (see Open questions).

## Compared with the alternative use of capital

| | Kestrel Austria extension (management estimate) | Czech Republic, 3-rep plan (base case) | Czech Republic, 5-rep plan (base case) |
|---|---|---|---|
| Capital | EUR 2m | up to EUR 5m | up to EUR 5m |
| Revenue by 2030 | EUR 3.5m | EUR 4.04m | EUR 6.74m |
| EBIT margin by 2030 | 10% | 1.4% | 10.3% |
| EBIT by 2030 | EUR 0.35m | EUR 0.06m | EUR 0.70m |
| EBIT / capital cap | ~17.5% | ~1.1% | ~13.9% |
| Evidence basis | Single precedent (2024 Salzburg-region extension) — weak | Austria 2023-25 actuals transferred to CZ, unproven locally — weak-medium | Same, plus an unvalidated share-gain assumption — weak |

The Austria extension is the more capital-efficient option on the numbers given, and rests on fewer new assumptions (same country, same team, one comparable precedent) than either Czech scenario. The 5-rep Czech plan delivers roughly double the absolute EBIT and revenue if its win-rate and reaction assumptions hold — but those assumptions are the least tested of anything in this case. As scoped (3 reps), Czech entry is dominated by the Austria alternative on every measure.

## What would change the answer

1. If CZ rep productivity tests out close to the Austria 40/year benchmark (via a short local pilot or the country-manager candidate's own view), the 5-rep plan becomes a credible "enter" case.
2. If hospital/lab demand in the three regions — entirely unsized today — adds even EUR 1.5–2m of 2030 revenue at a similar 70% variable-cost ratio, the 3-rep plan could clear the bar without adding headcount; this needs its own bottom-up sizing before resizing the sales plan.
3. If the incumbent reaction is confirmed to be specific and sustained against multi-rep entrants (not just the single 2024 episode), the 5-rep plan's margin cushion disappears and the recommendation flips to "do not enter."
4. If CZ medical courier certification/regulatory lead time runs past the 2027 start date, the whole ramp shifts a year later against the 2030 bar.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Rep productivity transfers unchanged from Austria to CZ | 40 new accounts/rep/year | Kestrel Austria actuals, 2023-25 average | CZ win rate is materially lower (e.g. <30/year) against an entrenched incumbent — pushes even the 5-rep plan below the bar |
| 2 | Account churn transfers unchanged from Austria to CZ | 8%/year | Kestrel Austria actuals, 2023-25 average | CZ churn is higher under incumbent price retaliation |
| 3 | No incumbent reaction in the base case | 0% price/win-rate impact | 2024 precedent treated as a stress test only, not the base | Reaction is milder than 2024 (improves answer) or targeted/sustained against Kestrel specifically (kills even the 5-rep plan) |
| 4 | Depot and rep fixed costs stay flat 2027-2030 regardless of scale (3 or 5 reps, up to ~700 accounts) | EUR 0.9m depot + EUR 85k/rep, no step-up | Single Austria depot cost figure given; no CZ-specific facility sizing data | Scaling to 5 reps / ~700 accounts needs a larger facility or second depot |
| 5 | Hospital/lab revenue = EUR 0 in the model | Not sized | 2026 market study explicitly excludes hospitals and labs | This channel alone could close most of the 3-rep plan's ~EUR 2m revenue gap |
| 6 | Capital draw = modeled cumulative EBIT losses only | No separate depot fit-out, vehicle, IT, or country-manager capex included | Not itemized in the data given | Real capex brings total spend materially closer to the EUR 5m cap, especially in the 5-rep scenario |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is the bottom-up size and spend-per-account for hospitals and labs in the three target regions? | Explicitly excluded from the 2026 study; could close most or all of the 3-rep plan's revenue gap without adding headcount | Market-study provider / direct interviews with target hospitals/labs | Could flip "do not enter at 3 reps" to "enter as scoped" |
| Does the incumbents' ~55% share apply evenly to pharmacies specifically, or is it a medical-segment-wide figure (including hospitals/labs)? | Determines how much of the 2,700-pharmacy pool is actually contestable, and how aggressive the 5-rep plan's 26% penetration really is | Market-study author | Changes how credible the scaled-plan share gain is |
| Will CZ rep productivity match the Austria benchmark (40 accounts/year) given no local brand and an entrenched, price-cutting incumbent? | The single biggest swing factor across every scenario modeled | A short local pilot, or the interviewed CZ country-manager candidate | Determines whether either the 3-rep or 5-rep plan is achievable at all |
| What capex sits outside the EUR 0.9m/year depot opex and EUR 85k/rep figures (fit-out, vehicles, systems, country-manager cost)? | Determines how much of the EUR 5m cap is actually available to fund the ramp losses modeled here | Kestrel finance | Could tighten or loosen the capital headroom found above |
| Are there CZ-specific medical/pharma courier requirements (cold-chain, controlled-substance handling, GDP-style distribution certification) that add cost or delay the 2027 start? | Could push the whole ramp a year later against a fixed 2030 bar | Legal/regulatory counsel (CZ pharma logistics) | Must be resolved before the January 2027 board decision |
| What are CZ hiring terms and notice periods for reps and depot staff? | Sets the wind-down cost component of the board's requested exit mechanism, not yet defined | HR/labour-law counsel | Needed to actually cost the "way out" the board has asked for |
| What would a distributor/partnership entry mode cost and yield, versus the own-depot model modeled here? | Not provided in the data; could lower capital at risk if the own-depot margin stays marginal | Kestrel corp-dev / local partner candidates | Could offer a lower-capital path if reps-only plans don't validate |

