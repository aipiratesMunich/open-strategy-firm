# em-03-resume on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (6/6 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reply reflects content of 00-status.md and 02-hypotheses.md, not only the workplan | yes | Response discusses hypothesis statuses (H3 killed, H1 implied confirmed via catering reference) and gate status alongside workplan progression, and reproduces both files in full with statuses like 'confirmed (EUR 2.5-3.3m)', 'killed 2026-10-01', 'open'. |
| Reports current answer and hypothesis statuses, including H3 killed | yes | 00-status.md: 'Current best answer (v2): Fund corporate catering and online delivery; no franchising.' and 02-hypotheses.md shows H1 confirmed, H2 open, H3 killed 2026-10-01, H4 open. |
| Notices ghost deck still has franchising page and says it must be removed/rewritten | yes | "Ghost deck was stale. Page 4 still presented franchising as a live 'adds EUR 4m' hypothesis even though H3 was killed... Rewritten to carry the rejection" |
| Identifies next open workplan row with highest impact (H2) as next step | yes | "Opened the H2 research branch (delivery order growth ≥15%/yr) — the swing hypothesis, since it's the highest-impact, highest-uncertainty piece left" |
| Notices gate 2 partner review marked open and runs it or flags it must run first | yes | "Gate 2 on the v2 workplan had never been formally reviewed, even though two analyses already ran against it. I ran that review now (reviews/gate2-v2.md) — verdict Release with fixes" |
| Does not restart engagement from scratch or re-ask problem statement questions | yes | Response proceeds directly from existing status/files with no re-asking of framing questions like scope or objectives. |

## Transcript

## Turn 1

**User:** Where are we on the Brightwell engagement? Continue. (Attached in the working directory: engagement/brightwell/.)

## Where things stand

I fixed two things that were out of sync, then pushed the highest-priority open hypothesis forward:

1. **Ghost deck was stale.** Page 4 still presented franchising as a live "adds EUR 4m" hypothesis even though H3 was killed on 2026-10-01 after operator interviews showed the royalties needed would breach the 14% margin floor. Rewritten to carry the rejection (`03-ghost-deck.md`).
2. **Gate 2 on the v2 workplan had never been formally reviewed**, even though two analyses already ran against it. I ran that review now (`reviews/gate2-v2.md`) — verdict **Release with fixes**, the one blocker being the ghost-deck page above, now closed.
3. **Opened the H2 research branch** (delivery order growth ≥15%/yr) — the swing hypothesis, since it's the highest-impact, highest-uncertainty piece left and the catering+delivery headline needs delivery to deliver roughly EUR 3m. Wrote the evidence plan, data requests, and an interview guide in `research/delivery-growth.md`.

**What I couldn't do:** WebSearch permission wasn't granted, so I couldn't pull real comparable-chain delivery-growth benchmarks for the outside view — that's now logged as a data/approval request rather than a guessed number.

**What I need from you to keep H2 moving (due 2026-10-20):**
- Pilot-store delivery order counts/revenue, monthly, last 12–18 months
- Delivery order cost breakdown (platform commission, packaging, incremental labour)
- A short list of comparable chains you'd consider fair benchmarks
- Either grant WebSearch so I can desk-research category growth and comparables, or tell me to proceed on client data alone

H4 (suburban rent-reset, due 2026-10-24) is next in line after H2 — lower impact, so I held off starting it this round.


## Files in work dir after run

- engagement/brightwell/00-status.md
- engagement/brightwell/01-problem-statement.md
- engagement/brightwell/02-hypotheses.md
- engagement/brightwell/03-ghost-deck.md
- engagement/brightwell/04-workplan.md
- engagement/brightwell/research/delivery-growth.md
- engagement/brightwell/reviews/gate2-v2.md

## File written by the run: engagement/brightwell/00-status.md

# Engagement status: Brightwell Bakeries, two growth moves for the 2027 budget

*Fictional company. All figures invented for evaluation.*

| Phase | Artefact | Status | Owner | Partner gate |
|---|---|---|---|---|
| Frame | Problem statement | approved 2026-09-12 | EM | passed |
| Structure | Issue tree, hypotheses, ghost deck | v2 | EM | passed (gate 2 on v1) |
| Plan | Workplan | v2 | EM | passed (gate 2 on v2, 2026-10-14, release with fixes — see reviews/gate2-v2.md) |
| Analyse | Analyses per branch | 2 of 5 done | | |
| Synthesise | Storyline, executive summary | not started | | |
| Review | Partner review | | | |
| Decide | Board, 12 November 2026 | | | |
| Hand over | Implementation plan | | | |

**Current best answer (v2):** Fund corporate catering and online delivery; no franchising.
**Biggest open risk:** delivery order growth may be far below plan.
**Next decision needed from the client:** none yet — pilot-store delivery order data and comparable-chain benchmarks requested for H2 (workplan row 3, due 2026-10-20); see research/delivery-growth.md.

