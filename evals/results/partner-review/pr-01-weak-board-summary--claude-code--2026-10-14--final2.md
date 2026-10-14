# pr-01-weak-board-summary on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Return | yes | "Verdict: **Return**" |
| Finds D1, D2 and D3, each rated Blocker | yes | Finding #1 (Blocker): '"Exploring"/"considering" name no moves, budget, owner or date'; Finding #2 (Blocker): catering EUR9m vs table EUR6.4m/5.2m delta; plus explicit 'Question the draft must answer'/'Answer the draft gives' mismatch |
| Finds at least two of D4, D5, D6 | yes | Finding #8 (40 loyalty members, Major), Finding #6 (35%/yr no benchmark, Major), Finding #5 (franchising disappears, Major) — all three found |
| States the question the draft must answer and notes draft does not answer it | yes | "Question the draft must answer:... Answer the draft gives:... These don't match." |
| Gives a concrete fix for every finding | yes | e.g. 'Name the two funded moves, the budget for each, the owner, and the 2027 start date'; 'Correct the figure (or the table) so the summary and source agree' |
| Includes a premortem with three reasons | yes | Premortem section lists three numbered scenarios (catering shortfall, delivery cost eroding margin, suburban margin drag) |
| Lists at least one good thing (store-level margin data solid) | yes | "The store economics table is well-sourced (company P&L, format, store count, year)" |
| Shows what 'fixed' looks like in two to four sentences | yes | Three sentences under 'What "fixed" looks like' section |
| Must not invent benchmark figures without a source | yes | "No comparable bakery/QSR delivery growth rate is cited... need a comparable bakery/QSR delivery growth benchmark" — flags the gap rather than inventing a number |
| Must not rewrite the whole document instead of reviewing it | yes | Output is structured findings, tables, premortem, and a short 3-sentence illustrative fix — not a full rewritten summary |

## Transcript

## Turn 1

**User:** Review this executive summary before it goes to the Brightwell board next week. Is it ready? (Attached in the working directory: pr-01-input.md.)

Verdict: **Return**. Here's the review.

# Partner review: Brightwell Bakeries Growth Strategy — Executive Summary, gate 3

**Verdict:** Return
**In one line:** The recommendation doesn't commit to anything the board can fund, one of its two headline numbers doesn't tie to its own table, and neither recommended move is checked against the board's explicit 14% margin floor.

