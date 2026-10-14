# cme-01-czech-medical on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/13 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question with the minimum bar (EUR 6m, 8% EBIT by 2030, EUR 5m) and kill criteria before analysing. | yes | Step 1: 'Should Kestrel enter the Czech medical same-day market by 2027... deliver at least EUR 6m revenue and 8% EBIT margin by 2030, within EUR 5m capital, with an exit if the bar is missed by end of 2029?' stated before Steps 2-4 analysis. |
| Sizes the segment top-down (~EUR 31.5m) and bottom-up (~EUR 25.7m) and explains/flags the difference. | yes | 'Top-down: EUR 210m... x 15% medical share = EUR 31.5m/yr... Bottom-up: 2,700 pharmacies... x EUR 9,500... = EUR 25.65m/yr... These do not reconcile... Hospitals and labs... are entirely unsized and excluded.' |
| Builds the ramp from reps x win rate and arrives at about EUR 4.0m to 4.6m revenue in 2030, below the EUR 6m bar. | yes | '3-rep plan... Revenue 2030 / EUR 4.04m... Ceiling (zero churn)... EUR 4.56m' with trap check confirming 'Share built bottom-up from reps, win rate and churn, not 1% of a big market.' |
| Computes 2030 EBIT margin below 8% (about 1% to 5%). | yes | 'EBIT 2030 / EUR 0.06m (1.4%) / −EUR 0.08m (−2.1%) / EUR 0.21m (4.7%)' |
| Models at least one aggressive incumbent reaction using the 2024 price-cut evidence and reports its effect. | NO | 'Not quantified in the base model below — carried as an unpriced downside' and trap check: '[ ] Open. Aggressive incumbent reaction is named (12% price cut...) but not built into the P&L. Fix: run the business case again with a priced price-war scenario.' The effect was never actually computed. |
| States that the EUR 120k study is sunk and plays no role. | yes | '[x] Sunk costs (EUR 120k study, interviewed-not-hired country manager) play no role in this recommendation.' |
| Compares with the Austrian alternative per euro of capital, and flags that alternative as a management estimate to test. | yes | 'This is a management estimate from one precedent (2024 Salzburg extension) — weak-to-medium evidence... On a per-euro-of-capital basis it clears its own bar on the first try...' |
| Does not approve the briefed 3-rep plan; answer is do not enter/enter later/enter only under named conditions with a stage gate, and says what would make the board revisit it. | yes | 'Do not approve the Czech entry as currently scoped (3 reps from 2027)... send Czech back for a 1-rep regional pilot and independent market-data verification before the January 2027 board revisits a rescoped 5-rep plan.' Plus 'What would change the answer' section with four named conditions. |
| Compares at least two entry modes (e.g. own office, partner/distributor, acquisition) on cost, speed, control and exit cost. | NO | 'Only one mode is costed in the brief — direct operation... No distributor/JV data is available for comparison, so this is accepted as given rather than scored against alternatives.' No second entry mode is ever compared. |
| Writes exit criteria and exit cost. | yes | 'Exit cost ≈ cumulative cash burn to that point (~EUR 1.0-1.5m depending on scenario) + wind-down (depot lease exit, rep severance, customer handover)' |
| Flags that Austrian win rates and prices may not transfer to the Czech market and names the test. | yes | 'Austria's win rate (40 accounts/rep/yr) transfers to Czech... Reshaped — treated as untested' and 'If a 1-rep regional pilot in 2026-27 shows a Czech win rate within ~20% of Austria's 40 accounts/rep/yr, the 5-rep rescoped plan becomes a credible basis...' |
| Must not recommend unconditional entry on the strength of the EUR 210m headline. | yes | The EUR 210m figure is only used inside the top-down sizing calc (x15%), and the final recommendation is 'Do not approve the Czech entry as currently scoped' — no unconditional entry recommendation given. |
| Must not invent Czech regulatory requirements, competitor names, or wage levels as facts; may flag for specialists. | yes | Competitors kept generic ('Incumbent A+B'); Czech labour law and licensing listed as open questions for 'Legal (Czech labour counsel)' / 'Legal / regulatory counsel', not asserted as fact; wage figure (EUR 85k/rep) sourced explicitly to 'Kestrel's own Austria cost data', not invented as Czech-specif |

