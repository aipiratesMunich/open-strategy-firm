# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes | yes | **Verdict:** Release with fixes |
| No Blocker findings | yes | All findings table entries are labeled 'Major' or 'Minor'; no 'Blocker' severity appears |
| Every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo | yes | e.g. Finding 1: 'the "revisit the target" ask is sized on an optimistic assumption'; Finding 5: 'the year-4 payback claim is wrong'; catering math cross-check (1.6/2.1/2.5/2.7 × 32% − 0.35 = 0.16/0.32/0.45/0.51, cumulative 0.93/1.44) matches reference values exactly |
| Names what is good and must survive | yes | Section 'What is good and must survive' lists six specific strengths (clear ask, triangulated estimate, verified payback math, benchmarked growth assumption, falsifiable kill criteria, honest gap framing) |
| Must not demand a named framework, more length, or more slides | yes | All fixes are narrow additions (one sentence, one footnote, one calc) with no mention of frameworks, length, or slide count |
| Must not flag the stated uncertainty or explicit assumptions as weaknesses | yes | Review praises the falsifiable kill criteria as 'rare and worth keeping' rather than penalizing them; Finding 1 criticizes treating a contingent decision as realized in a headline number, not the memo's honesty about uncertainty |
| Must not claim numbers do not tie when they actually do (per reference list) | yes | The only 'Numbers that do not tie' entry concerns the delivery EUR 2.4m figure lacking a shown bridging calculation — distinct from the catering/gap figures in the reference list, which the review explicitly confirms 'verifies exactly' |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: "Fund corporate catering and a delivery pilot in 2027," gate 3

**Verdict:** Release with fixes
**In one line:** The core recommendation is sound and the catering payback math ties exactly, but the memo treats a not-yet-approved delivery rollout as already-realized revenue in its headline gap figure, and skips the capacity, pilot-payback, and floor-rationale checks a CEO will reasonably ask about before tomorrow's board meeting.

**Question the draft must answer:** Should Brightwell fund a corporate catering unit and a delivery pilot in 2027, decline suburban expansion/franchising, and how should the board resolve the resulting gap to the 2031 target? (given)
**Answer the draft gives:** Yes to catering (EUR 1.2m) and delivery pilot (EUR 0.3m), no to suburban/franchising, and recommends revisiting the 2031 revenue target rather than the margin floor.

These match — the memo answers its own question directly and gives a clear position on the secondary ask.

## Findings
| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | Skeptical CFO | "What it adds up to" | The EUR 2.4m delivery figure in the EUR 12.7m gap calc assumes the pilot succeeds *and* a future, not-yet-taken board decision to fund the EUR 0.6m rollout — but it's counted as realized. | The board revisits the 2031 target against a gap that's smaller than it really is if the rollout decision doesn't happen; the "revisit the target" ask is sized on an optimistic assumption. | Show the gap under a "pilot only, rollout not yet approved" scenario alongside the base case. |
| 2 | Major | Skeptical CFO | "Why a delivery pilot" | Catering gets a full profit/payback build (0.16/0.32/0.45/0.51m); the EUR 0.3m delivery pilot gets only revenue and per-order contribution, no payback. | CEO is asked to fund the pilot without seeing whether or when it pays back, unlike the parallel catering ask. | Add a one-line payback calc: 38 orders/day × 8 stores × EUR 3.10 × 365 vs. EUR 0.3m spend. |
| 3 | Major | Logician | "Why a delivery pilot" / "What would change our view" | Scale-up threshold is 60 orders/day; kill threshold is below 50. The 50–59 zone has no stated rule. | At month six, Head of Digital has no decision rule for the most likely outcome band. | State what happens in the 50–59 range (extend, partial rollout, etc.). |
| 4 | Major | Evidence Auditor | "Why not suburban stores or franchising" | Claim that 6–8% royalty cuts margin below the 14% floor doesn't show the baseline margin or the calculation. | Board can't verify the "why not franchising" conclusion, the weakest-evidenced part of the memo by the memo's own later admission. | State the current margin for franchise-candidate stores and show royalty-adjusted margin vs. floor. |
| 5 | Major | Skeptical CFO | "Why catering" | No statement of the central kitchen's production capacity against ~3x volume growth implied by the EUR 2.9m 2031 case. | If EUR 1.2m kitchen can't physically scale that far, the year-4 payback claim is wrong. | State designed capacity (orders/day or revenue ceiling) and confirm it covers the 2031 base case. |
| 6 | Major | Logician | Header / "What it adds up to" | The 14% floor is used to reject suburban/franchising, and is itself one of the two things decision (2) asks the board to revisit — but its origin is never stated. | Board can't judge whether revisiting the floor is safe without knowing what it protects (covenant? policy? historical average?). | Add one sentence on the floor's origin and what's at risk if it moves. |
| 7 | Minor | Outsider | Throughout | Three different margin concepts ("contribution margin" 32%, per-order contribution EUR 3.10, "store margin" 13.1%/14%) are used without distinguishing them. | A first-time reader may conflate measures when comparing initiatives. | One footnote defining each margin term. |
| 8 | Minor | Evidence Auditor | "Why catering" | 12 interviews (9 citing delivery pain) is thin colour evidence, though not load-bearing for the revenue estimate itself. | Low risk — not used quantitatively — but could be over-cited later. | Label as directional context if reused in the board deck. |

