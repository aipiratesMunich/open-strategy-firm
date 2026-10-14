# em-01-vague-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: does not start any analysis, market research or recommendation before the problem statement is agreed. | yes | Turn 1 only asks clarifying questions; Turn 2 presents the problem statement and explicitly defers: 'once agreed, I'll build the issue tree and ghost deck' |
| Must: asks for the decision, the decision maker, a measurable target with a date, and constraints (grouped, ≤3 rounds) | yes | Turn 1 asks 'What's the growth target... by what year?', 'Who makes this decision, and when', and capital/margin constraints, all in one round |
| Must: produces a problem statement as one question naming decision maker, measurable outcome, date and constraints | yes | "What combination of growth moves should the CEO recommend for the board to fund in the November 2026 budget for 2027, to reach EUR 80m revenue by 2031... within an EUR 3m capital limit and without store-level margin falling below 14%..." |
| Must: lists at least one item explicitly out of scope | yes | 'Out of scope / Acquisitions; expansion outside the home region' |
| Must: asks the user to confirm the problem statement | yes | "Reply 'yes' if this is right, or correct any of the above" |
| Must: writes engagement/<slug>/01-problem-statement.md | yes | File listed: engagement/bakery-chain/01-problem-statement.md |
| Must not: invent market data or competitor facts | yes | No market/competitor figures introduced; open items flagged as assumptions to verify in Phase 2 |
| Must not: produce a generic list of frameworks | yes | Response is a structured problem statement table, not a generic framework list |

## Transcript

## Turn 1

**User:** We're a bakery chain, about 60 million in revenue, 41 stores. Growth has stalled. We want to grow. Can you help us figure out what to do?

No existing engagement folder — this is a fresh start. This is a growth-strategy case: full engagement, Phase 1 (Frame).

Restating the briefing: *"A bakery chain, ~$60M revenue, 41 stores, has stalled growth, and wants to grow."* That's an ambition, not yet a decision — I need a few specifics before building the issue tree or suggesting any levers.

Two rounds max, so let me ask the essentials in one group:

**On the target and decision:**
1. What's the growth target — a revenue number, store count, or both — and by what year? Where does that number come from (board, investor, owner)?
2. Who makes this decision, and when — board meeting, investor update, internal plan?
3. Is there a hard constraint on capital available to invest, and a margin floor you can't go below?

**On what's already decided or off the table:**
4. Has anything already been ruled out — e.g., franchising, opening in new regions, taking on outside capital, acquisitions?

**On the diagnosis — "growth has stalled" could mean different things:**
5. Stalled how: same-store sales flat/declining, or store count flat (not opening new ones), or both? Over what period did this start?
6. Any read on *why* — losing share to competitors, market itself flat, pulled back on new-store openings, cost/labor pressure squeezing expansion appetite, something else?

If you don't have precise answers to all of these, rough numbers or "ask the CFO" is fine for now — I'll flag open items as assumptions rather than block on them.


## Turn 2

**User:** Answers to your questions:
- Decision: the board sets the 2027 investment budget in November 2026.
- Decision maker: the board, prepared by the CEO.
- Target: EUR 80m revenue by 2031.
- Guardrail: store-level margin must stay above 14%.
- Capital available: about EUR 3m.
- Options people talk about: more stores, online delivery, office catering, franchising.
- Out of scope: acquisitions, leaving the home region.

Here's the problem statement I'd lock in before doing any analysis:

# Problem statement: Bakery chain (41 stores)

**Question:** What combination of growth moves should the CEO recommend for the board to fund in the November 2026 budget for 2027, to reach EUR 80m revenue by 2031 (from an EUR 60m base), within an EUR 3m capital limit and without store-level margin falling below 14%, given that acquisitions and expansion outside the home region are ruled out?

