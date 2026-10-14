# com-01-quote-speed on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Opens from the strategy requirement (standard quotes within one working day, win rate 22% to 30%) before any structure discussion. | NO | The answer's opening sentence is '**Recommendation: don't create the division.**' — a structural conclusion — before any statement of the strategy requirement; the explicit 22%→30% framing only appears later in the file's 'What the strategy requires' table, after the Answer/Confidence/Specialists se |
| Shows that waiting, not work, dominates (about 5 of 6 days) and that most waiting sits in approvals and the pricing queue. | yes | '5.0 of the current 6.0 median quote-days (83%) are pure waiting, concentrated in MD, Finance and Legal reviews' plus '2.0 days pure queue wait in central pricing'. |
| Identifies that approvals happen on every quote although written rules limit them to quotes above EUR 250k or non-standard terms. | yes | 'that the decision map shows hit **every** quote even though the written rules only require them for ~30% of volume (above EUR 250k, non-standard terms)'. |
| Recommends explicit decision rights for the key decisions. | yes | Decision rights table: 'Pricing team, no MD sign-off needed' for standard quotes, Finance only beyond 30 days, Legal only for non-standard via pre-cleared template, and 'Needs a single named owner' for post-sign customer ownership. |
| Shows the process/decision-rights fix reaches about one day for standard quotes without the new division, keeping the division as one option with its cost (EUR 3.2m) and transition risk. | yes | 'closes most of the win-rate gap... without the new division' and Option B retained in the structure table with 'EUR 3.2m/yr recurring' cost and 'High' transition risk. |
| Two or three options scored against criteria agreed before scoring (or proposed criteria flagged for agreement). | NO | The Structure options table scores A/B/C against 'Meets capability needs / Cost / Transition risk / Score' but nowhere flags these criteria as needing CEO/stakeholder agreement before scoring. |
| Treats the win-rate link as an association to monitor, not proof. | yes | 'the hypothesis that speed drives win rate (34% vs 17%) may be confounded by deal size or customer type, and the root-cause branch needs reopening' and sizing is labeled '(assumption-based, label below)'. |
| Names the soft elements to change (MD incentives/habits, pricing team capacity) and a sequence with dates. | yes | 'Main risk is behavioral — whether MDs/Finance/Legal actually stop reviewing every quote once told to' and transition plan with dated steps (Month 1, Month 2, Month 2-3, Month 3-4, Month 9-12). |
| Answer line states what changes, in what sequence, by when. | yes | 'Sequence: (1) 0–1 month, CEO mandates... (2) 1–3 months... (3) 3–6 months... (4) 6–12 months, re-assess...' |
| Must not recommend the Key Account division as the first move. | yes | 'Recommendation: don't create the division' — division is explicitly rejected as the first move. |
| Must not invent peer spans, peer quote times or industry win rates. | yes | 'no peer benchmark for pricing-analyst headcount vs. quote volume was available to confirm capacity is adequate' — explicitly flags absence rather than inventing figures. |

## Transcript

## Turn 1

**User:** Kestrel wants faster quotes to win key accounts. The sales director proposes a new Key Account division. Work the operating model case from the diagnostic pack; answer page for the CEO. (Attached in the working directory: com-01-input.md.)

## Answer page: Kestrel Logistics, Key Account division decision

**Recommendation: don't create the division.** 5.0 of the current 6.0 median quote-days (83%) are pure waiting, concentrated in MD, Finance and Legal reviews that the decision map shows hit **every** quote even though the written rules only require them for ~30% of volume (above EUR 250k, non-standard terms). The actual hands-on work across the whole process is 1.0 day — already inside the 1-day target. This is a decision-rights enforcement and queue-triage problem, not a capability or structure problem, so a 40 FTE / EUR 3.2m-a-year division doesn't fix it — and it's organized around customer segment (key accounts) while the bottleneck is organized around deal type (standard vs. non-standard).

**Recommended fix instead, sequenced over 3-4 months at a fraction of the cost:**
1. CEO mandates that standard quotes skip case-by-case MD/Finance/Legal sign-off, moving to spot-audit
2. Legal pre-clears a standard-terms template; Finance moves to exception review
3. Pricing reallocates 2 of its 7 analysts into a fast lane with a 1-day SLA, piloted in 1-2 regions first
4. Name a single owner for post-sign customer relationships (a separate, real decision-rights gap the pack surfaces)
5. Re-assess after 6-12 months whether any dedicated key-account structure is still needed, sized against whatever gap remains

