# com-03-interview-notes on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Counts the themes in line with reference values | yes | Issue tree organizes evidence into 6 branches (Capability, Process & systems, Decision rights, Structure, Spans & layers, People & culture) with citations across I1-I9 |
| Links symptom (waste 4.8%→9.2%, stockouts ~2→~7) to 2025 changes as main hypothesis, marked as hypothesis to test with store-level data (I8) | yes | 'waste and stockouts both jumped after the same 2025 event—centralizing the bakery and moving the order cut-off from 6pm to 2pm'; confidence rated 'medium' and open question lists 'Store-level waste and stockout figures (I8 offered to share)... sizes the "safe ordering" effect' |
| Names unowned decisions (late order changes after cut-off, substitutions/allocation when short, sharing the plan) and proposes explicit owners | NO | Decision rights table only gives explicit owners for cut-off time, plan sharing, and shortage allocation; 'no structured channel for late changes arrive by phone/WhatsApp' is identified as a failure point but never assigned its own owner or transition step distinct from cut-off/plan-sharing fixes |
| Treats culture statements (I2, I7) as opinions without examples and doesn't base recommendation on them | NO | I7 is explicitly downgraded ('I7's "culture thing" is opinion with no example — weak evidence'), but I2 is instead used as load-bearing operational evidence for the core hypothesis: 'I2, I5: decisive demand info... isn't known until ~5pm' — never flagged as an unsupported culture opinion |
| Recommends process/decision-rights fixes first, keeps regional layer as one option to judge after, with cost/attention flagged | yes | 'Winner: Option 2, sequenced as Option 3' with Option 1 costed as 'High (4 salaries + hiring/onboarding months)... Slow' and 'Revisit the regional-manager idea only if, after this fix, a genuine cross-store coordination gap remains' |
| States what data would confirm the diagnosis (store-level waste/stockouts before and after 2025 change, timing of late changes) | NO | Open questions ask for generic 'Store-level waste and stockout figures' but do not frame this as a before/after-2025 comparison, and no data request is made regarding the timing/frequency of late order changes |
| Answer line states what changes, in what sequence, by when | yes | Transition plan table: 'Step 1... Weeks 1–2... Step 5... One quarter after step 1–4 live' |
| Does not recommend the new regional layer as the main answer | yes | 'Fix the process and decision rights first... before adding any management layer' |
| Does not invent quotes, interview counts, or figures not in the notes | yes | Quotes and figures (e.g. 'not their job really', 4.8%→9.2%) are consistently attributed to specific interview numbers without apparent fabrication |

## Transcript

## Turn 1

**User:** These are my notes from 9 interviews about why our central bakery and stores don't work together. CEO wants regional managers. Make sense of it and tell me what we should change. (Attached in the working directory: com-03-input.md.)

Full analysis saved to `case-operating-model-brightwell-bakeries.md`. Here's the short version.

**The CEO's proposal doesn't match the evidence.** Nothing in the nine interviews points to a missing management layer — they point to a broken process that regional managers wouldn't fix.

**What actually happened:** waste and stockouts both jumped after the same 2025 event — centralizing the bakery and moving the order cut-off from 6pm to 2pm. There was no regional-manager layer before or after that change, so the before/after swing can't be an org-structure problem. Walking the process end to end, three concrete failures explain it:

1. **Cut-off precedes the demand signal.** Stores know tomorrow's real demand (weather, train timetable) around 5pm — three hours *after* the plan is already locked (I2, I5).
2. **The plan is invisible to stores.** It sits on the planner's personal drive, not the ERP (I3, I8). She'd share it "if someone said I may" — that's a permission gap, not a capacity gap.
3. **Nobody owns the shortage decision.** When an item runs short, the driver improvises substitutions on the ramp (I1, I6) — "not their job really," as the logistics lead says. Stores, unable to see the plan, over-order "safe" to hedge, which is where finance says the waste concentrates (I8).

**Recommendation:** fix the process and assign decision rights before touching structure:
- Reset the cut-off against when demand signals actually arrive.
- Share the plan with stores (interim read access now, ERP integration as the real fix).
- Assign the shortage-allocation rule to an existing role (e.g., the production planner), so drivers execute a rule instead of inventing one.
- Add store-level waste/stockout visibility (finance already offered the data) to stop rewarding over-ordering.

This is cheap and fast — weeks, not months — versus hiring and onboarding 4 regional managers, which wouldn't itself move the cut-off, share the plan, or create a shortage rule unless explicitly mandated to. Revisit the regional-manager idea only if, after this fix, a genuine cross-store coordination gap remains.

