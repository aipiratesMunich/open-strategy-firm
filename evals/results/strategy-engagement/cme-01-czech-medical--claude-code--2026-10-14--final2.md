# cme-01-czech-medical on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (12/13 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question with the minimum bar (EUR 6m, 8% EBIT by 2030, EUR 5m) and kill criteria before analysing. | yes | "Minimum bar agreed with client... Revenue at least EUR 6m and EBIT margin at least 8%... capital up to EUR5m. If the bar is missed by end of 2029, the board wants a way out" appears before the market/business-case analysis sections. |
| Sizes the segment top-down (~EUR31.5m) and bottom-up (~EUR25.7m) and explains/flags the difference. | yes | "Top-down: EUR210m... × 15%... ≈ EUR31.5m/yr. Bottom-up... 2,700 pharmacies × EUR9,500 ≈ EUR25.65m/yr. The two triangulate reasonably (gap ≈ hospitals/labs...)" |
| Builds the ramp from reps x win rate and arrives at ~EUR4.0-4.6m revenue in 2030, below the EUR6m bar. | yes | "Accounts in force = prior year's accounts net of 8% annual churn, plus new accounts won (40/rep/year...)" yielding 2030 Revenue EUR4.04m, below the EUR6m bar. |
| Computes 2030 EBIT margin below 8% (about 1% to 5%). | yes | Base case table: 2030 EBIT margin 1.4%. |
| Models at least one aggressive incumbent reaction using the 2024 price-cut evidence and reports its effect. | yes | "a 12% price effect in the final year consistent with the 2024 incumbent-reaction precedent" producing Low case 2030 revenue EUR3.17m, margin -6.5%. |
| States that the EUR120k study is sunk and plays no role. | yes | "the EUR120k study is spent regardless of outcome" under sunk/not-committed costs. |
| Compares with the Austrian alternative per euro of capital, and flags that alternative as a management estimate to test. | yes | "roughly EUR0.35m / EUR2m ≈ 17.5%" and "The Austria extension's management estimate is also unverified (it is an estimate to test, not a sourced fact)" |
| Does not approve the briefed 3-rep plan; answer is do-not-enter/enter-later/conditional with stage gate, states what would make the board revisit it. | yes | "Do not enter on the current plan." plus "What would change the answer" section listing conditions (5 reps, pilot results, incumbent reaction confirmation). |
| Compares at least two entry modes (own office, partner/distributor, acquisition) on cost, speed, control and exit cost. | NO | "Only one mode is specified in the brief and costed here: own depot + own direct sales reps... No distributor, partnership or JV figures were given, so no alternative mode is sized" — explicitly only one mode is analysed, no second mode compared. |
| Writes exit criteria and exit cost. | yes | Assumption #8 estimates exit/wind-down cost ("EUR1.5m... plus an estimated EUR0.3-0.8m wind-down") and the "What would change the answer" list functions as stage-gate/exit criteria. |
| Flags that Austrian win rates and prices may not transfer to the Czech market and names the test. | yes | "Czech ramp is slower (likely, new market, no brand)" and open question recommending "A short Czech pilot, or interviews with the team that ran the 2024 Salzburg extension." |
| Does not recommend unconditional entry on the strength of the EUR210m headline. | yes | Recommendation is "Do not enter on the current plan," not based on the headline figure. |
| Does not invent Czech regulatory requirements, competitor names, or wage levels as facts. | yes | Competitors referred to only as "Incumbent A+B"/"two local players"; regulatory requirements listed as an open question for "Legal/tax/compliance specialists," not invented as fact. |

## Transcript

## Turn 1

**User:** Work the Kestrel Czech entry case from the briefing. Quick case, answer page for the board. (Attached in the working directory: cme-01-input.md.)

**Do not enter on the current plan.** The 3-rep/EUR0.9m-depot plan Kestrel has on the table reaches only ~EUR4.0m revenue and ~1% EBIT margin by 2030, against the board's EUR6m/8% bar — and that's the *optimistic* case (full Austria productivity from day one, no incumbent reaction). A realistic downside (slower new-market ramp, a repeat of the 2024 12% incumbent price cut) lands around EUR3.2m and negative margin. The plan only clears the bar at roughly 5 reps (EUR6.7m / 10.3%), which isn't what's currently planned or costed.

