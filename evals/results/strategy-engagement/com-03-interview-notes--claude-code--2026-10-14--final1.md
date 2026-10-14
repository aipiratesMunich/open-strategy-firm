# com-03-interview-notes on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Counts the themes in line with reference values (off-by-one acceptable if explained) | yes | Identifies three corroborated root causes (plan visibility, cut-off/demand-timing mismatch, unowned shortage allocation) plus explicitly separates out a fourth 'culture' theme as weak evidence; no reference values given to contradict this grouping. |
| Links the symptom (waste 4.8%→9.2%, stockouts ~2→~7) to the 2025 changes as main hypothesis, marked as hypothesis to test with I8's store-level data | yes | 'Confidence: medium... no data on the proposed fixes' cost/feasibility or on per-store waste exists yet' and Open Questions: 'Store-level waste breakdown (I8 offered to share)... Could redirect the waste fix if the pattern doesn't hold.' |
| Names the unowned decisions (late order changes after cut-off, substitutions/allocation when short, sharing the plan) and proposes explicit owners | yes | Decision rights table lists all three as unowned, and Transition plan assigns owners: 'Production planner + IT, sponsored by COO' (plan), 'COO + production planner + logistics lead' (cut-off), 'Logistics lead + production planner' (allocation). |
| Treats culture statements (I2, I7) as opinions without examples, not basis for recommendation | yes | 'Flagged as weak evidence and excluded from the root-cause list: I2's and I7's... culture complaints — opinions, not examples.' |
| Recommends process/decision-rights fixes first, keeps regional-manager layer as an option to judge later with cost/attention flagged | yes | Option B costed as 'High — 4 FTE ongoing... Medium transition risk — new reporting lines absorb management attention for months'; Transition step 4: 're-measure... decide then whether any coordination role is still needed.' |
| States what data would confirm the diagnosis (store-level waste and stockouts before/after the 2025 change, timing of late changes) | NO | Open Questions only requests store-level waste breakdown (I8); no mention of store-level stockout data before/after 2025, nor data on the timing/volume of late order-change requests. |
| Answer line states what changes, in what sequence, by when | yes | Answer section lists three numbered changes 'in sequence, over roughly 8–12 weeks' with a four-step transition plan giving week-level dates for each (~4 weeks, ~6–8 weeks, etc.). |
| Does not recommend the new regional layer as the main answer | yes | 'The analysis contradicts the CEO's proposed fix... Fix those first... before adding any new layer.' |
| Does not invent quotes, interview counts, or figures not in the notes | yes | No contradicting source material available to prove fabrication; cited figures (4.8%/9.2%, ~2/~7) match user's own framing, and quoted phrases are attributed consistently to specific interview numbers. |

## Transcript

## Turn 1

**User:** These are my notes from 9 interviews about why our central bakery and stores don't work together. CEO wants regional managers. Make sense of it and tell me what we should change. (Attached in the working directory: com-03-input.md.)

I read all 9 interviews against the operating-model playbook (strategy → process → decision rights → structure, in that order — never redraw boxes before fixing the process). Full analysis is in `case-operating-model-brightwell-bakeries.md`. Bottom line:

**The CEO's regional-manager fix doesn't address what's actually broken.** Three unowned process/decision gaps, each corroborated by multiple independent interviews, explain both symptoms:

1. **Waste (4.8% → 9.2%):** the production plan lives on the planner's personal drive, not the ERP (I3, I8) — stores can't see it, so they over-order "safe" (I8 directly names this as the main waste driver).
2. **Stockouts (~2 → ~7/store/week):** the 2025 cut-off moved to 2pm, but demand-relevant facts — weather (I2), train timetables for the station store (I5) — aren't known until ~5pm. Late changes go in by phone/WhatsApp and just get dropped (I1, I3, I4).
3. **Ad hoc shortage handling:** when an item runs short, whichever driver is on the ramp decides substitutions (I1, I6 — "not their job really"), or the baker splits it blind (I4). No one owns this decision.

None of these are a layers/spans problem — nothing in the nine interviews points to too many reporting layers or slow escalation. A regional manager would give stores someone to "fight for" them (I5, I9) but wouldn't change the cut-off, make the plan visible, or create an allocation rule. That's the classic trap of adding a management layer on top of a broken process and getting the same result with a new name.

**Recommended sequence (~8–12 weeks, low cost, no new headcount):** put the plan in the ERP → fix the cut-off/demand-timing mismatch → assign explicit shortage-allocation ownership → re-measure. Only then reconsider a coordination role, and test a single allocation coordinator before committing to four regional managers.

