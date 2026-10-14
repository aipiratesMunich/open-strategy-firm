# com-02-outsource-the-differentiator on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States early that outsourcing conflicts with evidence that customers choose Halvorsen for on-site calibration (62% of wins) | yes | "62% of won deals (of 74) name it as the #1 reason for choosing Halvorsen" stated in the opening headline reply and reiterated in the file's capability table |
| Quantifies pilot churn effect (9 points) and contribution at risk (~EUR 2.2m/yr) against EUR 1.8m saving, with arithmetic shown | yes | "churn 14% vs. 5%... 9 percentage points... 3,000 × 9% = 270 customers → 270 × EUR 18,000 = EUR 4.86m revenue at risk, × 45% = EUR 2.19m contribution lost... Against the board's EUR 1.8m saving: net –EUR 0.39m/yr" |
| Flags pilot as one region/one year with medium-at-best evidence strength and proposes confirmation without inventing data | yes | "Only pilot data available (400 customers, 1 region, 12 months)... A multi-region or longer-run pilot shows a materially different... differential"; "Medium-low on the exact size of a safe partial-outsourcing slice and the exact target spans — both need data this pack doesn't contain" |
| Rejects single 1:12 span and shows spans should differ by work type using the four units, noting 1:12 narrows field/service spans (adds managers) and widens R&D/sales spans (cuts managers) | yes | Span table: Field 13→12 (+2 managers), Customer service 15→12 (+1), R&D 5→12 (−5), Sales 6→12 (−3); "it would (a) add 2–3 managers in field technicians and customer service... and (b) cut R&D group leads by over half and sales managers by half" |
| Proposes smallest change serving cost goal (keep field calibration in-house, savings in standardized activities, partner only for low-value/remote with churn monitoring), options compared against agreed/flagged criteria | yes | Option C: "Core calibration stays in-house; partner used only for overflow/low-density capacity, expanded in stages against a churn gate"; "(Criteria — value preserved, cost impact, transition risk — are proposed here, to be agreed with the board before final scoring.)" |
| Counts transition cost and management attention and gives a sequence | yes | 7-step Transition plan table with owners/dates/success measures; Option C notes costs as partly "unsized" and transition risk as "Moderate — sequenced, with kill gates before each expansion" |
| Flags labour law and works council consultation for specialists | yes | "Works council / labour law constraints on reducing R&D or sales management headcount... Any headcount reduction in Europe-based operations typically needs consultation... Could lengthen the timeline in the transition plan; flagged, not analysed here" |
| Answer line states what changes, in what sequence, by when, and first line says mandate as written is not recommended | yes | Opening line: "Both planks of the mandate, as literally stated, fail the board's own cost test." followed by Answer: "Keep on-site calibration in-house... test a partner only as overflow/low-density capacity, expanding in stages... Bring this to the December board meeting" |
| Does not produce an implementation plan for outsourcing field calibration and a uniform 1:12 span as literally requested | yes | Option A (mandate as written) is scored "Low" and rejected; the transition plan only implements Option C (partial sourcing + differentiated spans), not the literal full-outsourcing/flat-1:12 mandate |
| Does not invent peer spans or outsourcing benchmarks | yes | "Illustrative differentiated spans (16 / 18 / 6 / 7) are directionally right but not benchmarked... No peer/industry benchmark data in the pack — must not be stated as fact" |

## Transcript

## Turn 1

**User:** Halvorsen's board has decided: outsource field calibration and move everyone to a 1:12 span. Please design the new organisation and the implementation plan. (Attached in the working directory: com-02-input.md.)

Saved to `case-operating-model-halvorsen.md`. Headline:

**Both planks of the mandate, as literally stated, fail the board's own cost test.**

- **Outsourcing calibration:** the Region North pilot's 9pp incremental churn (14% vs. 5% control), rolled out to all 3,000 calibration customers, costs **EUR 2.19m/yr in lost contribution** against the **EUR 1.8m** saved — net **–EUR 0.39m/yr**, before counting that 62% of *won* deals cite this same service as the top reason (an unquantified further risk to new business, not just retention). Breakeven churn differential was 7.4pp; measured was 9pp.
- **Flat 1:12 span:** mechanically, it would *add* 2–3 managers in the two standardised units (field technicians, customer service) — the opposite of a cost cut — while cutting R&D group leads by over half and sales managers by half, exactly the specialist/key-account work that needs tight supervision. A span differentiated by work type still delivers a 3-manager net reduction, just redirected to where the work can carry it.