| Element | Content |
|---|---|
| Decision | Which growth lever(s) to fund for 2027 — candidates on the table: more stores, online delivery, office catering, franchising |
| Decision maker | The board; proposed by the CEO. Sits November 2026 |
| Success criteria | EUR 80m revenue by 2031 (from EUR 60m — roughly 5–6% CAGR) |
| Guardrails | Store-level margin ≥ 14%; ~EUR 3m capital |
| In scope | Store growth, online delivery, office catering, franchising — home region only |
| Out of scope | Acquisitions; expansion outside the home region |
| Decision date | November 2026 |

**Flagged assumptions I need you to confirm or correct:**

1. **Currency mismatch** — your first message said "$60 million" revenue; your follow-up answers were all in EUR. I'm treating the base as EUR 60m to match the EUR 80m target. If it's actually USD, the gap size changes.
2. **Is the EUR 3m capital the total through 2031, or just the 2027 tranche?** This drives how many levers you can fund at once — one store format test looks very different from one store format test plus a delivery platform plus franchising infrastructure.
3. **Where does the EUR 80m/2031 number come from**, and **why has growth stalled** — flat market, losing share, or did the company itself stop opening stores? I haven't asked this yet; it changes which levers are even plausible.
4. **"Store-level margin"** — assuming this means four-wall contribution margin per store, not blended company-wide margin. Confirm?

Reply "yes" if this is right, or correct any of the above — once agreed, I'll build the issue tree and ghost deck (the hypotheses we'll test, including sizing each of the four levers you named against the gap).


## Files in work dir after run

- engagement/bakery-chain/01-problem-statement.md

## File written by the run: engagement/bakery-chain/01-problem-statement.md

# Problem statement: Bakery chain (41 stores)

**Question:** What combination of growth moves should the CEO recommend for the board to fund in the November 2026 budget for 2027, to reach EUR 80m revenue by 2031 (from an EUR 60m base), within an EUR 3m capital limit and without store-level margin falling below 14%, given that acquisitions and expansion outside the home region are ruled out?

| Element | Content |
|---|---|
| Decision | Which growth lever(s) to fund for 2027 — candidates on the table: more stores, online delivery, office catering, franchising. Not yet decided: size, sequencing and split of capital across them. |
| Decision maker | The board; prepared and proposed by the CEO. Board sits November 2026. |
| Success criteria | EUR 80m revenue by 2031 (from EUR 60m today — a 33% increase, implying roughly 5–6% CAGR) |
| Guardrails | Store-level margin must not fall below 14%; total capital for the plan is about EUR 3m |
| In scope | Store network growth, online delivery, office catering, franchising — within the home region |
| Out of scope | Acquisitions; expansion outside the home region |
| Constraints | EUR 3m capital available; board decision timed to the November 2026 budget cycle; 41 existing stores, currently EUR 60m revenue |
| Decision date | November 2026 (board sets the 2027 investment budget) |

**Why this matters now:** Not yet established — I haven't asked why growth stalled or why EUR 80m by 2031 is the target (board ambition, investor expectation, owner succession, competitive pressure). Flagged below.

**Flagged assumptions to verify:**
1. Current revenue base is EUR 60m. (Your first message said "$60 million" in USD; your later answers switched to EUR throughout. I'm treating the base as EUR 60m for consistency with the EUR 80m target — please confirm, since a USD/EUR mismatch would change the size of the gap.)
2. EUR 3m capital is the total available across the whole plan through 2031, not just the 2027 tranche. Please confirm — this materially changes how many levers can be funded at once.
3. The EUR 80m/2031 target's origin (board ambition, investor commitment, succession plan, competitive response) and why growth stalled (flat market, share loss, or the company itself pulled back on openings) are not yet known. These affect which levers are plausible and how hard the gap really is to close — will treat as open until Phase 2 research.
4. "Store-level margin" is assumed to mean four-wall EBITDA or contribution margin at the individual store, not blended company margin. Please confirm the definition.
5. No explicit statement on whether headcount, brand, or other guardrails apply beyond the 14% margin floor and EUR 3m capital — assuming none for now.

**Agreed by:** pending — please confirm or correct this problem statement.

