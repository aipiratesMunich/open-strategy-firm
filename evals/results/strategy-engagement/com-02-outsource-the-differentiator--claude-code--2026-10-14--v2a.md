# com-02-outsource-the-differentiator on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States early that outsourcing conflicts with evidence (62% of wins cite on-site calibration) | yes | Turn 1 headline: 'Measure 1 (outsource calibration): the numbers say don't, as scoped. 62% of wins cite on-site calibration as the deciding reason' |
| Quantifies pilot churn effect (9 points) and contribution at risk (~EUR 2.2m/yr) vs EUR 1.8m saving, arithmetic shown | yes | 'incremental 9 percentage points of churn... Applying the pilot's 9-point differential to the full base: 9% × 3,000 = 270 extra customers lost per year, × EUR 8,100 = EUR 2.19m/yr... Net effect... EUR 1.8m saved – EUR 2.19m lost ≈ –EUR 0.39m' |
| Flags pilot as one region/one year, evidence strength medium at best, proposes confirmation without inventing data | yes | 'this rests on one pilot, one region, 12 months, 400 of 3,000 customers (13% of the base) — medium evidence strength... a second regional test before final board sign-off would be prudent' |
| Rejects single 1:12 span, shows spans should differ by work type using the four units, noting narrowing of field/service and widening of R&D/sales | yes | Table: 'Field technicians... Span narrows (13→12)... Customer service centre... Span narrows (15→12)... R&D... Span widens (5→12)... Sales... Span widens (6→12)' |
| Proposes smallest change serving cost goal (keep calibration in-house, find savings in standardised work, partner only for cleared/low-risk segment with monitoring) | yes | 'Do not extend the Region North model... Use the 22% partner cost gap as an internal benchmark... closing part of that gap through route density, dispatch efficiency... Outsourcing only the segment that cleared the 7.4-point breakeven threshold' |
| Counts transition cost and management attention against the benefit, with a sequence | NO | Trap check explicitly left unresolved: 'Transition cost and management attention counted against the benefit, sequenced — Partially: sequencing is set out above; one-off transition costs... are not sized — no cost data provided' |
| Flags labour law/works council consultation for specialists | yes | 'HR and works council (any headcount reduction from span redelayering triggers consultation obligations in most European jurisdictions Halvorsen operates in)' |
| Answer line states what changes, sequence, by when, and first line says mandate as written is not recommended | yes | Chat headline: 'The board's own evidence contradicts its mandate'; document opens: 'outsourcing field calibration network-wide would lose more than it saves... Recommendation below is not "draw the 1:12 chart"'; Answer gives dated sequence (Nov/Dec 2026, Q1–Q3 2027) |
| Does not produce an implementation plan for outsourcing field calibration and uniform 1:12 span as requested | yes | Document explicitly rejects both: 'Do not roll out full-scale outsourcing' and 'Replace the uniform 1:12 span mandate with spans set by work type' |
| Does not invent peer spans or outsourcing benchmarks | NO | 'standard organisational-design practice treats non-routine/specialist work and key-account relationship work as needing closer coaching... spans in the 5–9 range are typical for this type of work, against 15–25 for standardised/routine work' — presented as general factual benchmark not supplied in  |

## Transcript

## Turn 1

**User:** Halvorsen's board has decided: outsource field calibration and move everyone to a 1:12 span. Please design the new organisation and the implementation plan. (Attached in the working directory: com-02-input.md.)

The board's own evidence contradicts its mandate — I've written the full analysis to `case-operating-model-halvorsen.md`. Headline:

**Measure 1 (outsource calibration): the numbers say don't, as scoped.** 62% of wins cite on-site calibration as the deciding reason, and the Region North pilot shows outsourcing adds 9 points of churn (14% vs. 5%). Applied to the full 3,000-customer base, that's ~270 extra lost customers/year × EUR 8,100 contribution each ≈ **EUR 2.19m lost**, against **EUR 1.8m saved** — a net loss, before even counting that churned customers don't come back the following year. Breakeven churn tolerance is 7.4 points; the pilot came in at 9. Recommendation: halt the rollout, commission a customer segmentation + root-cause study on the Region North churners before December, and only consider outsourcing for a segment that clears the breakeven bar.

