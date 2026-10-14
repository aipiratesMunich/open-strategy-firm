# cme-01-czech-medical on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (13/13 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question with the minimum bar (EUR 6m, 8% EBIT by 2030, EUR 5m) and kill criteria before analysing. | yes | Step 1 states 'at least EUR 6m revenue ... 8% EBIT margin ... EUR 5m' and Step 2 issue tree lists a 'Kill criterion' column per hypothesis, both preceding the Step 3 deciding analyses. |
| Sizes the segment top-down (~EUR 31.5m) and bottom-up (~EUR 25.7m) and explains or flags the difference. | yes | 'Top-down... 210m × 15% = EUR 31.5m... Bottom-up... 2,700 × EUR 9,500 = EUR 25.65m... these two figures are not on the same footing... treat as a scope mismatch' |
| Builds the ramp from reps x win rate and arrives at about EUR 4.0m to 4.6m revenue in 2030, below the EUR 6m bar. | yes | '3 reps from 2027, each winning 40 new accounts/year... Revenue (EUR m)... 4.04' at 2030, explicitly below the EUR 6m bar. |
| Computes 2030 EBIT margin below 8% (about 1% to 5%). | yes | 'EBIT margin ... 1.4%' for 2030 base case, versus the 8% bar. |
| Models at least one aggressive incumbent reaction using the 2024 price-cut evidence and reports its effect. | yes | 'Low case (12% revenue-per-account compression... mirroring the 2024 incumbent reaction)... margin... turns negative in the compression period.' |
| States that the EUR 120k study is sunk and plays no role. | yes | 'the EUR 120k study and the interviewed-not-hired country manager are sunk and excluded from the decision' |
| Compares with the Austrian alternative per euro of capital, and flags that alternative as a management estimate to test. | yes | 'EUR 2m capital → EUR 3.5m revenue at 10% EBIT by 2030 (management estimate, but anchored to an actual completed comparable...); return ≈ 17.5% of capital' |
| Does not approve the briefed 3-rep plan; answer is do not enter/enter later/enter under conditions with a stage gate. | yes | 'Do not approve full-scale Czech entry... approve a bounded Czech pilot (1 rep, single region...) to test the two assumptions... before committing capital at the ~5-rep scale' |
| Compares at least two entry modes on cost, speed, control and exit cost. | yes | Entry modes table compares 'Own depot + sales reps' vs 'Partner with an existing Czech courier/distributor' across Investment, Time to revenue, Control, Exit cost, Fit. |
| Writes exit criteria and exit cost. | yes | 'Board-set exit trigger: if the bar is not on track by end of 2029' and cumulative burn figures (e.g. '3 reps: ≈ -EUR 1.46m cumulative') used as the exit-cost proxy, with wind-down cost flagged separately as needing refinement. |
| Flags that Austrian win rates and prices may not transfer to the Czech market and names the test. | yes | 'both price (EUR 9,500) and productivity (40/rep/year) are transplanted, untested locally. Fix: the recommended pilot' (bounded Czech pilot, 1 rep, one region, 12-18 months). |
| Does not recommend unconditional entry on the strength of the EUR 210m headline. | yes | Recommendation is to not approve full entry and instead fund Austria plus a bounded pilot, not unconditional entry on the EUR 210m/EUR 31.5m headline. |
| Does not invent Czech regulatory requirements, competitor names or wage levels as facts; flags them for specialists. | yes | 'Barriers and regulation / Not addressed in the brief / — / open — needs regulatory/compliance specialist'; incumbents referred to only as 'Incumbent A+B', not invented names. |

## Transcript

## Turn 1

**User:** Work the Kestrel Czech entry case from the briefing. Quick case, answer page for the board. (Attached in the working directory: cme-01-input.md.)

Written to `case-market-entry-kestrel.md`. Headline result:

**The plan as budgeted (3 reps, own depot) misses the board's bar badly** — EUR 4.04m revenue by 2030 (-33% vs. EUR 6m) and 1.4% EBIT margin (vs. 8%) — even under optimistic assumptions (full Austria-level rep productivity transferred unchanged to a new country, zero incumbent price reaction). Hitting the bar would need ~5 reps instead of 3, and even then the result (10.3% margin) rests on stacked, unverified assumptions, against incumbents who cut price ~12% for six months the last time a new carrier entered.

Capital turns out not to be the constraint anywhere — every scenario burns well under the EUR 5m cap. The real risk is commercial execution: Czech rep productivity, incumbent reaction, and the true depot footprint (one depot vs. one per region, which would wreck every scenario) are all untested.

**Recommendation:** don't approve full Czech entry at the January 2027 board. Fund the Austria two-region extension now (EUR 2m, EUR 3.5m revenue / 10% margin by 2030, backed by an actual 2024 precedent) — it beats Czech on a risk-adjusted basis. Run a bounded Czech pilot (1 rep, one region, ~EUR 0.3-0.5m, 12-18 months) to get real data on the two assumptions the whole case depends on, with a hard checkpoint at end of 2029 per the board's own exit requirement.

Full breakdown — issue tree, all eight deciding analyses with arithmetic, business case (base/low/high), entry-mode comparison, assumptions, open questions (incl. regulatory/legal specialists to loop in), and trap checks — is in the file.


## Files in work dir after run

- case-market-entry-kestrel.md
- cme-01-input.md

## File written by the run: case-market-entry-kestrel.md

# Market entry: Kestrel Logistics, Czech Republic medical same-day, quick case

## Step 1: Sharpen the question

Decision question: **"Should Kestrel take medical same-day delivery into the Czech Republic by 2030, given it must deliver at least EUR 6m revenue and 8% EBIT margin within EUR 5m capital, with an exit if the bar is missed by end of 2029 — and is this better than adding two Austrian regions for EUR 2m?"**

Everything the sharpening round normally has to ask for is already in the brief: minimum bar (EUR 6m / 8% / by 2030), capital ceiling (EUR 5m), time window (board decides Jan 2027, exit checkpoint end-2029), segment (pharmacies named and modelled; labs/clinics named in scope but not sized), and what's already spent (EUR 120k study, one interviewed-not-hired country manager — both sunk, see trap checks). No further round needed; gaps are carried as Open questions below rather than blocking the case.

## Step 2: Issue tree

| Branch | Hypothesis | Kill criterion | Verdict (this case) |
|---|---|---|---|
| Attractive: size | Pharmacy SAM in the 3 target regions is at least EUR 6m and growing | Bottom-up SAM below EUR 6m | **Not killed** — SAM ≈ EUR 25.65m (§3a), far above the bar; growth rate unknown (open question) |
| Attractive: structure | No player holds more than ~50% of the segment | Top incumbents together above ~50% with entrenched relationships, proven aggressive reaction | **Caution** — two players hold ~55% combined and cut price ~12% for 6 months against a 2024 entrant (§3b) |
| Attractive: barriers | Certification/local rules passable within the window | Approval takes longer than the window or needs local content Kestrel can't provide | **Open** — no data; see Open questions (specialist needed) |
| Can win: need | Target pharmacies would switch from current couriers | Buyers solve it well today, no switching trigger found | **Open** — no interview evidence either way |
| Can win: position | Kestrel beats incumbents on at least one buying criterion | No advantage once local price/service is included | **Weak** — no differentiation named beyond matching the going rate (EUR 9,500/pharmacy) |
| How: mode | One mode reaches revenue within budget and exits cheaply | Every mode needs more capital/time than allowed | **Reshaped** — capital is not binding (§3e, §3f); recommend a bounded pilot mode, not immediate full own-build |
| Pays | Base case reaches the bar by 2030 | Base case misses the bar, or low case loses more than tolerable | **Killed** as currently planned (3 reps); **marginal-at-best** even scaled up (§3f) |
| Beats alternatives | Czech entry returns more per euro of capital than the Austria extension | Austria earns more for the same capital | **Killed** — Austria wins on a risk-adjusted basis (§3h) |

