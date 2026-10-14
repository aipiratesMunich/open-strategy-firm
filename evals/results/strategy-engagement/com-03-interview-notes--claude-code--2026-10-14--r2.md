# com-03-interview-notes on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Counts the themes in line with reference values (difference of one acceptable if explained) | NO | The write-up attributes the 'plan not visible' theme only to I3 and I8 ('lives on the planner's personal drive... (I3, I8)'), but I1 ('we cant see what the bakery plans to bake tomorrow so we guess') and I5 ('don't know what the bakery is planning') independently raise the same theme and are left ou |
| Links the symptom (waste/stockout spikes) to the 2025 changes as hypothesis to test with store-level data (I8) | yes | 'That timing match is circumstantial, not proof, but it points at the 2025 process redesign' and open question: 'Can store-level waste and stockout data (offered by I8) be pulled before deciding?' |
| Names unowned decisions (late order changes after cut-off, substitutions/allocation when short, sharing the plan) and proposes explicit owners | yes | Decision rights table: 'Accept a late order change... Should decide: Production planner, within a published tolerance'; 'Who gets the item when one runs short... Should decide: Production planner or logistics lead'; plan-sharing owner 'Production planner, authorised by COO'. |
| Treats culture statements (I2, I7) as opinions without examples, not basis for recommendation | yes | 'I7's "culture, HQ never listens" is an opinion, not an example; treat as a symptom of the above, not a separate cause' — excluded from the root-cause table and from the recommendation, and I2's parallel aside is only ever used for its weather fact, never as causal evidence. |
| Recommends process/decision-rights fixes first, keeps regional layer as option to judge after, with cost/attention flagged | yes | 'Recommendation: run B now, decide on C only after measuring the result' and Option A flagged 'Cost: High — 4 FTE ongoing, plus a new layer's coordination overhead... Score: Low'. |
| States what data would confirm the diagnosis (store-level waste/stockouts before/after 2025 change, timing of late changes) | yes | 'If store-level waste data (which I8 offered to share) shows waste is concentrated in a few outlier stores rather than system-wide, the fix is coaching... not a system-wide process redesign' plus assumption that another confound in the 2025 window would change the answer. |
| Answer line states what changes, in what sequence, by when | yes | Transition plan steps with 'Within 1 week', 'Within 2–3 weeks', '4–8 weeks', 'After one full cycle (6–8 weeks post steps 1–3)'. |
| Must not recommend the new regional layer as the main answer | yes | 'Don't add the 4 regional managers yet' stated as the headline answer. |
| Must not invent quotes, interview counts, or figures not in the notes | yes | All cited figures (4.8%→9.2%, ~2→~7 stockouts, 6pm→2pm) and quoted phrases ('orders safe', 'stores feel alone') match the source notes. |

## Transcript

## Turn 1

**User:** These are my notes from 9 interviews about why our central bakery and stores don't work together. CEO wants regional managers. Make sense of it and tell me what we should change. (Attached in the working directory: com-03-input.md.)

I wrote the full analysis to `case-operating-model-brightwell.md`. Here's the short version:

**Don't add the 4 regional managers yet.** The 9 interviews trace the waste spike (4.8%→9.2%) and stockout spike (~2→~7/week) to three unowned things created by the 2025 change, not to a missing layer:

1. **Stores can't see the production plan** — it lives on the planner's personal drive, not shared, not in the ERP (I3, I8). That's why stores "order safe" and drive the waste (I8).
2. **The 2pm cutoff locks before the information that drives next-day demand exists** — weather (I2), train timetable for the station store (I5) — both known by ~5pm.
3. **No one owns the substitution decision when an item runs short** — it defaults to whoever's on the ramp: the driver (I1, I6) or an even split by the baker (I4).

The "stores feel alone, HQ doesn't listen" complaints (I5, I7, I9) that are feeding the CEO's regional-manager idea read as symptoms of those three gaps, not a separate cause — and as proposed, regional managers wouldn't actually get any decision right over the plan, the cutoff, or substitutions, so they wouldn't fix any of this. That's the classic trap: new boxes on an unfixed process give the same numbers with a new org chart.

**Recommended sequence**, cheap and fast before committing to 4 new salaries:
1. Share the plan sheet with stores now (days, no cost — just authorize it).
2. Split the cutoff into a 2pm bake-commit + a bounded late-adjustment window matching when real demand signals arrive.
3. Publish a substitution priority rule owned by the planner/logistics lead, decided before dispatch.
4. Get the plan into the ERP so it's not one person's personal file.
5. Re-measure waste and stockouts after one cycle (~6–8 weeks) — only then decide if any coordination role is still needed, and size it to whatever gap remains (likely far lighter than a 4-person management tier).

Open questions worth chasing before finalizing: why 2pm was chosen (any hard bakery constraint), total store count/geography (affects whether one planner can handle this alone), and pulling the store-level waste data I8 offered to confirm the "ordering safe" mechanism.


## Files in work dir after run

- case-operating-model-brightwell.md
- com-03-input.md

## File written by the run: case-operating-model-brightwell.md