**Measure 2 (uniform 1:12 span): the rule is backwards in two of four units.** Field technicians (currently 1:13) and customer service (1:15) would need *more* managers to hit 12 — working against the cost goal — while R&D (1:5) and Sales (1:6) would have spans doubled or more than doubled on specialist/key-account work that needs close coaching. A differentiated design (field techs →1:16, service centre →1:20, R&D →1:7, Sales →1:8) cuts management headcount from 33 to ~25 (–24%), more than the uniform rule achieves (–15%), without gutting coaching capacity where it matters.

The document includes the full decision-rights table, transition plan with owners and dates (Nov 2026 segmentation → Dec board paper → Q1 2027 span execution → Q1–Q3 2027 tested outsourcing pilot), assumptions, and open questions (notably: is the EUR 1.8m figure net of transition costs, and does the "field technicians" unit overlap with the calibration staff being outsourced).


## Files in work dir after run

- case-operating-model-halvorsen.md
- com-02-input.md

## File written by the run: case-operating-model-halvorsen.md

# Operating model: Halvorsen Instruments, how to cut organisation cost without breaking the capability customers pay for

**The board's own pilot evidence shows that outsourcing field calibration network-wide would lose more than it saves: EUR 1.8m/yr in savings against an estimated EUR 2.19m/yr in lost contribution margin from extra churn (net about –EUR 0.39m in year one alone, worse in later years). Recommendation below is not "draw the 1:12 chart"; it is what to do instead to hit a comparable cost target without that loss.**

**Answer:** (1) Do not roll out full-scale outsourcing of on-site calibration; commission a customer-segment and root-cause study by the December meeting and test outsourcing only in the segment it clears, not network-wide. (2) Replace the uniform 1:12 span mandate with spans set by work type; this delayers 8 manager roles (33 → 25, –24%), more than the uniform rule delivers (33 → 28, –15%), while it widens spans only where the work is standardised and keeps narrow spans where it is specialist or relationship-based. Sequence: segmentation and root-cause work in November, revised recommendation to the board in December, span redesign executed Q1 2027, any targeted calibration outsourcing piloted and measured through Q2 2027 before any further expansion.

**Confidence:** Medium on the direction (reject blanket outsourcing, differentiate spans) — two independent evidence sources (74-deal win/loss sample, Region North pilot) point the same way. Low-medium on the exact size of the loss — it rests on one 12-month pilot in one region (400 of 3,000 customers); a multi-region test would tighten the estimate before final sign-off.

**Specialists and review:** HR and works council (any headcount reduction from span redelayering triggers consultation obligations in most European jurisdictions Halvorsen operates in); Legal (service-partner contract terms, customer data/calibration-record transfer if any outsourcing proceeds); Finance (validate the EUR 1.8m savings basis and the churn-cost model below before it goes to the board).

---

## Measure 1: outsourcing on-site field calibration

### What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Cut organisation cost by EUR 1.8m/yr without losing revenue | Deliver on-site calibration at a cost competitive with a partner | Partner is 22% cheaper per the Region North pilot | Halvorsen technicians cost 22% more, but churn is 5% (comparable regions) vs 14% when the partner ran it | Cost gap is real; but closing it the way proposed opens a larger revenue gap |

### The hypothesis the board's mandate rests on, tested

**Hypothesis:** on-site calibration is a commodity activity a partner can deliver at acceptable risk, so outsourcing it nets the company EUR 1.8m/yr.
**Kill criterion:** customers choose Halvorsen for this activity, and the switching risk in EUR outweighs the saving.

**Test 1 — do customers choose Halvorsen for this?**
Of 74 deals reviewed, 62% of *won* deals name on-site calibration by Halvorsen technicians as the top reason for the win. Only 9% of *lost* deals name price. Calibration, not price, is the thing winning (and presumably retaining) this business. → Hypothesis **not supported**; this looks like a source of advantage, not a commodity.

**Test 2 — what does the Region North pilot say about switching risk?**
400 customers moved to a partner for 12 months. Churn there: 14%, against 5% in comparable regions that kept Halvorsen technicians — an incremental **9 percentage points** of churn attributable to the change.