**2026-10-14:** fixed ghost deck p.4 (still presented killed franchising hypothesis as live) and closed gate 2 on v2 — see reviews/gate2-v2.md. Opened research branch for H2 (delivery order growth).


## File written by the run: engagement/brightwell/02-hypotheses.md

# Hypotheses

**Current answer (v2, 2026-10-02):** Fund corporate catering and online delivery; no franchising.

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Catering can reach at least EUR 2.5m revenue by 2031 | high | medium | order data + 12 office interviews | below EUR 1.5m in both estimates | confirmed (EUR 2.5-3.3m) |
| H2 | Delivery orders can grow at least 15% a year for five years | high | high | pilot-store order data, comparable chains | below 8% a year | open |
| H3 | Franchising adds at least EUR 4m by 2031 within the margin floor | medium | high | 3 franchise-operator interviews | royalties push store margin below 14% | killed 2026-10-01 |
| H4 | Suburban stores can be lifted above 14% margin | low | medium | store P&L | no store above 14% after rent reset | open |

**Change log:** v1 → v2: franchising killed after operator interviews. 2026-10-14: opened research branch on H2, see research/delivery-growth.md — evidence plan and data request only, no result yet.


## File written by the run: engagement/brightwell/03-ghost-deck.md

# Ghost deck v2

| # | Section | Action title | Status |
|---|---|---|---|
| 1 | Executive summary | Catering and delivery can add EUR 6m+ by 2031 within the margin floor | hypothesis |
| 2 | 1. Catering | Office catering tripled without sales effort and can reach EUR 3m by 2031 | proven |
| 3 | 2. Delivery | High-street stores can carry a profitable delivery business | hypothesis |
| 4 | 3. Franchising | Franchising is ruled out: royalty levels needed to attract operators push store margin below the 14% floor | killed |
| 5 | 4. Stores | Suburban expansion does not pay back under current rents | partly |

**Change log:** v1 → v2: page 4 rewritten 2026-10-14 to carry the franchising rejection (H3 killed 2026-10-01); the page previously still presented franchising as a live EUR 4m hypothesis, contradicting the current answer.


## File written by the run: engagement/brightwell/research/delivery-growth.md

# Research: delivery order growth (H2), 2026-10-14

*Fictional engagement. All figures invented for evaluation.*

**Hypothesis (H2):** Delivery orders from Brightwell's high-street stores can grow at least 15% a year for five years (2027–2031).
**Kill criterion:** Growth below 8% a year in both the pilot-store trend and the comparable-chain outside view.
**Verdict:** Open — no decisive data in hand yet. Strength: none (no findings logged below; this file is the evidence plan and data request, not a result).
**So what:** This is the swing hypothesis for the recommendation — H1 (catering) is already confirmed at EUR 2.5–3.3m and H3 (franchising) is killed, so the EUR 6m+ headline in the ghost deck depends on delivery clearing roughly EUR 3m of the gap. Nothing below should be read as a finding; it is the plan for getting one.

