# cme-01-czech-medical on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/13 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question with the minimum bar (EUR 6m, 8% EBIT by 2030, EUR 5m) and kill criteria before analysing. | yes | Title states 'should Kestrel enter by 2027 to reach EUR 6m revenue / 8% EBIT margin by 2030 within EUR 5m capital?' and the 'Minimum bar agreed with board' section (revenue ≥6m, EBIT ≥8%, capital ≤5m, exit trigger) appears before the 'Is the market attractive?' analysis. |
| Sizes the segment top-down (~EUR 31.5m) and bottom-up (~EUR 25.7m) and explains/flags the difference. | yes | "Bottom-up: 2,700 pharmacies x EUR 9,500 = EUR 25.65m/yr ... Top-down: EUR 210m B2B same-day x 15% medical share = EUR 31.5m/yr nationally ... consistent with hospitals/labs and other regions adding the difference." |
| Builds the ramp from reps x win rate and arrives at ~EUR 4.0-4.6m revenue in 2030, below the EUR 6m bar. | yes | "Gross adds/year (reps x 40/rep): 120 ... Accounts end-2030: 425 ... Revenue 2030: EUR 4.04m ... Clears EUR 6m / 8% bar? No (-33% revenue, -6.6pp margin)" |
| Computes 2030 EBIT margin below 8% (about 1% to 5%). | yes | "EBIT margin 2030: 1.4%" for the 3-rep plan. |
| Models at least one aggressive incumbent reaction using the 2024 price-cut evidence and reports its effect. | yes | "5-rep plan under incumbent price war (-12% price) ... Revenue 2030 EUR 5.93m ... EBIT margin 2030 7.7% ... No, narrowly" |
| States that the EUR 120k study is sunk and plays no role. | yes | Assumption #7: "Sunk costs (EUR 120k study, interviewed-but-unhired country manager) carry no weight in the recommendation ... Standard treatment of sunk cost" |
| Compares with the Austrian alternative per euro of capital, and flags that alternative as a management estimate to test. | yes | "Head of Austria's proposal ... EUR 2m capital, management estimate off the 2024 Salzburg extension — a single analogous data point, same evidence grade as the Czech ramp assumptions ... delivers EUR 3.5m revenue at 10% EBIT ... EUR 0.35m EBIT for EUR 2m committed." |
| Does not approve the briefed 3-rep plan; answer includes a stage gate before full capital is committed and says what would make the board revisit it. | NO | Recommendation is "Recommend entering with a 5-rep team from 2027, own depot, pharmacy-led ... and the board's exit trigger kept as written" — this commits to the full 5-rep buildout immediately from 2027 with no pilot phase or staged capital gate before scaling; no 'pilot region' or phased test-the |
| Compares at least two entry modes on cost, speed, control and exit cost. | yes | Entry modes table compares 'Own depot + own sales reps' vs 'Distributor / local partner' across Investment, Time to revenue, Control, Exit cost, Fit. |
| Writes exit criteria and exit cost. | NO | "Exit trigger: if the bar is missed by end of 2029, the board wants a pre-agreed way out (exit cost not yet defined — see Open questions)." Exit cost is explicitly left unquantified and punted to a specialist, not written. |
| Flags that Austrian win rates and prices may not transfer to the Czech market and names the test. | yes | Assumption #1: "Czech reps match Austria's historical win rate from year one ... Would change the answer if: Actual Czech year-1 productivity is materially lower" and item #1 under 'What would change the answer' makes the same point. |
| Does not recommend unconditional entry on the strength of the EUR 210m headline. | yes | Recommendation is built from the detailed ramp/EBIT model and explicit bar comparison, not from the EUR 210m/31.5m headline figure. |
| Does not invent Czech regulatory requirements, competitor names or wage levels as facts; flags them for specialists. | yes | "Czech regulatory/licensing for medical and pharma same-day transport ... is unchecked in the briefing — needs local counsel"; competitors referred to generically as "Incumbent A+B" with no invented names or figures. |

## Transcript

## Turn 1

**User:** Work the Kestrel Czech entry case from the briefing. Quick case, answer page for the board. (Attached in the working directory: cme-01-input.md.)

**Phase done: quick case, market entry.** Answer page written to `case-market-entry-kestrel-czech.md`.