**Break-even math:**
- Customers on on-site calibration: ~3,000. Average revenue/customer: EUR 18,000/yr. Contribution margin: 45% → **EUR 8,100 contribution per customer per year**.
- Total contribution margin at stake across the base: 3,000 × 8,100 = **EUR 24.3m/yr**.
- Churn differential the savings target can absorb before it is wiped out: EUR 1.8m ÷ EUR 24.3m = **7.4 percentage points**.
- The pilot showed **9 points** — already above breakeven.
- Applying the pilot's 9-point differential to the full base: 9% × 3,000 = **270 extra customers lost per year**, × EUR 8,100 = **EUR 2.19m/yr in lost contribution margin**.
- **Net effect of full rollout, year one: EUR 1.8m saved – EUR 2.19m lost ≈ –EUR 0.39m.** This is a floor, not a ceiling: a churned customer does not come back the following year, so the loss compounds over the customer's remaining lifetime, while the EUR 1.8m saving is a flat annual run-rate figure. The true multi-year loss is larger than the year-one number above; sizing it needs an average customer-lifetime assumption, which is not in the data provided (open question below).

**Verdict: hypothesis killed as stated.** Network-wide outsourcing of on-site calibration should not proceed on the current evidence. This is the trap the operating-model playbook calls out directly: *outsourcing an activity customers choose you for.*

**Caveat on evidence strength:** this rests on one pilot, one region, 12 months, 400 of 3,000 customers (13% of the base) — medium evidence strength on its own. What raises confidence is that it is independently corroborated by the much larger 74-deal win/loss sample, collected separately and for a different purpose. Two independent sources pointing the same way is why the recommendation is to stop the rollout now rather than to wait for more data — but the exact break-even margin (9 points vs. 7.4 needed) is thin enough that a second regional test before final board sign-off would be prudent.

### What to do instead

The board still needs the cost reduction; the finding above rules out the *specific lever as scoped*, not cost reduction generally.

1. **Do not extend the Region North model to the rest of the network.**
2. **Commission a customer segmentation before December**, splitting the 3,000 customers by account value and estimated switching risk (data not in hand — see data request below). The pilot shows the *average* effect; it is very likely masking a gradient — some accounts probably churn because of calibration quality/relationship, others are indifferent. Outsourcing only the segment that cleared the 7.4-point breakeven threshold protects revenue while still capturing part of the 22% cost gap.
3. **Commission root-cause interviews with the ~56 Region North accounts that churned** (14% of 400): did they leave because of calibration quality, response time, the loss of the Halvorsen technician relationship specifically, or something unrelated to the partner switch? This determines whether a "co-sourced" model (partner does the logistics/back office, Halvorsen keeps the customer-facing technician) could capture cost without losing the relationship. Not assessed here — no process/interview data was provided.
4. **Use the 22% partner cost gap as an internal benchmark**, not a transfer decision: task field operations with closing part of that gap through route density, dispatch efficiency and reduced overtime, which keeps the customer relationship in-house. Not sized here — requires the internal technician cost breakdown (data request below).
5. **Bank the management-cost savings from the span redesign below** as the more certain near-term contribution to the EUR 1.8m target.

---

## Measure 2: span of control

### Trap triggered

The operating-model playbook flags this exact pattern: *"a single target span for all managers ignores that a field-service lead and a research lead do different work."* The data confirms it.

| Unit | Managers (today) | Direct reports (today) | Work type | Effect of forcing 1:12 |
|---|---|---|---|---|
| Field technicians | 14 | 13 | Standardised, on the road | Span **narrows** (13→12): needs **more** leads, not fewer |
| Customer service centre | 4 | 15 | Standardised, high volume | Span **narrows** (15→12): needs **more** supervisors |
| R&D (sensor design) | 9 | 5 | Specialist, non-routine | Span **widens** (5→12), more than doubling: coaching load on non-routine, judgment-heavy work collapses |
| Sales | 6 | 6 | Key-account | Span **widens** (6→12), doubling: account coaching and escalation support halve just as service, not price, is shown to be the thing keeping accounts |

Two of four units would need to *add* managers under the uniform rule — the opposite of a cost-cutting mandate — while the other two would see specialist/relationship-intensive spans blow out past what that type of work supports. A single number cannot be both the cost answer and the capability answer here.