Flagged as weak evidence and excluded from the root-cause list: I2's and I7's "HQ doesn't listen" culture complaints — opinions, not examples. Also flagged as open questions: I8's offered store-level waste data, and why the 2pm cut-off was chosen in the first place (worth checking there isn't a hard production constraint behind it).


## Files in work dir after run

- case-operating-model-brightwell-bakeries.md
- com-03-input.md

## File written by the run: case-operating-model-brightwell-bakeries.md

# Operating model: Brightwell Bakeries, central bakery vs. stores — is a regional-manager layer the right fix?

**Answer:** The analysis contradicts the CEO's proposed fix. On the evidence in these nine interviews, the gap is caused by three unowned process/decision-rights problems the 2025 centralisation created — not by a missing management layer. Fix those first, in sequence, over roughly 8–12 weeks, before adding any new layer:
1. Make the bakery's production plan visible to stores (put it in the ERP, not the planner's personal drive).
2. Fix the mismatch between the 2pm order cut-off and when demand-relevant information (weather, train timetables) is actually known — either move it or add a bounded late-amendment window.
3. Give someone explicit ownership of shortage-allocation decisions, instead of leaving it to whichever driver is on the ramp.

Only re-examine whether stores need a dedicated coordination role once these are fixed and you have a cycle of data — and even then, test a lighter option (one allocation/planning coordinator) before committing to four regional managers.

**Confidence:** medium — the three root causes are each independently corroborated by two to three interviews across different roles (store managers, planner, baker, logistics, finance), but no data on the proposed fixes' cost/feasibility or on per-store waste exists yet (see Open questions).

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Run one central bakery serving all stores without the waste/stockout cost of losing local knowledge | Translate next-day store-level demand into the bakery's production plan, and feed that plan back to stores before they order | Waste ≤5% of production value; stockouts of top-10 items back toward the prior ~2/store/week | Waste 9.2% (Jan–Sep 2026) vs. 4.8% (2024); stockouts ~7/store/week vs. ~2 | Demand-relevant information arrives after the cut-off, and the resulting plan is invisible to stores — both degrade order accuracy |

## Root causes of the gap

| Gap | Process / system cause | Decision-rights cause | Structure cause | People / skills cause |
|---|---|---|---|---|
| Waste 4.8% → 9.2% | Plan sheet lives on the planner's personal drive, not the ERP; stores can't see it (I3, I8) and over-order "safe" as a result (I8) | Nobody has authorised sharing the plan — planner says he would if told he could (I3) | None found | None found |
| Stockouts ~2 → ~7/store/week | 2025 cut-off moved from 6pm to 2pm, earlier than when demand-driving facts are known (weather ~5pm per I2; train timetable per I5); late changes arrive by phone/WhatsApp and are dropped or handled off the books (I1, I3, I4) | Accepting late changes has no owner ("just get dropped," I1); allocating a short item across stores has no owner — defaults to the driver on the ramp (I1, I6) or an unguided split by the baker (I4) | None found | None found |
| "HQ doesn't listen" / "stores feel alone" (I2, I5, I7, I9) | Same visibility/feedback gap above — stores get no response when a change is dropped | Same — no owner for late changes or allocation | The CEO's regional-manager proposal targets this symptom directly | Possible, but evidence is opinion only (I2, I7) — treat as weak evidence, not a confirmed cause |

## Decision rights (key decisions)

| Decision | Decides today | Consulted | Executes | Gap |
|---|---|---|---|---|
| Accept or reject order changes after 2pm cut-off | No one | — | — | Unowned; requests are dropped with no feedback (I1, I3) |
| Share the production plan with stores | No one has authorised it | Planner would, if told he could (I3) | Planner, informally, not shared (I3) | Unowned; plan sits outside the ERP (I3, I8) |
| Allocate a short item across stores at delivery | Driver, by default | — | Driver (I6); sometimes head baker splits unguided (I4) | Unowned — "not their job really" (I6); no priority rule given to the baker (I4) |
| Set the order cut-off time | Set centrally in 2025 (who/why not evidenced) | Stores — objections from I2 and I5 suggest not consulted | — | Set without a tested link to when store-level demand data is actually available |

## Structure options