Against that, the Head of Austria's EUR2m ask for two more Austria regions (EUR3.5m / 10% EBIT) rests on a real 2024 precedent in a market Kestrel already runs — better-evidenced and lower-risk per euro of capital than the Czech plan as scoped.

Full answer page with the business-case math, sensitivities, assumptions and open questions is written to `case-market-entry-kestrel.md` in the working directory.


## Files in work dir after run

- case-market-entry-kestrel.md
- cme-01-input.md

## File written by the run: case-market-entry-kestrel.md

# Market entry: Kestrel Logistics, Czech Republic (medical same-day), board decision for January 2027

**Answer:** Do not enter on the current plan. Three reps and one EUR0.9m depot reach only about EUR 4.0m revenue and ~1% EBIT margin by 2030 — against a bar of EUR 6m / 8%. The plan clears the bar only if resourced to about 5 reps, with no incumbent price reaction and Austria-level productivity from day one — none of which is tested. Recommend: fund the Austria two-region extension now (lower risk, proven precedent); revisit Czech only if the board will resource ~5 reps and a pilot confirms local rep productivity and price survives an incumbent reaction.
**Confidence:** medium, because the core arithmetic (accounts × EUR9,500, 70% variable cost, EUR0.9m depot) is Kestrel's own and robust to the account-value uncertainty (±20% still misses the bar at 3 reps); confidence is capped at medium because the single biggest driver — whether a new Czech rep can win 40 accounts/year from day one against entrenched incumbents — is an untested Austria-to-Czech transfer, not Czech evidence.
**Specialists and review:** legal/tax/labour for Czech entity setup, depot lease and sales-rep employment; a pharma-logistics/compliance check on medical sample and document handling; CFO sign-off on what counts inside the EUR5m capital cap (country manager salary, depot capex, working capital) before any commitment.

## Minimum bar agreed with client (from briefing, not re-sharpened)
- Revenue at least EUR 6m and EBIT margin at least 8% in the Czech business by 2030; capital up to EUR 5m.
- If the bar is missed by end of 2029, the board wants a way out (no numeric 2029 checkpoint given — see Open questions).
- Sunk and not-yet-committed costs excluded from the decision: the EUR120k study is spent regardless of outcome; the country-manager candidate is interviewed but not hired, so no cost is committed there either way.

## Is the market attractive?
| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Addressable size | Top-down: EUR210m B2B same-day × 15% medical/pharmacy share ≈ EUR31.5m/yr. Bottom-up (pharmacies only, 3 target regions): 2,700 pharmacies × EUR9,500 ≈ EUR25.65m/yr. The two triangulate reasonably (gap ≈ hospitals/labs, not in the bottom-up figure). | 2026 market study | pass, but see weak-evidence flag below |
| Pharmacy spend figure | EUR9,500/pharmacy/year, survey of 60 of 2,700 pharmacies (2.2% sample) | 2026 market study | weak evidence — see Assumptions #3 |
| Concentration | Two local players hold ~55% of the medical segment combined (individual shares unknown); in 2024 the larger one cut price ~12% for 6 months when a new carrier entered | 2026 market study (interviews) | caution, not an automatic kill, but confirms incumbents will defend share on price |
| Hospitals/labs | Not covered by the survey; no account-economics data given | 2026 market study | gap — upside not sized, not counted in the business case below |

## Can we win?
| Factor | Us (Kestrel entering) | Incumbent A+B (combined ~55% share) |
|---|---|---|
| Local brand / relationships | None — new entrant | Established, long-standing |
| Price | Would price at the ~EUR9,500/account market rate (unverified for a new entrant) | Proven willing to cut price ~12% for 6 months to defend share |
| Service model, language, approvals | Not described in the brief | Unknown — not covered by the study |
| Our transferable advantage | Austria same-day medical operating model (depot + rep playbook) | N/A |