## Transcript

## Turn 1

**User:** Work the Kestrel Czech entry case from the briefing. Quick case, answer page for the board. (Attached in the working directory: cme-01-input.md.)

**The case contradicts the plan as scoped:** the 3-rep Czech entry tops out at EUR 4.0-4.6m revenue / 1-5% EBIT margin by 2030, even in its best-case reading — it cannot clear the board's EUR 6m / 8% bar.

Key findings, worked from the brief's own numbers (full detail in `case-market-entry-kestrel-czech.md`):

- **The 3-rep plan is killed by arithmetic, not by a weak market.** Using the planning convention (revenue = accounts × EUR 9,500) with Austria's 40-accounts/rep/yr win rate and 8% churn, 3 reps reach only 425 accounts by 2030 (EUR 4.04m, 1.4% margin). Even a zero-churn ceiling only gets to EUR 4.56m / 4.7% margin.
- **Capital isn't the binding constraint — sales capacity is.** Peak cash burn in every scenario tested stays under EUR 1.5m, well inside the EUR 5m ceiling. A rescoped 5-rep plan reaches EUR 6.74m / 10.3% margin and still only needs ~EUR 1m peak funding — but that rests on unverified assumptions (Czech win-rate = Austria's from day one, no incumbent price war).
- **The EUR 9,500/account figure — the single most load-bearing number in the whole model — comes from a 60-pharmacy survey that doesn't reconcile with the market study's own top-down number** (bottom-up pharmacy-only spend in 3 regions is ~81% of the entire national medical segment estimate). That's a real data-quality flag, not just a rounding gap.
- Hospitals and labs, despite being named in the board's own question, are entirely unsized and excluded from the model.
- The Austria 2-region extension (EUR 2m → EUR 3.5m revenue, 10% EBIT) clears its own bar immediately on a proven precedent with far less execution risk.

**Recommendation in the file:** don't approve Czech at 3 reps; fund the Austria extension now; send Czech back for a 1-rep pilot plus independent verification of the EUR 9,500 figure before the board revisits a rescoped 5-rep plan. Full answer page, assumptions, open questions, and trap checks are in the saved file.


## Files in work dir after run

- case-market-entry-kestrel-czech.md
- cme-01-input.md

## File written by the run: case-market-entry-kestrel-czech.md

# Market entry: Kestrel Logistics, Czech Republic medical same-day, quick case

*Fictional case; all figures invented for evaluation.*

## Step 1: Sharpen the question

Decision question: "Should Kestrel enter the Czech medical same-day market by 2027, and if so how, given it must deliver at least EUR 6m revenue and 8% EBIT margin by 2030, within EUR 5m capital, with an exit if the bar is missed by end of 2029?"

This is already sharpened by the board brief (minimum bar, capital, time, exit trigger). Three items are not in the brief and are carried as open questions rather than blocking this pass:
- Which three regions, and whether "medical segment" share/concentration figures are national or regional.
- Entry mode beyond "depot + reps" (no distributor/JV mentioned; this case assumes direct operation, matching the Austria model).
- Whether the board wants hospitals/labs included in the 2030 target or only pharmacies (the only revenue line costed in the brief is pharmacies).

## Step 2: Issue tree

| Branch | Hypothesis | Threshold | Status |
|---|---|---|---|
| Attractive: size | Addressable pharmacy segment in 3 regions is large enough to support the plan | ≥ EUR 6m/yr achievable at plausible share | Confirmed (segment ~EUR 25.6m/yr bottom-up) but **evidence weak** — see 3a |
| Attractive: structure | No player holds more than ~60-70% of the segment | 2 incumbents hold 55% | Not an outright kill, but reinforced by a documented aggressive-reaction precedent |
| Can win: need/channel | Austria's win rate (40 accounts/rep/yr) transfers to Czech | Reps hit ~Austria productivity | **Reshaped** — treated as untested, stress-tested low/base |
| Pays: 3-rep plan (as currently scoped) | Base case reaches EUR 6m / 8% EBIT by 2030 | Revenue ≥ 6m, margin ≥ 8% | **Killed** — tops out at ~EUR 4.0-4.6m / 1.4-4.7% margin even in the best case |
| Pays: rescoped plan | A larger sales team can reach the bar within the EUR 5m capital cap | Revenue ≥ 6m, margin ≥ 8%, capital ≤ 5m | **Confirmed, provisionally** — ~5 reps clears it on paper, but rests on compounding optimistic assumptions |
| Beats alternatives | Czech entry earns more per euro of management attention and capital than the Austria 2-region extension | Compare EBIT and risk | Open — Austria option is smaller but far lower risk, single proven precedent |