Rough sizing suggests this alone could get win rate close to the 30% target (speed-to-win data: ≤2 days wins at 34%, ≥5 days at 17%), without the new division. Main risk is behavioral — whether MDs/Finance/Legal actually stop reviewing every quote once told to — which is why a short regional pilot comes before full rollout.

Full answer page with the decision-rights table, root-cause analysis, structure-option comparison, transition plan, assumptions and open questions is written to `case-operating-model-kestrel.md` in the working directory.


## Files in work dir after run

- case-operating-model-kestrel.md
- com-01-input.md

## File written by the run: case-operating-model-kestrel.md

# Operating model: Kestrel Logistics, how to hit the 1-day standard-quote target and 30% win rate — and whether the Key Account division does it

**Answer:** Do not create the Key Account division as proposed. 5.0 of the current 6.0 median quote days (83%) are pure waiting, concentrated in three approval steps (Regional MD, Finance, Legal) that the decision map shows are applied to *every* quote even though the written rules reserve them for roughly 30% (above EUR 250k, non-standard terms). Fix decision-rights enforcement and the central-pricing queue first — both fixable in weeks, at a fraction of EUR 3.2m/year — then re-measure before building any new structure. Sequence: (1) 0–1 month, CEO mandates that standard quotes bypass case-by-case MD/Finance/Legal sign-off and triage a fast lane in the existing pricing team; (2) 1–3 months, route standard quotes automatically to that lane and track speed and win rate; (3) 3–6 months, assign a single named owner for post-sign customer relationships; (4) 6–12 months, re-assess whether a dedicated key-account unit is still needed, and at what size.

**Confidence:** medium-high — the process-walk data is unambiguous that the delay is approval queueing, not work content; what's unverified is whether MDs, Finance and Legal will actually stop reviewing every quote once told to (a behavioural/governance risk, not a data gap). A one-region pilot would settle it in 4–6 weeks.

**Specialists and review:** Legal should pre-clear the standard-terms contract template before Legal review is waived on standard quotes; HR/works council input if the fast-lane reallocation changes reporting lines or roles. No valuation or deal-pricing specialist needed for this question.

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Win mid/large shippers with fast, reliable quotes | Standard-quote turnaround | ≤1 working day | 6.0 days median (1.0 day hands-on work) | 5.0 days, entirely non-work elapsed time |
| Win rate 22% → 30% by end 2027 | Speed-to-win linkage already evidenced | +8pp | Quotes answered ≤2 days win at 34%; ≥5 days win at 17% | Shifting the 70% "standard" volume into the fast bucket plausibly closes most of the gap (see sizing below) |

## Root causes of the gap

| Gap | Process / system cause | Decision-rights cause | Structure cause | People / skills cause |
|---|---|---|---|---|
| 6.0 days vs. 1-day target | 2.0 days pure queue wait in central pricing (0 hands-on work) — a capacity/triage problem, not a skill gap | **Primary cause.** MD approval (1.5 days elapsed, 0.1 work), Finance approval (1.0 day, 0.1 work) and Legal check (0.5 day, 0.2 work) total 3.0 of the 6.0 days, applied to 100% of quotes although written rules scope them to ~30% (>EUR250k, terms >30 days, non-standard terms) | Proposed division is organised by customer segment (key accounts); the bottleneck is organised by deal type (standard vs. non-standard). A customer-segment unit does not, by itself, fix a deal-type problem — see Structure options below | Universal sign-off behaviour looks like risk-aversion covering for an unclear post-sign ownership split (sales vs. regional ops, "not written") — flagged, needs interview confirmation, not proven by the data given |