No data in the brief supports a verdict beyond "unproven" on this branch — flagged as an open question for buyer interviews before any commitment.

## Entry mode
Only one mode is specified in the brief and costed here: own depot + own direct sales reps (the Austria operating model transplanted to the Czech Republic). No distributor, partnership or JV figures were given, so no alternative mode is sized — this would need its own data request if the board wants it compared.

## Business case (bottom-up, built from Kestrel's own Austria unit economics)

Planning convention (given): revenue in a year = pharmacy accounts in force at year end × EUR9,500. Accounts in force = prior year's accounts net of 8% annual churn, plus new accounts won (40/rep/year, Kestrel Austria 2023-25 average). Fixed cost = EUR0.9m depot + EUR85k per rep. Variable cost = 70% of revenue.

### Base case — plan as given: 3 reps from 2027, full Austria productivity from day one
| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| Accounts, year end | 120 | 230 | 332 | 425 |
| Revenue | EUR1.14m | EUR2.19m | EUR3.15m | **EUR4.04m** |
| EBIT | -EUR0.81m | -EUR0.50m | -EUR0.21m | **EUR0.06m** |
| EBIT margin | -71% | -23% | -7% | **1.4%** |

**Misses the bar on both dimensions**: revenue 33% short of EUR6m, margin 6.6 points short of 8%. Cumulative EBIT 2027-2030 ≈ -EUR1.46m (cumulative loss through 2029 alone ≈ -EUR1.52m).

