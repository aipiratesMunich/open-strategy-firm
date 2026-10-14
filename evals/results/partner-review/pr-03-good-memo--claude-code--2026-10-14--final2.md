# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (5/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| verdict is Release or Release with fixes | NO | **Verdict:** Return |
| no Blocker findings | NO | / 1 / **Blocker** / Logician / CFO / ... / |
| every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo | yes | Finding 2: 'A board member asks "is 2.9m by 2031 realistic..." and there's no answer.'; Numbers that do not tie section confirms all figures tie correctly. |
| names what is good and must survive | yes | '## What is good and must survive' section lists specific strengths (named owner/budget/start month, numbers tying, triangulation, kill criteria). |
| must not demand a named framework, more length, or more slides | yes | Required fixes ask for content additions (a sized revenue estimate, one external comparable, one sentence on risk) not more slides/length/frameworks. |
| must not flag the stated uncertainty or the explicit assumptions as weaknesses | yes | 'Explicit, falsifiable kill criteria ("what would change our view") for both moves — this is exactly the kind of stated uncertainty that should survive into the final version.' |
| must not claim numbers do not tie | yes | '## Numbers that do not tie\nNone found. ... all tie on independent recalculation.' |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: Brightwell catering & delivery memo, gate 3

**Verdict:** Return
**In one line:** The memo asks the board to choose "lower the target, not the floor" but never sizes the revenue suburban stores or franchising would actually add — so the one piece of evidence that decision needs is missing, not just thin.

