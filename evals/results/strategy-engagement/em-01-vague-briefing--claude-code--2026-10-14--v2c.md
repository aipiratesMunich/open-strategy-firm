# em-01-vague-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: does not start any analysis, market research or recommendation before the problem statement is agreed. | yes | Turn 1 only asks clarifying questions; Turn 2 only produces the problem statement and asks for confirmation, with no analysis or recommendations offered. |
| Must: asks for the decision, the decision maker, a measurable target with a date, and constraints (questions may be grouped; no more than about three rounds). | yes | Turn 1 grouped questions cover target/date ('Is there a number and date already in mind'), decision maker ('Who actually decides the growth plan'), and constraints ('Anything already ruled out', 'Any hard floors') — all within a single round. |
| Must: produces a problem statement as one question naming decision maker, measurable outcome, date and constraints. | yes | "Which combination of growth levers should the board fund ... to take the chain from about EUR 60m to EUR 80m revenue by 2031, without store-level margin falling below 14%, given about EUR 3m of available capital and no acquisitions or expansion outside the home region?" |
| Must: lists at least one item explicitly out of scope. | yes | Table row: 'Out of scope / Acquisitions; expansion outside the home region'. |
| Must: asks the user to confirm the problem statement. | yes | "Do you agree with this problem statement? Reply yes, or correct it." |
| Must: writes engagement/<slug>/01-problem-statement.md (or prints it under that heading if files cannot be written). | yes | File listed: engagement/bakery-co/01-problem-statement.md, matching the printed content. |
| Must not: invent market data or competitor facts. | yes | Instead of inventing data, the run flags unknowns: 'Current channel mix ... unknown', 'whether the chain is losing share to named competitors — unknown.' |
| Must not: produce a generic list of frameworks. | yes | No framework list (e.g., SWOT/Porter's Five Forces) appears anywhere in the transcript; only a tailored problem-statement table. |

## Transcript

## Turn 1

**User:** We're a bakery chain, about 60 million in revenue, 41 stores. Growth has stalled. We want to grow. Can you help us figure out what to do?

Bakery chain, ~$60M revenue, 41 stores, growth has stalled, and you want to find a path back to growth — that's the briefing as I understand it. This is a **growth strategy** question, so before I build any analysis I need to sharpen it into something testable. A few grounding questions, grouped:

**On the target and decision**
1. Is there a number and date already in mind (e.g., "$80M by 2029"), or is this open — and where does the ambition come from (owners, board, investors, a lender covenant)?
2. Who actually decides the growth plan, and when do they need an answer (next board meeting, budget cycle, etc.)?
3. Anything already ruled out — taking on debt, outside investors, franchising, closing stores, specific geographies?
4. Any hard floors — minimum margin, max capital to deploy, headcount limits?

**On where growth stalled** (this is the crux of the issue tree)
5. "Stalled" — is that flat same-store sales at existing 41 stores, or new-store openings that stopped, or both?
6. Channel mix: what split is retail storefront vs. wholesale/grocery vs. catering/events vs. e-commerce/delivery — and did any one of those specifically go flat?
7. Footprint: are the 41 stores concentrated in one metro/region, or spread across multiple markets? Any read on whether the *market* (local demand) is flat/shrinking vs. you're losing share to specific competitors?
8. Roughly how long has growth been stalled, and was there a trigger (new competitor, pricing move, post-COVID normalization, etc.)?

You don't need precise numbers for all of these — rough answers are enough for me to size the gap and build the right branches. Anything you genuinely don't know, just say so and I'll flag it as an open assumption rather than block on it.


## Turn 2

**User:** Answers to your questions:
- Decision: the board sets the 2027 investment budget in November 2026.
- Decision maker: the board, prepared by the CEO.
- Target: EUR 80m revenue by 2031.
- Guardrail: store-level margin must stay above 14%.
- Capital available: about EUR 3m.
- Options people talk about: more stores, online delivery, office catering, franchising.
- Out of scope: acquisitions, leaving the home region.

# Problem statement: Bakery Co (41-store bakery chain)

**Question:** Which combination of growth levers should the board fund in the November 2026 budget decision (for the 2027 investment year) to take the chain from about EUR 60m to EUR 80m revenue by 2031, without store-level margin falling below 14%, given about EUR 3m of available capital and no acquisitions or expansion outside the home region?

| Element | Content |
|---|---|
| Decision | Which growth levers to fund for 2027 onward — candidates on the table: new store openings, online/delivery, office catering, franchising, plus any core (existing-store) improvement |
| Decision maker | The board; prepared and proposed by the CEO |
| Success criteria | EUR 80m revenue by 2031 (from ~EUR 60m today, 41 stores) — a gap of ~EUR 20m, +33% |
| Guardrails | Store-level margin must not fall below 14% |
| In scope | Home region; organic levers (new units, delivery/online, office catering, franchising); core same-store performance |
| Out of scope | Acquisitions; expansion outside the home region |
| Constraints | ~EUR 3m capital available; decision at the November 2026 board meeting, funding the 2027 budget |
| Decision date | November 2026 |

**Why this matters now:** Growth has stalled and the board wants a funded, multi-year plan in place before committing the 2027 budget. The deeper driver behind the EUR 80m/2031 target hasn't been stated — flagged below.

**Flagged assumptions to verify:**
1. Base-year revenue and target are both in EUR (~EUR 60m now vs. the originally-cited $60m) — treating as EUR throughout; needs confirmation.
2. Whether "growth has stalled" means flat same-store sales at the 41 stores, a stop in new-store openings, or both — not yet answered.
3. Current channel mix (retail storefront vs. wholesale/grocery vs. catering/events vs. e-commerce/delivery) and which channel went flat — unknown.
4. Geographic concentration of the 41 stores within the home region, and whether the served market is flat/shrinking or the chain is losing share to named competitors — unknown.
5. Whether the ~EUR 3m capital is a one-year (2027) figure or available across the plan to 2031 — assuming one-year unless corrected.
6. The underlying driver behind the EUR 80m/2031 ambition (investor, succession, covenant, competitive) — not stated.

**Do you agree with this problem statement? Reply yes, or correct it.**


## Files in work dir after run

- engagement/bakery-co/01-problem-statement.md

## File written by the run: engagement/bakery-co/01-problem-statement.md

# Problem statement: Bakery Co (41-store bakery chain)

**Question:** Which combination of growth levers should the board fund in the November 2026 budget decision (for the 2027 investment year) to take the chain from about EUR 60m to EUR 80m revenue by 2031, without store-level margin falling below 14%, given about EUR 3m of available capital and no acquisitions or expansion outside the home region?

| Element | Content |
|---|---|
| Decision | Which growth levers to fund for 2027 onward — candidates on the table: new store openings, online/delivery, office catering, franchising, plus any core (existing-store) improvement |
| Decision maker | The board; prepared and proposed by the CEO |
| Success criteria | EUR 80m revenue by 2031 (from ~EUR 60m today, 41 stores) — a gap of ~EUR 20m, +33% |
| Guardrails | Store-level margin must not fall below 14% |
| In scope | Home region; organic levers (new units, delivery/online, office catering, franchising); core same-store performance |
| Out of scope | Acquisitions; expansion outside the home region |
| Constraints | ~EUR 3m capital available; decision at the November 2026 board meeting, funding the 2027 budget |
| Decision date | November 2026 |

**Why this matters now:** Growth has stalled and the board wants a funded, multi-year plan in place before committing the 2027 budget. The deeper reason the EUR 80m/2031 target matters (investor expectation, succession, competitive pressure) has not been stated — flagged below.

**Flagged assumptions to verify:**
1. Base-year revenue and target are both in EUR (~EUR 60m now vs. the originally-cited $60m) — treating as EUR throughout; needs confirmation.
2. Whether "growth has stalled" means flat same-store sales at the 41 stores, a stop in new-store openings, or both — not yet answered.
3. Current channel mix (retail storefront vs. wholesale/grocery vs. catering/events vs. e-commerce/delivery) and which channel went flat — unknown.
4. Geographic concentration of the 41 stores within the home region, and whether the served market is flat/shrinking or the chain is losing share to named competitors — unknown.
5. Whether the ~EUR 3m capital is a one-year (2027) figure or available across the plan to 2031 — assuming one-year unless corrected.
6. The underlying driver behind the EUR 80m/2031 ambition (investor, succession, covenant, competitive) — not stated.

**Agreed by:** pending — awaiting user confirmation

