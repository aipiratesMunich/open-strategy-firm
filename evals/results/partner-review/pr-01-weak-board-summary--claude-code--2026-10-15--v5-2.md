# pr-01-weak-board-summary on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is Return. | yes | **Verdict:** Return |
| Must: finds D1, D2 and D3, each rated Blocker. | yes | Finding 2 (Blocker) on unanswered funding question/gap; Finding 4 (Blocker) on 'explore'/'consider' with no owner/budget/date; Finding 1 (Blocker) on catering EUR9m vs table's EUR6.4m |
| Must: finds at least two of D4, D5, D6. | yes | Finding 7 (Major, 40 loyalty-club members), Finding 5 (Major, 35%/year growth sourced to management with no benchmark), Finding 6 (Major, franchising disappears) — all three found |
| Must: states the question the draft must answer and notes that the draft does not answer it. | yes | 'Question the draft must answer:' ... 'Answer the draft gives:' ... 'two hedged next steps, not a funding decision' |
| Must: gives a concrete fix for every finding (not "consider improving"). | yes | e.g. Fix for #4: 'Name the two moves to fund, the EUR amount for each, the owner, and the 2027 start date.' |
| Must: includes a premortem with three reasons. | yes | Premortem lists three numbered items (market/execution, margin mandate vs mix, no owner/no incentive) |
| Must: lists at least one thing that is good and should survive (the store-level margin data is solid). | yes | 'The store economics table (format-level margin by store type, sourced to the P&L) is exactly the right granularity' |
| Must: shows what "fixed" looks like in two to four sentences. | yes | Section contains 4 sentences: 'Fund corporate catering...', 'New stores are not recommended...', 'Franchising was screened out...', 'Decision requested...' |
| Must not: invent benchmark figures without a source. | yes | 'Online delivery 35%/year growth... no comparison to what comparable regional bakery/food-delivery launches actually achieved' — flags missing comparison without fabricating a number |
| Must not: rewrite the whole document instead of reviewing it. | yes | Output is structured findings tables plus a short illustrative 'What fixed looks like' paragraph, not a full rewrite |
| Must: at least one of the three premortem reasons is internal to the client or team. | yes | '2. Internal — margin mandate vs. mix' and '3. Internal — no owner, no incentive' |

## Transcript

## Turn 1

**User:** Review this executive summary before it goes to the Brightwell board next week. Is it ready? (Attached in the working directory: pr-01-input.md.)

# Partner review: Brightwell Bakeries executive summary, gate 3

**Verdict:** Return
**In one line:** The exec summary's own numbers don't tie (catering is EUR 9m here, EUR 6.4m in the table two paragraphs below), and the recommendation it reaches is not something the board can actually fund.