Open items that could change this: the bakery's minimum lead time to bake against a later cut-off, whether the ERP can host a live plan view, and actual span-of-control data (not in the interviews) — plus clarifying whether the CEO's "regional manager" is meant to solve this operational gap or is really an advocacy/account-management role.


## Files in work dir after run

- case-operating-model-brightwell-bakeries.md
- com-03-input.md

## File written by the run: case-operating-model-brightwell-bakeries.md

# Operating model: Brightwell Bakeries, central bakery ↔ stores

*Fictional company; all figures and quotes are from the attached interview notes.*

## Step 1: Sharpen the question

Raw request: "draw us a new org chart" (4 regional managers). First test what the current set-up can't deliver.

**Decision question:** Which capabilities and decisions does reliable next-day store supply require that today's set-up cannot deliver, and what is the smallest change that gets waste from 9.2% back under the 5% target and stockouts of top-10 items from ~7/store/week back toward the ~2/store/week baseline, fastest?

Measurable symptom: waste 4.8% (2024) → 9.2% (Jan–Sep 2026), target 5%; stockouts ~2 → ~7/store/week. Both moved in the same direction, after the same event: 2025 production centralisation to one bakery + order cut-off moved 6pm → 2pm. Proposed structure (CEO): 4 regional managers between stores and HQ. Held as **one option**, not the frame.

## Step 2: Issue tree

| Branch | Hypothesis | Kill criterion | Evidence |
|---|---|---|---|
| Capability | Stores need a plan that reflects same-day-evening demand signals (weather, train timetable, local events); bakery needs enough lead time to bake it | A capability already exists to reconcile late signals with the bake plan | I2, I5: decisive demand info (weather, next-day timetable) isn't known until ~5pm, 3h after the 2pm lock |
| Process & systems | Cut-off timing, plan visibility and change-handling cause the gap, not reporting lines | Misses persist even where process runs to standard | I1,I3,I8: plan not shared, not in ERP, on a personal drive; I3,I4: changes arrive by phone/WhatsApp with no path into the plan |
| Decision rights | Shortage allocation and cut-off policy have no real owner | A decision map shows clear owners already | I1,I6: driver decides substitutions on the ramp; I6: "not their job really"; I4: "nobody tells me which store gets priority" |
| Structure | The store→HQ axis or layer count blocks the fix | Gaps close with process + decision-rights fixes alone | No interview describes a span/layer overload; I5, I9 want advocacy ("fight for us", "stores feel alone"), not a missing operational link |
| Spans & layers | Current spans/layers slow decisions against what the work needs | No delay traced to spans/layers | Not evidenced in notes — **open**, flagged below |
| Sourcing | n/a | n/a | not raised |
| People & culture | Incentives reward "safe" over-ordering; "HQ doesn't listen" is a symptom of (1)–(3), not a separate cause | Culture claim holds even after process/rights are fixed | I8: waste concentrated where stores can't see the plan, so they over-order "safe"; I7's "culture thing" is opinion with no example — weak evidence |

## Step 3: Deciding analyses

**a. Strategy-to-capability map.** Priority: next-day supply matched to actual demand at acceptable waste/stockout levels. Needed capability: a plan that can absorb demand signals known only in the early evening, visible to the people who have to act on it, with a rule for what happens when an input runs short. Today: none of the three exist. **Gap confirmed.**

**b. Process diagnostics — order-to-shelf walk:**
Demand signal available (weather ~5pm / timetable next day / local events) → **cut-off 2pm, before the signal exists** → planner locks the sheet (I3) → late changes arrive by phone/WhatsApp with no system to record them (I3, I4) → baker bakes the frozen sheet (I4) → when an ingredient/item is short, the **driver** improvises substitutions on the ramp (I1, I6) → stores, unable to see the plan, **over-order "safe" to hedge** (I8) → waste rises on top of stockouts.

Four failure points, all upstream of any org chart: (1) cut-off precedes the demand signal by 3+ hours; (2) plan sheet isn't shared or in the ERP; (3) no structured channel for late changes; (4) no shortage-allocation rule. The 2024→2026 jump in both waste and stockouts lines up with the 2025 centralisation + cut-off change — there was no regional-manager layer before or after, so the before/after swing can't be attributed to a missing layer. **Hypothesis confirmed: this is a process and information gap.**

**c. Decision-rights review.** Of the "ten to fifteen decisions that matter," at least three have no real owner today:
- Cut-off time/policy — set in 2025, no evidence it was tested against when stores actually know demand, and no owner for revisiting it.
- Plan visibility — planner holds it on a personal drive and would share it "if someone said I may" (I3): a permission gap, not a capacity or structural gap.
- Shortage/substitution allocation — defaults to the driver by default, not by design (I6: "not their job really"; I1 confirms outcome).