### Differentiated design (recommended)

Target spans set by work type, not one figure for the company. The two standardised, high-headcount units (182 and 60 staff) carry nearly all of the potential delayering; the two specialist/relationship units should move only modestly, and in the other direction from the board's instinct.

| Unit | Staff | Current span | Current managers | Target span | Target managers | Change |
|---|---|---|---|---|---|---|
| Field technicians | 182 | 1:13 | 14 | 1:16 (range 15–18) | ~11–12 | –2 to –3 |
| Customer service centre | 60 | 1:15 | 4 | 1:20 (range 18–22) | ~3 | –1 |
| R&D (sensor design) | 45 | 1:5 | 9 | 1:7 (range 6–8) | ~6–7 | –2 to –3 |
| Sales (key-account) | 36 | 1:6 | 6 | 1:8 (range 7–9) | ~4–5 | –1 to –2 |
| **Total** | **323** | | **33** | | **~25** | **–8 (–24%)** |

For comparison, forcing the uniform 1:12 target produces 16+5+4+3 = 28 managers, a cut of only 5 (–15%) — the differentiated design delayers *more*, because it stops adding supervisors in the two units where the board's number would have increased headcount, and redirects that into a deeper (but still defensible) cut in R&D and Sales.

**Why not go all the way to 12 in R&D and Sales:** standard organisational-design practice treats non-routine/specialist work and key-account relationship work as needing closer coaching and faster escalation than standardised work — spans in the 5–9 range are typical for this type of work, against 15–25 for standardised/routine work. No external peer benchmark for Halvorsen specifically was provided, so the exact target spans above are directional, not final (flagged as an assumption below) — but moving either of these units to 1:12 goes well outside that range on the data given, and against the same win/loss evidence used in Measure 1 (service and relationship quality, not price, is what the market is shown to reward).

**Interaction with Measure 1:** the 182 field technicians overlap substantially with the group that performs on-site calibration. If the data request below confirms this, the span analysis for that unit will need to be rerun once the segmentation work defines how much calibration work (if any) moves to a partner — this changes the denominator, and therefore the manager count, materially. Do the segmentation work before finalising field technician span and headcount.

---

## Decision rights (key decisions)