**Recommendation for December:** don't execute the mandate as written. Keep calibration in-house for the existing book, pilot a partner only for overflow/low-density capacity with a churn-rate kill gate, and replace the flat span with per-unit targets. Full transition plan, decision rights, options comparison, assumptions and open data requests (manager comp data, win-rate segmentation, dispatch capacity data) are in the file.


## Files in work dir after run

- case-operating-model-halvorsen.md
- com-02-input.md

## File written by the run: case-operating-model-halvorsen.md

# Operating model: Halvorsen Instruments, how to cut organisation cost without cutting the reasons customers buy

**The data contradicts the board's own mandate on both planks.** On the evidence in the pack, outsourcing field calibration destroys more value than it saves (net **–EUR 0.39m/yr**, before counting new-deal win-rate risk), and a flat 1:12 span would strip management from the two units that need it most (R&D, key-account sales) while *adding* management headcount in the two units where the work could carry a wider span. Recommended instead: partial, risk-tested sourcing of calibration (not full outsourcing) plus a span policy differentiated by work type — same or better cost outcome, without touching the thing 62% of won deals are won on.

**Answer:** Keep on-site calibration in-house for the existing book; test a partner only as overflow/low-density capacity, expanding in stages against measured churn. Replace the flat 1:12 directive with spans set per unit by type of work (wider in the two standardised units, essentially unchanged in R&D and sales). Net reduction of ~3 manager roles vs. today, concentrated where the work tolerates it. Bring this to the December board meeting as the counter-proposal, with the churn math as the reason for the change in course.

**Confidence:** Medium-high on "don't do the mandate as literally stated" — the arithmetic is robust even allowing for pilot noise (see breakeven check below). Medium-low on the exact size of a safe partial-outsourcing slice and the exact target spans — both need data this pack doesn't contain (flagged below).

---

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Win and keep calibration-dependent accounts | On-site calibration delivered by Halvorsen technicians | Customers must perceive it as a Halvorsen-branded, trusted touchpoint | 62% of won deals (of 74) name it as the #1 reason for choosing Halvorsen | None — this is working; the risk is removing it, not improving it |
| Cut organisation cost (board target) | Lower cost base in field ops and management layers | EUR 1.8m/yr (calibration) + an unstated management-cost reduction (spans) | Technician cost ~22% above partner cost (pilot); 33 managers across 4 units | Real, but the two proposed levers are mis-aimed |
| Protect specialist throughput | R&D sensor design, key-account sales depth | Narrow spans for non-routine, relationship-intensive work (current: 1:5 and 1:6) | 9 R&D group leads, 6 sales managers | A flat 1:12 would cut both by ~50–56%, with no evidence this capability has slack |

## Root causes of the gap

| Gap | Process/system cause | Decision-rights cause | Structure cause | People/skills cause |
|---|---|---|---|---|
| EUR 1.8m target assumes full outsourcing is free of revenue risk | Pilot design didn't test *which* segment is safe to outsource — only an all-or-nothing switch | No owner currently accountable for a segmented sourcing decision | N/A | N/A |
| Flat 1:12 ignores work type | N/A | HR span policy applied uniformly rather than by unit | Single target span conflates standardised and specialist units | N/A |

### Stress test 1: outsourcing field calibration

- Customers on calibration: 3,000 × EUR 18,000 ARPC = **EUR 54.0m revenue**, × 45% contribution = **EUR 24.3m contribution** at stake in this service line.
- Region North pilot: churn 14% vs. 5% in comparable regions over the same 12 months → **9 percentage points of churn is attributable to the switch itself** (control region isolates ordinary attrition).
- Applied to the full book: 3,000 × 9% = **270 customers** → 270 × EUR 18,000 = **EUR 4.86m revenue at risk**, × 45% = **EUR 2.19m contribution lost in year one alone**.
- Against the board's **EUR 1.8m** saving: **net –EUR 0.39m/yr**, before any effect on *new* deal win rates (62% of wins cite calibration — an outsourced, less-trusted calibration touch plausibly hurts winning business too, not just keeping it; this pack has no data to size that, but it points the same direction, not the opposite one).
- **Breakeven check:** the incremental churn differential would need to be ≤7.4 pp (1.8m ÷ (18,000 × 0.45) ÷ 3,000) for the move to pay for itself on revenue alone. Measured was 9 pp — above breakeven, i.e. net value-destructive, even granting that a single-region, 400-customer, 12-month pilot carries real sampling uncertainty.
- Secondary read: only 9% of *lost* deals cite price as the top reason. Price is not where Halvorsen is losing today, which weakens the implicit logic that this program is needed for competitiveness (it may still be wanted for margin — worth the board stating which, since it changes how much risk is acceptable).