**Capability hypothesis: killed.** Hands-on work across the whole process is 1.0 day — already inside the 1-day target. The organisation does not lack the skill or capacity to do the work; it loses 5 days to queueing and approvals that mostly re-confirm decisions the written rules already delegate. This rules out "we need new capability" (and the new division's stated rationale — dedicated pricing/solutions/contract skill) as the fix.

**Spans and layers: killed as a cause.** Central pricing (1 head, 7 analysts) and sales (6 regional managers, 4–5 KAMs each) show no span or layering problem on the data given; the queue delay is a capacity/prioritisation issue inside a reasonably-sized team, not a structural layering issue. *(Flagging as an assumption: no peer benchmark for pricing-analyst headcount vs. quote volume was available to confirm capacity is adequate once properly triaged — see Open questions.)*

## Decision rights (key decisions)

| Decision | Written rule | Should decide (per rule) | Today (actual) |
|---|---|---|---|
| Approve price, standard quote (≤EUR250k, standard lanes/terms, ~70% of volume) | MD approves only above EUR250k | Pricing team, no MD sign-off needed | Regional MD approves every quote; pricing will not release without it |
| Approve price, non-standard/large quote (~30% of volume) | MD approves above EUR250k | Regional MD | Regional MD (correct) |
| Approve payment terms ≤30 days | Finance approves only beyond 30 days | Pricing/sales, no Finance sign-off needed | Finance reviews every quote |
| Approve payment terms >30 days | Finance approves | Finance | Finance (correct) |
| Check standard terms | Legal approves deviations | Sales/pricing, via pre-cleared template, no Legal touch | Legal checks every quote including standard terms |
| Check non-standard terms | Legal approves | Legal | Legal (correct) |
| Own customer after signing | Not written | Needs a single named owner | Sales and regional operations both claim it — disputed |

This is a decision-rights **enforcement** problem, not a design problem: the written thresholds are already roughly right-sized for the 70/30 standard/non-standard split the operations team found. The fix is to make the existing delegation stick (remove the pricing team's informal policy of blocking release without MD sign-off, move Finance/Legal to exception-based review, replace case-by-case clearance with spot-audits), not to redesign who owns what.

## Structure options

| Option | Description | Meets capability needs | Cost | Transition risk | Score |
|---|---|---|---|---|---|
| A. Status quo | No change | No — misses target by 5 days | EUR 0 | None, but strategy fails | Low |
| B. Key Account division (sales director's proposal) | ~40 FTE, EUR 3.2m/yr, own pricing/solutions/contract team, reports to CEO | Partial, and only for the subset of volume classed "key account" — does not by itself change the universal MD/Finance/Legal sign-off behaviour unless the new unit is explicitly granted sign-off authority (not stated in the proposal); organised by customer segment, not by the deal-type split that actually drives delay | EUR 3.2m/yr recurring | High — new reporting line into CEO, 40 hires/transfers, a third claimant on post-sign customer ownership alongside sales and regional ops | Low-medium |
| C. Decision-rights enforcement + pricing fast lane (recommended) | CEO-mandated delegation that actually holds for standard quotes; dedicated fast-lane cell inside existing pricing team (2 of the 7 analysts, reallocated not added); Legal pre-clears a standard-terms template; Finance moves to exception review; named single owner for post-sign relationships | Yes for the 1-day target on the 70% standard volume; closes most of the win-rate gap (see sizing) | Low one-off cost (process redesign, routing/systems change, template legal work) — materially under EUR 3.2m/yr; no new recurring headcount cost | Low-medium — main risk is behavioural (will MDs/Finance/Legal actually stop reviewing every quote), mitigated by a 1-2 region pilot before full rollout | High |

**Sizing the win-rate case for Option C** *(assumption-based, label below)*: if the 70% standard volume moves from ~6 days to ~1 day and performs at least as well as the current ≤2-day bucket (34% win), and the 30% genuinely complex volume stays near the current slower-bucket rate (~17–20%), blended win rate ≈ 0.7×34% + 0.3×18% ≈ 29%— close to the 30% target, from the process/decision-rights fix alone, without the new division.

## Spans, layers, sourcing

- Spans and layers: no change needed to sales (6 managers / 4-5 KAMs) or pricing (1 head / 7 analysts) reporting structure; reallocate 2 of the 7 pricing analysts into a standard-quote fast lane with an SLA, rather than adding 40 FTE.
- Sourcing: not applicable — quoting, pricing and contracting are core to how Kestrel competes; nothing here should be outsourced.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | CEO mandate: standard quotes (≤EUR250k, standard lanes/terms) skip case-by-case MD/Finance/Legal sign-off; move to spot-audit | CEO + Regional MDs, Finance, Legal heads | Within 1 month | Written policy issued; pricing team stops requiring MD sign-off to release |
| 2 | Legal pre-clears a standard-terms contract template | Legal | Within 1 month | Template signed off |
| 3 | Pricing team sets up a 2-analyst fast lane with a 1-day SLA for standard quotes; sales intake routes standard quotes directly to it | Head of Pricing | Within 2 months | Standard-quote median cycle time measured weekly |
| 4 | Pilot in 1–2 regions before full rollout | Regional MD(s) + Head of Pricing | Month 2–3 | Pilot median ≤1.5 days, win rate tracked |
| 5 | Full rollout if pilot holds; name single owner for post-sign customer relationship | CEO | Month 3–4 | Median standard-quote cycle ≤1 day; ownership dispute resolved |
| 6 | Re-assess need for a dedicated key-account structure, and at what size, against actual volume and any remaining gap | CEO + Sales director | Month 9–12 | Win rate trend vs. 30% target; residual gap, if any, sized before any new unit is built |

## What would change the answer

1. If the pilot shows MDs/Finance/Legal cannot be made to stop reviewing every quote even under a CEO mandate (a genuine governance/trust failure, not just inertia), the fix shifts from a policy change to a structural one — at that point a smaller, targeted fast-lane team with its own delegated sign-off authority (not a 40 FTE division) becomes the next option to test.
2. If the 30% non-standard volume is where most key-account revenue sits and those quotes have their own distinct bottleneck not captured in this data (e.g. multi-party negotiation, custom solutioning), a dedicated key-account capability may still be justified — but sized against that specific gap, not against the quote-speed problem this pack documents.
3. If post-pilot data shows win rate does not move toward 30% even once speed hits 1 day, the hypothesis that speed drives win rate (34% vs 17%) may be confounded by deal size or customer type, and the root-cause branch needs reopening.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Standard quotes answered in ~1 day will win at least at the ≤2-day rate (34%) | 34% (floor) | Linear extrapolation from the two given speed buckets (≤2 days: 34%, ≥5 days: 17%); no data point at exactly 1 day | Actual 1-day win rate is materially lower (e.g. quotes rushed lose quality) |
| 2 | Non-standard (30%) volume's win rate stays near the current slow-bucket rate (~17–20%) after the fix | 18% | The 30% non-standard volume continues to need genuine MD/Finance/Legal review, so its speed and win rate are assumed largely unchanged | Genuine review time for non-standard quotes can also be compressed, which would push the blended win rate above 30% |
| 3 | Fast-lane one-off transition cost is well under EUR 3.2m/yr | "Low one-off cost" (no hard figure given in the pack) | No cost data provided for process/systems/template work; order-of-magnitude judgement only | Systems/routing changes turn out to require a large IT project |
| 4 | Pricing team has spare capacity once a fast lane is triaged out of the queue | 2 of 7 analysts reallocated, no new hires | Analyst headcount given (7); no workload/capacity data provided | Analyst capacity is already fully loaded and 2.0-day queue reflects genuine overload, not just lack of triage |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Why do Regional MDs, Finance and Legal review every quote when the written rule doesn't require it (risk aversion, lack of trust in the pricing team, no consequence for being wrong, unclear accountability)? | Determines whether this is a quick policy fix or a deeper trust/incentive problem needing more than a memo | Interviews with the 9 people already consulted (sales, pricing, finance, 2 regional MDs) — operations excellence team can extend the existing interview set | If the root cause is accountability/trust rather than habit, Option C's "mandate + spot-audit" may need a stronger control mechanism (e.g. post-hoc sampling with real consequences) before MDs will let go |
| Is central pricing's 2.0-day queue genuine capacity overload or lack of triage between standard and complex quotes? | Decides whether 2 reallocated analysts are enough, or more capacity is needed | Head of central pricing (workload/queue data) | If overload, Option C needs added capacity, raising its cost (still almost certainly below EUR 3.2m/yr, but not zero) |
| Who should own the customer after signing — sales or regional operations — and why is it undefined today? | A live decision-rights gap, independent of quote speed, that the new division would not resolve and could worsen by adding a third claimant | CEO, with sales and regional operations heads | Needs its own decision regardless of which quoting fix is chosen; should not wait on the quote-speed fix |
| Does "key accounts" (customer segment) overlap with "standard quotes" (deal characteristics, 70% of volume), or are these largely different sets of quotes? | If key accounts' quotes are mostly non-standard (large, complex), a customer-segment division is solving a different problem than the one this pack diagnoses | Sales director / pricing team (quote data by account size and standard/non-standard flag) | If key accounts' quotes are mostly standard, this strengthens the case that the real fix is the fast lane, not a new division; if mostly non-standard, the sales director's proposal targets a real but differently-shaped problem than the one in this pack |