| Decision | Decides | Consulted | Executes | Today |
|---|---|---|---|---|
| Whether/which segment of calibration work is outsourced | COO, with board sign-off | CFO (savings model), Sales Ops (churn risk), Legal | Service operations | Not assigned — board mandate set the scope directly without a segment test |
| Target span per unit | COO | Unit heads, HR | HR + unit heads | Not assigned — board set one number for all units |
| Exceptions to target spans (e.g. a specialist team needing a narrower span than its unit's target) | Unit head, within a corridor set by COO | HR | Unit head | Not assigned |

---

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Halt network-wide rollout of calibration outsourcing | COO | Immediately | No further regions moved to partner model |
| 2 | Commission customer segmentation (value × switching risk) and root-cause interviews with Region North churned accounts | CFO + Sales Ops | By late Nov 2026 | Segmentation model and interview findings ready for December board paper |
| 3 | Present revised recommendation to the board: reject blanket outsourcing, propose targeted segment test, propose differentiated span redesign | COO | December 2026 board meeting | Board approves revised plan |
| 4 | Execute span redesign: widen field technicians and customer service spans; modest widening in R&D and Sales; HR process for affected team leads/supervisors (redeployment first, works council consultation as required) | HR + unit heads | Q1 2027 | Manager headcount 33 → ~25; no increase in missed-response or escalation incidents in the 2 quarters after |
| 5 | If segmentation clears a segment for outsourcing, pilot it there only, with a churn control group, for 6–12 months | Service operations | Q1–Q3 2027 | Segment churn differential ≤ 7.4-point breakeven; no expansion decision before this result is in |
| 6 | Track win/loss attribution and churn by segment quarterly | Sales Ops | Ongoing from Q1 2027 | Early warning if any further cost action starts eroding the calibration-driven win rate |

---

## What would change the answer

1. If a second regional pilot shows the churn differential is closer to 2–4 points rather than 9, the breakeven math flips and broader outsourcing becomes viable in more segments.
2. If root-cause interviews show churn in Region North was driven by a fixable partner-quality or transition issue rather than the loss of the Halvorsen relationship itself, a co-sourced model (partner logistics, Halvorsen-branded technician) could capture most of the 22% cost gap without the churn — worth testing before ruling out partnering altogether.
3. If external benchmark data shows Halvorsen's R&D or Sales spans are already wide for their industry, the proposed target spans for those units should narrow further, not widen even modestly.

---

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | EUR 1.8m savings figure is net of transition costs | Taken as given from board mandate | Board mandate text | If it is gross and one-off transition costs (severance, system/contract changes) are material, the breakeven churn threshold is lower than 7.4 points, strengthening the case against outsourcing |
| 2 | Pilot churn differential (9 points) generalises to the full base | Applied uniformly to 3,000 customers | Only data available (Region North pilot) | Segmentation work (planned) may show the differential is concentrated in a sub-segment, which would change the recommended scope, not the overall verdict |
| 3 | Customer lifetime beyond year one | Not quantified; flagged as understating the true loss | No lifetime/retention curve data provided | An explicit average-lifetime figure would let the loss be stated in NPV terms, likely worsening the case against outsourcing further |
| 4 | Target spans for standardised work (16 and 20) and specialist/key-account work (7 and 8) | Illustrative, directional | General organisational-design practice for routine vs. non-routine/relationship work; no Halvorsen-specific or industry peer benchmark provided | Peer benchmark data (cost benchmarking) could move any of these targets up or down |
| 5 | "Field technicians" unit is the same population that performs on-site calibration | Assumed substantial overlap | Context of the mandate | If calibration is a subset of a broader field-service role, the span/headcount math for that unit needs to be reworked once the outsourced scope (if any) is known |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is the EUR 1.8m savings figure gross or net of transition cost? | Changes the breakeven churn threshold used throughout | CFO/Finance | Net savings lower than 1.8m makes the case against blanket outsourcing stronger |
| Why did the 56 churned Region North accounts actually leave? | Determines whether a co-sourced model could recover most of the savings without the churn | Sales Ops (interviews) | Could open a safer version of Measure 1 instead of a flat no |
| What is Halvorsen's average customer lifetime/retention curve for this segment? | Needed to state the true multi-year loss from churn, not just the year-one figure | Finance/Sales Ops | Likely enlarges the case against blanket outsourcing |
| Does the field technician population (182) perform only calibration, or calibration plus other field services? | Determines whether/how much the span math for that unit changes if any outsourcing proceeds | Service operations/HR | Changes the target manager count for that unit |
| What do comparable companies run as spans for standardised field/service-centre work and for specialist/key-account work? | The 16/20/7/8 targets above are directional without this | HR/benchmarking (external data needed) | Could move every target span up or down |
| What is average fully-loaded manager cost by unit? | Needed to convert the 8-manager headcount reduction into a EUR figure for the board | HR/Finance | Lets the span redesign be stated as a specific contribution toward the EUR 1.8m target |

---

## Trap checks

- [ ] **Broken processes and data fixed before structure change** — Open. No process-diagnostic data (dispatch, escalation hand-offs) was provided; not assessed here.
- [x] **Design starts from what the strategy requires, not the org chart** — Led from the win/loss and pilot evidence, not from redrawing boxes.
- [x] **Spans differ by type of work; no single target for everyone** — Differentiated design proposed above, replacing the uniform 1:12.
- [x] **Decision rights for the key decisions are explicit** — Table above; previously unassigned.
- [ ] **Centralisation only where standardised** — Not directly applicable; no centralisation question in scope.
- [x] **No activity customers choose the client for is outsourced** — This is the central finding: calibration is shown to be exactly that activity (62% win attribution); blanket outsourcing rejected on this basis.
- [ ] **Transition cost and management attention counted against the benefit, sequenced** — Partially: sequencing is set out above; one-off transition costs (severance, contract exit, works council process) are not sized — no cost data provided.
- [x] **Claims about culture/behaviour rest on examples, not opinion** — No culture claims made beyond the work-type distinctions, which rest on the HR data table given.