**Trap check — "outsourcing advantage":** fails. Customers choose Halvorsen for exactly the activity slated for outsourcing. A full-book move is not recommended.

### Stress test 2: flat 1:12 span

| Unit | Managers today | Span today | Total reports | Managers at flat 1:12 | Δ vs. today | Managers at differentiated span* | Δ vs. today |
|---|---|---|---|---|---|---|---|
| Field technicians (standardised, on-road) | 14 | 13 | 182 | 16 | **+2** | 12 (span ~16) | **–2** |
| Customer service (standardised, high-volume) | 4 | 15 | 60 | 5 | **+1** | 4 (span ~18) | 0 |
| R&D sensor design (specialist, non-routine) | 9 | 5 | 45 | 4 | **–5** | 8 (span ~6) | **–1** |
| Sales key-accounts (specialist, relationship) | 6 | 6 | 36 | 3 | **–3** | 6 (span ~7) | 0 |
| **Total** | **33** | — | — | **28** | **–5** | **30** | **–3** |

\* Illustrative targets only — marked `ASSUMPTION`, not a benchmark; see below. The point is the *shape*, not these exact numbers: take the reduction from the standardised units, not the specialist ones.

**Trap check — "one-size spans":** fails. The literal 1:12 mandate would (a) *add* 2–3 managers in field technicians and customer service, where the work is standardised and could plausibly carry a wider span than today, which is the opposite of a cost cut there, and (b) cut R&D group leads by over half and sales managers by half, in the two units doing the least routine, highest-skill work — exactly where thin supervision shows up as quality and attrition problems later, not immediately. It also compounds Stress test 1: thinner key-account coverage during a period when the company is already taking on customer-relationship risk from the calibration change is the wrong sequencing.

**Net effect:** even the differentiated design still delivers a 3-manager (9%) reduction — most of the board's intent survives, just redirected to where the work can take it.

## Decision rights (key decisions — gap, not yet assigned)

| Decision | Should decide | Should be consulted | Executes | Today |
|---|---|---|---|---|
| Which customer segments (if any) move to a calibration partner | COO, with CFO sign-off on the business case | Sales (churn/win-rate read), Field Ops (capacity data) | Field Ops + partner | No segmented decision exists; board brief treats it as all-or-nothing |
| Target span per unit | Unit head, within a board-set cost envelope | HR (workload data), Finance (cost) | Unit head | HR currently proposing one number for all units |
| Approving exceptions to target span | Unit head's manager | HR | — | Not defined |

## Structure/sourcing options

| Option | Description | Meets capability needs | Cost (vs. EUR 1.8m target) | Transition risk | Score |
|---|---|---|---|---|---|
| A — Board mandate as written | Full outsourcing of calibration; flat 1:12 everywhere | No — removes the top deal-winning reason; guts R&D/sales leadership | Nets to roughly –EUR 0.4m/yr on calibration alone (before management-cost effect, not sized — see Assumptions) | High — irreversible customer and technical-leadership loss | Low |
| B — Do nothing | Keep sourcing and spans as is | Yes | EUR 0 saved; board's cost target unmet | Low | Fails the mandate |
| **C — Recommended: staged partial sourcing + differentiated spans** | Core calibration stays in-house; partner used only for overflow/low-density capacity, expanded in stages against a churn gate; spans set per unit (wide in standardised units, near-unchanged in specialist units) | Yes — preserves the differentiator, still cuts cost | Partial calibration saving (lower than EUR 1.8m until stages prove safe) + management-headcount saving from 3 roles (EUR value pending comp data) + technician routing/utilisation efficiency (unsized) | Moderate — sequenced, with kill gates before each expansion | **Recommended** |

*(Criteria — value preserved, cost impact, transition risk — are proposed here, to be agreed with the board before final scoring.)*

## Spans, layers, sourcing — summary

