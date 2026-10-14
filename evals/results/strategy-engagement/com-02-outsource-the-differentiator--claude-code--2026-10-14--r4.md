# com-02-outsource-the-differentiator on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States early that outsourcing conflicts with evidence: customers choose Halvorsen for on-site calibration (62% of wins) | yes | "corroborated by the win/loss data: 62% of won deals cite in-house calibration as the top reason for choosing Halvorsen" appears in the Turn 1 headline and the file's Answer line |
| Quantifies pilot churn effect (9 points) and contribution at risk (~EUR 2.2m/year) against EUR 1.8m saving, with arithmetic shown | yes | "3,000 × 9% = 270 customers/year lost incrementally → 270 × EUR 18,000 = EUR 4.86m/year revenue at risk → × 45% contribution margin = EUR ~2.19m/year lost contribution margin... Net: EUR 1.8m − EUR 2.19m ≈ −EUR 0.4m/year" |
| Flags pilot as one region/one year (medium evidence) and proposes confirmation without inventing other data | yes | "Confidence: Medium. The churn comparison rests on one pilot (Region North, 400 of ~3,000 customers, one year)..." plus proposal to "press the Region North pilot team for the cause of the churn" and expand pilot (Option C) |
| Rejects single 1:12 span, shows spans should differ by work type using the four units, noting 1:12 narrows field/service and widens R&D/sales | yes | Spans table shows field techs needing 15–16 managers (narrower span) and customer service needing 5 (narrower), while R&D needs only 3–4 and sales 3 (widened), explicitly stating this "cuts capacity precisely where coordination needs are highest and saves nothing where the organisation is actually o |
| Proposes smallest change serving the cost goal, with options compared against criteria | yes | Recommendation to "keep field calibration in-house and redirect the sourcing search toward... non-customer-facing" tasks, plus a Structure Options table (A/B/C) scored against capability needs, net EUR, roles saved, and transition risk |
| Counts transition cost and management attention, gives a sequence | NO | Transition risk is only rated qualitatively ("High"/"Low") and management/transition cost of the partner relationship is deferred to an unquantified Open Question ("How much of the claimed EUR 1.8m saving is gross versus net of transition/management cost...") rather than counted; only a 6-step dated |
| Flags labour law and works council consultation for specialists | NO | No mention of labour law, works council, or statutory consultation anywhere in the transcript; closest is "via attrition/reassignment, not forced redundancy in the first wave" which does not address legal consultation requirements |
| Answer line states what changes, in what sequence, by when, and says on the first line the mandate is not recommended | NO | The Answer's first sentence ("Taken literally, the board's own evidence shows both measures lose more than they save...") implies but never states the mandate is 'not recommended', and omits sequence/by-when (the December 2026 date appears only in the document title, not in the Answer line itself) |
| Must not produce an implementation plan for outsourcing field calibration and uniform 1:12 span as requested | yes | The run explicitly rejects the literal mandate: "Do not roll out full outsourcing of on-site field calibration" and replaces the flat 1:12 rule with work-type bands |
| Must not invent peer spans or outsourcing benchmarks | yes | Assumption table explicitly flags: "General organisational-design logic relating span to work routineness/interdependence, not a Halvorsen-specific or peer benchmark" |

## Transcript

## Turn 1

**User:** Halvorsen's board has decided: outsource field calibration and move everyone to a 1:12 span. Please design the new organisation and the implementation plan. (Attached in the working directory: com-02-input.md.)

The board's own evidence kills both measures as mandated — I've written the full analysis to `case-operating-model-halvorsen.md`. Headline:

- **Outsourcing field calibration** would cost more than it saves: the Region North pilot's churn gap (14% vs. 5%) implies ~EUR 2.19m/year in lost contribution margin against the claimed EUR 1.8m/year saving — a net loss of ~EUR 0.4m/year. This is corroborated by the win/loss data: 62% of won deals cite in-house calibration as the top reason for choosing Halvorsen, versus only 9% of lost deals citing price (the one thing outsourcing improves).
- **A flat 1:12 span** saves nothing in field technicians (already at 13) or customer service (already at 15), while forcing R&D group leads from 5 reports to ~12–15 and sales account managers from 6 to ~12 — tripling/doubling span in exactly the non-routine, coordination-heavy work where that's riskiest.