### Low case — same 3 reps, but a realistic new-market ramp and incumbent reaction
Assumptions (ours, not Kestrel's): first-year rep productivity at 50% of the Austria rate (new market, no book, no brand) rather than full speed from day one; a 12% price effect in the final year consistent with the 2024 incumbent-reaction precedent.
| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| Revenue | EUR0.57m | EUR1.66m | EUR2.67m | **EUR3.17m** |
| EBIT margin | -173% | -39% | -13% | **-6.5%** |

Revenue 47% short of the bar, and the business is still loss-making in 2030.

### What it would take to clear the bar
Solving the same model for the rep count needed: 3 reps → EUR4.0m, 4 reps → EUR5.4m / 7.0% margin (still short), **5 reps → EUR6.7m / 10.3% margin by 2030** (clears both parts of the bar, with cumulative EBIT 2027-2030 roughly breakeven, so cash burn stays well inside the EUR5m cap).

The gap is specifically sales headcount: the plan as given (3 reps) is undersized for the board's bar by about two reps, even under the optimistic assumption that Austria-level productivity transfers unchanged.

### Sensitivity: is this just a market-study measurement issue?
Varying the EUR9,500 account-value figure ±20% (to stress-test the thin 60-pharmacy survey) moves 2030 revenue at 3 reps between EUR3.2m and EUR4.8m — still below the EUR6m bar at every point. The shortfall is structural (headcount/scale), not an artefact of survey noise.

## Compared with the alternative use of capital
Head of Austria's proposal: EUR2m for two additional Austria regions → ~EUR3.5m revenue, 10% EBIT (EUR0.35m) by 2030, based on the actual 2024 Salzburg-region extension — a real precedent in a market Kestrel already operates in, not a cross-border transfer. On a simple EBIT-to-capital basis that is roughly EUR0.35m / EUR2m ≈ 17.5%, with comparatively low execution risk (same regulatory regime, known customer base, known rep productivity).

The Czech plan as given (3 reps) produces roughly EUR0.06m EBIT on a materially larger and less certain capital/management-attention commitment — clearly worse per euro of capital. Even the 5-rep version that clears the board's bar (EUR0.70m EBIT, cumulative cash need likely EUR1-1.5m once the cumulative loss and setup capex are added) rests on two assumptions that haven't been tested anywhere in the brief: that a brand-new Czech rep matches a mature Austria rep's win rate from day one, and that the two incumbents who cut price 12% against the last new entrant do not react to Kestrel. The Austria extension's management estimate is also unverified (it is an estimate to test, not a sourced fact), but it is grounded in a comparable, same-market, same-team precedent, which makes it the better-evidenced of the two options.

**This favours the Austria extension over the Czech entry as currently planned.** It does not rule out Czech Republic permanently — see conditions below.

## What would change the answer
1. If the board is willing to resource ~5 reps (not 3) for the Czech operation, the base case clears the revenue and margin bar — worth re-running once Kestrel confirms whether 5-rep capital fits inside the EUR5m cap alongside country-manager and setup costs.
2. If a short Czech pilot (even 1 rep for 6-12 months) shows win rates well below 40 accounts/year, the whole plan should be killed regardless of headcount, since the gap would only widen.
3. If the two incumbents are confirmed to react aggressively to any Kestrel launch (as they did in 2024), the low case becomes the realistic case and the answer hardens to "do not enter."
4. If hospital/lab same-day volumes turn out to be large and reachable through the same reps, the revenue bar could be cleared at lower pharmacy-only headcount — currently unsized.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | New Czech reps match Austria's steady-state win rate from day one | 40 new accounts/rep/year | Kestrel Austria 2023-25 average | Czech ramp is slower (likely, new market, no brand) — base case gets worse, strengthens "do not enter" |
| 2 | Account churn transfers unchanged | 8%/year | Kestrel Austria data | Czech churn is higher under incumbent retaliation — same direction, worse |
| 3 | Average account value | EUR9,500/pharmacy/year | 2026 market study, survey of 60/2,700 pharmacies (weak evidence, small sample) | True average outside the tested ±20% band — shown not to change the structural conclusion |
| 4 | Sales headcount fixed for the full period | 3 reps, 2027-2030 | Board's stated plan | Board approves ~5 reps — bar is cleared, see business case |
| 5 | One depot covers all 3 target regions, cost transfers from Austria | EUR0.9m/year | Kestrel Austria depot cost, applied as a Czech estimate | Czech depot needs regional footprint or local cost structure is higher than Austria's |
| 6 | Incumbent price reaction | None in base case; -12% one-time effect in low case | 2026 study interview note on a 2024 entrant | Incumbents react harder/softer than the 2024 precedent |
| 7 | Capital required beyond cumulative operating loss (country manager, depot/vehicle capex, working capital) stays well inside EUR5m | Not itemised by Kestrel; assumed modest relative to the EUR5m cap in the base and 5-rep cases | Our estimate, not sourced | Setup capex is materially higher than assumed, e.g. because of fleet or IT requirements not in the brief |
| 8 | Exit/wind-down cost at a 2029 "way out" checkpoint | Cumulative cash burn to that point (~EUR1.5m in the 3-rep base case) plus an estimated EUR0.3-0.8m wind-down (severance, lease break, customer handover) | Our estimate, not sourced from Kestrel data | Actual Czech labour/lease terms make wind-down materially more expensive |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What numeric threshold at end-2029 triggers the board's "way out"? | The bar is stated only for 2030; without an interim number, nobody can act on the 2029 checkpoint the board itself set | Board / CFO | Needed before 2027 launch, not before this entry decision |
| Individual shares and service models of the two incumbents (vs. the combined 55%) | Refines "can we win" beyond a combined concentration number | Further primary research / the market study provider | Could sharpen or soften the concentration caution above |
| Size and reachability of the hospital/lab same-day segment, not covered by the survey | Only source of upside not already in the business case | Commission a follow-up study or direct interviews | Could close part of the headcount gap without adding reps |
| Realistic Czech rep ramp curve vs. Austria's mature-market 40/rep/year | Single largest driver of the whole model | A short Czech pilot, or interviews with the team that ran the 2024 Salzburg extension (closer analog than Austria steady-state) | Directly moves the revenue/margin numbers in every scenario above |
| Local entity, employment, VAT/customs and data-handling requirements for Czech depot and medical logistics | Needed before any commitment; not a strategy question | Legal/tax/compliance specialists | Could add cost or time not in this model |
| Does the EUR5m capital cap include the already-spent EUR120k study and the (unhired) country-manager cost? | Determines real headroom for the 5-rep option that clears the bar | CFO / board | Could make the 5-rep path infeasible inside the stated cap |

