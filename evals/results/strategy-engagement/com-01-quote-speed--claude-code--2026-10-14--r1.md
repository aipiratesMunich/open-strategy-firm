# com-01-quote-speed on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (10/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Opens from the strategy requirement (standard quotes within one working day, win rate 22% to 30%) before any structure discussion. | NO | Both the chat headline and the file's Answer section open with 'Don't approve the 40-FTE / EUR 3.2m/year Key Account division yet...' — a structural recommendation — before any mention of the 1-day target or the 22%→30% win-rate goal, which only appears later in the 'What the strategy requires' tabl |
| Shows that waiting, not work, dominates (about 5 of 6 days) and that most waiting sits in approvals and the pricing queue. | yes | '6.0 days median (1.0 day hands-on, 5.0 days waiting)' and breakdown '1.5 days at regional MD... 1.0 day at finance... 0.5 day at legal... 2.0 days waiting in central pricing queue' = 5.0 days. |
| Identifies that approvals happen on every quote although written rules limit them to quotes above EUR 250k or non-standard terms. | yes | 'Written rule: MD approves only above EUR 250k. Practice: MD approves every quote'; same pattern stated for finance (30-day terms) and legal (deviations). |
| Recommends explicit decision rights for the key decisions. | yes | Decision rights table: 'MD only above EUR 250k; below that, pricing team releases directly against policy'; 'Finance only beyond 30 days'; 'Legal only on actual deviations'; and a recommendation to 'Write it down explicitly (e.g., sales/KAM owns the commercial relationship, regional operations owns  |
| Shows the process/decision-rights fix reaches about one day for standard quotes without the new division, and keeps the division as one option with its cost (EUR 3.2m) and transition risk. | yes | Headline: 'reaching close to the board's 1-day target for standard quotes within one quarter, at near-zero run-rate cost'; Option C row lists 'EUR 3.2m/yr recurring' and 'Transition risk: High'. |
| Two or three options scored against criteria agreed before scoring (or proposed criteria flagged for agreement). | yes | 'Scoring criteria below are proposed by this analysis, to agree with the CEO before final scoring: (1)...(4)...' followed by scored options A, B, C (D explicitly deferred: 'To be scored after the Option B pilot'). |
| Treats the win-rate link as an association to monitor, not proof. | yes | Assumption #3: 'Directional extrapolation from the two given buckets... would change the answer if: The ≤2-day bucket is dominated by deals that were already easy to win regardless of speed (reverse causality)'. |
| Names the soft elements to change (e.g. MD incentives or habits, pricing team capacity) and a sequence with dates. | yes | 'the sign-off habit causing the delay' is referenced repeatedly, and the Transition plan table sequences steps with dates like 'Within 4-6 weeks' and 'Within 8-10 weeks' and owners. |
| Answer line states what changes, in what sequence, by when. | yes | 'First enforce the decision rights... and open a fast lane... Pilot in 2 regions for a quarter; only then decide if a smaller, dedicated team is needed.' |
| Does not recommend the Key Account division as the first move. | yes | 'Do not approve the 40-FTE / EUR 3.2m/year Key Account division yet.' |
| Does not invent peer spans, peer quote times or industry win rates. | yes | No peer-company, industry benchmark, or external win-rate figures appear anywhere in the transcript. |

## Transcript

## Turn 1

**User:** Kestrel wants faster quotes to win key accounts. The sales director proposes a new Key Account division. Work the operating model case from the diagnostic pack; answer page for the CEO. (Attached in the working directory: com-01-input.md.)

Answer page written to `case-operating-model-kestrel.md`. Headline for the CEO:

**Don't approve the 40-FTE / EUR 3.2m/year Key Account division yet.** The diagnostic shows the 6-day median quote cycle is almost entirely a decision-rights and queueing problem, not a missing structure:

- Regional MD, finance and legal each have written approval thresholds (EUR 250k, >30-day terms, deviations only) — but in practice all three review **every** quote, standard or not. That's 3.0 of the 6.0 days, for the 70% of quotes that shouldn't need any of this sign-off.
- The remaining 2.0-day wait is sitting in the central pricing team's queue — but a back-of-envelope capacity check (120 quotes over ~65 working days, 0.5 day hands-on each, 7 analysts) puts that team at roughly **13% utilisation** on pricing work. It's a triage problem, not a staffing shortfall.

So the smallest fix — enforce the thresholds that already exist on paper, and carve a same-day fast lane out of the existing pricing team — plausibly gets standard quotes near the board's 1-day target at close to zero run-rate cost, versus EUR 3.2m/year recurring for a division that doesn't itself change the override habit causing the delay. I'd pilot that in two regions for a quarter before considering any new structure, and even then only size something much smaller than 40 FTE for the genuinely complex 30%.

Biggest open question: *why* do MDs/finance/legal override the thresholds today — if it's catching real risk, the fix is different; if it's habit, enforcing the policy is safe. That's listed as the top item to test before acting.


## Files in work dir after run

- case-operating-model-kestrel.md
- com-01-input.md

## File written by the run: case-operating-model-kestrel.md

# Operating model: Kestrel Logistics, does a new Key Account division get standard quotes to 1 working day?