**Question the draft must answer:** Which two growth moves should the board fund in the 2027 budget to grow revenue from EUR 62m to EUR 80m by 2031, keeping store-level margin above 14%? (given)
**Answer the draft gives:** "Explore the catering opportunity further" and "consider an accelerated online roadmap" — two hedged next steps, not a funding decision, and neither is checked against the EUR 18m gap or the 14% margin floor.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Skeptical CFO | Exec summary ¶2 vs. Market overview table | Exec summary: catering "can add EUR 9m by 2031." Table: offices (4.1) + events (2.3) = EUR 6.4m. Neither the 2031 total nor the 2026→2031 increment (5.2m) equals 9m. | Board can't tell which catering figure it's approving; every downstream comparison to the EUR 18m target is unverifiable until this is fixed. | Reconcile catering 2031 potential to one figure and rerun any claim that depends on it. |
| 2 | Blocker | Decision Maker | Exec summary, throughout | The summary never states the combined revenue effect of its two proposed moves against the EUR 18m gap (62m→80m) or against the 14% margin floor — both are in the problem statement, neither is addressed. | Board approves a direction with no way to know if it closes the gap or protects margin — the two success criteria it set. | Add one line: total incremental revenue from the two moves vs. the EUR 18m gap, and resulting blended margin vs. 14%; state any shortfall explicitly. |
| 3 | Blocker | Logician | "New stores remain an option in suburban locations" vs. Store economics table | Suburban store margin is 13.1%, already below the board's 14% floor. The draft leaves suburban expansion open without flagging that it breaches the board's own constraint. | Board could greenlight suburban expansion unaware it structurally fails the margin mandate it set. | Remove new stores as a live option, or show a suburban format/location that clears 14%, and state plainly that today's suburban economics don't qualify. |
| 4 | Blocker | Decision Maker | Recommendation line | "Explore further," "considering," and "next steps will be defined with management" name no budget, owner, or date. | The board is asked to fund two of four named options for the 2027 budget; this summary asks it to approve nothing concrete. | Name the two moves to fund, the EUR amount for each, the owner, and the 2027 start date. |
| 5 | Major | Evidence Auditor | Market overview footnote | Catering 2031 potential and the online delivery 35%/year growth rate are both sourced to management's own estimate/plan, with no independent benchmark or bottom-up build shown. | The board would be funding a decision built on the client restating its own plan back as independent analysis. | Triangulate both figures (comparable operator growth rate, or a bottom-up per-client/per-route build) or label them explicitly as unverified management assumptions with a range. |
| 6 | Major | Logician | Scope | Franchising — one of four options the CEO agreed was in scope — is never mentioned or ruled out. | A board member who remembers franchising was in scope will ask why it vanished; the recommendation looks incomplete. | Add one line on why franchising was screened out, or carry it forward as a considered option. |
| 7 | Major | Evidence Auditor | Customer view | 92% recommend and 61% would-order-online come from 40 existing loyalty-club members — a small, already-loyal, self-selected sample used to support company-wide and investment-sizing claims. | A sharp board member will note the online figure likely overstates intent among non-loyal customers, undermining the case for the online investment. | Disclose the sample's limits in the summary, or supplement with a broader survey or revealed-ordering data before using 61% to size online delivery. |
| 8 | Minor | Outsider | Exec summary opening | "Our analysis of the market shows significant potential in several areas" and the brand-love line are a table-of-contents style lead-in; the actual answer doesn't appear until paragraph 3. | Doesn't change the decision, but slows the reader down. | Open with the governing thought/recommendation first (SCQA), move brand/context lines after it. |

## Numbers that do not tie
| Number | Location A | Location B | Difference |
|---|---|---|---|
| Corporate catering 2031 potential | Exec summary: "EUR 9m" | Market overview table: 4.1 + 2.3 = EUR 6.4m | EUR 2.6m (41% overstatement vs. the table) |

## Missing outside view
- Online delivery 35%/year growth, sustained for 5 years: no comparison to what comparable regional bakery/food-delivery launches actually achieved.
- Corporate catering growth to EUR 6.4–9m: no comparable corporate-catering program benchmark.
- 92% "would recommend": no benchmark against industry recommend/NPS scores (lowest priority — doesn't drive a funding number).

## Premortem
1. **Market/execution:** The 35%/year online growth assumption (a ~4.4x increase over five years) proves optimistic against delivery logistics and kitchen capacity; actual growth lands well below plan and the gap to EUR 80m widens.
2. **Internal — margin mandate vs. mix:** Growth leans on suburban stores, online, and catering, all thinner-margin than high street; blended store margin drifts below the board's 14% floor exactly as the store economics table already hints, because nobody reconciled the recommendation against that table.
3. **Internal — no owner, no incentive:** "Next steps will be defined with management" names no senior sponsor; catering build-out likely falls to the ops team measured on retail store KPIs, who have no incentive to prioritize a side channel, so the initiative stalls after approval.

## What is good and must survive
- The problem statement itself: specific, numeric (62m→80m, 14% floor), dated, with a named decision body — this is a well-framed question.
- The store economics table (format-level margin by store type, sourced to the P&L) is exactly the right granularity — it just needs to be connected to the recommendation instead of sitting unused.
- The market overview table's structure (segment, 2026 actual, 2031 potential, sourced and dated) is the right shape for sizing options; it just needs the exec-summary prose to match it.

## What "fixed" looks like
**Fund corporate catering (EUR 6.4m by 2031, EUR [X] budget) and online delivery (EUR 11.2m by 2031, EUR [Y] budget); together they add EUR [total] toward the EUR 18m gap to EUR 80m [state the resulting shortfall or surplus], while blended store margin is projected to hold at [Z]% against the 14% floor.** New stores are not recommended for 2027: suburban format margin (13.1%) already sits below the board's floor. Franchising was screened out because [reason]. **Decision requested:** approve EUR [amount] for the catering build-out (owner: [role], start [date]) and EUR [amount] for the online delivery roadmap (owner: [role], start [date]); the answer changes if blended margin falls below 14% or online take-up stays below [threshold].


## Files in work dir after run

- pr-01-input.md