Headline finding, worth flagging up front: the plan as briefed (3 Czech reps from 2027) doesn't come close to the board's bar. Running Kestrel's own Austria account economics (40 accounts/rep/year, 8% churn, EUR 9,500/account) forward to 2030 gives **EUR 4.0m revenue at 1.4% EBIT margin** — a third short on revenue and well short on margin. Capital isn't the constraint (only ~EUR 1.5m of the EUR 5m ceiling gets used).

Resourcing it correctly changes the picture: **5 reps instead of 3** clears both bars (EUR 6.7m revenue, 10.3% margin) at a peak capital draw of only ~EUR 1.0m. But that pass has almost no safety margin — the one piece of competitive evidence in the data (incumbent cut price ~12% for 6 months when a carrier entered in 2024) pushes the 5-rep case right back to the edge: EUR 5.9m revenue, 7.7% margin, a narrow miss on both.

Recommendation: enter, but with a 5-rep team, not 3, and treat the price-war risk and the unsurveyed hospitals/labs channel as the two things to verify before the January 2027 board paper is locked. The Austria alternative (EUR 2m for EUR 3.5m revenue / 10% EBIT) is lower-risk but delivers less EBIT per euro of capital than a correctly-sized Czech entry — not a reason to prefer it outright given capital isn't binding, but worth keeping as the lower-risk fallback.

Full answer page includes the business-case table, entry-mode comparison, assumptions with evidence grades, and open questions (regulatory/licensing specialist, exit-cost specialist, competitor profiling) — all in the file.


## Files in work dir after run

- case-market-entry-kestrel-czech.md
- cme-01-input.md

## File written by the run: case-market-entry-kestrel-czech.md

# Market entry: Kestrel Logistics, Czech Republic medical same-day, should Kestrel enter by 2027 to reach EUR 6m revenue / 8% EBIT margin by 2030 within EUR 5m capital?

**Answer:** Enter, but not on the plan as currently sized. The planned 3-rep team misses the board's own bar by a wide margin (EUR 4.0m revenue, 1.4% EBIT margin by 2030 vs. the EUR 6m / 8% bar). A 5-rep team, using Kestrel's own Austria account-economics unchanged, clears both (EUR 6.7m revenue, 10.3% EBIT margin) at a peak capital draw of about EUR 1.0m — well inside the EUR 5m ceiling. Recommend entering with a 5-rep team from 2027, own depot, pharmacy-led, with hospitals/labs as unsized upside, and the board's exit trigger kept as written.
**Confidence:** Medium — the 5-rep case clears the bar comfortably on Kestrel's own historical account economics, but those economics (40 accounts/rep/year, EUR 9,500 average spend, 8% churn) are an untested transfer from Austria to a new country, and the downside precedent is already in the data: a 2024 incumbent price cut of ~12% would push the 5-rep case to the edge of both bars (EUR 5.9m revenue, 7.7% margin) — a near-miss, not a cushion.
**Specialists and review:** Czech regulatory/licensing for medical and pharma same-day transport (cold chain, controlled substances, patient-data handling) is unchecked in the briefing — needs local counsel before the January 2027 board paper is final. Labour-law review needed for Czech depot and sales-rep contracts (exit/severance terms) before the exit cost in this case is quoted to the board as a number.

## Minimum bar agreed with board
- Revenue at least EUR 6m and EBIT margin at least 8% in the Czech business by 2030; capital at most EUR 5m.
- Exit trigger: if the bar is missed by end of 2029, the board wants a pre-agreed way out (exit cost not yet defined — see Open questions).

## Is the market attractive?
| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Addressable size | Bottom-up: 2,700 pharmacies x EUR 9,500 = EUR 25.65m/yr pharmacy spend in the 3 target regions. Top-down: EUR 210m B2B same-day x 15% medical share = EUR 31.5m/yr nationally (all medical, incl. hospitals/labs). The two triangulate reasonably — national all-medical (31.5m) a little above regional pharmacy-only (25.65m), consistent with hospitals/labs and other regions adding the difference. EUR 6m target is well under 25% of the regional pharmacy pool alone. | Market study 2026; planning convention | Pass |
| Concentration | Two local players hold ~55% of the medical segment combined; per-player split not given. Moderate concentration — not extreme, but the segment is clearly not fragmented. | Market study 2026 (interviews) | Pass with caution |
| Incumbent reaction | In 2024, a new carrier's entry triggered the larger incumbent to cut price ~12% for 6 months. This is the single strongest risk in the data: it is directly actionable against a repeat of the move. | Market study 2026 (interviews, single episode) | Flag — modelled as downside scenario below |
| Barriers / regulation | Not covered in the briefing. | — | Open — see Open questions |