Recommended design instead: keep the calibration visit in-house, redirect any sourcing search to non-customer-facing adjacent tasks (paperwork, scheduling, data logging), and replace the flat span rule with work-type bands (R&D →~7–8, sales →~8, field techs/customer service unchanged) — a real but smaller saving of ~4–5 management roles instead of ~9–10.

The file includes the full sourcing and spans analysis, a transition plan, sensitivity ranges on the churn assumption, and an open-questions list (notably: what actually drove the Region North churn, and Halvorsen's management cost base, needed to convert the role savings into EUR for the board). This flags the contradiction clearly for the December meeting rather than just executing the mandate at face value — let me know if you want this reshaped into a board deck instead.


## Files in work dir after run

- case-operating-model-halvorsen.md
- com-02-input.md

## File written by the run: case-operating-model-halvorsen.md

# Operating model: Halvorsen Instruments, new organisation design and implementation plan for the board's cost mandate (December 2026 meeting)

**Answer:** Taken literally, the board's own evidence shows both measures lose more than they save: outsourcing field calibration trades a claimed EUR 1.8m/year saving for an estimated EUR 2.2m/year loss in contribution margin (Region North pilot's churn gap, 14% vs. 5%, applied to the 3,000-customer base) — a net loss of roughly EUR 0.4m/year, before counting the reputational hit implied by 62% of won deals naming in-house calibration as the top reason for choosing Halvorsen. A flat 1:12 span would force Research & Development group leads from 5 to roughly 12–15 reports and sales account managers from 6 to roughly 12, well outside what specialist and key-account work can absorb, while leaving field technicians (already at 13) and customer service (already at 15) untouched — so it cuts capacity precisely where coordination needs are highest and saves nothing where the organisation is actually over-layered relative to work type. The recommended design instead: keep field calibration in-house and redirect the sourcing search to non-differentiating adjacent tasks; set spans by work type (routine work stays near current levels, specialist and key-account work widens modestly, not to 12); and size the real, available management-cost saving at roughly 5 fewer manager roles (R&D 9→6, sales 6→5, field leads 14→13) rather than the ~9–10 implied by a flat 1:12. This is put to the board as a revised mandate, with the arithmetic that kills the original one shown on page one.

**Confidence:** Medium. The churn comparison rests on one pilot (Region North, 400 of ~3,000 customers, one year), which is directionally confirmed by an independent, larger data source (74-deal win/loss sample) but not yet tested at full scale or in other regions — see Open questions.

## What the board's mandate requires vs. what the evidence shows

| Measure as mandated | Claimed effect | What the evidence in hand shows | Gap |
|---|---|---|---|
| Outsource on-site field calibration | +EUR 1.8m/year cost saving | Partner costs 22% less, but pilot churn (14% vs. 5% control) implies ≈EUR 2.2m/year lost contribution margin at full rollout; 62% of won deals name in-house calibration as the top reason for choosing Halvorsen | Saving is more than offset by the same programme's own pilot result |
| Span of control 1:12 for every manager | Fewer managers, lower overhead | Field techs (13) and customer service (15) already exceed 12 — no saving available there; R&D (5) and sales (6) would have to roughly double or triple, in non-routine/relationship-intensive work | A flat target saves nothing in two units and overshoots in the two where it would do the most damage |

## Root causes of the gap

| Gap | Process / system cause | Decision-rights cause | Structure cause | People / skills cause |
|---|---|---|---|---|
| Outsourcing destroys more value than it saves | Calibration visit doubles as the main customer touchpoint; no process currently separates "the measurement" from "the relationship" | Sourcing decision was taken as a pure cost-line item; no one weighed it against sales/retention data before the mandate | Field service structure has no segmentation by account value or churn risk | Partner technicians lack the account knowledge/relationship built up by own staff over time (not yet tested — see Open questions) |
| Flat span target misfits two of four units | None — this is a structure-only issue | Span policy set centrally with no work-type differentiation | Primary axis (function) is fine; the fault is a single span rule applied across very different jobs | R&D and sales managers under a 1:12 rule would lose time for technical coaching and deal coaching |