# Operating model: Brightwell Bakeries, why central bakery and stores don't coordinate, and what the fix should be

**Answer:** Don't add the 4 regional managers yet. The 9 interviews point to three process/decision-rights failures created by the 2025 change (centralised production + 2pm cutoff), not to a missing management layer: (1) stores can't see the production plan, (2) the 2pm cutoff is set before the information that drives real demand exists, (3) no one owns the substitution/shortage decision. Fix those three — cost is near zero, timeline is weeks — then re-measure waste and stockouts before deciding whether any new layer is needed at all, and if one is, make it a liaison role with explicit rights into planning rather than a 4-person management tier that sits above the problem.

**Confidence:** medium-high on the root cause (three failures each confirmed by two or more independent interviewees across different functions); low on sizing the fix, since no cost, headcount or timeline data was collected.

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Hit 5% waste target | Stores order against visible, current production plan | Waste ≤5% of production value | Waste 9.2% (Jan–Sep 2026), up from 4.8% in 2024 | Stores order "safe" with no visibility into what's actually being baked (I8) |
| Keep top-10 items in stock | Store-level demand signal reaches the bake plan before it locks | ~2 stockouts/store/week (2024 level) | ~7 stockouts/store/week | Cutoff (2pm) sits before weather (I2) and timetable (I5) data that drives next-day demand |
| Resolve shortages without ad hoc calls | A named owner for substitution decisions when an item runs short | Decision made by someone accountable, before dispatch | Decided improvised by the driver on the ramp (I1, I6) or split evenly by the baker (I4) | No decision right assigned for this case at all |

Both symptom metrics (waste, stockouts) started moving the wrong way after the 2025 change (centralisation + cutoff move from 6pm→2pm). That timing match is circumstantial, not proof, but it points at the 2025 process redesign, not at the org chart, as the thing to fix first.

## Root causes of the gap

| Gap | Process / system cause | Decision-rights cause | Structure cause | People / skills cause |
|---|---|---|---|---|
| Waste at 9.2% | Plan sheet lives on the planner's personal drive, not in the ERP (I3, I8); stores have no view of it | — | — | None evidenced — I7's "culture, HQ never listens" is an opinion, not an example; treat as a symptom of the above, not a separate cause |
| Stockouts 2→7/week | 2pm cutoff locks before weather (I2) and next-day timetable (I5) signals exist; late changes arrive by phone/WhatsApp into a locked plan (I3, I4) | Nobody is authorised to accept a late change after 2pm | — | — |
| Ad hoc substitution on the ramp | — | Substitution decision has no named owner; defaults to whoever is physically present (driver, per I1 and I6) | — | — |
| "Stores feel alone" (I5, I9) | Downstream effect of the three gaps above — stores have no channel into planning, so they escalate emotionally instead | No one owns "represent store demand into the bake plan" | A new layer (regional manager) is being proposed to carry this, but as proposed it doesn't carry any decision right over the plan, the cutoff, or substitutions | — |

## Decision rights (key decisions)

| Decision | Decides today | Should decide | Consulted | Executes |
|---|---|---|---|---|
| Daily bake plan (volumes by item) | Production planner, locked at 2pm | Production planner | Store managers (via visible plan + a late-adjustment window) | Night baker |
| Accept a late order change (after 2pm) | No one — changes arrive by phone/WhatsApp and are not entered (I3) | Production planner, within a published tolerance and a fixed late-adjustment window | — | Production planner |
| Who gets the item when one runs short | No one — driver decides on the ramp (I1, I6), or baker splits evenly (I4) | Production planner or logistics lead, decided before dispatch, against a published priority rule | Logistics lead | Driver |
| Represent store-level demand signal (weather, local events, timetables) into planning | No one | Store manager, through a direct channel into the plan (see below); a regional-manager layer is one option for this, not the only one | — | — |

This table is the core finding: three of four key decisions have no owner today. Adding a layer above stores does not, by itself, assign any of these — the CEO's proposal doesn't specify that regional managers would get a say in the bake plan, the cutoff, or substitutions.

## Structure options

| Option | Description | Meets capability needs | Cost | Transition risk | Score |
|---|---|---|---|---|---|
| A — CEO's proposal: 4 regional managers | New layer between stores and HQ, no change to bakery process | Low — doesn't touch plan visibility, cutoff timing, or substitution rights, which are the evidenced causes | High — 4 FTE ongoing, plus a new layer's coordination overhead | Medium — risks the "reorganising before fixing the process" trap: same waste/stockout numbers, new org chart | Low |
| B — Fix process and decision rights, no new layer | Share the plan (into ERP or at minimum a shared view); split cutoff into a 2pm bake-commit + a bounded late-adjustment window; assign substitution priority to planner/logistics before dispatch | High — directly closes the three evidenced gaps | Low — mostly a visibility and a rule change, no new headcount; ERP integration is the only real spend | Low-medium — requires the planner, baker, logistics lead and drivers to adopt new rules and drop the phone/WhatsApp workaround | High |
| C — B, plus a lightweight demand-liaison mechanism (not 4 managers) | B's fixes, plus a standing channel for stores to feed local signals (weather, events, timetable) into planning — e.g. a rotating store-rep slot on a daily planning call, or one coordinator role, not four | High | Low-medium — B's cost plus at most one role, a fraction of Option A's cost | Low-medium | Highest |