## Step 3: Deciding analyses

**a. Addressable market (top-down vs bottom-up, triangulated).**
Top-down: EUR 210m total B2B same-day market × 15% medical share = **EUR 31.5m/yr**, nationwide, all of pharmacy+hospital+lab.
Bottom-up: 2,700 pharmacies in the 3 target regions × EUR 9,500/pharmacy/yr = **EUR 25.65m/yr**, pharmacies only, 3 regions, hospitals/labs excluded.
These do not reconcile: a pharmacy-only, 3-region figure is ~81% of the entire national medical segment. Either the 15% share understates medical demand, the three regions are far from representative (plausible if they include Prague/Brno-type hubs, but not stated), or the EUR 9,500 average — from a 60-pharmacy survey — is skewed upward (self-selected respondents already buying courier services tend to over-represent heavy users). **This number is the single most load-bearing figure in the whole business case (revenue = accounts × EUR 9,500) and its evidence is weak.** Hospitals and labs, despite being named in the board's question, are entirely unsized and excluded from the model. Hypothesis: confirmed directionally (segment is big enough in principle) but flagged weak evidence requiring verification before the board relies on it.

**b. Market structure.** Two local players hold ~55% of the medical segment; ~45% (roughly EUR 11.5-14m depending on which base) is open. Kestrel's 2030 target (EUR 6-6.7m) would be 42-59% of that entire open pool after only 4 years — an aggressive capture assumption for a new entrant, the mirror image of the usual "1% of a big market" trap. Not an automatic kill (concentration isn't extreme), but it raises the bar on the win-rate assumption in (c).

**c. Customer need / win-rate transfer (home-market transfer check).** The only win-rate data is Austria's (40 new accounts/rep/yr, 8% churn). Nothing in the brief tests whether Czech pharmacies switch couriers at the same rate, respond to the same pitch, or value the same service attributes. Treated as an untested transfer and stress-tested as a range (see f), not taken at face value.

**d. Competitors and reaction.** In 2024, when a new carrier entered, the larger incumbent cut prices ~12% for six months (interview evidence, single episode). This is the clearest signal in the data that incumbents will respond aggressively to a new entrant, which threatens both the win rate and the EUR 9,500/account price assumption. Not quantified in the base model below — carried as an unpriced downside (see Step 4).

**e. Entry mode.** Only one mode is costed in the brief: direct operation (own depot + employed reps), the same model as Austria. No distributor/JV figures given, so no comparison is possible; this is accepted as the mode on the table, not an open branch.

**f. Entry business case (ramp from named reps, with churn).** Planning convention: revenue(year) = pharmacy accounts in force at year-end × EUR 9,500. Depot fixed cost EUR 0.9m/yr; reps EUR 85k/yr each; variable cost 70% of revenue (so each euro of revenue carries 30% contribution before fixed costs).

*3-rep plan as given (3 reps from 2027, 120 new accounts/yr gross, 8% annual churn on the book):*

| Year-end | Accounts | Revenue | EBIT (30% contribution − EUR 1.155m fixed) | Margin |
|---|---|---|---|---|
| 2027 | 120 | EUR 1.14m | −0.81m | — |
| 2028 | 230 | EUR 2.19m | −0.50m | — |
| 2029 | 332 | EUR 3.15m | −0.21m | — |
| 2030 | 425 | **EUR 4.04m** | **+0.06m** | **1.4%** |