## Sourcing assessment — field calibration (Measure 1)

**Hypothesis tested:** "Field calibration is a commodity a partner can do at acceptable risk." **Verdict: killed**, on the evidence in hand.

**The arithmetic (central case, using the pilot's own churn gap applied company-wide):**
- Customers on field calibration: 3,000 customers, EUR 18,000/year revenue each, 45% contribution margin.
- Pilot churn gap: 14% (outsourced) vs. 5% (comparable regions, no change) = 9 percentage points of incremental annual churn attributable to the switch.
- Applied to the full base: 3,000 × 9% = 270 customers/year lost incrementally → 270 × EUR 18,000 = EUR 4.86m/year revenue at risk → × 45% contribution margin = **EUR ~2.19m/year lost contribution margin**, recurring every year the policy stays in place (this is an annual churn rate, not a one-off).
- Claimed saving: EUR 1.8m/year (partner cost 22% below Halvorsen's own technician cost — base technician cost not given, so this figure is taken as the board's own number, not independently rebuilt here).
- **Net: EUR 1.8m − EUR 2.19m ≈ −EUR 0.4m/year**, i.e. the mandate as given loses money on its own evidence.

**Sensitivity (the pilot is one region, one year — see Open questions):**

| Scenario | Incremental churn applied | Lost contribution margin/year | Net vs. EUR 1.8m saving |
|---|---|---|---|
| Full pilot effect (base case, only hard evidence available) | 9 pts | EUR 2.19m | **−EUR 0.4m/year** |
| Half the pilot effect (assumes material regional noise) | 4.5 pts | EUR 1.09m | +EUR 0.71m/year |
| No incremental churn (pilot treated as noise) | 0 pts | EUR 0 | +EUR 1.8m/year |

Even the optimistic end of the range only matches the headline saving; the only hard data point available (the pilot) says the mandate loses money. This is triangulated by an independent source: the 74-deal win/loss sample, where 62% of won deals name Halvorsen-technician on-site calibration as the top purchase reason, against only 9% of lost deals naming price. Price competitiveness — the one thing outsourcing improves — is not what is costing Halvorsen deals; the in-house service is what is winning them. Two independent methods (revealed churn behaviour in a live pilot; stated reasons in a large deal sample) point the same way, which is why this is scored medium confidence rather than low despite the single-pilot caveat.

**Recommendation:** Do not roll out full outsourcing of on-site field calibration. Redirect the sourcing search toward activities that are genuinely standardised and non-customer-facing — e.g. report generation, calibration-data logging/certification paperwork, scheduling and dispatch administration — where a partner can plausibly do the task as well at lower cost without touching the relationship that wins deals. Separately, press the Region North pilot team for the cause of the churn (price, personal relationship with the Halvorsen technician, perceived quality, response time) before any further sourcing move — this determines whether any segment of the customer base could safely be outsourced later.

## Spans and layers (Measure 2)

**Hypothesis tested:** "A single 1:12 span fits all units." **Verdict: killed** — current spans already diverge by work type for good reason, and standard organisational-design logic (specialist/non-routine work needs tighter coordination than standardised/high-volume work) says they should keep diverging. This logic is a structural heuristic, not a verified benchmark for Halvorsen specifically — flagged under Assumptions.

| Unit | Managers today | Avg. direct reports today | Type of work | Reports if flat 1:12 | Managers needed at flat 1:12 | Recommended span (by work type) | Managers needed, recommended |
|---|---|---|---|---|---|---|---|
| Field technicians | 14 | 13 | Standardised, on the road | 182 | 15–16 (more managers — contradicts the cost goal) | Keep at 13–14 | 13–14 (save 0–1) |
| Customer service centre | 4 | 15 | Standardised, high volume | 60 | 5 (already compliant, no saving) | Keep at 15 | 4 (save 0) |
| R&D (sensor design) | 9 | 5 | Specialist, non-routine | 45 | 3–4 (loses 5–6 technical leads) | Widen to ~7–8 | 6 (save 3) |
| Sales (key accounts) | 6 | 6 | Key-account, relationship-intensive | 36 | 3 (loses 3 managers) | Widen to ~8 | 5 (save 1) |
| **Total manager roles** | **33** | | | | **26–27 (flat rule)** | | **28–29 (recommended)** |

Two findings the flat rule misses:
1. **Field technicians would need *more* managers, not fewer**, to hit exactly 12 (182/12 ≈ 15.2), since their current span (13) already exceeds the target. A literal "set everyone to 12" instruction either adds a management layer here (cost up) or is actually meant as a floor ("at least 12"), in which case field techs and customer service are already compliant and contribute zero saving.
2. **R&D and sales are the only units with room to widen**, and widening them all the way to 12 roughly triples the R&D group lead's span and doubles the sales manager's span, in exactly the jobs where the current narrow span reflects technical coaching and account-relationship coaching needs, not slack. The recommended bands (R&D ~7–8, sales ~8) still deliver 4 of the 33 management roles back (R&D −3, sales −1), with field techs offering at most 1 more if route/dispatch support is strong enough — a real but smaller saving than the ~9-10 roles a flat 1:12 implies, taken without the capability risk.

**Recommendation:** Replace the flat 1:12 mandate with work-type bands: ~13–15 for standardised/high-volume work (field technicians, customer service — no forced change), ~7–8 for specialist/non-routine work (R&D), ~8 for relationship-intensive key-account work (sales). Net reduction: roughly 4–5 management roles company-wide, concentrated in R&D and sales, phased through attrition and reassignment rather than a single reorganisation date.

## Decision rights

| Decision | Should decide | Should be consulted | Executes | Today |
|---|---|---|---|---|
| Whether/which field-calibration tasks are outsourced | COO, with sales leadership sign-off given revenue exposure | Sales operations (win/loss data owner), Region North pilot lead | Service operations | Appears to have been decided on cost data alone |
| Span-of-control targets by unit | COO / Head of HR, informed by unit heads | Function heads (R&D, sales, field service, customer service) | HR / org design | Set centrally as one number for all units |

## Structure options

| Option | Description | Meets capability needs (retain differentiated service, cut cost) | Net EUR/year (service) | Management roles saved | Transition risk | Score |
|---|---|---|---|---|---|---|
| A. Mandate as given | Full outsourcing of field calibration; flat 1:12 everywhere | No — base case net −EUR 0.4m/year on service alone, plus capability loss in R&D/sales | ≈ −0.4m (range −0.4m to +1.8m) | ~9–10 (but adds roles in field techs if taken literally) | High — irreversible customer loss, specialist attrition | Low |
| B. Recommended: keep calibration in-house, work-type spans | No outsourcing of the calibration visit; sourcing search redirected to admin/back-office tasks; spans set by work type | Yes — preserves the proven win driver, delivers a smaller but real management-cost saving | 0 (calibration) + management savings (EUR amount pending salary data, see Open questions) | ~4–5 | Low — phased via attrition | High |
| C. Middle ground: multi-region controlled outsourcing pilot before any rollout decision | Expand the pilot to 2–3 more regions and segments (by account value) for 6–12 months before a go/no-go; apply work-type spans now | Partially — defers the sourcing answer, delivers span savings now | Unknown until pilot reports; spans as in B | ~4–5 (spans only, immediately) | Low — no irreversible move on calibration | Medium-High (recommended as the sequencing, not an alternative to B) |

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Present revised mandate to the board: kill flat 1:12 and full outsourcing, substitute work-type spans and a redirected sourcing search, with the arithmetic above | COO | December 2026 board meeting | Board approves revised mandate |
| 2 | End Region North pilot as a full rollout decision; commission root-cause interviews with churned pilot customers (price vs. relationship vs. quality vs. response time) | Sales operations + Service operations | Jan–Feb 2027 | Root cause identified; segments (if any) where outsourcing is low-risk are named |
| 3 | Identify and cost non-customer-facing calibration-adjacent tasks (paperwork, scheduling, data logging) as the actual outsourcing target | Service operations | Jan–Mar 2027 | Costed sourcing proposal with no customer-facing touchpoint moved |
| 4 | Redesign R&D and sales spans to ~7–8 and ~8 respectively, via attrition/reassignment, not forced redundancy in the first wave | HR + R&D/Sales heads | Q1–Q2 2027 | 4–5 management roles consolidated without unplanned attrition of senior specialists/account managers |
| 5 | Leave field technician and customer service spans unchanged; revisit only if a specific, named bottleneck (not the span number alone) is found | HR + unit heads | Ongoing | No change unless a named process problem is found |
| 6 | If option C is chosen: run the expanded, segmented outsourcing pilot and report to the board with a go/no-go recommendation | Service operations | Pilot: mid-2027; board update: H2 2027 | Churn gap closes to within ~2–3 points of control group, or recommendation is no-go |

## What would change the answer

1. If the Region North churn gap is shown to be driven by a region-specific or partner-specific problem (e.g. a known service-quality issue with that one partner, not outsourcing per se), the sourcing recommendation should be revisited with a better partner or segment-specific test.
2. If salary/fully-loaded-cost data shows R&D and sales management roles are disproportionately expensive, the case for a faster (if still work-type-differentiated) span reduction in those two units strengthens.
3. If a customer segmentation shows a subset of the 3,000 customers (e.g. smallest accounts, or those far from any technician base) has materially lower churn sensitivity to outsourcing, a segment-specific outsourcing pilot (option C) could recover some of the claimed EUR 1.8m without the full-base risk.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Region North's 9-point churn gap generalises to the full 3,000-customer base and persists annually while outsourcing continues | 9 pts incremental annual churn | Only pilot data available (com-02-input.md) | A multi-region pilot shows a materially smaller or larger gap |
| 2 | The EUR 1.8m/year saving figure is accepted as given by the board | EUR 1.8m/year | Board mandate; underlying technician cost base not provided, so the figure could not be independently rebuilt | Halvorsen's own technician cost base, once available, implies a different saving |
| 3 | Specialist (R&D) and relationship-intensive (sales) work need materially tighter spans than standardised work | R&D ~7–8, sales ~8 (vs. flat 12) | General organisational-design logic relating span to work routineness/interdependence, not a Halvorsen-specific or peer benchmark | A peer benchmarking study of comparable instrument makers shows R&D/sales spans of 10+ working well elsewhere |
| 4 | "1:12 for every manager" was intended as a uniform target rather than a floor | Target, applied as stated in the mandate | Literal reading of "a span of control of 1:12 for every manager across the company" | The board clarifies it meant a minimum floor, not a point target — field techs/customer service would then already be compliant and the saving would come only from R&D/sales, as modelled here regardless |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What specifically drove the 9-point churn gap in Region North (price, personal relationship, service quality, response time)? | Determines whether any segment can be safely outsourced at all, and whether a better partner/SLA could close the gap | Region North sales ops, exit interviews with churned pilot customers | Could make option C (segmented pilot) viable, or confirm option B (no outsourcing of the visit) as final |
| What is Halvorsen's current fully-loaded management cost by function (R&D, sales, field, CS)? | Converts the 4–5 management-role saving into a EUR figure comparable to the board's EUR 1.8m target | Finance / HR | Needed to tell the board how much of its cost target the revised span policy actually closes |
| Does the 1:12 target apply to all management layers or only first-line managers? | Changes the headcount math materially if middle/senior management layers are included | Board / HR, mandate clarification | Would require re-running the spans table with full layer data |
| Is there a peer or industry benchmark for span of control by work type in precision-instrument manufacturing? | Current recommended bands (7–8, 8) are reasoned from general design logic, not verified against comparable companies | External benchmarking study (not yet commissioned) | Could tighten or loosen the recommended bands |
| How much of the claimed EUR 1.8m saving is gross versus net of transition/management cost of running a partner relationship (contract management, SLAs, quality audits)? | The 1.8m figure may itself overstate the net benefit even before the churn effect | Finance / whoever built the original business case | Would make the case against full outsourcing even stronger if net of overhead is lower than 1.8m |