## Step 3: Deciding analyses

### 3a. Addressable market (bottom-up / top-down, triangulated)

- Top-down, national: EUR 210m B2B same-day × 15% medical/pharmacy share = **EUR 31.5m**, Czech Republic-wide (market study, 2026).
- Bottom-up, regional: 2,700 pharmacies in the 3 target regions × EUR 9,500/year average spend = **EUR 25.65m**, but only for the 3 target regions, not nationwide, and pharmacy-only (survey of 60 pharmacies; hospitals/labs explicitly not covered).

These two figures are not on the same footing — one is national, the other is three regions and pharmacy-only — so they don't triangulate cleanly; treat as a scope mismatch, not a reconciled estimate. **Kestrel's own business model (reps, accounts, the EUR 9,500 planning convention) is built purely around pharmacy accounts**, so EUR 25.65m (3-region, pharmacy-only) is the relevant SAM for the plan as designed. The gap between the two figures (≈ EUR 5.85m, if the regions were representative of the national split, which is unverified) is the untested headroom in hospitals/labs — named in scope ("pharmacies, labs, clinics") but absent from every number in the brief. **Hypothesis: not killed on size** — EUR 25.65m pharmacy SAM comfortably clears the EUR 6m bar in principle; the open question is share, not size.

### 3b. Market structure

Two local players hold ~55% of the medical segment combined, leaving ~45% (≈ EUR 11.5m of the EUR 25.65m pharmacy SAM, or ~1,215 of the 2,700 pharmacies) not held by the top two — though that 45% is "not the top two," not "available to Kestrel"; smaller incumbents may already hold part of it (no competitor-profiling data for the long tail). More material: when a new carrier entered in 2024, the larger incumbent cut prices ~12% for six months. That is a direct precedent for how Kestrel's own entry would be met. **Hypothesis: caution, not an automatic kill** — concentration is moderate-high (below the ~70-80% level that would be an automatic kill in a more concentrated market) but the demonstrated reaction is a real cost that the business case below does not yet price in except as a sensitivity.

### 3c. Customer need and switching

No interview data in the brief on why a pharmacy would switch couriers, or what it values (price, speed, reliability, cold-chain handling). **Open, untested** — this is the home-market-transfer trap: Kestrel is carrying over its Austrian price point (EUR 9,500/account) and win rate (40 accounts/rep/year) into a market where neither has been tested. Flagged as the single largest source of uncertainty in the numbers below.

### 3d. Competitors and their reaction

Only the two large incumbents are profiled, and only on one data point each (combined share, one historical price reaction). No profile of their service model, relationships, or how they'd specifically respond to Kestrel (vs. the unnamed 2024 entrant). Used directionally in the Low case (§3f) via the 12%-price-cut precedent; a full profile is an open question.

### 3e. Entry modes

| Mode | Investment | Time to revenue | Control | Exit cost | Fit |
|---|---|---|---|---|---|
| Own depot + sales reps (as planned) | EUR 0.9m/yr depot + EUR 85k/rep/yr; cumulative burn ≈ EUR 0.75-1.5m over 2027-30 (§3f) | Slow — 3-4 years to approach the bar | High | Depot lease break + rep severance (unestimated, see Open questions) | Matches the Austria playbook, but untested cross-border |
| Partner with an existing Czech courier/distributor for last-mile, thin local commercial layer | Lower upfront — no depot capex, pay-per-delivery to partner (no partner economics in brief; ASSUMPTION, directional only) | Faster launch, no depot build time | Lower — depends on partner | Low — contract termination | Better fit for a bounded pilot to de-risk the untested assumptions in §3c/3d before committing capital |

The brief only costs the first mode in detail; the second is included directionally and labelled as an assumption, not left "not costed."

### 3f. Entry business case

