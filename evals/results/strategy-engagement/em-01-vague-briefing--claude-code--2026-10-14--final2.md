# em-01-vague-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: does not start any analysis, market research or recommendation before the problem statement is agreed. | yes | Turn 1 only asks clarifying questions ('Before I analyze anything, I need to pin that down'); Turn 2 produces only the problem statement and asks for confirmation, no analysis or recommendations given. |
| Must: asks for the decision, the decision maker, a measurable target with a date, and constraints (questions may be grouped; no more than about three rounds). | yes | Turn 1 asks 'Who actually decides the growth plan...', 'What revenue... are you trying to hit, and by when?', and constraints like capital cap and margin floor, all grouped in one round. |
| Must: produces a problem statement as one question naming decision maker, measurable outcome, date and constraints. | yes | "Which combination of growth moves should the CEO recommend for the board to fund in the November 2026 2027 investment budget, in order to reach EUR 80m revenue by 2031... within EUR 3m of capital and without store-level margin falling below 14%, given that acquisitions and expansion outside the hom |
| Must: lists at least one item explicitly out of scope. | yes | "Out of scope / Acquisitions; expansion outside the home region" |
| Must: asks the user to confirm the problem statement. | yes | "Do you agree with this problem statement? Reply yes, or correct it." |
| Must: writes engagement/<slug>/01-problem-statement.md (or prints it under that heading if files cannot be written). | yes | File listed: engagement/bakery-chain/01-problem-statement.md, with matching content shown. |
| Must not: invent market data or competitor facts. | yes | No competitor names or market statistics appear anywhere in the transcript; only user-supplied figures (revenue, stores, budget) are used. |
| Must not: produce a generic list of frameworks. | yes | No framework list (e.g., SWOT/Porter's) appears; output is a tailored problem statement table. |

## Transcript

## Turn 1

**User:** We're a bakery chain, about 60 million in revenue, 41 stores. Growth has stalled. We want to grow. Can you help us figure out what to do?

Got it — this is exactly a "we need to grow" briefing, which is sharp-sounding but actually vague: no decision, no target, no deadline. Before I analyze anything, I need to pin that down, otherwise any answer I give will be a list of generic ideas rather than a decision you can act on.

**Restating your briefing in your words:** "We're a bakery chain, ~$60M revenue, 41 stores, growth has stalled. We want to grow."

That's an ambition, not yet a decision. Here's what I need from you to turn it into one — answer what you can, and it's fine to say "don't know" on some:

**1. The target and the clock**
- What revenue (and profit/margin) are you trying to hit, and by when? Is there a board- or investor-set number, or should I help you set one?
- Who actually decides the growth plan, and when's the next meeting/budget cycle it needs to land in?

**2. What's already off the table**
- Is this franchising? New geographies? M&A (buying other bakery chains)? New channels (wholesale/grocery, e-commerce, catering)? Anything the board/ownership has already ruled out?
- Capital available to spend on this — is there a cap?
- Margin floor — is there a level profitability can't fall below while you grow?

**3. The "why stalled" diagnosis — this is the one I most need your gut read on**
- Is same-store revenue flat, or are total sales flat because store count stopped growing while existing stores still grow? (i.e., is this a *new unit* problem or a *same-store* problem?)
- Do you believe you're losing share to competitors in existing markets, or is the whole category/market flat (people just aren't buying more baked goods)?
- Has unit economics on new stores gotten worse (harder to find good sites, rents up, labor costs up), which is why store count growth stopped?