*(Design criteria above — meets capability needs, cost, transition risk — are proposed for this quick case; agree them with the CEO before using them to make the final call.)*

**Recommendation: run B now, decide on C only after measuring the result.** The smallest change that closes the gap wins over the most complete redesign — four new management salaries are not justified until the cheaper fix has been tried and measured.

## Spans, layers, sourcing

- Spans and layers: current — unknown number of stores reporting into HQ/bakery functions directly (store count not given in the notes; flagged below). Adding 4 regional managers inserts one layer between all stores and HQ regardless of whether any store's problem is a layer problem — a single target structural fix applied to a problem that is evidenced as process and decision rights, not span of control.
- Sourcing: not in scope — production stays central; the question here is planning visibility and decision rights, not whether baking itself should be done centrally or locally.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Planner's daily plan sheet shared with all store managers (shared drive link or email as an interim step; ERP integration follows) | Production planner, authorised by COO | Within 1 week | Stores report they can see tomorrow's plan |
| 2 | Cutoff redesigned: 2pm bake-commit stays; a late-adjustment window (e.g. to 5–6pm) opens for bounded swaps within already-committed volumes | Production planner + COO sign-off | Within 2–3 weeks | Late changes logged and actioned, not lost by phone/WhatsApp |
| 3 | Substitution priority rule published (who gets the item when short) and applied before dispatch, not on the ramp | Production planner + logistics lead | Within 2–3 weeks | Driver substitution decisions drop to near zero |
| 4 | Plan sheet moved into the ERP so visibility doesn't depend on one person's drive | Finance controller + IT | 4–8 weeks | Plan sheet accessible without a manual share |
| 5 | Re-measure waste % and stockouts/store/week against the 2024 baseline | COO | After one full cycle (6–8 weeks post steps 1–3) | Waste trending back toward 5%; stockouts trending back toward ~2/week |
| 6 | Only then decide on a liaison/coordinator mechanism (Option C) for the residual "stores feel unrepresented" gap, sized to the gap that remains | CEO/COO | After step 5 | Decision made on measured residual gap, not on the original proposal |

## What would change the answer

1. If store-level waste data (which I8 offered to share) shows waste is concentrated in a few outlier stores rather than system-wide, the fix is coaching/incentives for those stores, not a system-wide process redesign.
2. If the number of stores per prospective region is large enough that no single planner/logistics lead can realistically run steps 2–3 (e.g., dozens of stores, high volume of late changes), a coordination role becomes necessary sooner — this is a spans-and-layers question the notes don't have data to answer.
3. If stores need to negotiate shelf-space, pricing or local promotions with HQ (not evidenced in these notes), that is a different, commercial decision right that could genuinely justify a regional-manager layer — separate from the bakery-coordination problem analysed here.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | The 2025 timing (centralisation + cutoff move) is the trigger for the waste/stockout increase | Treated as the likely cause, not proven | Timing match between the 2025 change and the metric trend; no causal test run | Another change (e.g. a supplier, recipe or demand shift) in the same window is identified |
| 2 | "Orders safe" (I8) is the main waste driver | Treated as the dominant mechanism | Single source (finance controller); not cross-checked against store-level data | Store-level waste data (which I8 can supply) shows a different pattern, e.g. waste concentrated in overproduction, not over-ordering |
| 3 | I7's "culture, HQ never listens" and I9's "stores feel alone" are symptoms, not root causes | Excluded from the root-cause table | Per the skill's own evidence rule: opinions without examples are weak evidence | Specific, repeated examples of HQ ignoring a flagged issue (not just a general feeling) are surfaced |
| 4 | Cost and headcount of the 4 regional managers were not given | No cost used; Option A marked "high cost" qualitatively only | Not stated in the notes | CEO supplies the actual cost/budget for the regional-manager plan, which could shift the relative scoring |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Why was the cutoff moved to 2pm in 2025 (bakery capacity/logistics constraint)? | If there's a hard production constraint behind 2pm, the late-adjustment window (step 2) needs to be designed around it, not just layered on top | Production planner, head baker | Could narrow how much flexibility step 2 can actually offer |
| How many stores, and how are they distributed geographically? | Determines whether one planner/logistics lead can realistically own steps 2–3, or whether a coordination role is needed sooner | COO | Could move the recommendation toward Option C sooner |
| Can store-level waste and stockout data (offered by I8) be pulled before deciding? | Confirms or kills the "orders safe" mechanism and shows whether the problem is system-wide or concentrated in a few stores | Finance controller | Could change Option B's design or flag a narrower, cheaper fix |
| Does the CEO's regional-manager plan include any specific decision right (over the plan, cutoff or substitutions), or is it purely a reporting-line/advocacy layer? | As proposed, it isn't evidenced to fix any of the three root causes; if the CEO intends to also give regional managers planning authority, the option needs re-scoring | CEO | Could change Option A's score materially |