**Answer:** Do not approve the 40-FTE / EUR 3.2m/year Key Account division yet. First enforce the decision rights Kestrel already has on paper and open a fast lane in the existing 8-person central pricing team for the 70% of quotes that are "standard" (below EUR 250k, standard lanes and terms). That alone removes 3.0 of the 6.0 median days (regional MD, finance and legal each re-approving quotes the written rules say they shouldn't touch) and lets a retimed pricing step close most of the rest — reaching close to the board's 1-day target for standard quotes within one quarter, at near-zero run-rate cost, versus EUR 3.2m/year recurring for a division that does not by itself fix the sign-off habit causing the delay. Pilot in 2 regions for a quarter; only then decide if a smaller, dedicated team is needed for the complex 30%.

**Confidence:** medium, because the time-and-queue arithmetic rests on the traced 120-quote data, but *why* regional MDs, finance and legal override the written thresholds on every quote is not yet tested — that determines whether removing the sign-off is safe or removes a control that is catching real problems (see Open questions, #1).

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Win rate 22%→30% by end-2027 via faster quotes | Standard-quote turnaround | ≤1 working day, board target | 6.0 days median (1.0 day hands-on, 5.0 days waiting) | 5 days of pure queueing/waiting, on a process that takes 1 day of actual work |
| Reliable quotes on complex/large deals | Risk-appropriate review (pricing, credit terms, legal deviations) | Full review only where the deal is genuinely non-standard | Full review applied to 100% of quotes regardless of value or terms | Review capacity spent on the 70% of quotes that do not need it |

## Root causes of the gap

| Gap | Process / system cause | Decision-rights cause | Structure cause | People / skills cause |
|---|---|---|---|---|
| 1.5 days at regional MD step | Quote sits in an approval queue with a single sign-off gate | Written rule: MD approves only above EUR 250k. Practice: MD approves every quote; pricing team won't release without it | — | Not tested — see Open Q1 |
| 1.0 day at finance | Same pattern | Written rule: finance approves only terms beyond 30 days. Practice: finance reviews every quote | — | Not tested — see Open Q1 |
| 0.5 day at legal | Same pattern | Written rule: legal approves only deviations from standard terms. Practice: legal checks every quote, including standard terms | — | Not tested — see Open Q1 |
| 2.0 days waiting in central pricing queue | No fast lane; standard and complex quotes processed FIFO; hands-on pricing work is only 0.5 day | — | Single central team (1 head, 7 analysts) with no triage by quote complexity | Team's real workload appears far below capacity (~13% utilisation, see Spans/layers below) — queue looks like a triage design problem, not a staffing shortfall |

None of this traces to the sales/regional structure itself — the 6 regional sales managers and their 4-5 KAMs each are not named anywhere in the diagnostic as a bottleneck. The bottleneck is entirely in approval hand-offs after the quote leaves sales.

## Decision rights (key decisions)

| Decision | Written rule | Decides today (in practice) | Recommended |
|---|---|---|---|
| Approve price | MD above EUR 250k | MD on every quote | MD only above EUR 250k; below that, pricing team releases directly against policy, spot-audited after the fact |
| Approve payment terms | Finance beyond 30 days | Finance on every quote | Finance only beyond 30 days; standard terms use a pre-approved template, no case-by-case check |
| Approve terms deviation | Legal on any deviation | Legal on every quote, including standard terms | Legal only on actual deviations; standard-terms quotes close against pre-approved legal language |
| Who owns the customer after signing | Not written | Disputed — sales and regional operations both claim it | Write it down explicitly (e.g., sales/KAM owns the commercial relationship, regional operations owns delivery); see Open Q3 — this ambiguity is a plausible driver of MDs' instinct to control the quote stage since they have no clear claim post-sign |

## Structure options

*Scoring criteria below are proposed by this analysis, to agree with the CEO before final scoring: (1) gets standard quotes (70% of volume) to ≤1 working day by end-2027, (2) run-cost, (3) transition risk/disruption, (4) addresses the full 70% standard-quote population the board target is about, not a subset.*

| Option | Description | Meets capability needs | Cost | Transition risk | Score |
|---|---|---|---|---|---|
| A. Status quo | No change | No — stays at 6.0 days | EUR 0 | None | Low |
| B. Enforce decision rights + fast lane (recommended) | Reissue thresholds as binding; redeploy 2 of 7 existing pricing analysts into a same-day fast lane for standard quotes; spot-audit instead of pre-approve | Yes, for the 70% standard population, if the queue retimes as the utilisation math suggests | ~EUR 0 run-rate; one-off tooling for rule-based/self-service pricing, ASSUMPTION EUR 150k-300k | Medium — depends on MDs/finance/legal actually letting go of the sign-off habit | High |
| C. Sales director's Key Account division (40 FTE, EUR 3.2m/yr) | New division with own pricing, solutions and contract team, reporting to CEO | Uncertain — duplicates an existing pricing function that is ~13% utilised on pricing-calc work, and only covers "key accounts," not necessarily the full 70% standard-quote population the target is measured against (Open Q4); doesn't itself change the MD/finance/legal override habit unless the new unit is given real autonomy | EUR 3.2m/yr recurring | High — new reporting line to CEO, likely reopens the same "who approves/who owns the customer" disputes with regional MDs in a new form | Medium-low |
| D. Hybrid fallback | Small dedicated solutions/contract team, sized only for the complex 30% of quotes that genuinely need bespoke handling, layered on top of B | Addresses the segment where full review is legitimate | Lower than C — scoped to ~30% of volume, size TBD after pilot | Lower than C — adds, doesn't replace, existing teams | To be scored after the Option B pilot |

## Spans, layers, sourcing

- **Pricing team capacity check:** 120 quotes traced over roughly 13 weeks (~65 working days) ≈ 1.85 quotes/working day. Pricing hands-on time is 0.5 day/quote, so required capacity ≈ 0.92 analyst-days/day. Against 7 analysts, that is roughly 13% utilisation on pricing-calc work. ASSUMPTION: even arrival rate and no major non-quote workload (flagged below) — but directionally, the 2.0-day queue looks like a triage/process design problem, not an under-resourced team. This argues against adding a parallel 40-FTE pricing capability (Option C) and for retriaging the existing team (Option B).
- **Sales spans:** 6 regional sales managers, 4-5 KAMs each — nothing in the diagnostic traces delay to this layer; leave unchanged.
- **Sourcing:** not in scope here — all steps (pricing, approval, legal) are core to winning and are not commodity activities a partner should run.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Interview MDs, finance and legal on why they override the written thresholds; reissue thresholds as binding with a compliance dashboard | COO / CEO | Within 4-6 weeks | Override reasons documented; policy reissued |
| 2 | Redeploy 2 of 7 pricing analysts into a same-day fast lane for standard quotes; pilot in 2 regions | Head of central pricing | Within 8-10 weeks | Fast-lane SLA live in pilot regions |
| 3 | Measure cycle time and win rate for standard quotes, pilot vs. control regions | Sales ops | One quarter after pilot start | Standard-quote median at or near 1 day; win-rate movement vs. control |
| 4 | Resolve post-signing account ownership in writing (parallel to step 1) | CEO / sales director / regional MDs | Within 4-6 weeks | Written, communicated ownership rule |
| 5 | National rollout decision; only then size Option D for the complex 30% if step 3 shows the existing teams still can't cover it | CEO | After step 3 data | Go/no-go with sizing, if needed |

## What would change the answer

1. If the interviews in step 1 show MDs, finance or legal are catching real pricing, credit or legal errors on standard quotes that the thresholds miss, the control should stay and cycle time must be cut another way (e.g., parallel rather than sequential review), not removed — and Option B's savings shrink.
2. If pricing analysts' true workload includes substantial non-quote duties not captured in the 120-quote trace, the 13% utilisation estimate is wrong and the fast lane needs added headcount, which changes the cost comparison with Option C.
3. If win rate at ≤1 day turns out materially lower than the ≤2-day bucket (34%), the case for cutting the review chain purely for speed weakens relative to the risk it removes.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Quote volume is roughly even over the trace window | 120 quotes / ~65 working days ≈ 1.85/day | Quote-walk data (120 quotes, Jul-Sep 2026) | Arrival is bursty (e.g., month-end spikes) — utilisation would need recalculating on peak load, not average |
| 2 | Fast-lane/self-service pricing tooling cost | EUR 150k-300k one-off | Analogy to typical rule-based quoting tool builds — NOT from client data | Existing systems already support rule-based auto-pricing (cost much lower) or need custom integration (cost higher) |
| 3 | Win rate at ≤1 day is at least as good as the ≤2-day bucket | ≥34% | Directional extrapolation from the two given buckets (34% at ≤2 days, 17% at ≥5 days) | The ≤2-day bucket is dominated by deals that were already easy to win regardless of speed (reverse causality) |
| 4 | "Standard" quotes (below EUR 250k, standard lanes/terms) are the same population exempt from MD/finance/legal sign-off under the written rules | 70% of volume | Both references in the pack use the EUR 250k / standard-terms language | The sign-off thresholds and the "standard" quote definition turn out to use different criteria in practice |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| 1. Why do regional MDs, finance and legal override the written thresholds and review every quote? | Determines whether the control is safe to relax or is catching real risk | MDs, finance, legal (interviews) | If risk-driven: keep a lighter-touch check, don't fully remove it. If habit/visibility-driven: safe to enforce thresholds as written |
| 2. What is Kestrel's current blended win rate, and how does it break down by speed bucket beyond ≤2 days / ≥5 days? | Confirms the 1-day target actually closes enough of the 22%→30% gap | Sales ops | May show the speed fix alone is insufficient and other levers (pricing, terms) are also needed |
| 3. Who should own the customer relationship after signing — sales/KAM or regional operations? | Resolves a live turf dispute that plausibly feeds MDs' instinct to control the quote stage | CEO, sales director, regional MDs | Fixing this may reduce MD override behaviour on its own, independent of the policy reissue |
| 4. Does the sales director's Key Account division proposal cover the full 70% standard-quote population, or only a defined subset of large/strategic accounts? | Determines whether Option C could ever be sized to hit the board's actual target, or structurally addresses a smaller problem than the one diagnosed | Sales director | If it's a subset, Option C cannot deliver the board's standard-quote target by itself regardless of its internal efficiency |
| 5. What non-quote work occupies the 7 pricing analysts' time? | Tests whether the ~13% utilisation estimate is realistic or whether a fast lane needs added headcount | Head of central pricing | If analysts are already near capacity on other work, Option B needs a cost line for added headcount, narrowing the gap with Option C |

