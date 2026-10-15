# pr-01-weak-board-summary on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is **Return**. | yes | **Verdict:** Return |
| Must: finds D1, D2 and D3, each rated Blocker. | yes | Finding #2 (Blocker) covers vague 'explore'/'consider' recommendation with no budget ask (D2); the 'Question the draft must answer' / 'Answer the draft gives' section plus Finding #2/#3 cover D1 (no funded move named); Finding #1 (Blocker) covers the EUR 9m vs EUR 6.4m catering mismatch (D3). |
| Must: finds at least two of D4, D5, D6. | yes | Finding #7 (Major) covers D4 (40-person loyalty survey) and D5 (35% growth, no external comparison); Finding #5 (Major) covers D6 (franchising dropped without comment). |
| Must: states the question the draft must answer and notes that the draft does not answer it. | yes | "Question the draft must answer:" ... "Answer the draft gives:" ... "These do not match. The draft hedges where the mandate requires a decision." |
| Must: gives a concrete fix for every finding (not "consider improving"). | yes | e.g. #1 'Reconcile the catering 2031 figure to one number...'; #9 'Name an accountable executive owner and a first 2027 milestone for each of the two recommended moves.' |
| Must: includes a premortem with three reasons. | yes | Premortem lists three numbered items: no owner/budget, B2B catering capability gap, delivery economics eroding margin. |
| Must: lists at least one thing that is good and should survive (the store-level margin data is solid). | yes | "The store economics table is exactly the right level of granularity (format-level revenue and margin) and should be the template extended to catering and online delivery." |
| Must: shows what "fixed" looks like in two to four sentences. | yes | "What 'fixed' looks like" section gives a 4-sentence model answer with placeholders for budget split, sponsor, and milestones. |
| Must not: invent benchmark figures without a source; it may say which comparison is missing. | yes | "Missing outside view" section states no comparable bakery/food-service or delivery-adoption benchmark is cited, without fabricating a specific figure. |
| Must not: rewrite the whole document instead of reviewing it. | yes | Output is a structured review (findings table, premortem, missing outside view) with only a short illustrative placeholder paragraph for 'what fixed looks like', not a full rewritten summary. |
| Must: at least one of the three premortem reasons is internal to the client or the team. | yes | Premortem items 1 and 2 are explicitly labeled '(Internal)': 'No owner, no budget commitment' and 'Capability gap in B2B catering'. |

## Transcript

## Turn 1

**User:** Review this executive summary before it goes to the Brightwell board next week. Is it ready? (Attached in the working directory: pr-01-input.md.)

# Partner review: Brightwell Bakeries Growth Strategy — Executive Summary, gate 3

**Verdict:** Return
**In one line:** The two numbers that are supposed to prove the plan closes the EUR 18m growth gap don't agree with each other, and the summary never actually recommends anything the board can fund.

**Question the draft must answer:** Which two growth moves should the board fund in the 2027 budget to grow revenue from EUR 62m to EUR 80m by 2031, keeping store-level margin above 14%? (given, from the problem statement)
**Answer the draft gives:** "Explore the catering opportunity further" and "consider an accelerated online roadmap," with next steps left to management — no budget figure, no committed decision, no mention of the margin constraint, and franchising dropped without comment.

