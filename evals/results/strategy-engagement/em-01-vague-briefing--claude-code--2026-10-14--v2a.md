# em-01-vague-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| does not start any analysis, market research or recommendation before the problem statement is agreed | yes | Turn 1 contains only clarifying questions; Turn 2 only restates answers into a problem statement and asks for confirmation, with no market analysis or recommendations given. |
| asks for the decision, the decision maker, a measurable target with a date, and constraints (grouped, ≤3 rounds) | yes | Turn 1 asks in one grouped round: 'What revenue...targeting, and by when?', 'Who makes this call...', capital/margin constraints, and scope exclusions. |
| produces a problem statement as one question naming decision maker, measurable outcome, date and constraints | yes | "...should the CEO recommend the board fund in the November 2026 budget to close the gap from EUR 60m to EUR 80m revenue by 2031, within an EUR 3m capital limit and without store-level margin falling below 14%..." |
| lists at least one item explicitly out of scope | yes | Table row: 'Out of scope / Acquisitions; expansion outside the home region' |
| asks the user to confirm the problem statement | yes | "Do you agree with this problem statement? Reply yes, or correct it." |
| writes engagement/<slug>/01-problem-statement.md (or prints under that heading) | yes | File 'engagement/bakery-chain/01-problem-statement.md' listed in files written and its content shown. |
| does not invent market data or competitor facts | yes | Only flagged assumptions about currency, target rationale, and capital timing are listed; no competitor names or market figures are invented. |
| does not produce a generic list of frameworks | yes | Output is a problem statement table and assumptions list, not a framework list (e.g., no SWOT/Porter's Five Forces mentioned). |

## Transcript

## Turn 1

**User:** We're a bakery chain, about 60 million in revenue, 41 stores. Growth has stalled. We want to grow. Can you help us figure out what to do?

This is a growth-strategy case. Before we analyze anything, I need to sharpen your ambition into one precise, decidable question — otherwise we'll just produce a busy-looking report that doesn't land on a decision.

**Restating what I heard:** A 41-store, ~$60M-revenue bakery chain whose growth has stalled, and you want to know what to do to get growing again.

To turn that into a real problem statement, I need answers to these (one round, grouped):

**The target and the gap**
1. What revenue (and profit/margin) are you targeting, and by when? Where does that number come from — a board plan, an investor commitment, a personal goal?
2. "Stalled" — flat total revenue, flat same-store sales, or both? For roughly how long, and do you have monthly/quarterly same-store-sales trends you could share?

**What's ruled out**
3. Is this organic-only, or is M&A (buying other bakery/café chains) on the table? Any explicit no-go's — franchising, new states/regions, new formats (e.g., wholesale, grocery/retail channel, delivery-only)?
4. How much capital is actually available to fund growth (new stores, remodels, systems), and is there a margin floor the plan can't breach?

**Who decides**
5. Who makes this call — you, a board, private-equity owners — and when's the next decision point (budget cycle, board meeting)?

**Diagnosis starting point**
6. Do you believe you're losing share in flat/growing markets, or is the whole category/your trade areas flat? Any read on same-store sales vs. new-unit contribution, and on unit economics (is a new store at $X revenue still paying back in Y years)?

Answer what you can — flag anything unknown and I'll mark it as an assumption to verify rather than block on it.


## Turn 2

**User:** Answers to your questions:
- Decision: the board sets the 2027 investment budget in November 2026.
- Decision maker: the board, prepared by the CEO.
- Target: EUR 80m revenue by 2031.
- Guardrail: store-level margin must stay above 14%.
- Capital available: about EUR 3m.
- Options people talk about: more stores, online delivery, office catering, franchising.
- Out of scope: acquisitions, leaving the home region.

I've written the problem statement to `engagement/bakery-chain/01-problem-statement.md`:

**Question:** Which combination of growth levers — more stores, online delivery, office catering, franchising, or a subset — should the CEO recommend the board fund in the November 2026 budget to close the gap from EUR 60m to EUR 80m revenue by 2031, within an EUR 3m capital limit and without store-level margin falling below 14%, given that acquisitions and expansion outside the home region are ruled out?

| Element | Content |
|---|---|
| Decision | Which growth lever(s) to fund: new stores, online delivery, office catering, franchising — or a combination |
| Decision maker | The Board; prepared by the CEO |
| Success criteria | EUR 80m revenue by 2031 (from ~EUR 60m, 41 stores) |
| Guardrails | Store-level margin > 14% |
| In scope | New stores, online/delivery, office catering, franchising — home region only |
| Out of scope | Acquisitions; expansion outside the home region |
| Constraints | ~EUR 3m capital; decision ready for November 2026 board meeting |

**Flagged assumptions** (don't block, but worth confirming): currency consistency between the EUR 60m current revenue and EUR 80m target; whether "stalled" means flat market vs. share loss; why the board picked EUR 80m/2031 specifically; whether EUR 3m is one-time, annual, or cumulative through 2031.

Do you agree with this problem statement, or want to correct anything?


## Files in work dir after run

- engagement/bakery-chain/01-problem-statement.md

## File written by the run: engagement/bakery-chain/01-problem-statement.md

# Problem statement: Bakery chain (41 stores, ~EUR 60m revenue)

**Question:** Which combination of growth levers — more stores, online delivery, office catering, franchising, or a subset — should the CEO recommend the board fund in the November 2026 budget to close the gap from EUR 60m to EUR 80m revenue by 2031, within an EUR 3m capital limit and without store-level margin falling below 14%, given that acquisitions and expansion outside the home region are ruled out?

| Element | Content |
|---|---|
| Decision | Which growth lever(s) to fund for the 2027 investment budget: more company-owned stores, online delivery, office catering, franchising — or some combination |
| Decision maker | The Board; prepared and proposed by the CEO |
| Success criteria | EUR 80m revenue by 2031 (from ~EUR 60m today, 41 stores) |
| Guardrails | Store-level margin must stay above 14% |
| In scope | Organic growth levers within the home region: new company-owned stores, online/delivery channel, office/corporate catering, franchising |
| Out of scope | Acquisitions of other chains; geographic expansion outside the home region |
| Constraints | ~EUR 3m capital available for the plan; decision must be ready for the November 2026 board meeting |
| Decision date | November 2026 (board sets 2027 investment budget) |

**Why this matters now:** Growth has stalled at 41 stores and ~EUR 60m revenue, and the board wants a funded plan to resume growth to EUR 80m by 2031. I haven't yet confirmed the root reason the board picked this target or deadline (e.g., financing covenant, shareholder expectation, competitive pressure) — flagged below.

**Flagged assumptions to verify:**
1. Current revenue (~EUR 60m) and the EUR 80m target are in the same currency — the first conversation mentioned "60 million" without specifying currency; your answers switched to EUR. I'm assuming both are EUR; please confirm.
2. "Growth has stalled" means store count and/or same-store sales have been flat — not yet confirmed whether this is a flat market, share loss, or both (needed to diagnose where the gap comes from).
3. Why the board set EUR 80m / 2031 specifically (e.g., investor return target, debt covenant, founder succession plan) — not yet known; doesn't block framing but may matter for urgency and risk tolerance.
4. EUR 3m capital is assumed to be a one-time or annual-equivalent pool for the whole plan period — please confirm whether it's a single injection, annual, or cumulative through 2031.

**Agreed by:** pending your confirmation

---

Do you agree with this problem statement? Reply yes, or correct it.