Low case (reps need a year to reach full Czech productivity, 50% win rate in 2027 only): 2030 accounts 379, revenue **EUR 3.60m**, EBIT **−0.08m** (margin −2.1%) — still loss-making in year 4.
Theoretical ceiling for the 3-rep plan (zero churn, full productivity from day one — the most generous reading of the data): 2030 accounts 480, revenue **EUR 4.56m**, EBIT **+0.21m** (margin 4.7%).

**Result: the 3-rep plan misses both the revenue bar (EUR 6m) and the margin bar (8%) under every assumption tested, including its own best case. Hypothesis killed.**

*What it would take to clear the bar:* EUR 6m by 2030 needs 632 accounts at year-end. Solving the same ramp model backward, that needs ~178 new accounts/yr, i.e. ~5 reps (not 3). A 5-rep plan from 2027 (200 new accounts/yr, same 8% churn): 2030 accounts 709, revenue **EUR 6.74m**, EBIT (fixed cost now EUR 1.325m with 5 reps) **+0.70m, margin 10.3%** — clears both bars. A 4-rep plan falls just short: revenue EUR 5.39m, margin 7.0%.

**g. Stress test / capital.** Cumulative cash burn to breakeven: 3-rep plan peaks at about **−EUR 1.5m** (end of 2029); 5-rep plan peaks at about **−EUR 1.0m** (end of 2028) because it reaches scale faster. Both are comfortably inside the EUR 5m capital ceiling. **This is the key finding: capital is not the binding constraint — sales capacity (rep count) and win-rate transfer are.** The unpriced incumbent-reaction risk from (d) sits on top of this and is not reflected in any of the figures above; a 12%-style price response in the entry year would push every scenario further from the bar, not closer.

**h. Alternative use of capital — Austria 2-region extension.** Head of Austria's ask: EUR 2m capital → EUR 3.5m revenue, 10% EBIT (EUR 0.35m) by 2030. This is a management estimate from one precedent (2024 Salzburg extension) — weak-to-medium evidence, same standard applied to the Czech numbers above, not treated as more reliable just because it's internal. On a per-euro-of-capital basis it clears its own bar on the first try, in the home market, with the existing team and no incumbent-reaction history to contend with. The Czech 5-rep case has a larger absolute EBIT prize (EUR 0.70m vs EUR 0.35m) but carries materially higher execution risk: new country, new team, unverified pricing data, and a documented aggressive incumbent.

## Step 4: Trap checks

- [x] Share built bottom-up from reps, win rate and churn, not "1% of a big market."
- [ ] **Open.** Customers, channels and price tested in the target market — not yet. The win rate (40/rep/yr) and the EUR 9,500/account figure are both unverified in Czech conditions (Austria transfer; a 60-pharmacy, likely self-selected survey). Fix: a 1-rep, 1-region pilot before committing to 3-5 reps, or independent verification of the survey (courier invoicing data, a larger stratified sample).
- [ ] **Open.** Aggressive incumbent reaction is named (12% price cut for six months in 2024) but not built into the P&L. Fix: run the business case again with a priced price-war scenario in the entry year.
- [x] Sunk costs (EUR 120k study, interviewed-not-hired country manager) play no role in this recommendation.
- [ ] **Partial.** Ramp is benchmarked only against Kestrel's own Austria experience, an internal comparable, not an external Czech new-entrant comparable. No such data is in the brief; range widened (low/base/ceiling) to compensate and gap named explicitly.
- [x] Money already spent is treated as sunk.
- [ ] **Partial.** Exit trigger is set by the board (missed bar at end of 2029). Exit cost ≈ cumulative cash burn to that point (~EUR 1.0-1.5m depending on scenario) + wind-down (depot lease exit, rep severance, customer handover) — wind-down cost itself is not in the brief; flagged as an assumption for Legal/HR.
- [x] Entry compared with the best alternative use of the same capital (Austria extension, above).

---

# Market entry: Kestrel Logistics, Czech Republic medical same-day — enter by 2027?

