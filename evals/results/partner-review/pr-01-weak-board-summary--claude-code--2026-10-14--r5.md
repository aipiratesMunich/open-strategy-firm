# pr-01-weak-board-summary on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is **Return**. | yes | "Verdict:** Return" |
| Must: finds D1, D2 and D3, each rated Blocker. | yes | Finding #1/#2 (Blocker) cover unanswered question/no owner-amount-date; Finding #3 (Blocker) covers EUR 9m vs EUR 6.4m table mismatch. |
| Must: finds at least two of D4, D5, D6. | yes | Finding #9 (40 loyalty-club members), #8 (35%/year growth no benchmark), #7 (franchising dropped) — all three present, Major. |
| Must: states the question the draft must answer and notes that the draft does not answer it. | yes | "Question the draft must answer:... Answer the draft gives: ... no moves funded, no amounts, no margin discussion" |
| Must: gives a concrete fix for every finding (not "consider improving"). | yes | Each row has a 'Required fix' e.g. "State: fund move A (EUR Xm, owner, start date) and move B (EUR Ym, owner, start date)." |
| Must: includes a premortem with three reasons. | yes | Three numbered premortem items on catering, online growth, and franchising. |
| Must: lists at least one thing that is good and should survive (store-level margin data solid). | yes | "Store economics tables are the right shape: segment-level revenue with dates and sources, store margin by format. Keep this structure in the rewrite" |
| Must: shows what "fixed" looks like in two to four sentences. | yes | Three-sentence 'What fixed looks like' block (Fund [...]; Brightwell's EUR 62m...; The answer changes if...). |
| Must not: invent benchmark figures without a source. | yes | "Missing outside view" section states comparisons are absent rather than inventing figures. |
| Must not: rewrite the whole document instead of reviewing it. | yes | Output is a structured review (findings table, premortem, short fixed-template) not a full rewritten summary. |

## Transcript

## Turn 1

**User:** Review this executive summary before it goes to the Brightwell board next week. Is it ready? (Attached in the working directory: pr-01-input.md.)

# Partner review: Brightwell Bakeries Growth Strategy — Executive Summary, gate 3

**Verdict:** Return
**In one line:** The exec summary never says which two moves to fund, its one firm number (catering, EUR 9m) doesn't tie to its own market table, and the margin constraint in the question is never addressed even though the store-economics table shows two formats already below the 14% floor.

**Question the draft must answer:** Which two growth moves should the board fund in the 2027 budget to grow revenue EUR 62m → EUR 80m by 2031, keeping store margin above 14%? (given)
**Answer the draft gives:** "Explore catering further" and "consider an accelerated online roadmap," with next steps "defined with management" — no moves funded, no amounts, no margin discussion, no total-vs-target math.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Decision Maker / Logician | Exec summary, opening | Opens with brand praise and "significant potential in several areas" instead of naming the two funded moves. Classic table-of-contents-in-prose. | Board reads the summary and still doesn't know what it's being asked to approve. | Lead with the governing thought: the two named moves, their cost, and the total effect against EUR 80m. |
| 2 | Blocker | Decision Maker / So-What | Exec summary, final para | "Exploring," "considering," and "next steps will be defined with management" are not decisions — no amount, owner, or date for either move. | The board has nothing to vote on; the paper fails its own purpose. | State: fund move A (EUR Xm, owner, start date) and move B (EUR Ym, owner, start date). |
| 3 | Blocker | Evidence Auditor | Exec summary vs. Market overview table | "Catering can add EUR 9m by 2031" doesn't tie to the table: offices (0.8→4.1) + events (0.4→2.3) = EUR 6.4m total 2031 potential, i.e. +EUR 5.2m growth from 2026. Neither equals EUR 9m. | A sharp board member recalculates from the board's own table in two minutes and stops trusting every other number in the deck. | Recompute consistently with the table, or show the bridge from EUR 6.4/5.2m to EUR 9m explicitly. |
| 4 | Blocker | Evidence Auditor | Market overview, source line | Both catering and online numbers rest solely on "management estimate" / "management plan" — the client's own plan returned to the board as independent analysis, with no outside check. | The two numbers driving the entire recommendation are unverified; if management's plan is optimistic, the whole case collapses. | Triangulate against external benchmarks (comparable bakery/catering/delivery operators) before using these as base case. |
| 5 | Blocker | Logician / CFO | Exec summary vs. Store economics table | The margin half of the question is never addressed. Worse, "new stores remain an option in suburban locations" sits next to a table showing suburban margin at 13.1% and station kiosk at 11.4% — both already below the 14% floor the board set. | Board could fund a move that breaches its own margin mandate on day one, or believe the constraint was checked when it wasn't. | Either rule out suburban/kiosk expansion explicitly with the margin data as the reason, or show a credible path back above 14%. State margin impact for every recommended move. |
| 6 | Blocker | So-What / Exec Summary standard | Whole document | No statement of total effect against the EUR 80m target (the EUR 18m gap). Catering and online numbers are given in inconsistent frames ("add" vs. "reach") and never summed against the target. | Board cannot tell whether the recommended moves close the gap, fall short, or overshoot — the one number that matters most is hidden. | Add explicit arithmetic: 62m + catering Δ + online Δ = Zm vs. 80m target; state what remains open. |
| 7 | Major | Logician | Whole document | Franchising — one of only four options named in the agreed problem statement — is never mentioned, analyzed, or ruled out. | Board later learns a scoped-in alternative, possibly the lowest-capital path to the target, was silently dropped. | Add a franchising estimate, or state explicitly why it was excluded and what evidence supports that. |
| 8 | Major | CFO | Exec summary / Market overview | 35%/year online delivery growth (to reach EUR 11.2m) has no outside-view check against what comparable regional food-delivery rollouts actually achieved. | Base case may be well above what's achievable; no downside case is shown either. | Benchmark against comparable operators' delivery ramp-ups; add a downside case. |
| 9 | Major | Evidence Auditor | Customer view | The 92% "would recommend" and 61% "would order online" figures come from 40 existing loyalty-club members only — already-loyal customers, not a representative or non-customer sample. | Figures likely overstate appeal to the broader customer base the growth moves are meant to reach. | Flag the sample limitation explicitly, or supplement with a broader/non-customer sample. |
| 10 | Major | Exec Summary standard | Whole document | No risks stated — nothing on what would change the answer (take-up miss, delivery margin erosion, etc.). | Board has no way to know what to watch for after approving funding. | Add 2–3 explicit risks/triggers that would flip the recommendation. |
| 11 | Minor | So-What | Exec summary, para 1 | "92% would recommend" is included but never tied to any of the three moves under discussion. | Reader spends effort on a fact that doesn't inform the decision. | Cut it, or tie it explicitly to a specific move (e.g., catering cross-sell to loyal base). |
| 12 | Minor | Evidence Auditor | Store economics heading | Store margins are 2025 P&L; catering/online figures are 2026-based. One-year gap not flagged. | Minor — unlikely to change the decision, but invites a "which year?" question. | Note whether 2025 margins are assumed to hold into 2027, or refresh to 2026 actuals. |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Catering growth | Exec summary: "EUR 9m" | Market overview table: EUR 6.4m total 2031 potential (EUR 5.2m growth from 2026) | EUR 2.6–3.8m unexplained |

*(Online delivery ties correctly: 2.5 × 1.35⁵ ≈ 11.2, matching the table — flagged below as something that works.)*

## Missing outside view

- Corporate catering EUR 9m/6.4m target: no comparison to what similar regional bakery/catering operators have achieved in office and events catering.
- Online delivery 35%/year growth: no comparison to comparable regional food-delivery ramp-ups.
- New-store suburban economics: no comparison showing whether 13.1% margin is typical for maturing suburban bakery stores or a sign of a structurally weaker format.

## Premortem

1. The board funds catering expecting something near EUR 9m, which never reconciled to the firm's own EUR 6.4m market-sizing table and rested only on management's estimate — actual results land well short, and nobody can explain why using this document.
2. The "accelerated online roadmap" assumes 35%/year growth with no outside benchmark; actual delivery economics come in lower and more capital-intensive, squeezing consolidated margin below 14% — the very constraint the mandate existed to protect, worsened by already-thin suburban/kiosk formats.
3. Franchising, a scoped-in option, was never evaluated; two years later it's clear it may have reached the EUR 80m target faster and with less capital, and the board asks why it was never on the table.

## What is good and must survive

- The problem statement itself (gate 1) is sharp and quantified — a real number, a real date, a real constraint, named options. The exec summary should be judged against it, which is exactly what makes its gaps visible.
- The Market overview and Store economics tables are the right shape: segment-level revenue with dates and sources, store margin by format. Keep this structure in the rewrite — just use it consistently.
- The online delivery figure is the one number in the draft that actually ties to its source table (2.5 × 1.35⁵ ≈ 11.2) — a model for how the catering number should work.
- The underlying 2026 revenue baseline is internally plausible: stores (~EUR 58m from the table) + catering (1.2m) + online (2.5m) ≈ EUR 62m, consistent with the problem statement's starting point. Worth stating explicitly as a sanity check in the rewrite.

## What "fixed" looks like

**Fund [move A] at EUR Xm (owner, start date) and [move B] at EUR Ym (owner, start date); together they add approximately EUR Zm by 2031 against the EUR 18m gap to the EUR 80m target, with consolidated store margin held above 14% by [excluding further suburban/kiosk openings / specific mitigation].** Brightwell's EUR 62m revenue has been flat against a board target of EUR 80m by 2031; catering and online delivery are the two best-evidenced levers, while new suburban stores are excluded because suburban (13.1%) and station-kiosk (11.4%) formats already sit below the required margin floor, and franchising has been [evaluated and ruled out for reason X / included as move B]. The answer changes if catering take-up or online delivery margins miss the triangulated base case by more than [threshold].


## Files in work dir after run

- pr-01-input.md