**Confirmed:** these are assignable today, to existing roles, without a new layer.

**d. Spans and layers.** No interview reports a manager overloaded with direct reports or decisions stuck at a layer boundary; the complaints are about missing links (no visibility, no rule), not too few people per manager. **Provisional kill** of the structure/layer hypothesis — pending span-of-control data Brightwell hasn't shared (see Open questions).

**e. Sourcing.** Not raised in any interview — out of scope.

**f. Option comparison** *(criteria proposed here — waste ≤5%, stockouts back near baseline, cost, speed — to agree with COO/CEO before final scoring):*

| Option | Description | Meets capability needs | Cost | Speed | Risk |
|---|---|---|---|---|---|
| 1. CEO's proposal: 4 regional managers | New layer between stores and HQ | Indirect — doesn't itself move the cut-off, put the plan in the ERP, or create a shortage rule unless explicitly mandated to | High (4 salaries + hiring/onboarding months) | Slow (months to hire and ramp) | Could become a new "driver one level up" — an extra hop in a chain stores already say is too distant (I2, I7) |
| 2. Fix process, systems, decision rights | Move/test the cut-off against real signal timing; put the plan sheet somewhere stores can see it (ERP or, as an interim step, shared read access); give the planner a structured late-change channel; assign the shortage rule to an existing role | Directly — matches every failure point in 3b/3c | Low — mostly permission and policy decisions, not headcount | Fast — I3 is already willing; this is a go-ahead, not a project | Low; reversible |
| 3. Hybrid (recommended sequencing) | Run Option 2 first; revisit a regional layer afterward only if store-level data still shows a genuine cross-store coordination gap it would fix | Full, staged | Low now, deferred decision on more | Fast relief, option kept open | Avoids paying for a structural fix before the cheap fix is tested |

**Winner: Option 2, sequenced as Option 3.** Smallest change that closes the measured gap.

**g. Alignment check (7S).** Visibility + an explained, fair shortage rule directly answers the lived complaints (I1, I2, I4, I6, I8). I7's "HQ never listens" is a culture claim with no example attached — treat as a symptom to re-test after the process fix, not as its own workstream. Incentives currently reward over-ordering (stockouts are visible and blamed; waste is diffuse) — recommend store-level waste/stockout scorecards (I8 can supply the data) to realign incentives alongside the process fix.

## Step 4: Trap checks

- [x] Broken process and data fixed/scheduled before any structure change — Option 2 sequenced first.
- [x] Design starts from what the capability gap requires, not from the org chart.
- [ ] Spans differ by type of work — not evidenced either way; no claim made, flagged open.
- [x] Decision rights for cut-off policy, plan visibility and shortage allocation made explicit.
- [x] Centralisation (of information, not units) proposed only where it standardises an already-single plan.
- [x] No activity customers choose Brightwell for is outsourced — n/a, not proposed.
- [x] Transition cost and attention counted: Option 1 costed as high/slow and deferred; Option 2 kept deliberately cheap and fast.
- [x] Culture claims rest on examples, not opinion: I7 flagged as weak evidence; grounded claims (I1,I2,I4,I6,I8) carry the recommendation instead.

## Answer page

**Answer:** Fix the process and decision rights first — adjust the order cut-off to where real demand signals exist, put the production plan where stores can see it, give late changes a real channel, and assign the shortage-allocation rule to an existing role — before adding any management layer. Target: waste back under 5% and stockouts back near the ~2/store/week baseline within one quarter of the fix going live.
**Confidence:** medium — six of nine interviews independently converge on the same three mechanisms (cut-off timing, plan invisibility, unowned shortage rule), and the before/after timing lines up with the 2025 change rather than an org gap; medium not high because spans-of-control data and the ERP's technical ability to host a live plan view aren't in hand.

### What the strategy requires
| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Reliable next-day supply | Plan reflects late demand signals (weather, timetable) | Cut-off close to when signal is known | Cut-off fixed at 2pm, signal at ~5pm | 3h+ mismatch |
| Reliable next-day supply | Plan visible to stores | Real-time or daily shared view | On planner's personal drive, not in ERP | No visibility |
| Reliable next-day supply | Shortage handled by rule | Pre-agreed priority rule, owned role | Driver improvises on the ramp | No owner |