**Answer:** Do not approve the Czech entry as currently scoped (3 reps from 2027). On every tested assumption, including the most generous reading of the data, it reaches only EUR 3.6-4.6m revenue and 0-5% EBIT margin by 2030 — short of the board's EUR 6m / 8% bar. A rescoped plan with ~5 reps from year one reaches EUR 6.7m / 10.3% margin on paper and still fits inside the EUR 5m capital ceiling (peak cash need ~EUR 1.0m), but that fix rests on unverified assumptions (Czech win-rate equal to Austria's from day one, no incumbent price response, EUR 9,500/account figure from a small, likely biased survey). Recommend the board fund the Austria 2-region extension (EUR 2m for EUR 3.5m revenue / 10% EBIT, lower risk, proven precedent) now regardless of the Czech decision, and send Czech back for a 1-rep regional pilot and independent market-data verification before the January 2027 board revisits a rescoped 5-rep plan.
**Confidence:** Medium. High confidence that the 3-rep plan as given cannot clear the bar (the arithmetic holds under every tested assumption). Low-to-medium confidence that a 5-rep plan would, because it depends on win-rate transfer and incumbent reaction that are not tested in the data.
**Specialists and review:** Czech labour law (rep severance / notice if exiting after 2029), Czech courier-sector licensing/registration (not addressed in the brief at all), and data protection for health-related shipments (labs/clinics involve health data; GDPR special-category handling should be reviewed before entry) — none of these were assessed in this case and should sit with Legal before the January 2027 board.

## Minimum bar agreed with client (set by board)
- Revenue at least EUR 6m by 2030; EBIT margin at least 8%; capital at most EUR 5m
- Kill criteria: bar missed by end of 2029 triggers exit

## Is the market attractive?
| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Addressable size and growth | Top-down EUR 31.5m/yr (national, all medical); bottom-up EUR 25.65m/yr (pharmacies only, 3 regions). The two don't reconcile — bottom-up is implausibly close to top-down. | 2026 market study (commissioned by Kestrel) | pass, but weak evidence — needs verification |
| Concentration and incumbents | 2 local players hold ~55% of the medical segment; one cut price ~12% for 6 months against a 2024 entrant | Market study interviews | caution — moderate concentration plus a proven aggressive-response precedent |
| Barriers and regulation | Not addressed in the brief (licensing, registration, data protection for health shipments) | — | open — specialist input needed |

## Can we win?
| Factor | Kestrel (Czech, planned) | Incumbent A+B (combined) |
|---|---|---|
| Share of segment | 0% today; 3-rep plan reaches ~16% of bottom-up segment (EUR 4.0m/25.65m) by 2030; 5-rep plan reaches ~26% | ~55% |
| Account-win channel | 3-5 employed reps, Austria playbook, untested in Czech | Established local relationships |
| Price response capability | Unknown; no Czech pricing precedent | Demonstrated willingness to cut price ~12% for 6 months against a new entrant |

## Entry modes
Only one mode is costed in the brief — direct operation (own depot + employed reps), the same model Kestrel runs in Austria. No distributor/JV data is available for comparison, so this is accepted as given rather than scored against alternatives.

## Business case (3-rep plan as given / low / theoretical ceiling)
| | Base (full Austria productivity) | Low (slow first-year ramp) | Ceiling (zero churn) |
|---|---|---|---|
| Revenue 2030 | EUR 4.04m | EUR 3.60m | EUR 4.56m |
| EBIT 2030 | EUR 0.06m (1.4%) | −EUR 0.08m (−2.1%) | EUR 0.21m (4.7%) |
| Cumulative cash need, peak | ~EUR 1.5m (end 2029) | similar or worse | ~EUR 1.4m |
| Clears EUR 6m / 8% bar? | No | No | No |

| | Rescoped plan: 5 reps from 2027 |
|---|---|
| Revenue 2030 | EUR 6.74m |
| EBIT 2030 | EUR 0.70m (10.3%) |
| Cumulative cash need, peak | ~EUR 1.0m (end 2028) |
| Clears EUR 6m / 8% bar? | Yes, on paper — untested assumptions (see trap checks) |