**Question the draft must answer:** Which two 2027 growth moves should the board fund, and should the 2031 revenue target or the margin floor give way to close the remaining gap? (Given, stated in the header.)
**Answer the draft gives:** Fund catering (EUR 1.2m) and a delivery pilot (EUR 0.3m); don't fund suburban stores or franchising; revisit the revenue target rather than the margin floor.
**Match:** Mostly — the funding call is well supported; the target-vs-floor call is not (see Finding 1).

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | Logician / CFO | "What it adds up to" — target vs. floor | The memo recommends lowering the revenue target rather than the margin floor because options that need a lower floor "carry the weakest evidence." But suburban stores and franchising are only shown to *fail the 14% floor* (13.1% margin; 6–8% royalty) — their revenue potential is never estimated at all. "Weakest evidence" conflates a margin-floor breach with a revenue-sizing gap; the two are different questions. The board can't judge whether relaxing the floor would unlock meaningful revenue toward the EUR 12.7m gap, because no one sized it. | The CEO could revisit the wrong lever: lowering the target forecloses a growth path that was never actually measured, or the board challenges the recommendation live and the memo can't answer "how much revenue are we giving up?" | Add a rough revenue estimate for suburban expansion and for the three franchise offers (even a single bottom-up range), compare it to the EUR 12.7m gap, then state the target-vs-floor recommendation. If that analysis isn't ready for tomorrow, say so explicitly and frame the recommendation as provisional, not settled. |
| 2 | Major | Evidence Auditor / CFO | "Why catering" | Delivery's 12% growth case is checked against two regional chains' actual results (outside view). Catering's EUR 2.9m base case, 32% contribution margin, and the 40% framework-agreement threshold have no external comparable at all — only internal bottom-up/top-down triangulation. | A board member asks "is 2.9m by 2031 realistic, or is this just our own math checking itself?" and there's no answer. | Add one outside reference for corporate-catering growth or margin (a competitor, a catering platform's published numbers, an industry report) — even directionally. |
| 3 | Major | Outsider | "Why a delivery pilot" | "The EUR 2.4m assumes a rollout... (about EUR 0.6m, a separate board decision at the end of the pilot)" — it's not stated what the EUR 0.6m is (rollout capex? incremental contribution? something else). | A reader can't tell whether this program implicitly commits the company to another EUR 0.6m later, which matters for planning even though formal approval is deferred. | State explicitly: "EUR 0.6m is the estimated capex/investment to extend delivery to the remaining 10 stores." |
| 4 | Major | Premortem | General — no section covers it | The central kitchen is a new capability (new site, new staff, EUR 1.2m capex) launching in 4 months. No risk or mitigant is stated for build/ramp delay or cost overrun — the only named risks are demand-side (framework agreement take-up, delivery order volume). | If the kitchen is late or over budget, the EUR 1.2m payback-in-year-4 case slips with no stated fallback, and the memo gave the board no warning this was possible. | Add one sentence naming the execution risk and its mitigant (e.g., phased buildout, contingency budget, go-live gate before April 2027). |
| 5 | Major | Logician | "Why catering" / "What would change our view" | "Framework agreements" appears only in the risk-trigger sentence ("if fewer than 40% ... sign framework agreements") — the term and the sales mechanism behind it are never introduced in the "Why catering" section that builds the revenue case. | A board member can't tell if converting ad hoc catering orders into committed contracts is already part of the April 2027 plan or a new, undesigned workstream the 40% threshold is quietly assuming will exist. | Add one clause in "Why catering" naming framework agreements as the mechanism for converting order growth into contracted revenue, owned by Head of Operations from launch. |
| 6 | Minor | Evidence Auditor | "Why catering" | 9 of 12 office managers named slow delivery as the main pain; the other 3 aren't characterized. | Doesn't change the funding case (the hard order-growth data carries it), but a sharp reader may ask what the dissenters said. | One clause: what the other three cited instead. |

## Numbers that do not tie
None found. The EUR 62m → EUR 80m → EUR 12.7m gap, the 8.5% growth figure, the kitchen payback build (1.6/2.1/2.5/2.7 at 32% minus EUR 0.35m fixed costs = 0.16/0.32/0.45/0.51, cumulative EUR 1.44m against EUR 1.2m invested), and the "less than a quarter of the gap" claim for price/hours (EUR 2.0m vs. EUR 12.7m) all tie on independent recalculation. This is a genuine strength — flag it as a model of how to show the arithmetic, not hide it.

## Missing outside view
- Catering revenue growth, contribution margin, and the 40% framework-agreement conversion threshold: no comparable company or program cited (delivery has this; catering does not).
- Suburban store and franchising revenue potential: no sizing at all, outside-view or otherwise (Finding 1).

## Premortem
1. The central kitchen build runs late or over the EUR 1.2m budget — not addressed anywhere in the memo (Finding 4).
2. "Framework agreements" turn out to require a sales motion Brightwell hasn't built, and the 40% conversion threshold is missed in month 6 without anyone having owned building that capability (Finding 5).
3. The 8-store pilot (chosen for highest order density) doesn't generalize to the other 10 stores in the 2028 rollout — lower-density stores may never reach 60 orders/day even if the pilot succeeds. Partially anticipated by deferring rollout to a separate board decision, but worth naming explicitly as the reason that gate exists.

## What is good and must survive
- The recommendation is genuinely specific: named owner, budget, and start month for both moves, and an explicit no on suburban/franchising.
- Every number in the executive math ties on independent recheck — rare, and worth protecting in the rewrite.
- The catering growth claim pre-empts the obvious counter-argument (return-to-office rebound) with the Q2-on-Q2 data — good discipline.
- Both the catering range (2.5–3.3m from two independent methods) and the delivery range (2.4–3.5m tied to named comparables) are real triangulation, not single-source numbers dressed up.
- Explicit, falsifiable kill criteria ("what would change our view") for both moves — this is exactly the kind of stated uncertainty that should survive into the final version.

## What "fixed" looks like
"We recommend revisiting the 2031 revenue target rather than the margin floor. Lowering the floor to allow suburban stores and franchising would add an estimated EUR [X–Y]m in revenue by 2031 — well short of closing the remaining EUR 12.7m gap even before accounting for the margin dilution — so relaxing the floor does not solve the shortfall catering and delivery leave." This single addition — a sized, if rough, revenue estimate for the rejected alternatives — is the difference between an asserted conclusion and a proven one, and it's the only change that needs to happen before tomorrow.


## Files in work dir after run

- pr-03-input.md
