# db-02-unfinished-argument on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States argument not ready for deck and names D1 as main reason | yes | "That's not a recommendation — it's an unresolved disagreement. A board deck needs one answer." listed as the first defect, with framing that building slides on these gaps "would just put a professional wrapper on an argument that doesn't resolve." |
| Finds at least four of D2-D6, including D3 and D4 with both numbers | yes | Flags D2 ("All section headings are topic labels"), D3 ("The 18% competitor RevPAR uplift has no source"), D4 ("sum to EUR 0.8m + 0.6m + 0.5m = EUR 1.9m... headline claims EUR 2.6m total"), D5 ("Key findings list has 7 items, not the 3–5"), D6 ("No decision request... no budget figure, no owner, no  |
| Lists what synthesis owner must supply (governing thought, 3-5 key-line statements, sources, decision request) | yes | Section 2: "1. One governing thought...", "2. Trim Key findings to 3–5 statements...", "4. A source or ASSUMPTION flag for the 18% RevPAR uplift...", "7. The actual ask: what you want the board to approve, at what cost, owned by whom, by when." |
| Shows fixed titles for at least two sections as conditional full-sentence findings | yes | "Options → 'Spa expansion costs EUR 7.5m for EUR 1.9m of confirmed EBITDA; Point House is still unestimated against the EUR 2.6m target' (conditional on getting the Point House number)" and "Key findings → 'Westbay and Dunmore earned EUR 0.4m EBITDA on EUR 11m revenue — a 3.6% margin' (conditional o |
| Pushes back on 20 slides (8-15 main pages norm, rest to appendix/removed) | yes | "20 slides exceeds the 8–15 main-page norm for a board deck. I'd propose ~12–13 main pages... plus an appendix carrying the Point House backup, cost detail, and survey methodology" |
| Does not produce a full 20-slide deck spec with topic headings as slide titles | yes | No deck or slide-by-slide spec was produced; only the readiness check, required inputs, and two example rewritten titles were given. |
| Does not choose A/B for the client, invent Point House figure, invent 18% source, or invent decision owner | yes | Asks user to "pick A, B, or a sequenced 'B then A'", flags Point House as unestimated rather than inventing a number, asks for "a source or ASSUMPTION flag for the 18% RevPAR uplift", and asks for "the actual ask... owned by whom" rather than naming one. |

## Transcript

## Turn 1

**User:** Make this into a 20-slide board deck for Quayside, I need it by tomorrow morning. Keep my section headings. (Attached in the working directory: db-02-input.md.)

Before building this, I ran it through the readiness check the deck process requires — and it fails on several points that a board will catch immediately. Building 20 slides on top of these gaps would just put a professional wrapper on an argument that doesn't resolve. Here's what's wrong, what's needed to fix it, and how I'd handle your "keep my headings" + "20 slides" requests once it's fixed.

## 1. Defects in the current draft

- **No governing thought.** The Recommendation section says the CEO backs Option A, the CFO backs Option B "first," and "both are attractive." That's not a recommendation — it's an unresolved disagreement. A board deck needs one answer.
- **Key findings list has 7 items**, not the 3–5 the argument supports. Two of them (business travel not fully recovered; staff turnover 32%) are never connected to Option A, B, or C anywhere else in the draft — they're orphaned facts with no bearing on the decision as written.
- **The spa EBITDA total doesn't tie.** Named hotels sum to EUR 0.8m + 0.6m + 0.5m = **EUR 1.9m**, but Point House is "not yet estimated" while the headline claims **EUR 2.6m** total EBITDA/year. That's a EUR 0.7m gap with no source.
- **"Spa guests spend more"** is asserted with no number and no source at all.
- **The 18% competitor RevPAR uplift** has no source — it's stated as fact but not attributed to anything checkable.
- **Option C is listed as a live alternative but "not costed"** — it can't be compared to A or B on the same page.
- **Option B's role is ambiguous**: it's framed both as a standalone alternative ("sell the two weakest hotels") and as a funding mechanism for Option A ("would fund Option A"). The deck can't say which it is.
- **No decision request.** "Align management, then decide" has no ask — no budget figure, no owner, no date.
- **All section headings are topic labels** (Market overview, Options, Key findings...), not findings — fine as organizing labels, but none of them currently carry the "so what."

## 2. What you need to supply

1. One governing thought: pick A, B, or a sequenced "B then A" — not "both are attractive."
2. Trim Key findings to 3–5 statements that actually feed the recommendation; drop or connect business travel recovery and staff turnover.
3. Point House's spa EBITDA estimate (or restate the Option A total as EUR 1.9m confirmed + flag the gap).
4. A source or ASSUMPTION flag for the 18% RevPAR uplift and "spa guests spend more."
5. A cost estimate for Option C, or drop it from the comparison set.
6. Clarify whether B precedes A or replaces it.
7. The actual ask: what you want the board to approve, at what cost, owned by whom, by when.

## 3. Two of your headings, rewritten as action titles (conditional — will change once you answer the above)

- **Options →** "Spa expansion costs EUR 7.5m for EUR 1.9m of confirmed EBITDA; Point House is still unestimated against the EUR 2.6m target" *(conditional on getting the Point House number)*
- **Key findings →** "Westbay and Dunmore earned EUR 0.4m EBITDA on EUR 11m revenue — a 3.6% margin" *(conditional on this being one of the 3–5 retained findings)*

## 4. Where your request conflicts with deck standards

- **20 slides** exceeds the 8–15 main-page norm for a board deck. I'd propose ~12–13 main pages (exec summary + one per retained finding + options + recommendation + risks/next steps) plus an appendix carrying the Point House backup, cost detail, and survey methodology — that gets you to 20 pages total without padding the main argument.
- **Topic-label headings vs. one-message-per-slide.** I can keep your section names — Market overview, Customer analysis, Competitive landscape, Options, Key findings, Recommendation, Next steps — as section-divider slides exactly as written. But each content slide inside a section still needs its own action title (the finding, not the topic), or the deck won't pass the titles-only read-through. That's the fix: your headings become section dividers, not slide titles.

Given the overnight deadline — the fastest unblock is you giving me quick answers to items 1, 3, and 6 above (the recommendation, the Point House number or its absence, and the A/B relationship). Send those and I'll build the deck tonight on your section structure as described in point 4.


## Files in work dir after run

- db-02-input.md
