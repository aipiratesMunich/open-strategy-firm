# cg-01-revenue-gap on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question in the skill's form (gap EUR140m→175m by 2030, EUR15m capital, no acquisitions, EBIT margin ≥10%, March 2027 board) | yes | Title/question: 'which levers close the gap from EUR 140m to EUR 175m revenue by 2030, within EUR 15m capital, no acquisitions, and without group EBIT margin falling below 10%, for the March 2027 board meeting?' |
| Computes a momentum case of about EUR140-141m and a gap of about EUR34m, using the CFO convention | yes | 'Revenue, momentum case (segment CAGR 2023–2025 held to 2030, CFO convention)... EUR 140.7m' and 'Gap / — / EUR 34.3m' |
| Separates market growth from share change and states Kirkby lost share in both lab instruments and process sensors | yes | Table with 'Served market growth (given)' vs CAGR column; Reading column: lab 'Market growing, Kirkby shrinking: losing share'; sensors 'Market growing faster than Kirkby: losing share' |
| Sizes the core (share recovery, price) and installed base (service coverage) before the software adjacency, each with a base case, a range and an evidence grade | NO | Levers table only contains 'Service-contract conversion' and 'Lab-instruments price reset' plus software — there is no separate sized 'share recovery' lever (e.g. holding/regaining lost share in lab and sensors) with its own base case/range/evidence grade; share loss is diagnosed narratively but nev |
| Installed-base lever about EUR4.3m at 50% coverage (or another coverage level with consistent arithmetic) | yes | Base case +EUR7.4m derived from 14,300 uncontracted instruments (35% starting coverage, consistent with 7,700/22,000) at 40% conversion × ~EUR1,298/contract; range +4.6m to +10.2m matches 25%-55% conversion math — internally consistent arithmetic at a different (stated) coverage level. |
| Treats the EUR15m software figure as unsupported: widens range or kills it, names the comparison that would settle it, without inventing one | yes | 'EUR 0 in base case... EUR 0 to EUR 15m, entirely unvalidated... weak — no customer interviews, no pilots, no comparable launch cited'; next steps call for 'a EUR 1–2m paid pilot with 3–5 named customers... and find at least one comparable launch to benchmark ramp against' |
| Shows profit next to revenue for every kept lever and checks the 10% EBIT floor | yes | Levers table has 'EBIT effect (EUR)' column for each lever; 'Margin check' section computes momentum and lever-adjusted margins (~12.4% and ~14.0%) against the 10% floor |
| Shows the remaining gap openly after base-case levers and says how it is closed or accepted | yes | 'Sum of kept levers (base case): EUR 10.0m; remaining gap: EUR 24.3m (71% of the EUR 34.3m gap unclosed)... tell the board directly that validated levers plus even a fully successful software bet... still leave a EUR 9.2m shortfall' |
| Answer line names specific levers with amounts and investment, and a confidence level with one reason | yes | 'convert part of the uncontracted installed base... (base case +EUR 7.4m) and close half the unexplained lab-instruments price gap (+EUR 2.6m)... at under EUR 5m of the EUR 15m budget'; 'Confidence: medium, because the gap and the two core levers rest on Kirkby's own hard data... would change with p |
| Assumptions table and open-questions table in the skill's format | yes | Both tables present with columns '#, Assumption, Value used, Basis, Would change the answer if' and 'Question, Why it matters, Who can answer, Effect on the answer' |
| Must not close the gap by stretching assumptions (e.g. full share recovery plus EUR15m software at base case with no range) | yes | Software kept at EUR0 base case with explicit EUR0–15m range and 'weak' evidence grade rather than being admitted at face value |
| Must not invent market data, competitor prices or benchmark ramp-up rates | yes | Market growth figures are labeled '(given)'; no fabricated competitor prices or ramp benchmarks appear — report explicitly flags the lack of a comparable-launch benchmark rather than inventing one |

## Transcript

## Turn 1

**User:** Work the Kirkby growth case from the briefing pack. Quick case, no engagement folder. I need the answer page for the CEO. (Attached in the working directory: cg-01-input.md.)