Revenue convention given: revenue in a year = pharmacy accounts in force at year end × EUR 9,500. Churn 8%/year. 3 reps from 2027, each winning 40 new accounts/year (Austria 2023-25 average, applied unchanged to a new country — flagged assumption). Variable cost 70% of revenue (30% contribution margin). Fixed cost = EUR 0.9m depot + EUR 85k per rep.

**Base (plan as stated, 3 reps, full Austria productivity, no incumbent reaction):**

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| Accounts (year end) | 120 | 230 | 332 | 425 |
| Revenue (EUR m) | 1.14 | 2.19 | 3.15 | 4.04 |
| EBIT (EUR m) | -0.81 | -0.50 | -0.21 | +0.06 |
| EBIT margin | — | — | — | 1.4% |

2030 result: **EUR 4.04m revenue (-33% vs. the EUR 6m bar), 1.4% margin (vs. 8% bar)**. Needed accounts for EUR 6m: 6,000,000 / 9,500 ≈ **632**. The 3-rep plan reaches 425 — short by 207 accounts, even before any ramp-up discount or incumbent reaction is applied. **Hypothesis "pays" is killed as currently planned.**

**What it would take to hit the bar:** solving accounts(2030) = 632 for constant annual gross adds g: g × (1 + 0.92 + 0.92² + 0.92³) = 632 → g ≈ 178/year → **≈4.5 reps**, i.e. between 4 and 5 reps, not the planned 3.

- 4 reps (160 adds/yr): 2030 revenue EUR 5.39m (-10%), EBIT margin 7.0% (still under 8%).
- 5 reps (200 adds/yr): 2030 revenue EUR 6.74m (+12%), EBIT margin 10.3% (clears 8%).

Neither is a clean fit to the bar — the plan either slightly undershoots on 4 reps or overshoots on 5 — and both require Austria-level productivity and zero incumbent reaction to hold, unverified, in year one of a new country.

**Capital check:** cumulative EBIT (proxy for cash burn, ignoring capex/working capital — not itemised in the brief) across 2027-2030:
- 3 reps: ≈ **-EUR 1.46m** cumulative.
- 4 reps: ≈ **-EUR 0.75m** cumulative.
- 5 reps: ≈ **-EUR 0.04m**, roughly breakeven over the period.

All three are well inside the EUR 5m cap. **Capital is not the binding constraint in any scenario modelled — commercial execution is.**

**Low case** (12% revenue-per-account compression for ~12 months, mirroring the 2024 incumbent reaction, applied to the 5-rep plan): contribution margin compresses enough that the already-thin 7-10% margin case turns negative in the compression period and payback slips past 2030 — modelled directionally; exact figure needs the competitor-profiling work in §3d.

**High case:** 5 reps, full Austria productivity, no incumbent reaction → EUR 6.74m revenue, 10.3% margin by 2030, as above — the only scenario that clears both bars, and it stacks three unverified assumptions (productivity transfer, no retaliation, single depot serving all 3 regions — see Open questions on depot footprint, where 3 depots instead of 1 would push every scenario deeply negative).

**Hypothesis "pays": killed for the plan as budgeted (3 reps); reshaped to "marginal, and only with ~5 reps and every assumption holding" for the scaled-up version.**

### 3g. Stress test

Two stress factors dominate and are not yet quantified from independent data: (1) rep productivity in an unfamiliar country vs. the mature Austrian book, and (2) the incumbent's proven willingness to cut price ~12% for six months against a new entrant. Both push the already-marginal 4-5 rep case toward failing the 8% margin bar. No growth rate was given for the underlying market either, so the SAM in §3a is a static snapshot, not a 2030 projection — treat the 6m target as a larger effective share of today's market than stated.

### 3h. Alternative use of capital

Austria 2-region extension: EUR 2m capital → EUR 3.5m revenue at 10% EBIT by 2030 (management estimate, but anchored to an actual completed comparable — the 2024 Salzburg-region extension, a real domestic precedent). EBIT = EUR 0.35m; return ≈ 17.5% of capital at 2030 run-rate.