**4. Basic shape of the business** (so I don't assume wrong)
- Roughly what's average revenue per store, and how does that vary — is low performance concentrated in certain stores/regions?
- Retail-only, or do you also sell wholesale/through grocery, e-commerce, catering?
- Owned/operated stores only, or any franchised/licensed units?

Take your time — even rough, directional answers to these are enough for me to build a real issue tree and a day-one answer rather than guessing.


## Turn 2

**User:** Answers to your questions:
- Decision: the board sets the 2027 investment budget in November 2026.
- Decision maker: the board, prepared by the CEO.
- Target: EUR 80m revenue by 2031.
- Guardrail: store-level margin must stay above 14%.
- Capital available: about EUR 3m.
- Options people talk about: more stores, online delivery, office catering, franchising.
- Out of scope: acquisitions, leaving the home region.

Here's the problem statement — written to `engagement/bakery-chain/01-problem-statement.md`:

# Problem statement: Bakery chain (41 stores, ~€60m revenue)

**Question:** Which combination of growth moves should the CEO recommend for the board to fund in the November 2026 2027 investment budget, in order to reach EUR 80m revenue by 2031 (from a stalled base of ~EUR 60m), within EUR 3m of capital and without store-level margin falling below 14%, given that acquisitions and expansion outside the home region are ruled out?

| Element | Content |
|---|---|
| Decision | Which growth lever(s) — more stores, online delivery, office catering, franchising, and/or core-performance fixes — to fund in the 2027 budget, and at what size |
| Decision maker | The board; prepared and proposed by the CEO |
| Success criteria | EUR 80m revenue by 2031 (from ~EUR 60m today); ~EUR 20m / ~33% growth over 5 years, ~6%/year compounded |
| Guardrails | Store-level margin must stay above 14% throughout |
| In scope | Same-region store growth, online delivery, office/B2B catering, franchising, core same-store performance (pricing, mix, underperforming stores) |
| Out of scope | Acquisitions; expansion outside the home region |
| Constraints | Capital available: ~EUR 3m; decision must be ready for the November 2026 board meeting (2027 budget cycle) |
| Decision date | November 2026 |

**Why this matters now:** Growth has stalled at ~41 stores and ~EUR 60m revenue, and the board needs a funded, credible plan in the 2027 budget to resume growth toward EUR 80m by 2031.

**Flagged assumptions to verify:**
1. **Currency.** You first said "~60 million" without a currency; the target is EUR 80m. I'm assuming the current base is also ~EUR 60m, not USD — please confirm, since that changes the size of the gap.
2. **What the EUR 3m actually funds.** Closing a ~EUR 20m gap usually needs more than EUR 3m if it means building company-owned stores. I'm reading EUR 3m as the company's own cash (pilots, a delivery platform, franchise program setup, remodels) — not the total capital behind the plan, since franchising is largely funded by franchisees. Please confirm this reading, because it determines which levers are even affordable.
3. **Why growth stalled is still open** — market flat, losing share, new-store economics gone bad, or same-store decline. This is the first thing the analysis tests.
4. **Store performance spread and channel mix** (revenue/store, retail vs. wholesale/catering today) — not yet known, will shape lever sizing.

---

**Phase 1 done: Frame**
- Current answer: not yet — framing only
- Changed since last phase: n/a (first phase)
- Partner gate: self-reviewed against gate-1 checklist (right question, names decision/maker/outcome/date, scope has explicit outs) — no blockers found, pending your confirmation below
- Next: once you confirm (or correct) the problem statement, I'll build the issue tree and a day-one answer; need from you: **confirm assumptions 1 and 2 above, and reply yes or correct the statement**


## Files in work dir after run

- engagement/bakery-chain/01-problem-statement.md

## File written by the run: engagement/bakery-chain/01-problem-statement.md

# Problem statement: Bakery chain (41 stores, ~EUR 60m revenue)

**Question:** Which combination of growth moves should the CEO recommend for the board to fund in the November 2026 2027 investment budget, in order to reach EUR 80m revenue by 2031 (from a stalled base of ~EUR 60m), within EUR 3m of capital and without store-level margin falling below 14%, given that acquisitions and expansion outside the home region are ruled out?

| Element | Content |
|---|---|
| Decision | Which growth lever(s) — more stores, online delivery, office catering, franchising, and/or core-performance fixes — to fund in the 2027 budget, and at what size |
| Decision maker | The board; prepared and proposed by the CEO |
| Success criteria | EUR 80m revenue by 2031 (from ~EUR 60m today); implies roughly EUR 20m / ~33% growth over 5 years, about 6%/year compounded |
| Guardrails | Store-level margin must stay above 14% throughout |
| In scope | Same-region store growth, online delivery, office/B2B catering, franchising, core same-store performance (pricing, mix, underperforming stores) |
| Out of scope | Acquisitions; expansion outside the home region |
| Constraints | Capital available: ~EUR 3m; decision must be ready for the November 2026 board meeting (2027 budget cycle) |
| Decision date | November 2026 |

**Why this matters now:** Growth has stalled at ~41 stores and ~EUR 60m revenue, and the board needs a funded, credible plan in the 2027 budget to resume growth toward EUR 80m by 2031.

**Flagged assumptions to verify:**
1. **Currency/baseline consistency.** You first described revenue as "~60 million" without specifying currency; the target was given as EUR 80m. I'm assuming the current ~EUR 60m baseline is in the same currency as the target. Please confirm — if the current base is actually ~USD 60m, the gap is a different number in EUR terms.
2. **Nature of the EUR 3m capital figure.** Growing revenue by ~EUR 20m typically needs more capital than EUR 3m if it means building new company-owned stores. I'm treating EUR 3m as the capital the *company* puts in (e.g., pilots, a delivery platform, franchise program setup, remodels) — not the total investment behind the plan, since franchising in particular is funded largely by franchisees' capital, not the company's. This needs confirming with you, because it changes which levers are even feasible.
3. **Diagnosis of the stall is still open.** I don't yet know whether the ~41-store plateau and flat revenue are because (a) the market/category is flat, (b) you're losing share to competitors, (c) new-store unit economics worsened (so store count growth stopped on purpose), or (d) existing stores are flat/declining same-store. This is the first thing the analysis will test, and it changes which lever is the real priority.
4. **Store performance variance and channel mix** (average revenue/store, spread across stores, how much of today's EUR 60m is wholesale/catering vs. walk-in retail) is not yet known and will shape lever sizing.

These four will be tested as the first branch of the analysis (items 1-2 need your input before we proceed; items 3-4 we'll size from your data).

---

Do you agree with this problem statement? Reply yes, or correct it.