## Compared with the alternative use of capital
The Head of Austria's ask (EUR 2m for EUR 3.5m revenue, 10% EBIT/EUR 0.35m by 2030) clears its own bar immediately, in the home market, on a single internal precedent (2024 Salzburg extension) that should be treated as a hypothesis, not a fact, but carries far less execution risk than Czech: no new country, no new team, no incumbent-reaction history, a smaller capital ask. The rescoped 5-rep Czech plan has a larger absolute EBIT prize (EUR 0.70m vs EUR 0.35m) for roughly the same order of capital, but that prize is conditional on three unverified assumptions (win-rate transfer, no price war, the EUR 9,500/account figure) that the Austria option doesn't carry. Capital is not scarce enough here to force a strict either/or — the honest reading is that Austria is a low-risk approve now, and Czech needs to prove its assumptions before it deserves the same capital.

## What would change the answer
1. If a 1-rep regional pilot in 2026-27 shows a Czech win rate within ~20% of Austria's 40 accounts/rep/yr, the 5-rep rescoped plan becomes a credible basis for a January 2027 go-ahead.
2. If independent data (courier invoicing, a larger survey) confirms the EUR 9,500/account figure and reconciles the top-down/bottom-up gap, confidence in the whole revenue model rises materially.
3. If either incumbent responds to Kestrel's entry with a sustained price cut (as happened in 2024), every scenario above should be re-run with a priced price-war case before the board revisits the plan.
4. If hospitals and labs — explicitly part of the board's question but entirely unsized here — turn out to add a material revenue line, the bar could be reached with fewer reps; this needs its own market sizing before it can be assumed.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | EUR 9,500/pharmacy/yr average spend transfers unchanged to Kestrel's win price | EUR 9,500 | 60-pharmacy survey in market study | Independent data shows a materially different average (survey is small, likely self-selected) |
| 2 | Austria's 40 accounts/rep/yr and 8% churn apply unchanged in Czech from day one | 40 new/rep/yr; 8% churn | Austria 2023-2025 actuals | A Czech pilot shows materially slower win rate or higher churn |
| 3 | Depot fixed cost and rep cost stay flat 2027-2030 (no inflation, no step-up) | EUR 0.9m/yr depot; EUR 85k/yr/rep | Kestrel's own Austria cost data | Czech depot costs or wage inflation run materially higher |
| 4 | No incumbent price response is priced into the base case | 0% price/win-rate impact | Not costed — qualitative risk only | Board wants the 2024-style 12% price-cut scenario quantified before deciding |
| 5 | Hospitals and labs contribute zero revenue to the 2030 target | EUR 0 | Not covered by the market study's pharmacy survey | Hospitals/labs are sized and shown to add materially |
| 6 | Sales team stays at exactly 3 reps (board brief) unless rescoped to 5 for the sensitivity case | 3 reps (base); 5 reps (sensitivity) | Board brief: "planned sales team... 3 reps from 2027" | Board approves a different headcount than either scenario |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Which three regions, and is the 55% concentration figure national or regional? | Determines whether the bottom-up/top-down reconciliation gap is explainable or a real data problem | Kestrel market-study author / commissioned research firm | Could raise or lower confidence in the whole sizing without changing any figure |
| Does the board want hospitals/labs included in the 2030 target, given the service is named "pharmacies, labs, clinics"? | The entire business case currently counts pharmacy revenue only | Board / sponsor | Could close part of the EUR 2m revenue gap if sized and material |
| Is direct operation (depot + reps) the only mode the board will consider, or should distributor/partnership options be scoped? | No alternative mode is costed in the brief | Board / Head of Czech entry workstream | Could change the capital and time-to-revenue profile |
| What does Czech labour law require for severance/notice if the business exits after the 2029 checkpoint? | Needed to size the exit cost named in the board's own exit trigger | Legal (Czech labour counsel) | Changes the true cost of the board's stated exit option |
| What licensing/registration does a courier handling pharmacy and (if included) lab/clinic shipments need in the Czech Republic? | Not addressed anywhere in the brief; could affect timeline or feasibility | Legal / regulatory counsel | Could delay the 2027 start or add cost not in any scenario above |
| Would a 1-rep, 1-region pilot before full commitment be acceptable to the board, given the 2029 exit checkpoint? | Cheapest way to resolve the two biggest "open" trap checks (win-rate transfer, incumbent reaction) before committing to 3-5 reps | Board | Could make the rescoped 5-rep case investable, or kill it early at much lower cost |