Czech base case (3 reps): EUR 0.06m EBIT off ≈EUR 1.5m cumulative capital ≈ 4% — and misses the board's bar outright.
Czech high case (5 reps, all assumptions holding): EUR 0.70m EBIT off ≈EUR 1m cumulative capital ≈ 70% — nominally attractive, but rests on stacked, untested assumptions, against a domestic alternative resting on a real precedent.

**Hypothesis "beats alternatives": killed.** On a risk-adjusted basis — same company, same management bandwidth, one proven move vs. one unproven one — Austria is the better use of the next euro of capital today. Czech entry only outranks it if the pilot in the recommendation below confirms productivity and reaction assumptions that are currently just transplanted from a different country.

## Step 4: Trap checks

- [x] Share built bottom-up from named customers (2,700 pharmacies), channel capacity (reps × 40/year) and win rates, not "1% of a big market."
- [ ] Customers, channels and price levels tested in the target market — **open**: both the EUR 9,500/account figure and the 40-accounts/rep/year rate are transplanted from Austria/the Czech survey respectively, with no Czech-specific pilot evidence. Fix: run the bounded pilot in the recommendation.
- [x] At least one aggressive incumbent reaction modelled — the 2024 12%-price-cut precedent is used directionally in the Low case (§3f); not yet fully quantified (needs §3d competitor profiling).
- [x] Sunk costs play no role — the EUR 120k study and the interviewed-not-hired country manager are sunk and excluded from the decision below.
- [ ] Ramp compared with a comparable entry — **partially**: only a domestic comparable exists (Austria/Salzburg); no cross-border comparable was available, so the range is widened and the gap is named rather than hidden.
- [x] Money already spent called sunk, as above.
- [x] Exit criteria and exit cost written down before entry (see Answer page).
- [x] Entry compared with the best alternative use of the same capital (§3h, Austria extension).

## Step 5: Answer page

# Market entry: Kestrel Logistics, Czech Republic medical same-day, should Kestrel enter by 2030?

**Answer:** Do not approve full-scale Czech entry at the January 2027 board under the plan as scoped (3 reps, own depot). As budgeted it reaches EUR 4.04m revenue and 1.4% EBIT margin by 2030 — 33% short on revenue and far short on margin against the board's EUR 6m / 8% bar — even under optimistic assumptions. Instead: fund the Austria two-region extension now (EUR 2m, clears the bar on a proven 2024 precedent) and approve a bounded Czech pilot (1 rep, single region, 12-18 months, ≈EUR 0.3-0.5m exposure) to test the two assumptions the whole Czech case rests on — Czech-specific rep productivity and the incumbents' price reaction — before committing capital at the ~5-rep scale that would be needed to clear the bar.

