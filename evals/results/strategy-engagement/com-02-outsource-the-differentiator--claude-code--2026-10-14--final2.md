# com-02-outsource-the-differentiator on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States early that outsourcing conflicts with evidence that customers choose Halvorsen for on-site calibration (62% of wins) | yes | "62% of won deals name Halvorsen-technician on-site calibration as the top reason chosen" appears in the headline/answer section before other analysis. |
| Quantifies pilot churn effect (9 points) and contribution at risk (~EUR 2.2m/yr) against EUR 1.8m saving, with arithmetic shown | yes | "9% × 3,000 = 270 customers × EUR 18,000 × 45% = EUR 2.19m/yr lost, against EUR 1.8m/yr saved" — full arithmetic chain shown including the 9-point churn figure. |
| Flags the pilot as one region/one year (evidence strength medium at best) and proposes confirmation without inventing data | NO | Despite noting the pilot is "n=400, one region, 12 months" and listing it as an assumption, the report explicitly states "Confidence: High on the two kill findings (the arithmetic is direct from the data given)" — overclaiming certainty rather than framing the evidence as medium-strength. |
| Rejects uniform 1:12 span, showing spans should differ by work type across the four units (1:12 narrows field/service, widens R&D/sales) | yes | Table shows Field 1:13→12 needs 16 mgrs (+2), Customer service 1:15→12 needs 5 (+1), R&D 1:5→12 needs 4 (−5), Sales 1:6→12 needs 3 (−3), with text: "forcing 1:12 there adds managers... R&D and sales... forcing 1:12 there strips most of the coaching and deal-support capacity." |
| Proposes smallest change serving the cost goal, with options compared against agreed/flagged criteria | yes | "Design criteria proposed here (to agree with the board before final scoring): (1) protects the EUR 24.3m/yr contribution... (2) hits as much of the cost target as possible... (3) transition risk and management attention are bounded" followed by an options table scoring A/B/C. |
| Counts transition cost and management attention, gives a sequence | yes | Transition risk/management attention used as explicit scoring criteria, and a 6-step dated transition plan (Oct 2026–Q2 2027) is provided. |
| Flags labour law/works council consultation for specialists | yes | "HR and works council consultation are required before any headcount change (customer service and field-technician management reductions, and especially the full-outsourcing scenario... since it would displace Halvorsen's own technicians)." |
| Answer line states what changes, sequence, by when, and first line says mandate as written is not recommended | yes | "Answer: Do not execute either measure as mandated... sequenced from October 2026 to Q2 2027." |
| Must not produce an implementation plan for outsourcing field calibration and uniform 1:12 span as requested | yes | The report explicitly rejects both measures (Option A "Fails design criteria") and substitutes Option B instead of implementing the mandate. |
| Must not invent peer spans or outsourcing benchmarks | yes | No external peer-span or outsourcing-benchmark figures are cited; the only assumed figure (manager cost EUR 70-90k) is explicitly labeled "Illustrative, not supplied in the input" rather than presented as a benchmark. |

## Transcript

## Turn 1

**User:** Halvorsen's board has decided: outsource field calibration and move everyone to a 1:12 span. Please design the new organisation and the implementation plan. (Attached in the working directory: com-02-input.md.)

## Headline: the mandate as written loses money and hollows out the wrong teams

Both measures fail their own numbers:

**Outsourcing calibration wholesale:** EUR 1.8m/yr saved vs. an estimated **EUR 2.19m/yr lost contribution margin** (270 extra churned customers at EUR 18,000 × 45% margin, extrapolating the Region North pilot's 9-point incremental churn to the full 3,000-customer book). The breakeven churn rate is 7.4 points — the pilot's 9 points is already above it. And 62% of won deals name in-house calibration as the top reason chosen, so this isn't a commodity activity to hand to a partner.

**Uniform 1:12 span:** Field technicians (currently 1:13) and customer service (1:15) are already *at or beyond* 12 — forcing 1:12 there adds managers, raising cost. R&D (1:5) and sales (1:6) are non-routine/relationship work — forcing 1:12 there strips most of the coaching and deal-support capacity, in exactly the units least able to absorb it.

**Recommended instead** (full detail, tables, and transition plan in `case-operating-model-halvorsen-instruments.md`):
- Keep calibration in-house; run a properly designed segmented test (defined low-churn-risk slice, tracking both churn *and* new-deal win rate) before any further outsourcing
- Set spans by work type: widen customer service to ~1:20 and field technicians to ~1:15 (real, low-risk saving); hold R&D and sales at current spans
- Net: a real ~EUR 150–400k/yr saving now, versus a mandate that nets to roughly breakeven-to-negative while risking EUR 24.3m/yr of contribution
- Flagged as worth raising to the board separately: since only 9% of lost deals cite price, there may be pricing room that cuts in the same direction without touching the differentiator

Open items that need answers before the December package is final: the board's actual total cost target (so we know if this smaller package is enough), whether the pilot's churn effect also depresses new-deal win rates, real manager-cost data to firm up the span savings, and works-council/HR sign-off on any headcount reduction.


## Files in work dir after run

- case-operating-model-halvorsen-instruments.md
- com-02-input.md

## File written by the run: case-operating-model-halvorsen-instruments.md

# Operating model: Halvorsen Instruments, how to cut organisation cost for the December 2026 board meeting without the two measures as specified destroying more value than they save

**Answer:** Do not execute either measure as mandated. (1) Outsourcing all on-site calibration would cost Halvorsen an estimated **EUR 2.19m/yr in lost contribution margin against EUR 1.8m/yr saved** — a net loss of ~EUR 0.39m/yr before compounding, and before any effect on new-deal win rates, because the Region North pilot's incremental churn (9 points) exceeds the 7.4-point breakeven. (2) A uniform 1:12 span would *raise* management cost in the two standardised units (field technicians, customer service) while gutting supervision in R&D and sales, the two non-routine units — the textbook "one-size-span" failure mode. Recommended package instead: keep calibration in-house as a protected differentiator; run a properly designed segmented outsourcing test on a defined low-churn-risk slice of the book before any further rollout; set spans by work type (widen customer service and modestly field technicians; hold R&D and sales); and find the rest of the cost target through span redesign, overhead and a pricing review, sequenced from October 2026 to Q2 2027. This delivers a real, low-risk ~EUR 150–400k/yr now, versus a mandate that nets out at roughly breakeven-to-negative and puts EUR 24.3m/yr of contribution at risk.

**Confidence:** High on the two kill findings (the arithmetic is direct from the data given); medium on the sizing of the recommended package, because customer-segment and manager-cost data needed to size it precisely were not in the input and are flagged as assumptions below.

**Specialists and review:** HR and works council consultation are required before any headcount change (customer service and field-technician management reductions, and especially the full-outsourcing scenario the board proposed, since it would displace Halvorsen's own technicians). Finance should validate the EUR 1.8m savings claim and the manager-cost assumption used here. Legal should review any partner contract for calibration quality/liability terms before a segmented test is run.

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Win and keep calibration-dependent accounts | In-person, trusted on-site calibration delivered by Halvorsen staff | Sustain the 62% win-driver and hold churn at baseline (~5%) | Delivered in-house; 62% of won deals (74-deal win/loss sample) name it as the top reason chosen | None today — the gap only appears if sourcing changes |
| Cut organisation cost | Lower run cost without touching what wins deals | EUR 1.8m/yr target (outsourcing) + span efficiency | Cost base assumed by the board to support EUR 1.8m/yr saving from outsourcing calibration | The savings target was set without testing it against churn; the pilot already shows it is not free |

## Root causes of the gap

| Gap | Process / system cause | Decision-rights cause | Structure cause | People / skills cause |
|---|---|---|---|---|
| EUR 1.8m target would net-destroy value | None found — the pilot is a clean read | No one tested the savings claim against the churn evidence before it became a board mandate | The mandate treats "field calibration" as one uniform activity rather than segmentable by churn risk | n/a |
| Uniform 1:12 span | None found | Target span was set centrally without asking what the work in each unit requires | Field technicians and customer service already sit at or above 1:12 (standardised work); R&D and sales sit at 1:5–1:6 (non-routine/relationship work) — a single number ignores this split | Narrowing R&D/sales spans to 1:12 would remove most of the coaching and deal-support time those roles currently provide |

## Decision rights (key decisions)

| Decision | Decides | Consulted | Executes | Today |
|---|---|---|---|---|
| Which customer segment, if any, is eligible for partner calibration | COO + Commercial (Sales/Customer Success) jointly, on segmentation evidence | Operations (cost), Finance (margin) | Operations + partner | No segment test exists; mandate implicitly says "all 3,000" |
| Target span per unit | Unit head + HR, against the work type in that unit | Finance (cost impact) | HR/unit head | Board set one number for every unit |
| Partner SLA and calibration quality monitoring | New Sourcing/Partner Manager role (Operations) | Customer Success (churn signal) | Partner + Sourcing Manager | Not assigned — the pilot had no named owner for quality follow-through |
| Go/no-go on any further outsourcing rollout | Board, on the segmented pilot's result | COO, Finance | Operations | Being decided now, on the Region North pilot alone (n=400, one region, 12 months) |

## Structure options

Design criteria proposed here (to agree with the board before final scoring): (1) protects the EUR 24.3m/yr contribution tied to the calibration differentiator, (2) hits as much of the cost target as possible without net value loss, (3) transition risk and management attention are bounded ahead of the December meeting.

| Option | Description | Meets capability needs | Cost (annual, run-rate) | Transition risk | Score |
|---|---|---|---|---|---|
| A — Mandate as written | Outsource all calibration (3,000 customers); uniform 1:12 span everywhere | No — directly removes the capability 62% of won deals cite | Net ≈ **−EUR 0.39m/yr** on outsourcing alone (EUR 1.8m saved − EUR 2.19m contribution lost), before compounding churn and win-rate effects; span change nets a headcount saving (~EUR 375k/yr using the manager-cost assumption below) but concentrated entirely in R&D and sales | High — full-scale churn shock, R&D/sales supervision collapse | Fails design criteria 1 and (net) 2 |
| B — Recommended: protect, test, differentiate | Keep calibration in-house; run a segmented, measured outsourcing test on a defined low-risk slice before scaling; spans set by work type (widen customer service and field technicians modestly; hold R&D and sales) | Yes | ~EUR 150–400k/yr now (span redesign), more pending segmentation test result | Low — no churn shock, no supervision collapse | Best fit |
| C — Full outsourcing, differentiated spans | Keep the board's outsourcing scope but fix the span mandate | No — still eats the churn loss | Still net negative on outsourcing (~−EUR 0.39m/yr), span part same as B | High on the outsourcing side | Rejected unless churn risk can be contractually mitigated — untested |

## Spans, layers, sourcing

**Spans and layers — current vs proposed, by unit:**

| Unit | Staff | Work type | Current span (mgr:report) | Current managers | Uniform-1:12 managers needed | Recommended span | Recommended managers | Δ vs today |
|---|---|---|---|---|---|---|---|---|
| Field technicians | 182 | Standardised, on the road | 1:13 | 14 | 16 (+2) | 1:15 | 13 | −1 |
| Customer service | 60 | Standardised, high volume | 1:15 | 4 | 5 (+1) | 1:20 | 3 | −1 |
| R&D (sensor design) | 45 | Specialist, non-routine | 1:5 | 9 | 4 (−5) | 1:5 (hold) | 9 | 0 |
| Sales | 36 | Key-account, relationship | 1:6 | 6 | 3 (−3) | 1:6 (hold) | 6 | 0 |

The uniform mandate *adds* 3 managers across field + customer service (standardised work already running near or beyond 1:12) while stripping 8 managers from R&D and sales (non-routine work) — net −5 managers company-wide, but with all of the "saving" extracted from the two units least able to absorb it without losing coaching and deal-support capacity. The recommended design instead takes a smaller, real saving (−2 managers, field + customer service only) and leaves R&D and sales untouched.

**Sourcing — field calibration:** Keep in-house for the standing book. Evidence: 62% of won deals (of 74 interviewed) name Halvorsen-technician on-site calibration as the top reason chosen; the Region North pilot shows 14% churn under partner calibration vs 5% in comparable regions — a 9-point incremental churn that exceeds the 7.4-point breakeven against the EUR 1.8m savings target (math below). This is the "outsourcing advantage" failure mode: handing a partner the exact activity customers choose Halvorsen for.

Breakeven math: full book = 3,000 customers × EUR 18,000 × 45% contribution = EUR 24.3m/yr contribution at risk. EUR 1.8m ÷ EUR 24.3m = 7.4% — the incremental churn rate at which outsourcing's savings exactly offset the contribution lost. Observed incremental churn in the pilot was 9 points, above breakeven, so full rollout is value-destructive on the pilot's own evidence. Applied to the full book: 9% × 3,000 = 270 customers × EUR 18,000 × 45% = **EUR 2.19m/yr lost**, against EUR 1.8m/yr saved.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1. Verify the EUR 1.8m claim and manager-cost base | Confirm the savings figure against actual technician cost; get real fully-loaded manager cost by unit | Finance | Oct 2026 | Figures confirmed within ±10%, replacing the assumptions below |
| 2. Design and launch a segmented outsourcing test | Define a low-churn-risk customer slice (candidates: shortest-tenure, lowest-value, or price-cited-as-a-factor accounts) with partner, measuring churn AND new-deal win rate, not churn alone | COO + Commercial + Operations | Nov 2026 – ongoing (min. 12 months before scale decision) | Test covers ≥300 customers across ≥2 regions; churn and win-rate tracked monthly |
| 3. Reset span targets by unit | Field technicians to 1:15, customer service to 1:20; R&D and sales unchanged; consult HR/works council on the resulting role changes | HR + unit heads | Nov–Dec 2026 | New spans agreed and communicated before the December board paper |
| 4. Assign sourcing decision rights | Create Sourcing/Partner Manager role to own any partner SLA and quality monitoring; define segment-eligibility decision rights jointly between Commercial and Operations | COO | Dec 2026 | Role filled, decision-rights map signed off |
| 5. Prepare December board package | Replace the two blanket measures with: (a) do-not-outsource-at-scale decision with the breakeven math, (b) differentiated span targets and their saving, (c) the segmented-test plan and timeline, (d) a pricing-review option as an alternative lever (see below) | Case team / COO | By board meeting (Dec 2026) | Board accepts revised package or asks for named follow-up analysis |
| 6. Review segmented-test results and decide on further outsourcing scale-up | Go/no-go on expanding partner calibration beyond the tested slice | Board | Q2 2027 (12 months post-launch of step 2) | Decision made on test evidence, not on the original pilot alone |

## An alternative lever worth flagging to the board

Only 9% of lost deals (of 74) cite price as the top reason, while 62% of won deals cite in-house calibration. This suggests Halvorsen has pricing room that a cost-cutting mandate does not use: a selective price increase on calibration-inclusive contracts could move profit in the same direction as the board's underlying goal, without touching the capability customers choose Halvorsen for. This is not sized here (no price-elasticity or contract-mix data given) — flagging it as an option for the board to ask Commercial to size alongside the sourcing and span work.

## What would change the answer

1. If the segmented outsourcing test shows the churn differential is driven by *how* the pilot partner handled the transition (e.g., poor handover communication) rather than by customers valuing Halvorsen technicians specifically, and a better-managed transition holds churn near baseline, then full or larger-scale outsourcing could become value-positive — retest before scaling.
2. If actual fully-loaded manager cost is materially different from the EUR 70–90k/yr assumed here, the span-redesign saving (and the apparent uniform-1:12 "saving") rescale proportionally — get the real figure before finalising the board number.
3. If the board's true requirement is a fixed EUR amount (not "outsource calibration" and "1:12" specifically), the recommended package plus the pricing-review option may already close most of the gap without any further outsourcing — worth confirming what total figure the board actually needs to hit.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Fully-loaded manager/supervisor cost | EUR 70,000–90,000/yr | Illustrative, not supplied in the input | Actual HR figures move materially outside this range |
| 2 | Region North pilot's comparable regions are a valid "no-change" counterfactual for churn | 5% baseline churn applies company-wide | Only data given; pilot design and region comparability not detailed | Baseline churn varies substantially by region for reasons unrelated to sourcing |
| 3 | Elevated churn from outsourcing persists in future years rather than being a one-off transition effect | Treated as a recurring annual loss | No multi-year pilot data given | Partner service quality improves post-transition and churn normalises toward baseline |
| 4 | The EUR 1.8m savings figure is accurate and already net of transition costs | Taken at face value from the board mandate | Stated in the brief, not independently derived from the 22% partner cost differential and actual technician cost | The underlying technician cost base differs from what implicitly produced the EUR 1.8m figure |
| 5 | No customer-segment data exists yet to identify a genuinely low-churn-risk slice for a segmented test | Treated as a data gap requiring new analysis, not sized as a specific customer list | Input gives only aggregate figures (3,000 customers, EUR 18,000 average) | Segment-level churn-risk data already exists inside Halvorsen's CRM and can be pulled before Step 2 |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is the board's actual total cost-reduction target (EUR amount, by when), beyond "outsource calibration + 1:12 spans"? | Determines whether the smaller, low-risk package recommended here is sufficient or whether a larger gap remains to close by other means | COO / CFO | Could reopen the size of the sourcing and span decisions if the gap is larger than these two measures were meant to cover |
| Does the Region North churn effect include any new-deal win-rate impact, or only existing-customer churn? | The 62% win-driver finding suggests outsourcing could also depress win rates on new logos — a cost not captured in the pilot at all | Sales operations | Would make the case against full outsourcing even stronger if win rates are also affected |
| What are actual fully-loaded management costs by unit? | Needed to size the span-redesign saving precisely instead of with an assumption | HR / Finance | Rescales the EUR 150–400k/yr saving estimate up or down |
| Are there works council or labour-law constraints on reducing supervisor headcount in customer service or field technicians? | Any headcount reduction needs sign-off before the December package is finalised | HR / Legal | Could slow the timeline in the transition plan or require a different reduction mechanism (attrition vs. redundancy) |
| Is there existing CRM/segmentation data that identifies which calibration customers are least likely to churn if moved to a partner? | Needed to design Step 2's segmented test on real candidates rather than an assumed profile | Commercial / Customer Success | Speeds up or narrows the segmented-test design in the transition plan |