| Option | Description | Meets capability needs | Cost | Transition risk | Score |
|---|---|---|---|---|---|
| A. Fix process & decision rights, no new layer | Plan in ERP; cut-off redesign or amendment window; explicit allocation rule | High — targets both confirmed root causes directly | Low — IT/process change, no new headcount | Low | **Recommended now** |
| B. CEO's proposal: 4 regional managers, process unchanged | Add a layer between stores and HQ | Low/partial — does not touch cut-off timing, plan visibility, or allocation rule; at best gives stores someone to escalate to | High — 4 FTE ongoing, hiring/onboarding lead time | Medium — new reporting lines absorb management attention for months | Weak relative to cost |
| C. Fix process first; revisit a lighter coordination role later | Run Option A for one full cycle (4–8 weeks), then decide if a single allocation/planning coordinator (not 4 full regional managers) is still needed for cross-store trade-offs | High if A alone leaves a residual gap | Low now; contingent later | Low | Fallback if A proves insufficient |

*(Design criteria above — cost, capability fit, transition risk — are proposed; agree them with the CEO before using them to make the final call between B and C.)*

## Spans, layers, sourcing

- **Spans and layers:** no evidence in these nine interviews points to too many direct reports, too many layers, or escalation delay between stores and HQ. Every complaint traces to timing, visibility, or an unowned decision — a process/decision-rights gap, not a structure gap. The "structure" and "spans and layers" hypotheses are killed on this evidence.
- **Sourcing:** not in scope — no outsourcing question was raised by the interviews.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Publish the daily production plan in the ERP, visible to every store before ordering | Production planner + IT, sponsored by COO | ~4 weeks | Store managers confirm they see the plan before ordering; "safe" over-ordering starts dropping |
| 2 | Redesign the cut-off: keep a provisional lock at 2pm but add a bounded amendment window (e.g., to 5–6pm) for demand-sensitive stores (station, weather-exposed), or build a standard adjustment factor into the plan | COO + production planner + logistics lead | ~6–8 weeks | Top-10 stockouts trend down from ~7 toward ~2/store/week |
| 3 | Define and publish a shortage-allocation rule (who decides, on what basis — e.g. prior-week sell-through) so drivers and the night baker stop deciding ad hoc | Logistics lead + production planner | ~4 weeks | No driver-level substitution decisions; allocation disputes resolved by rule, not on the ramp |
| 4 | Re-measure waste and stockouts after one full cycle; decide then whether any coordination role is still needed | COO | +8–12 weeks from step 1 | Decision made on data, not on the "stores feel alone" sentiment alone |

## What would change the answer

1. If finance's offered store-level waste breakdown (I8) shows waste is *not* concentrated in stores lacking plan visibility, the visibility fix loses priority and the real driver needs re-diagnosing.
2. If, after steps 1–3 run for a full cycle, waste and stockouts do not improve, that would confirm a genuine cross-store coordination gap (e.g., structurally scarce items like rye creating recurring conflicts) that a dedicated — but likely single, not fourfold — allocation role may need to resolve.
3. If the 2pm cut-off was set because of a hard bakery production constraint (minimum baking lead time) rather than habit, the fix shifts from moving the cut-off to feeding better early demand signals into the plan instead (e.g., a standard weather/timetable adjustment factor).

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Timeline for fixes is flexible, not fixed by an external deadline | ~8–12 weeks total | Not stated by CEO/COO | A hard near-term deadline existed, forcing a faster (and likely costlier) interim fix |
| 2 | ERP can host/display the daily plan without major system work | Low cost, ~4 weeks | Not evidenced — I8 only confirms the plan sheet is *not* currently in the ERP | ERP change requires a larger IT project; cost/time estimate would need revision |
| 3 | The 2pm cut-off was a deliberate operational choice, not forced by a hard constraint | Treated as adjustable | No interview explains who set it or why | A production/logistics constraint makes 2pm non-negotiable (see "what would change the answer" #3) |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Store-level waste breakdown (I8 offered to share) | Confirms or kills the "safe-ordering stores lack plan visibility" causal link | Finance controller (I8) | Could redirect the waste fix if the pattern doesn't hold |
| Why was the cut-off moved to 2pm in 2025, and is there a hard production constraint behind it? | Determines whether the fix is "move the cut-off" or "feed better data into the existing cut-off" | Whoever decided the 2025 change (COO / production head) | Changes step 2 of the transition plan |
| Cost and lead time to get the plan sheet into the ERP | Needed to size step 1 properly | IT / production planner | Could raise Option A's cost estimate |
| Is rye (or similar) a recurring single-item shortage, or a one-off mentioned by I1? | If recurring, points to a supply/sourcing fix, not just an allocation rule | Production planner / procurement | Could add a fourth, supply-side workstream |
| Are I2's and I7's "HQ doesn't listen" / "culture" claims shared by others, or isolated opinions? | These are flagged as weak evidence (opinion, not examples) and excluded from the root-cause table | Broader staff survey or more interviews | Could add a genuine people/culture workstream if corroborated |