- **Spans:** differentiated by work type, not a single number. Standardised units (field technicians, customer service) take the headcount reduction; specialist units (R&D, key-account sales) keep spans close to today's, adjusted only where a workload review (not yet done) supports it.
- **Sourcing:** field calibration — keep in-house for the existing book; pilot a partner only for (a) demand overflow and (b) the lowest-density regions, where Halvorsen's own technician utilisation is weakest, mirroring a surge-capacity model rather than a wholesale handover. Expand only after a properly stratified pilot (see below) clears a churn gate.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Present this counter-analysis to the board in place of the literal mandate; agree the cost-vs-risk framing and the decision rights above | CEO/COO | Nov 2026 (ahead of Dec board meeting) | Board accepts staged approach over full rollout |
| 2 | Request manager compensation by band and field-tech dispatch/utilisation data (needed to size savings — see Assumptions/Open questions) | CFO, HR, Field Ops | Nov 2026 | Data in hand before Dec meeting |
| 3 | Design a stratified sourcing pilot: segment by region density, contract tenure, account value; route only the lowest-risk segment to partner; keep a matched control group as Region North did | Field Ops + Sales Ops | Dec 2026 – Jan 2027 | Pilot design signed off with explicit churn/win-rate kill criteria |
| 4 | Run technician routing/utilisation improvement in-house in parallel, to capture part of the 22% partner cost gap without customer-facing risk | Field Ops | Jan–Jun 2027 | Measurable EUR/technician cost reduction, no churn increase |
| 5 | Run the stratified pilot for 12 months with a mid-point churn/win-rate read at 6 months | Field Ops + Sales Ops | Q1–Q4 2027 | Churn differential ≤7.4 pp (breakeven) in the piloted segment before any further rollout |
| 6 | Re-set spans per unit per the differentiated design; implement via natural attrition/redeployment in field technicians and customer service first, since those units gain headcount under this design relative to the flat mandate | Unit heads + HR | Q1 2027 | 3 net manager-role reduction achieved without touching R&D/sales headcount |
| 7 | Report back to the board: realised savings, churn, win-rate readout; decide on further sourcing expansion only against the kill criterion | COO | Dec 2027 | Go/no-go on stage 2 of partner sourcing |

## What would change the answer

1. If the Region North pilot result is shown to be a regional outlier (e.g. a second control pilot in another region shows no churn differential), full outsourcing becomes viable and the EUR 1.8m saving can be taken at low risk.
2. If manager compensation data shows R&D/sales managers cost materially more per head than field/CS supervisors, the EUR savings from a flat 1:12 could exceed the differentiated design's, changing the cost-risk trade-off (though the capability loss in R&D/sales would still need separate justification).
3. If the board states the EUR 1.8m target is for margin, not competitiveness, and is willing to accept a slower path to it, the staged pilot (Option C) is clearly right; if the target is urgent and non-negotiable for this fiscal year, the board needs to see this memo's numbers and explicitly accept the churn risk before choosing Option A.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Region North's 9pp churn differential is representative of a company-wide rollout | 9 pp applied to all 3,000 customers | Only pilot data available (400 customers, 1 region, 12 months) | A multi-region or longer-run pilot shows a materially different (lower or higher) differential |
| 2 | Churned customers do not return and the EUR 2.19m contribution loss is at least a one-year effect, not fully one-off | Treated as a recurring-risk, not purely one-time, cost | No multi-year pilot data exists | Data shows churned accounts partially return, or that churn stabilises after year one |
| 3 | Illustrative differentiated spans (16 / 18 / 6 / 7) are directionally right but not benchmarked | Used only to show the *shape* of a better design | No peer/industry benchmark data in the pack — must not be stated as fact | A workload or peer-benchmarking study sets different, evidence-based targets |
| 4 | EUR 1.8m is the saving from outsourcing the full 3,000-customer book, not a partial figure already netting some risk | Compared directly against the EUR 2.19m contribution loss | Board brief states it as "saving EUR 1.8m a year" with no scope qualifier | The EUR 1.8m is already a partial/conservative estimate, narrowing or closing the gap |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Manager compensation by unit/band | Needed to convert the 3-vs-5 manager headcount deltas into EUR, and to compare Option A vs C on cost alone | CFO/HR | Could move the two options closer or further apart in pure cost terms |
| Does the 62% win-rate figure segment by which customers actually use on-site calibration, or is it company-wide? | If it's company-wide, the true calibration-specific win-rate could be even higher; if diluted, the risk is smaller than estimated | Sales Ops (owns the win/loss interview data) | Changes the size of the new-deal win-rate risk this memo flags but does not quantify |
| Field technician dispatch/capacity data by region | Determines which regions are genuinely low-density/overflow candidates for a partner, and whether a wider span is operationally safe in field technicians | Field Ops | Sizes the "safe" partial-outsourcing segment and validates the proposed span of ~16 |
| Is the EUR 1.8m target driven by competitiveness or margin? | Changes how much churn risk the board should be willing to accept and how fast | Board/CFO | Determines urgency of Option A vs. the staged Option C |
| Works council / labour law constraints on reducing R&D or sales management headcount, or on redeploying field/CS supervisors | Any headcount reduction in Europe-based operations typically needs consultation | Legal/HR | Could lengthen the timeline in the transition plan; flagged, not analysed here |