These do not match. The draft hedges where the mandate requires a decision.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Evidence Auditor / CFO | Exec summary ¶2 vs. Market overview table | Exec summary states catering adds "EUR 9m" by 2031; the table's own catering rows (offices 4.1 + events 2.3) sum to EUR 6.4m — a EUR 2.6m gap, not rounding. | The board cannot tell which catering figure it is approving, and every downstream claim about closing the revenue gap (below) is built on an unverified number. | Reconcile the catering 2031 figure to one number (state whether it is 6.4m or 9m and why) and rerun the gap-closing math in finding #3. |
| 2 | Blocker | Decision Maker | Exec summary ¶3 | The draft asks the board to approve nothing: "explore further," "consider," and "next steps will be defined with management" contain no budget ask and no firm choice of two moves. The problem statement asks exactly which two moves to *fund*. | The board cannot act on this document; it will have to send it back or approve in principle without knowing what it is committing money to. | Replace the recommendation with a named decision: the two moves, the 2027 budget figure for each, and what the board is being asked to approve at this meeting. |
| 3 | Blocker | Skeptical CFO / Logician | Whole document | The plan must close an EUR 18m gap (62m→80m). The two recommended moves contribute at most EUR 17.6m (6.4 + 11.2, using the table) or EUR 20.2m (using the exec summary's 9m) — and the document says nothing about the other ~EUR 58m of revenue (existing stores): flat, growing, or declining. Without that, there is no actual bridge from 62m to 80m. | The board could approve two initiatives that look sufficient on paper while the core store base is shrinking and the target is missed anyway. | Add a bridge: 2026 base revenue, expected organic trajectory of existing stores to 2031, plus the incremental contribution of each proposed move, reconciled to EUR 80m. |
| 4 | Blocker | Skeptical CFO | Exec summary vs. Store economics table | The mandate requires store-level margin above 14%. Current blended margin is already only ~14.4% (weighted average of the three formats), with suburban stores at 13.1% — below the floor. No margin data is given for catering or online delivery at all. | The board could fund initiatives that breach its own stated margin constraint with zero evidence either way, invalidating the recommendation on its own terms. | Add margin (or contribution margin) estimates for corporate catering and online delivery, and state the blended store margin impact of each move through 2031. |
| 5 | Major | Decision Maker | Exec summary | Franchising was explicitly in scope per the agreed problem statement but receives no analysis or even a mention anywhere in the draft. | The board is asked to choose "two of four" options but only ever sees data on two; it cannot tell whether franchising was screened out on evidence or simply forgotten. | Add a short section stating why franchising (and new stores) were not advanced, even if only qualitative screening criteria. |
| 6 | Major | Logician | Exec summary ¶2 vs. Store economics table | "New stores remain an option in suburban locations" is offered without acknowledging that the same document's own data shows suburban store margin (13.1%) already below the required 14% floor. | A board member cross-referencing the two sections would conclude the draft contradicts itself, undermining trust in the rest of the analysis. | Either drop the suburban new-store mention or explicitly address how new suburban stores would clear the margin bar that existing suburban stores do not. |
| 7 | Major | Evidence Auditor | Customer view section, feeding the EUR 11m online figure | The 35%/year online growth assumption rests on a single data point: 61% of 40 loyalty-club members (a small, self-selected, already-loyal sample) saying they'd order online under a 45-minute delivery promise. | The headline online-delivery number — one of only two figures behind the recommendation — has no basis beyond a non-representative survey of 40 people. | State the margin of error and bias of the loyalty-club sample, and triangulate the 35% growth assumption against an external source (e.g., comparable regional food-delivery adoption data) or label it a scenario, not a plan input. |
| 8 | Major | Evidence Auditor | Market overview, catering source note | Catering 2031 figures (implying ~39–42% CAGR over 5 years) are sourced only as "management estimate," with no market sizing, pipeline, or comparable benchmark. | The board is being asked to fund a move whose central growth number is an unverified internal guess, for a company with no stated B2B catering track record. | Replace or support the management estimate with external evidence (comparable catering market growth, a pipeline of named prospective accounts, or a bottom-up build from sales capacity). |
| 9 | Major | Outsider | Exec summary ¶3 | No executive owner is named for either initiative; "next steps will be defined with management" leaves accountability and timeline open after a board funding decision. | Funded initiatives with no named sponsor typically stall once the board meeting is over — this is one of the three most likely failure modes (see premortem). | Name an accountable executive owner and a first 2027 milestone for each of the two recommended moves. |
| 10 | Minor | Evidence Auditor | Exec summary ¶1 | "Customers love the brand" generalizes from a 40-person loyalty-club survey to the entire customer base. | Low — a qualitative framing line, not a number the recommendation depends on. | Qualify the claim: "Among surveyed loyalty-club members (n=40)..." |
| 11 | Minor | Evidence Auditor | Exec summary ¶2 | "Online delivery is growing fast across the industry" has no citation. | Low — rhetorical framing, not load-bearing for the decision. | Cite a source or cut the sentence. |
| 12 | Minor | Logician | Exec summary | The exec summary never restates the EUR 62m→80m target or the 14% margin floor, forcing the reader back to the problem statement to judge sufficiency. | Low — a presentation gap, not a factual error. | Open the executive summary with the target and constraint before stating the recommendation. |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Corporate catering 2031 revenue contribution | Exec summary ¶2: "EUR 9m" | Market overview table: 4.1 + 2.3 = EUR 6.4m | EUR 2.6m (41% of the smaller figure — not rounding) |

## Missing outside view

- **Corporate catering growth (~39–42% CAGR, 2026–2031):** no comparable bakery/food-service company's actual B2B catering growth is cited to support this rate.
- **Online delivery growth (35%/year):** no comparable regional food-delivery adoption curve is cited; the only support is the 40-person loyalty survey.
- **"92% would recommend" as a brand-strength proof point:** no comparison to industry NPS or recommend-rate benchmarks for regional food brands.

## Premortem

1. **(Internal) No owner, no budget commitment.** The draft hands the decision back to "management" rather than naming a budget and sponsor; momentum and funding commitment evaporate once the board meeting ends, which is the single most common reason approved-in-principle initiatives never launch.
2. **(Internal) Capability gap in B2B catering.** Brightwell is a consumer retail brand with no demonstrated corporate-sales or account-management capability; the catering growth assumption implicitly requires building a B2B sales motion from scratch, and the plan does not address hiring, skills, or management attention for this.
3. **(External) Delivery economics erode margin.** A 45-minute delivery promise typically requires a fleet or third-party delivery partner, both of which carry costs not modeled anywhere in this draft; if delivery costs push blended margin below 14%, the plan violates its own mandate even if the revenue target is hit.

## What is good and must survive

- The problem statement is sharp and quantified (specific revenue target, specific margin floor, named options) — this discipline should carry through to the rest of the document, which currently doesn't live up to it.
- The store economics table is exactly the right level of granularity (format-level revenue and margin) and should be the template extended to catering and online delivery.
- The online delivery EUR 11.2m figure is the one number in the draft that is internally consistent and independently checks out: EUR 2.5m × 1.35⁵ ≈ EUR 11.2m. Keep this calculation visible in the final version as the standard the catering numbers should be held to.

## What "fixed" looks like

"Brightwell should fund corporate catering and online delivery in the 2027 budget: together they close an estimated EUR [X]m of the EUR 18m revenue gap to 2031, with the remaining EUR [18-X]m expected from the existing store base growing at [Y]%. Both initiatives are projected to hold blended store-level margin above 14% [cite basis]. We are not recommending new stores or franchising at this time because [reason]. We request a 2027 budget of EUR [Z]m, split [A]/[B] between the two initiatives, with [named executive] as sponsor and first milestones due [date]."


## Files in work dir after run

- pr-01-input.md