## Numbers that do not tie
| Number | Location A | Location B | Difference |
|---|---|---|---|
| Delivery EUR 2.4m (2031) | "Why a delivery pilot" headline figure | Pilot's own per-order data (38 orders/day, EUR 3.10/order, 8 stores) in the same paragraph | No visible calculation bridges the per-order pilot data to the 18-store, 2031 aggregate — unlike catering, whose 1.6/2.1/2.5/2.7 build is fully shown. |

## Missing outside view
- **Catering central kitchen economics:** no external benchmark for corporate catering unit launches or central-kitchen ramp-up/payback at comparable bakery or food-service operators (delivery has two cited regional chains; catering has none).
- **14% margin floor:** no comparison to sector-typical margin floors, so the board has no external reference for judging whether 14% itself is still right.
- **3% price increase → EUR 1.1m:** no price-elasticity benchmark beyond "limited by two discount competitors" — the EUR 1.1m isn't shown to be derived from an elasticity estimate.

## Premortem
1. The central kitchen's physical/staffing capacity caps catering throughput well below the EUR 2.9m run-rate needed for payback, because capacity was never sized against the volume growth required (Finding 5).
2. Delivery platform economics erode, or the pilot lands in the undefined 50–59 orders/day zone, and there's no clear rule for what happens next — the "test before scale" structure quietly defaults to inaction or an ad hoc call (Finding 3).
3. The board revisits the 2031 target per this memo's recommendation without ever learning why the 14% floor exists, later discovering the floor foreclosed suburban/franchise options that might have been acceptable (Findings 4, 6).

## What is good and must survive
- A specific, unambiguous ask: amounts, owners, and start dates for both initiatives, with an explicit no on suburban stores and franchising.
- Catering revenue estimate triangulated two ways (bottom-up and top-down) before a base case is chosen near the midpoint of the resulting range, not cherry-picked.
- Catering payback math is fully shown and verifies exactly: 1.6/2.1/2.5/2.7m revenue × 32% minus EUR 0.35m fixed costs = 0.16/0.32/0.45/0.51m, cumulative crossing the EUR 1.2m investment in year 4.
- Delivery growth assumption benchmarked against two regional chains' actual reported results, with a stated downside/upside range (12% base, 18% upside).
- Genuinely falsifiable "what would change our view" kill criteria for both initiatives — this is pre-mortem thinking built into the decision itself, which is rare and worth keeping.
- Honest framing of the remaining gap to the 2031 target as a second, explicit board decision rather than papering over it.

---

**Note on scope:** this review checks logic, evidence, and internal consistency. The franchising royalty data and the 14% floor's origin should be confirmed with Finance/Legal before the board meeting — that's a sourcing check, not something I can verify from the memo text alone.


## Files in work dir after run

- pr-03-input.md