The analysis contradicts the head of strategy's premise: software can't be the answer, because it has zero supporting evidence, and even taken at face value it still wouldn't close the gap. Saved to `case-growth-kirkby.md`.

**Headline:** momentum carries Kirkby to only EUR 140.7m by 2030 against a EUR 175m target — a EUR 34.3m gap. Worse, the data shows Kirkby is losing share in *all three* served markets, not just stalling in a flat one. Two validated core levers — converting part of the uncontracted installed base to service contracts (+EUR 7.4m) and closing half the unexplained 7% lab-instruments price gap (+EUR 2.6m) — close only ~29% of the gap, using under a third of the EUR 15m budget, and comfortably keep margin above the 10% floor (margin isn't the real constraint — revenue is). The software bet (EUR 15m revenue claimed for EUR 9m) has no customer interviews, pilots, or comparable launches behind it, so it can't be entered as a plan line; even if it hit its number as claimed, the total still falls EUR 9.2m short of the board's target.

Recommendation: commit the two core levers, stage-gate software behind a cheap pilot instead of the full EUR 9m, and have the CEO tell the board plainly that EUR 175m isn't supportable from this data — it needs new levers (adjacencies/geography, not covered in the briefing), a relaxed constraint, or a reset, ahead of the March 2027 meeting.

Full levers table, risk/sensitivity notes, assumptions (each with a range and what would change it), and open questions (conversion-rate pilot, price-elasticity test, why lab instruments loses share despite being cheaper, and the software validation gate) are in the file.


## Files in work dir after run

- case-growth-kirkby.md
- cg-01-input.md

## File written by the run: case-growth-kirkby.md

# Growth strategy: Kirkby Analytical, which levers close the gap from EUR 140m to EUR 175m revenue by 2030, within EUR 15m capital, no acquisitions, and without group EBIT margin falling below 10%, for the March 2027 board meeting?

**Answer:** Two validated core levers — convert part of the uncontracted installed base to Kirkby service contracts (base case +EUR 7.4m) and close half the unexplained lab-instruments price gap (+EUR 2.6m) — close about EUR 10m of the EUR 34.3m gap (≈29%), at under EUR 5m of the EUR 15m budget, and lift group EBIT margin to about 14%. The head of strategy's process-analytics software is not a third lever yet: EUR 15m of claimed 2030 revenue rests on zero customer interviews, pilots or comparable launches. Recommendation: commit the two core levers now, fund a EUR 1–2m paid-pilot gate for software instead of the full EUR 9m, and tell the board honestly that even if every lever hits its upper case the plan still falls short of EUR 175m — the target needs either new levers not covered in this briefing, a relaxed constraint, or a reset.
**Confidence:** medium, because the gap and the two core levers rest on Kirkby's own hard data (revenue, installed base, contract rate, price gap), but the conversion rate and price-elasticity response are assumptions with no comparable cited; would change with pilot data.
**Specialists and review:** none required to frame the plan; before the board meeting, Legal should confirm service-contract terms support a conversion push, and Finance/FP&A should sign off the momentum and lever math before it goes to the board.

## The gap

| | 2025 | 2030 |
|---|---|---|
| Revenue, momentum case (segment CAGR 2023–2025 held to 2030, CFO convention) | EUR 140m | EUR 140.7m |
| Revenue, target | EUR 140m | EUR 175m |
| Gap | — | **EUR 34.3m** |
| Constraints | Capital ≤ EUR 15m; group EBIT margin ≥ 10%; no acquisitions this cycle; decision at March 2027 board meeting |

Momentum case by segment (CAGR 2023–2025 held for 5 more years to 2030):

| Segment | 2023–25 CAGR | 2030 momentum revenue | Served market growth (given) | Reading |
|---|---|---|---|---|
| Lab instruments | −1.2%/yr (82→80) | EUR 75.2m | +3%/yr | Market growing, Kirkby shrinking: **losing share** |
| Process sensors | +2.6%/yr (38→40) | EUR 45.5m | +6%/yr | Market growing faster than Kirkby: **losing share** |
| Service | 0%/yr (20→20) | EUR 20.0m | +4%/yr | Market growing, Kirkby flat: **losing share** |
| **Total** | | **EUR 140.7m** | | **Kirkby is losing share in all three served markets** — the core problem is not "the market is flat," it is share loss across the board. This kills the framing that the core has nothing left to give and the only growth is a new product line. |

## Levers

| Lever | Revenue base case (2030) | Range | EBIT effect (EUR) | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Service-contract conversion on uncontracted installed base | +EUR 7.4m | +EUR 4.6m to +10.2m | +EUR 1.5m base case (range +0.9m to +2.0m, assumed ~20% margin on incremental, below the 24% book rate to allow for ramp cost) | ~EUR 3m (field service capacity, dispatch/CRM) | Ramps 2027–2030 | weak–medium: installed base and current contract rate are hard CRM data; the conversion rate itself is an assumption with no comparable cited | keep |
| Lab-instruments price reset (close half the 7% gap, +3.5%) | +EUR 2.6m | EUR 0 to +5.3m | +EUR 2.1m base case (range 0 to +4.2m; assumed ~80% pass-through to EBIT) | <EUR 1m (repricing, sales enablement, phased test) | Fast — phase in 2027–2028 | weak–medium: the 7% gap and "no volume reason recorded" are hard sales data; the assumption of no volume loss from closing it is untested | keep, but test in one region/channel before full rollout |
| Process analytics software | EUR 0 in base case (claimed EUR 15m not admitted) | EUR 0 to EUR 15m, entirely unvalidated | not sizeable — no cost or margin data for a new software line | EUR 9m requested | Claimed by 2030, no ramp evidence | weak — no customer interviews, no pilots, no comparable launch cited; classic inside-view forecast | option — stage-gate behind a EUR 1–2m pilot with 3–5 named customers before committing more capital |

**Sum of kept levers (base case):** EUR 10.0m; **remaining gap:** EUR 24.3m (71% of the EUR 34.3m gap unclosed); **how we close or accept it:** present the two kept levers as committed, present software as a gated option (upside EUR 0–15m, not yet in the plan), and tell the board directly that validated levers plus even a fully successful software bet (EUR 10.0m + EUR 15m = EUR 25.0m) still leave a EUR 9.2m shortfall against EUR 175m — the target is not supportable from this data alone.

**Margin check:** momentum-case 2030 EBIT margin ≈ 12.4% (vs 12.3% in 2025); with the two kept levers added, revenue EUR 150.7m and EBIT ≈ EUR 21.1m → margin ≈ 14.0%, comfortably above the 10% floor. Even adding the unvalidated software revenue at a conservative 5% margin for a nascent line keeps the blended margin above 13%. **Margin is not the binding constraint here — revenue is.**

**Capital check:** the two kept levers need roughly EUR 3–5m of the EUR 15m budget. That leaves EUR 10–12m — enough to fund a staged software pilot (EUR 1–2m) and still hold a reserve, without touching the acquisition ban or the margin floor.

## Killed options and why

- **Software at the claimed EUR 15m / EUR 9m, taken as a planned lever:** not killed outright, but killed as a *base-case plan line* — no customer interviews, pilots or comparable launches were cited, so there is no evidence basis to size it. Re-opens only once a pilot produces real adoption and willingness-to-pay data.
- **"The market has stalled, so growth must come from a new product" (the implicit premise behind going straight to software):** killed by the market-growth data — all three served markets are growing (3–6%/yr); Kirkby is losing share in each one. The core is not out of room.

## Risks and what would change the answer

1. If service-contract conversion lands at the low end (25% instead of 40%), that lever drops from EUR 7.4m to EUR 4.6m, and the two-lever base case falls from EUR 10.0m to about EUR 7.3m — the gap gets even harder to close. A fast pilot campaign in 2027 would give a real conversion rate well before the 2030 horizon.
2. If the lab-instruments price increase triggers volume loss (plausible — spec-comparable instruments are already priced 7% below competitors and still losing share, which suggests price is not what is winning or losing volume there), that lever could net close to zero. Test in one region before rolling out everywhere.
3. If the software pilot fails to find paying, validated demand, the EUR 9m should not be spent at all — reallocate toward scaling the two core levers or funding the adjacency research named below.

## Next steps

| What | Who | By when |
|---|---|---|
| Launch service-contract conversion campaign on the 14,300 uncontracted instruments; track real conversion rate | Head of Service | Start Q1 2027 |
| Run a controlled price test (+3.5–7%) on lab instruments in one region/channel; measure volume response | Sales / Pricing | Result by Q1 2027, ahead of board meeting |
| Investigate why lab instruments is losing share despite being priced below competitors (product age, spec, channel — not a price problem on its face) | Product / Commercial | By mid-2027 |
| Run a EUR 1–2m paid pilot with 3–5 named customers for process analytics software, and find at least one comparable launch to benchmark ramp against, before committing the remaining EUR 7–8m | Head of Strategy | Pilot results by Q3 2027; go/no-go gate before further spend |
| Scope adjacency and geography levers not covered in this briefing (new segments, consumables, international) to find the EUR 24m still unaccounted for | Strategy team | Feed into a Q3 2027 plan update |
| Decide with the board whether to accept a lower 2030 number, add capital/relax the no-M&A rule, or extend the timeline, given validated levers plus even a successful software bet leave a EUR 9.2m shortfall | CEO with board | March 2027 meeting |

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Service-contract conversion rate on the 14,300 uncontracted instruments by 2030 | 40% base case (range 25–55%) | No Kirkby data on third-party-to-Kirkby conversion; ASSUMPTION, wide range | Pilot data from Q1 2027 campaign shows a materially different rate |
| 2 | Volume response to closing half the lab-instruments price gap | 0% volume loss from a +3.5% price move | ASSUMPTION — no price-elasticity study provided | Price test shows volume erosion, which would shrink or kill this lever |
| 3 | Incremental EBIT margin on new service-contract revenue | ~20% (vs 24% book rate on existing contracts, discounted for ramp cost) | ASSUMPTION | Actual cost-to-serve data for new contracts becomes available |
| 4 | Software revenue and margin | EUR 0 in the base case; EUR 15m / EUR 9m noted only as unvalidated upside | Head of strategy slide, Aug 2026 — no interviews, pilots or comparables cited | A pilot with named customers and a comparable-launch benchmark produces real adoption and margin data |
| 5 | All 14,300 uncontracted instruments are addressable (not retired or decommissioned) | 14,300 | CRM count; service manager's comment does not split active-but-third-party-serviced from genuinely unserviced/retired units | CRM data shows a material share of the 14,300 is inactive |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What conversion rate can a real campaign achieve on the uncontracted installed base? | It is the largest lever and swings the two-lever base case between EUR 7.3m and EUR 15.5m | Head of Service, via a 2027 pilot campaign | Could move total validated levers from ~21% to ~45% of the gap |
| Does a lab-instruments price increase cause volume/share loss? | Second lever; could net to zero if elasticity is high | Sales/Pricing, via a controlled regional price test | Swings this lever between EUR 0 and +EUR 5.3m |
| Why is lab instruments losing share while priced below competitors? | Suggests the problem isn't price — could be product age, spec, or channel, and could reveal a larger or entirely different core-defense lever | Product/Commercial team | Could add a new, currently unsized lever, or confirm the segment is structurally declining |
| Does the process-analytics opportunity hold up with a real pilot and a comparable launch benchmark? | EUR 9m of the EUR 15m budget and the board's current headline story rest on zero evidence today | Head of Strategy, via a staged pilot | Could add up to EUR 15m or be killed entirely — materially changes whether EUR 175m is even approachable |
| Are there adjacency or geography levers not covered in this briefing? | Even the optimistic case (all levers at upper end, software included) leaves a shortfall against EUR 175m | Strategy team, next-phase research | Could be the difference between reaching the target and falling well short |

