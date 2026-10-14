# em-01-vague-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: does not start any analysis, market research or recommendation before the problem statement is agreed. | yes | Turn 1 only asks grouped clarifying questions; Turn 2 only produces the problem statement document, no market analysis or recommendations given. |
| Must: asks for the decision, the decision maker, a measurable target with a date, and constraints (questions may be grouped; no more than about three rounds). | yes | Turn 1 round one groups: 'The target and timeline' (target/date, decision maker), 'What's already off the table' (constraints), all in a single round. |
| Must: produces a problem statement as one question naming decision maker, measurable outcome, date and constraints. | yes | "Which combination of growth levers should the board fund in the November 2026 budget decision ... to reach EUR 80m revenue by 2031 ... within ~EUR 3m of available capital and without store-level margin falling below 14%, given that acquisitions and expansion outside the home region are ruled out?" |
| Must: lists at least one item explicitly out of scope. | yes | "Out of scope / Acquisitions; expansion outside the home region" |
| Must: asks the user to confirm the problem statement. | yes | "Do you agree with this problem statement? Reply yes, or correct it — in particular, please confirm or correct assumptions 2 ... and 4..." |
| Must: writes engagement/<slug>/01-problem-statement.md (or prints it under that heading if files cannot be written). | yes | File listed: engagement/bakery-co/01-problem-statement.md, with matching content shown. |
| Must not: invent market data or competitor facts. | yes | No market data, competitor names, or figures beyond what the user supplied appear anywhere in the transcript. |
| Must not: produce a generic list of frameworks. | yes | No framework list (e.g., Ansoff, Porter's Five Forces) appears in either turn. |

## Transcript

## Turn 1

**User:** We're a bakery chain, about 60 million in revenue, 41 stores. Growth has stalled. We want to grow. Can you help us figure out what to do?

This is a full engagement — a growth strategy case. Before any analysis, I need to sharpen the question. Here's round one of questions, grouped:

**The target and timeline**
1. What revenue (and profit/margin) are you aiming for, and by when? Where does that number come from — board, investors, owners?
2. Who decides on the growth plan, and at what meeting? What will they actually approve — a budget, a set of initiatives, first moves?

**What's already off the table**
3. Is anything ruled out — new debt/equity raises, acquisitions, franchising, specific geographies?
4. How much capital is available to fund growth, and is there a margin floor the plan can't breach?

**Diagnosing the stall**
5. "Growth has stalled" — is that flat same-store sales, store count stuck at 41, or both? Roughly how long has it been flat, and does it track the broader bakery/QSR market, or are you underperforming competitors in your markets?
6. Are the 41 stores company-owned, franchised, or a mix? One region or spread out?

**Why now**
7. What's driving the urgency to fix this now — a board mandate, an investor, a refinancing event, something else?

Answer what you can — anything you don't know yet, I'll flag as an assumption and we'll keep moving.


## Turn 2

**User:** Answers to your questions:
- Decision: the board sets the 2027 investment budget in November 2026.
- Decision maker: the board, prepared by the CEO.
- Target: EUR 80m revenue by 2031.
- Guardrail: store-level margin must stay above 14%.
- Capital available: about EUR 3m.
- Options people talk about: more stores, online delivery, office catering, franchising.
- Out of scope: acquisitions, leaving the home region.

I've written the problem statement to `engagement/bakery-co/01-problem-statement.md`. Here it is:

# Problem statement: Bakery Co (41-store chain, ~EUR 60m revenue)

**Question:** Which combination of growth levers should the board fund in the November 2026 budget decision (for the 2027 investment year) to reach EUR 80m revenue by 2031 (from ~EUR 60m today), within ~EUR 3m of available capital and without store-level margin falling below 14%, given that acquisitions and expansion outside the home region are ruled out?

| Element | Content |
|---|---|
| Decision | Which growth levers to fund for 2027 (and the trajectory through 2031): candidates on the table are new store openings, online delivery, office/corporate catering, and franchising. Core-business levers (pricing, mix, same-store traffic) are implicitly in scope too. |
| Decision maker | The board, on a plan prepared by the CEO |
| Success criteria | EUR 80m revenue by 2031 (gap of ~EUR 20m, roughly +33% over 5 years, off a ~EUR 60m base) |
| Guardrails | Store-level margin must not fall below 14% |
| In scope | Home-region operations; the four named levers (stores, delivery, catering, franchising); core/same-store performance of the existing 41 stores |
| Out of scope | Acquisitions; expansion outside the home region |
| Constraints | ~EUR 3m capital available; board decides November 2026 for the 2027 budget; target horizon runs to 2031 |
| Decision date | November 2026 |

**Why this matters now:** Not yet established — flagged below.

**Flagged assumptions to verify:**
1. **Currency/base revenue** — assuming EUR throughout; confirm the ~60m figure is on the same basis as the 80m target.
2. **Capital envelope** — assuming EUR 3m is the capital pool for 2027 specifically, not the entire budget through 2031. This matters a lot: if EUR 3m is truly all the capital through 2031, it caps how many levers (especially new stores) are affordable.
3. **Nature of the stall** — not yet known whether it's same-store sales decline, a stuck store count, a flat market, or share loss. First hypothesis to test, not assumed.
4. **Store ownership model** — unknown if the 41 stores are company-owned or franchised. Directly affects how the franchising lever would work.
5. **Why now** — no stated trigger behind the 2031 target; assuming standard planning cycle for now.

Do you agree with this problem statement? Reply yes, or correct it — in particular, please confirm or correct assumptions 2 (is EUR 3m the total through 2031 or just 2027?) and 4 (store ownership model), since those two change the shape of the answer the most.


## Files in work dir after run

- engagement/bakery-co/01-problem-statement.md

## File written by the run: engagement/bakery-co/01-problem-statement.md

# Problem statement: Bakery Co (41-store chain, ~EUR 60m revenue)

**Question:** Which combination of growth levers should the board fund in the November 2026 budget decision (for the 2027 investment year) to reach EUR 80m revenue by 2031 (from ~EUR 60m today), within ~EUR 3m of available capital and without store-level margin falling below 14%, given that acquisitions and expansion outside the home region are ruled out?

| Element | Content |
|---|---|
| Decision | Which growth levers to fund for 2027 (and the trajectory through 2031): candidates on the table are new store openings, online delivery, office/corporate catering, and franchising. Core-business levers (pricing, mix, same-store traffic) are implicitly in scope too, since the client named a target, not a shortlist. |
| Decision maker | The board, on a plan prepared by the CEO |
| Success criteria | EUR 80m revenue by 2031 (gap of ~EUR 20m, or roughly +33% over 5 years, against a base of ~EUR 60m) |
| Guardrails | Store-level margin must not fall below 14% |
| In scope | Home-region operations; the four named levers (stores, delivery, catering, franchising); core/same-store performance of the existing 41 stores |
| Out of scope | Acquisitions; expansion outside the home region |
| Constraints | ~EUR 3m capital available; board decides November 2026 for the 2027 budget; target horizon runs to 2031 |
| Decision date | November 2026 |

**Why this matters now:** Not yet established with the client — flagged below.

**Flagged assumptions to verify:**
1. **Currency and base revenue.** The initial briefing said "~60 million" with no currency; the target and capital figures were given in EUR. Assuming EUR throughout. Confirm the current ~EUR 60m figure and whether it's the same fiscal-year basis as the EUR 80m target.
2. **Capital envelope.** EUR 3m was given as "capital available" — assuming this is the capital pool for the 2027 budget specifically, not the total available through 2031. If the board intends to approve capital year-by-year, later years may have separate (unknown) envelopes; if EUR 3m is genuinely the entire capital available through 2031, that materially caps how many levers (especially new stores) can be funded.
3. **Nature of the stall.** Not yet established whether flat growth reflects stalled same-store sales, a stalled store count, market-wide softness, or share loss to named competitors. This is the first hypothesis to test (Phase 4), not assumed here.
4. **Store ownership model.** Unknown whether the 41 stores are company-owned, franchised, or mixed. This matters directly for the franchising lever (converting existing stores vs. adding new franchised units) and is needed before that branch can be sized.
5. **Why now.** No stated trigger (investor pressure, refinancing, succession, competitive threat) behind the 2031 target. Assuming for now it is a standard strategic planning cycle; will revisit if it surfaces during research, since it can affect how much risk the board will accept.

**Agreed by:** Pending — awaiting your confirmation below.