**Confidence:** medium, because the arithmetic on the given data is solid (the 3-rep plan's shortfall and the capital headroom are not close calls), but the inputs that decide whether a scaled-up Czech entry *could* work — rep productivity outside Austria, actual incumbent reaction, true depot footprint, and the unsized labs/clinics segment — are all untested assumptions, not evidence; would change to low confidence if 3 depots (one per region) are actually needed, and to high confidence either way once the pilot produces real Czech data.

**Specialists and review:** regulatory/compliance (medical/pharma same-day certification, cold-chain and data-protection rules for health information — not addressed anywhere in the brief); legal (depot lease terms and rep employment/severance terms in Czech labour law, relevant to exit cost); finance (verify the cumulative-EBIT proxy against actual capex/working-capital needs before sizing the EUR 5m ask).

## Minimum bar agreed with client
- Revenue at least EUR 6m by 2030; EBIT margin at least 8%; capital at most EUR 5m
- Kill criteria: bottom-up SAM below EUR 6m (not met — SAM is well above); top incumbents' combined share plus proven aggressive reaction (caution, not an automatic kill — 45% of the pharmacy segment is not held by the top two, though not all of it is necessarily winnable); base case EBIT/revenue missing the bar (met — plan as budgeted misses by a wide margin)
- Board-set exit trigger: if the bar is not on track by end of 2029

## Is the market attractive?
| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Addressable size and growth | Pharmacy SAM ≈ EUR 25.65m (3 target regions); national medical segment ≈ EUR 31.5m (scope mismatch, not reconciled); no growth rate given | Market study 2026 (survey of 60 pharmacies; national B2B figure) | pass (size), open (growth) |
| Concentration and incumbents | Two players hold ~55% combined; cut price ~12% for 6 months against a 2024 entrant | Market study interviews | caution |
| Barriers and regulation | Not addressed in the brief | — | open — needs regulatory/compliance specialist |

## Can we win?
| Factor | Kestrel (planned) | Incumbent A+B (combined) |
|---|---|---|
| Share | 0% today; targeting ~15-25% of regional pharmacies by 2030 depending on rep count | ~55% of the medical segment |
| Price | EUR 9,500/account (transplanted survey average, untested as Kestrel's own price) | Unknown; demonstrated willingness to cut ~12% against a new entrant |
| Differentiation | None named in the brief | Entrenched relationships (unprofiled) |
| Evidence | Austria rep productivity and churn (own data, mature market) | One historical reaction data point (2024) |

## Entry modes
| Mode | Investment | Time to revenue | Control | Exit cost | Fit |
|---|---|---|---|---|---|
| Own depot + reps (as planned) | EUR 0.9m/yr depot + EUR 85k/rep/yr | Slow, 3-4 yrs | High | Depot lease break + severance (unestimated) | Matches Austria playbook; untested cross-border |
| Partner/distributor for last-mile (ASSUMPTION, directional) | Lower upfront, variable cost to partner | Faster | Lower | Low (contract exit) | Best fit for the recommended pilot |

## Business case (base / low / high)
| | Base (3 reps, as planned) | Low (5-rep plan + 12% price-war compression) | High (5 reps, full productivity, no reaction) |
|---|---|---|---|
| Revenue 2030 | EUR 4.04m | Materially below EUR 6.74m; exact figure needs §3d competitor profiling | EUR 6.74m |
| EBIT margin 2030 | 1.4% | Negative during the compression window; recovery uncertain | 10.3% |
| Cumulative investment 2027-30 | ≈ EUR 1.46m | Higher than EUR 0.04m base-5-rep case; not fully quantified | ≈ EUR 0.04m (near breakeven) |
| Payback by 2030 | Not reached | Not reached | Reached ≈2029 |

## Compared with the alternative use of capital
The Austria two-region extension turns EUR 2m into EUR 3.5m revenue and 10% EBIT (EUR 0.35m) by 2030, anchored to a completed 2024 comparable (Salzburg). That is a better risk-adjusted return than the Czech base case (which misses the bar outright) and is at least as good as the optimistic Czech high case — without the stacked untested assumptions (cross-border productivity transfer, no incumbent retaliation, single-depot footprint) that the Czech case depends on. Same management bandwidth, one proven move versus one unproven one: fund Austria now.

## What would change the answer
1. If a bounded Czech pilot (1 rep, one region, 12-18 months) shows win rates and account retention near the Austrian average with price intact, then scaling toward the 5-rep plan becomes evidence-based rather than assumption-based, and the case should be re-run at the January 2027+1 board.
2. If the depot footprint turns out to need one per region (3 depots, not 1), every scenario above goes deeply negative — resolve this before any capital commitment.
3. If labs/clinics (named in scope but entirely unsized) turn out to be a material, separately winnable revenue pool, the revenue gap to the EUR 6m bar could close without needing the full 5-rep pharmacy push — currently unverifiable from the brief.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Czech rep productivity equals Austria's | 40 new accounts/rep/year | Kestrel's own 2023-25 Austria average | Czech-market pilot shows materially lower (or higher) win rates |
| 2 | Single depot serves all 3 target regions | EUR 0.9m/year fixed | Brief states "a depot," singular | 3 regional depots are actually needed (fixed cost ×3, kills every scenario) |
| 3 | No incumbent price reaction in the base/high cases | 0% compression | Optimistic; the 2024 precedent (12% for 6 months) argues against this | Any price/win-rate compression is applied, which already threatens the 8% margin bar even in the 5-rep case |
| 4 | EUR 9,500/pharmacy/year average spend holds for Kestrel's own pricing | EUR 9,500 | Market study survey of 60 pharmacies | Kestrel's actual achievable price per account differs once tested |
| 5 | Churn rate of 8%/year transfers unchanged to Czech Republic | 8%/year | Austria own data | Czech churn proves materially higher/lower |
| 6 | Cumulative EBIT approximates cash/capital need (no separate capex or working-capital line) | EUR ~0-1.5m across scenarios | No capex figures given in brief | Depot build-out, vehicles or working-capital needs add materially to the EUR 5m ask |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is the national medical segment (EUR 31.5m) representative of the 3 target regions, or are these figures scope-mismatched? | Determines whether there's real headroom beyond the pharmacy-only EUR 25.65m SAM | Market study authors / Kestrel market research | Could widen or shrink the real addressable size |
| How big is the hospitals/labs/clinics opportunity, explicitly out of the pharmacy survey? | Service is scoped as "pharmacies, labs, clinics" but every number in the plan is pharmacy-only | Market study authors (follow-up study) | Could close some or all of the revenue gap to EUR 6m without more pharmacy reps |
| What regulatory/certification requirements apply to medical same-day delivery in the Czech Republic (cold-chain, controlled substances, health-data handling)? | Could gate the entire entry regardless of the commercial case | Regulatory/compliance specialist | Could add time or cost outside the current model, or rule out the planned mode |
| Is the EUR 0.9m depot cost for one depot covering all 3 regions, or per region? | Triples fixed cost if per-region, which kills every scenario modelled | Kestrel operations/finance | Determines whether any version of the plan can hit 8% margin |
| What would the two incumbents specifically do against Kestrel (not just the generic 2024 entrant)? | The 12% cut is one historical data point against an unnamed competitor, not a profile of these two players' likely response to Kestrel specifically | Competitor profiling / sales intelligence | Refines the Low case materially |
| What is the actual wind-down cost (depot lease break, rep severance, customer handover) if Czech is exited by end of 2029? | The board explicitly wants a defined way out; exit cost is currently just "cash burn to date," with no wind-down figure | Legal/HR + finance | Determines the true downside of entering at all |
| Does Czech labour and lease law allow the depot/rep structure to be exited cheaply within the board's timeframe? | Affects the true exit cost and the "reversibility" of the own-build mode | Legal specialist | Could favour the partner/distributor mode over own-build |

## Trap checks
- [x] Share is built bottom-up from customers (2,700 pharmacies), channel capacity (reps) and win rates, not "1% of a big market."
- [ ] Customers, channels and price levels tested in the target market — open; both price (EUR 9,500) and productivity (40/rep/year) are transplanted, untested locally. Fix: the recommended pilot.
- [x] At least one aggressive incumbent reaction modelled, via the 2024 12%-price-cut precedent (directional, in the Low case).
- [x] Sunk costs (EUR 120k study, interviewed country manager) play no role in the recommendation.
- [ ] Ramp compared with comparable entries — only a domestic comparable (Austria/Salzburg) exists; no cross-border comparable was available, so the range is widened and the gap is named rather than papered over.
- [x] Money already spent is called sunk and plays no role.
- [x] Exit criteria (end-2029 checkpoint against the account/margin trajectory) and exit cost (cash burn to date + wind-down, wind-down cost itself flagged as an open question) are written down before entry.
- [x] Entry is compared with the best alternative use of the same capital (Austria two-region extension, §3h) — and loses on a risk-adjusted basis as currently scoped.