## Can we win?
| Factor | Us (Kestrel) | Incumbent A+B (combined ~55% share) |
|---|---|---|
| Price | Planning assumes EUR 9,500/pharmacy/year holds; no Czech-specific pricing tested | Shown willing to cut ~12% for 6 months to defend share against a new entrant (2024 precedent) |
| Service / relationships | Austria account economics (40 new accounts/rep/year, 8% churn) assumed to transfer unchanged; unverified in Czech market | Established local relationships (no detail in briefing) |
| Capability | Depot + reps model proven in Austria; new country, language, no Czech team yet (candidate interviewed, not hired) | Operating at scale already |

Data gap: no incumbent pricing, service-level or relationship detail beyond the single 2024 price-cut episode. A competitor-profiling pass (not possible without external research access here) would sharpen this before the board paper is finalised.

## Entry modes
| Mode | Investment | Time to revenue | Control | Exit cost | Fit |
|---|---|---|---|---|---|
| Own depot + own sales reps (the plan in the briefing) | ~EUR 1–1.3m peak cash draw by 2028, see business case below | Immediate (reps sell from 2027) | High | Depot lease break + rep severance + customer handover (unquantified, see Open questions) | Matches Austria's proven model; only mode costed in the data given |
| Distributor / local partner *(ASSUMPTION — no data in briefing, directional only)* | Likely lower upfront capital (no EUR 0.9m depot) but gives up part of the 30% gross margin to the partner and loses direct customer relationships | Likely faster (uses partner's existing book) | Lower | Likely lower (contract exit vs. lease/severance) | Not costed — would need a distributor-economics data request before comparing on the board's numbers |

Only the own-depot mode is sized here because it is the only one the briefing gives figures for; the distributor row is directional and flagged, not a substitute for a costed comparison.

## Business case (base / 3-rep plan / 5-rep plan / downside)

Model mechanics, from the briefing's planning convention (revenue = year-end accounts x EUR 9,500) and Austria account economics: with gross adds *g* per year and 8% annual churn applied to the prior year's book, year-end accounts after 4 years (2027–2030) = *g* x 3.545 (compounding 0.92 retention plus new adds each year).

| | 3-rep plan (as briefed) | 5-rep plan (resourced to hit the bar) | 5-rep plan under incumbent price war (-12% price) |
|---|---|---|---|
| Gross adds/year (reps x 40/rep) | 120 | 200 | 200 |
| Accounts end-2030 | 425 | 709 | 709 |
| Revenue 2030 | EUR 4.04m | EUR 6.74m | EUR 5.93m |
| Variable cost (70% of revenue) | EUR 2.83m | EUR 4.72m | EUR 4.15m |
| Fixed cost (depot 0.9m + reps x 0.085m) | EUR 1.155m | EUR 1.325m | EUR 1.325m |
| EBIT 2030 | EUR 0.057m | EUR 0.696m | EUR 0.454m |
| EBIT margin 2030 | 1.4% | 10.3% | 7.7% |
| Clears EUR 6m / 8% bar? | No (-33% revenue, -6.6pp margin) | Yes | No, narrowly (-1.2% revenue, -0.3pp margin) |
| Peak cumulative cash draw before turning cash-positive | ~EUR 1.5m (2027–2029) | ~EUR 1.0m (trough after 2028) | ~EUR 1.1m (estimate) |

Revenue ramp by year, 5-rep plan: 2027 EUR 1.9m, 2028 EUR 3.65m, 2029 EUR 5.26m, 2030 EUR 6.74m. All comfortably inside the EUR 5m capital ceiling even at peak draw.

Two things this table shows the board directly: (1) the 3-rep plan in the briefing is not a close miss — it needs roughly 1.5x more reps than planned to clear either bar; (2) even resourced correctly, the plan has very little margin of safety against the one competitive reaction already seen in this market.

## Compared with the alternative use of capital
Head of Austria's proposal (two added Austrian regions, EUR 2m capital, management estimate off the 2024 Salzburg extension — a single analogous data point, same evidence grade as the Czech ramp assumptions) delivers EUR 3.5m revenue at 10% EBIT by 2030 — EUR 0.35m EBIT for EUR 2m committed. The 5-rep Czech plan delivers roughly double the EBIT (EUR 0.696m) for about half the peak capital (EUR 1.0m) and a larger absolute revenue base, but carries materially higher execution risk: new country, untested rep productivity, untested price point, and a demonstrated incumbent willingness to cut price on entry. The Austria option is lower-risk and capital is not the binding constraint for either, so this is not strictly either/or — but management attention is finite, and the board asked specifically about Czech entry. On the numbers alone, a correctly-resourced Czech entry clears its own bar more comfortably than the Austria alternative clears its; it does so with less certainty behind the inputs.

## What would change the answer
1. If Czech rep productivity in year one comes in materially below the Austria average of 40 accounts/rep/year (plausible — new market, new brand, no local team yet), the 5-rep case's margin of safety disappears and revenue could fall back toward the failing 3-rep case.
2. If hospitals and labs (not covered by the pharmacy survey) add verified, reachable revenue through the same depot and reps, the board could hit its bar with fewer than 5 reps, lowering both cost and execution risk.
3. If the incumbent price reaction in a real entry is sharper or longer than the 2024 precedent (12% for 6 months), the 5-rep case's narrow pass becomes a narrow fail — this is the single most important number to verify before the board paper is final.
4. If regulatory/licensing review turns up a hard blocker or a delay past the 2027 start, the whole ramp shifts a year to the right against a fixed 2030 target.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Czech reps match Austria's historical win rate from year one (no slower first-year ramp in a new market) | 40 new accounts/rep/year | Austria 2023–2025 average | Actual Czech year-1 productivity is materially lower — pushes both plans further below the bar |
| 2 | Churn rate transfers unchanged | 8%/year | Austria historical | Czech incumbents fight harder to retain accounts (raises churn) or Kestrel's service edge lowers it |
| 3 | Average annual spend per pharmacy holds at the surveyed level | EUR 9,500 | Market study survey of 60 of 2,700 pharmacies (2.2% sample — thin) | True average differs from the surveyed 60, or incumbents sustain a price cut beyond 6 months |
| 4 | Czech cost structure (variable cost %, depot fixed cost, rep cost) matches Austria | 70% variable; EUR 0.9m depot; EUR 85k/rep | Austria cost base | Czech labour, fuel or lease costs differ materially |
| 5 | Fixed costs (depot + rep headcount) held flat across the 2027–2030 ramp | EUR 1.155m (3 reps) / EUR 1.325m (5 reps) per year | No scaling data given in briefing | Depot or back-office costs need to scale with volume before 2030 |
| 6 | Hospitals and labs contribute no incremental revenue in this model | EUR 0 (unsized, not zero in reality) | Market study did not survey this channel | A follow-up study sizes this channel as materially positive or confirms it is immaterial |
| 7 | Sunk costs (EUR 120k study, interviewed-but-unhired country manager) carry no weight in the recommendation | EUR 0 influence | Standard treatment of sunk cost | N/A — this is a rule, not a finding |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What exactly triggers the board's "missed by end of 2029" exit — the full 2030 bar assessed early, or a separate interim milestone? | Determines when the exit decision actually fires and what "on track" looks like at each board review | The board | Changes the monitoring plan, not the entry decision itself |
| What is the real addressable spend from hospitals and labs in the 3 target regions? | Not in the 60-pharmacy survey; could close the gap with fewer reps or add upside once 5 reps already clear the bar | Commission a targeted hospital/lab procurement survey or interviews | Could lower the resourcing needed, or confirm 5 reps plus pharmacies is the right scope |
| How is the incumbents' combined 55% split, and what is their cost structure / capacity to sustain a price cut beyond 6 months? | Decides whether the 2024 precedent (12%, 6 months) understates or overstates the real risk | Competitor profiling (desk research + interviews) — not possible without external research access in this session | Could move the downside case from "narrow miss" to "clear fail" or "comfortable pass" |
| What Czech regulatory, licensing or certification requirements apply to medical/pharma same-day transport (cold chain, controlled substances, patient data)? | Could delay the 2027 start or add cost not in this model | Local legal/regulatory specialist | Could shift the whole ramp a year later against a fixed 2030 target, or add fixed cost |
| What does the exit actually cost — depot lease break clause, rep severance under Czech labour law, customer handover? | This is the "way out" the board explicitly asked for; it is currently unquantified | Local legal/HR specialist | Sizes the true downside capital at risk beyond the ramp losses already modelled (~EUR 1.0–1.5m) |
| Is the distributor/partnership entry mode viable, and at what margin give-up and capital saving? | Only the own-depot mode is costed here; a distributor could lower capital at risk further | Business development / local market contacts | Could change the recommended mode, not necessarily the enter/do-not-enter call |