**Question the draft must answer:** Which two growth moves should the board fund in the 2027 budget to grow revenue EUR 62m→80m by 2031, keeping store margin above 14%? *(given)*
**Answer the draft gives:** "Explore the catering opportunity further" and "consider an accelerated online roadmap" — no amounts, no owners, no dates, franchising never mentioned, new stores left open. These don't match.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Decision Maker | Exec summary, recommendation line | "Exploring" / "considering" name no moves, budget, owner or date; "next steps will be defined with management" hands the decision back instead of requesting one | Board has nothing to approve — the document fails the one job it has | Name the two funded moves, the budget for each, the owner, and the 2027 start date; replace the deferral with a decision request |
| 2 | Blocker | Skeptical CFO / Evidence Auditor | Exec summary vs. Market overview table | Text: "Corporate catering can add EUR 9m by 2031." Table: catering grows EUR 1.2m (0.8+0.4) → EUR 6.4m (4.1+2.3) — a delta of EUR 5.2m, not 9m | Board anchors on a number that is EUR 3.8m too high; every other number in the deck now invites doubt | Correct the figure (or the table) so the summary and source agree |
| 3 | Blocker | Evidence Auditor | Market overview, source line | Both 2031 figures (catering add, online EUR 11.2m) rest solely on "management estimate" / "management plan" — the client's own forecast returned to it as the team's finding | The one number the whole recommendation rests on has never been independently checked | Triangulate both figures (bottom-up build plus an outside-view check) and present as a range, not a point estimate |
| 4 | Blocker | Logician / Skeptical CFO | Store economics table vs. "suburban locations" line | The board's constraint is margin >14%. Suburban stores run 13.1%, kiosks 11.4% — both already below it — yet suburban is floated as a location with no flag. Catering and online delivery have no margin figures at all | The two things actually being recommended may violate the board's own stated constraint, and nobody checked | Drop suburban or show a credible path above 14%; add margin estimates for catering and online delivery and confirm the consolidated number clears 14% |
| 5 | Major | Logician | Whole document | Franchising — one of the four in-scope options — is never mentioned or ruled out | A sharp board member asks "what about franchising?" and the team has no answer on the record | Add one line stating why franchising was or wasn't pursued, with the reason |
| 6 | Major | Skeptical CFO | "Online delivery... grow 35% per year" | No comparable bakery/QSR delivery growth rate is cited against a sustained 5-year 35% CAGR | Base case may sit well above what any comparable company has achieved, and nobody would know | Cite one outside benchmark per driver, or flag the forecast as unvalidated |
| 7 | Major | Decision Maker | Exec summary | The two moves' contribution is never summed and compared against the EUR 18m gap (62→80m) the board must close | Board can't tell if the plan actually hits the target or falls short — classic "hiding the gap" | State the sum against EUR 18m explicitly, and what covers any shortfall |
| 8 | Major | Evidence Auditor | Customer view section | "92% would recommend" and "61% would order online under 45 min" come from 40 existing loyalty-club members — small, self-selected, stated (not revealed) preference. The 61% figure, most relevant to the online recommendation, is never connected to it in the text | A sharp board member discounts both stats on sight, and the one data point that should support the online bet is buried | Flag the sample limitation, or validate against actual order data; link the 61% figure explicitly to the online-delivery case |
| 9 | Major | Skeptical CFO / Premortem | Exec summary | No stated risks or triggers — nothing that says what would change the answer | Board has no way to know how fragile the recommendation is | Add 2–3 stated risks (e.g., take-up below plan, delivery cost eroding margin) |

## Numbers that do not tie
| Number | Location A | Location B | Difference |
|---|---|---|---|
| Corporate catering 2031 revenue add | Exec summary: "EUR 9m" | Market overview table: EUR 5.2m delta (1.2m→6.4m) | EUR 3.8m overstated |

## Missing outside view
- Online delivery 35%/yr sustained 5-year growth: need a comparable bakery/QSR delivery growth benchmark.
- Catering ramp (offices + events): need comparable B2B catering attach/win rates for a company with no catering sales history.

## Premortem
1. Catering revenue lands well below even the EUR 5.2m table figure because Brightwell has no B2B sales capability today and the number was management's own target, never tested with customers.
2. The 45-minute delivery promise requires driver, packaging and platform cost that erodes store-level margin below 14% — no delivery cost model is shown.
3. New suburban stores get opened to chase growth, but suburban margin (13.1%) is already below the board's 14% floor, dragging the consolidated number down just as revenue scales.

## What is good and must survive
- The problem statement is precise and decision-ready (two moves, a budget horizon, a margin constraint, four named options) — keep it verbatim.
- The store economics table is well-sourced (company P&L, format, store count, year) — it just needs to be connected to the decision instead of sitting unused next to a contradicting recommendation.
- Sourcing habit on the market table (source + date per segment) is the right instinct; only the catering arithmetic needs fixing.

## What "fixed" looks like
**Fund a EUR Xm corporate-catering push (offices and events) and a EUR Ym accelerated online-delivery rollout for 2027, together adding about EUR 17–18m by 2031 and meeting the EUR 80m target with little cushion.** Franchising is not recommended because [reason]; no further suburban stores are added because suburban margin (13.1%) already sits below the board's 14% floor. The answer changes if catering take-up stays below [X]% or delivery cost pushes blended margin under 14%.


## Files in work dir after run

- pr-01-input.md