## Why this is next
Workplan row 3, due 2026-10-20. Ranked above H4 (suburban stores, low impact) because H2 carries high impact and high uncertainty — exactly the branch a partner review would ask about first (premortem finding #2 in reviews/gate2-v2.md).

## Plan the evidence
Four decisive questions, each needs two independent sources:

| # | Question | Client data | Desk research / outside view | Would support H2 | Would kill H2 |
|---|---|---|---|---|---|
| 1 | What is the actual month-on-month delivery order growth in Brightwell's existing pilot stores? | Pilot-store POS/order data, last 12–18 months | — (internal only) | Trend ≥15%/yr, not just a launch spike | Trend flattens below 8%/yr after month 6 |
| 2 | What delivery order growth did comparable bakery/café chains achieve once past their first year? | — | Trade press, franchise disclosure documents, delivery-platform merchant reports for comparable chains | Comparables sustained ≥12–15%/yr for several years | Comparables saturate at 5–8%/yr after initial ramp |
| 3 | Does unit economics hold at scale (delivery commission, packaging, prep-time cost per order) or does margin erode as volume grows? | Pilot-store cost data per delivery order | Benchmark delivery-platform commission rates | Contribution margin per order stays flat or improves with volume | Margin erodes below the 14% store floor as volume rises |
| 4 | Is local demand for bakery delivery still growing, or is Brightwell's pilot growth just early-adopter share-shifting from competitors? | — | Local market data on food delivery penetration/growth | Category still growing, not just share-shifting | Category flat; growth would be zero-sum against competitors |

## Outside view
Not yet available. The honest outside-view range for delivery order growth in food/bakery retail depends on real comparables (chain scale, market maturity, platform mix) that I have not verified — I do not have web access approved in this session, so I am not stating a market growth figure from memory. **This needs checking** before H2 can be marked confirmed or killed on the outside view alone.

## Counter-evidence to look for
- Cases where a bakery/café chain's delivery orders grew fast in year one off a low base, then flattened as the early-adopter customer base was exhausted — would argue the pilot-store trend (if also early-stage) is not representative of a five-year run rate.
- Delivery-platform commission increases over the last two years that compress contribution margin faster than order volume grows.

## Assumptions and gaps
| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| Pilot-store order growth trend | missing | none — no figure assumed | Pilot-store order data, last 12–18 months, monthly | Client (ops/finance) |
| Comparable-chain delivery growth once past ramp-up | missing | none — no figure assumed | Named comparable chains (client to help identify fair comparables by format/region) + desk research | EM, once comparables named |
| Delivery contribution margin per order | missing | none — no figure assumed | Pilot-store cost breakdown per delivery order (platform commission, packaging, incremental labour) | Client (finance) |
| Category growth vs share-shifting | missing | none — no figure assumed | Local delivery-platform category data, or platform account manager briefing | EM |

**Break-even note:** the recommendation's EUR 6m+ headline needs delivery to contribute roughly EUR 3m of that by 2031. At Brightwell's assumed delivery order economics (not yet verified), the growth rate that clears the kill criterion (8%/yr) is the one figure this whole branch turns on — it should be the first thing triangulated once data arrives, not the last.

## Data requests
| What | Format | Why it matters | Fallback if missing | Owner |
|---|---|---|---|---|
| Pilot-store delivery order counts and revenue, monthly, last 12–18 months | spreadsheet/export | Direct trend read for the kill criterion | Use shortest available window and widen the range; flag as weak evidence | Client |
| Delivery order cost breakdown (platform commission %, packaging cost, incremental prep labour per order) | spreadsheet | Tests whether margin holds at scale (question 3) | Use published platform commission rates as a labelled assumption, wide range | Client |
| List of comparable chains the client considers fair benchmarks (format, region, size) | short list with reasoning | Needed before desk research can pick honest comparables rather than cherry-picked ones | EM proposes a list and flags it as EM's judgement, not client-validated | Client, or EM if client has no view |
| Approval to use web research for comparable-chain and category growth data | decision | Needed for the outside-view and category-growth questions (2 and 4) | Mark both as open/unverified in the business case and widen the range accordingly | Client/EM |

## Interview guide: comparable-chain or former delivery-ops contacts

**Hypotheses tested:** H2
**Target interviewees:** 3–4 operations or franchise contacts at comparable bakery/café/QSR chains with established delivery channels (mix of one chain where delivery is reported to be thriving and one where it is reported to have stalled, to get disagreement rather than confirmation). No current or former Brightwell competitor's confidential pricing or contracts to be requested.

### Opening (2 min)
Purpose, confidentiality, how notes will be used.

### Core questions
1. Walk me through how delivery order volume at your stores has changed month by month since you launched it.
2. What happened when growth slowed or sped up — what changed at the same time (marketing, platform, menu, competitor action)?
3. What does a delivery order actually cost you once commission, packaging and prep labour are counted, and has that changed as volume grew?
4. Who else should I talk to — a chain where delivery underperformed, not just one where it worked?

### Close
- What should I have asked?
- Who else should I talk to?

*No interviews have been conducted yet — this is the guide, to be run once the client names acceptable comparables (see data request above) or introduces contacts.*


## File written by the run: engagement/brightwell/reviews/gate2-v2.md

# Partner review: hypotheses v2, ghost deck v2, workplan v2, 2026-10-14, gate 2

*Fictional engagement. All figures invented for evaluation.*

**Verdict:** Release with fixes (fix applied before release)

**One-line reason:** Structure answers the question and the workplan is proportionate; one page still contradicted a killed hypothesis and has been rewritten.

## Findings
| # | Severity | Perspective | Check | Where | Problem | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Logician | 5, 8 | Ghost deck p.4 | Franchising page still titled "Franchising adds EUR 4m with no capital from Brightwell" and marked "hypothesis" although H3 was killed 2026-10-01 after operator interviews; reading the deck titles in order tells a story that contradicts the stated current answer ("no franchising") | Rewrite the page to carry the rejection and the fact that killed it — **done**, see 03-ghost-deck.md |
| 2 | Minor | Decision Maker | 4 | 00-status.md | Status table does not show which gate the v2 structure was reviewed against, so a reader cannot tell the workplan was already running ahead of its own gate | Add a gate-2 row/date once this review lands — **done**, see 00-status.md |

## Premortem
1. Board asks why franchising isn't in the plan and the deck has no page addressing it — closed by fix 1.
2. Delivery (H2) turns out to be the swing hypothesis but gets the same workplan effort as the already-settled catering branch — not yet addressed; flag for synthesis stage: delivery (high impact, high uncertainty) deserves the most scrutiny, not equal treatment.
3. Suburban stores (H4) analysis comes back "partly" and gets quietly dropped rather than driving a decision either way — not yet addressed; workplan row 4 should end in a clear keep/drop, not a shrug.

## What is good and must survive the rewrite
- Hypotheses carry numeric thresholds and kill criteria set before data (H1–H4).
- Franchising was actually killed on evidence (operator interviews showing royalty levels breach the margin floor), not dropped for convenience.
- Workplan is ordered by impact and links every row to a hypothesis.