### Root causes of the gap
| Gap | Process/system cause | Decision-rights cause | Structure cause | People/skills cause |
|---|---|---|---|---|
| Waste 4.8%→9.2% | Stores can't see the plan, so over-order "safe" | No one assigned to approve sharing it | None evidenced | Incentives reward visible stockout-avoidance over invisible waste |
| Stockouts 2→7/wk | Cut-off precedes real demand signal | Cut-off policy has no owner for revision | None evidenced | — |
| Ad hoc substitutions | No structured late-change channel | Shortage allocation unassigned | None evidenced | Driver doing a planning job by default |

### Decision rights (key decisions)
| Decision | Decides | Consulted | Executes | Today |
|---|---|---|---|---|
| Order cut-off time | Ops/COO (proposed) | Store managers, head baker | Production planner | Set unilaterally in 2025, unowned since |
| Plan sharing/visibility | Production planner, with COO sign-off | Finance (I8 has store-level waste data) | Planner, via ERP or interim shared access | Nobody — on a personal drive |
| Shortage/substitution allocation | Production planner (proposed) | Logistics lead, store managers | Logistics/drivers execute the rule | Driver decides ad hoc |

### Structure options
See option-comparison table in Step 3f above.

### Spans, layers, sourcing
- Spans and layers: not evidenced either way in the interviews — data request below before scoring Option 1 further.
- Sourcing: not raised; out of scope.

### Transition plan
| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Test and reset cut-off against actual signal timing (weather/timetable) | COO + production planner | Weeks 1–2 | New cut-off agreed with store managers |
| 2 | Share plan sheet (interim: read access; target: in ERP) | Production planner, IT | Weeks 1–4 | Stores can see tomorrow's plan daily |
| 3 | Define and assign shortage-allocation rule | Production planner + logistics lead | Weeks 2–3 | Written rule; drivers execute, don't decide |
| 4 | Store-level waste/stockout scorecard | Finance (I8) | Weeks 2–6 | Visible by-store waste and stockout trend |
| 5 | Re-measure waste and stockouts; revisit regional-manager case only if a genuine cross-store gap remains | COO | One quarter after step 1–4 live | Waste <5%, stockouts near 2/store/week |

### What would change the answer
1. If spans-of-control data show managers already overloaded across many stores with no bandwidth to run step 1–4, that supports a lighter structural add (not necessarily 4 regional managers) sooner.
2. If, after the process fix, waste/stockouts don't recover because stores still need someone with authority to reallocate scarce stock *across* stores in real time, that is a genuine capability gap a regional or hub role could close — re-open Option 1 then, sized to the residual gap, not the original one.
3. If the ERP genuinely cannot host a shared plan view even as an interim read-only export, the systems fix needs its own budget and timeline, which would push back the quarter-length test window.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Target date for CEO's decision | One quarter after fixes go live | Not stated by CEO — assumed | A harder deadline exists that rules out testing before restructuring |
| 2 | Interim plan-sharing doesn't require full ERP integration | Shared read access acceptable short-term | I3's sheet is a working document already; I8 confirms it's simply "not in the ERP" yet, not technically infeasible | IT confirms no interim access is possible at all |
| 3 | "Regional managers" in the CEO's proposal means an operational/decision layer, not a sales-support role | Scored as a structural fix to the waste/stockout problem | That's the problem the notes were collected on | CEO's real intent is a sales/account-management layer unrelated to production planning |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is the bakery's minimum lead time to bake to a changed plan? | Sets the floor for how late the cut-off can move | Head baker (I4), production planner (I3) | Determines the new cut-off time, not whether to move it |
| Can the ERP host a live plan view, and on what timeline? | Decides interim vs. final systems fix | IT / production planner | Could add a systems workstream and cost to the transition plan |
| What are current spans and layers from HQ to store? | Only unresolved branch of the issue tree | HQ org chart, COO | Could reopen the structure hypothesis if spans are genuinely stretched |
| Store-level waste and stockout figures (I8 offered to share) | Confirms whether waste is concentrated as I8 describes, and sizes the "safe ordering" effect | Finance controller (I8) | Prioritises rollout order and sizes the expected waste reduction |
| What does the CEO mean by "regional manager" — advocacy/account role, or an operational decision-owner? | Changes what Option 1 is actually being scored against | CEO | Could change Option 1's cost/benefit materially |

## Trap checks (restated with evidence)
- Process/data fixed before structure: yes — Option 2 first, Option 1 deferred to a trigger condition.
- Started from capability statement, not org chart: yes — Step 1/3a before any structure discussion.
- Spans differ by work type: no claim made; open.
- Decision rights explicit: yes — table above.
- Centralisation only where standardised: yes — centralising the *plan's visibility*, not adding a management layer.
- No customer-chosen activity outsourced: n/a.
- Transition cost counted and sequenced: yes.
- Culture claims rest on examples: yes — I7 downgraded to weak evidence, not load-bearing.

