# em-03-resume on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (6/6 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reply reflects content of 00-status.md and 02-hypotheses.md, not only the workplan | yes | "Hypothesis status — H1 (catering) confirmed at EUR 2.5–3.3m; H2 (delivery growth ≥15%/yr) open... H3 (franchising) killed 2026-10-01; H4 (suburban stores) open" and references to gate status matching 00-status.md |
| Reports current answer and hypothesis statuses including H3 killed | yes | "Current answer (v2): fund corporate catering and online delivery; no franchising... H3 (franchising) killed 2026-10-01" |
| Notices ghost deck still has franchising page needing removal/rewrite | yes | "the ghost deck's page 3 still pitched franchising as a live option ("hypothesis") even though H3 was killed two weeks ago... Rewrote both (03-ghost-deck.md) so franchising reads as a ruled-out alternative with its reason" |
| Identifies next open workplan row with highest impact (H2 delivery) as next step | yes | "Next open workplan row (highest impact): #3, delivery order growth (H2), due 2026-10-20... wrote the evidence plan, a data request list, and two interview guides" |
| Notices gate 2 partner review open and runs it or flags it must run | yes | "Open gate 2 closed: the plan/structure gate had only been run on v1, not on the current v2... Ran it (reviews/gate2-v2.md) — verdict Release with fixes." |
| Does not restart engagement from beginning or re-ask problem statement questions | yes | Reply is framed entirely as a resume/continuation with no re-ask of problem-statement questions |

## Transcript

## Turn 1

**User:** Where are we on the Brightwell engagement? Continue. (Attached in the working directory: engagement/brightwell/.)

Here's where things stand and what I just did to move it forward.

**Resume check (`engagement/brightwell/`):**
1. **Current answer (v2):** fund corporate catering and online delivery; no franchising. Hypothesis status — H1 (catering) confirmed at EUR 2.5–3.3m; H2 (delivery growth ≥15%/yr) open, highest impact and highest uncertainty; H3 (franchising) killed 2026-10-01; H4 (suburban stores) open.
2. **Inconsistency found and fixed:** the ghost deck's page 3 still pitched franchising as a live option ("hypothesis") even though H3 was killed two weeks ago, and the exec-summary headline asserted "EUR 6m+ by 2031" when only catering is actually confirmed — delivery's contribution is still untested. Rewrote both (03-ghost-deck.md) so franchising reads as a ruled-out alternative with its reason, and the headline now stops at what's proven.
3. **Open gate 2 closed:** the plan/structure gate had only been run on v1, not on the current v2 hypotheses/ghost deck/workplan. Ran it (`reviews/gate2-v2.md`) — verdict **Release with fixes**. Two fixes applied: the headline rewrite above, and a flag that the franchising kill rests on just 3 operator interviews (one evidence family) — added workplan row 2b to triangulate it against an independent source before the combined business case leans on it.
4. **Next open workplan row (highest impact):** #3, delivery order growth (H2), due 2026-10-20. No pilot-store data or comparable-chain benchmarks exist in this folder yet, so rather than guess I wrote the evidence plan, a data request list, and two interview guides (store managers, delivery customers) in `research/delivery-order-growth.md`, ready to run as soon as the data comes in.

**What I need from you:** the pilot-store delivery order data (weekly, by store, since launch), the delivery-channel P&L (commission/packaging/labour), and kitchen-capacity figures — listed in full in the data-request table — plus a go-ahead to schedule the two interview rounds.


## Files in work dir after run

- engagement/brightwell/00-status.md
- engagement/brightwell/01-problem-statement.md
- engagement/brightwell/02-hypotheses.md
- engagement/brightwell/03-ghost-deck.md
- engagement/brightwell/04-workplan.md
- engagement/brightwell/research/delivery-order-growth.md
- engagement/brightwell/reviews/gate2-v2.md

## File written by the run: engagement/brightwell/00-status.md

# Engagement status: Brightwell Bakeries, two growth moves for the 2027 budget

*Fictional company. All figures invented for evaluation.*

| Phase | Artefact | Status | Owner | Partner gate |
|---|---|---|---|---|
| Frame | Problem statement | approved 2026-09-12 | EM | passed |
| Structure | Issue tree, hypotheses, ghost deck | v2 | EM | passed (gate 2 on v2, 2026-10-14, release with fixes — see reviews/gate2-v2.md) |
| Plan | Workplan | v2 (+row 2b added) | EM | passed (same gate 2 review) |
| Analyse | Analyses per branch | 2 of 6 done (row 2b added) | | |
| Synthesise | Storyline, executive summary | not started | | |
| Review | Partner review | gate 2 done 2026-10-14 | | |
| Decide | Board, 12 November 2026 | | | |
| Hand over | Implementation plan | | | |

**Current best answer (v2):** Fund corporate catering and online delivery; no franchising.
**Biggest open risk:** delivery order growth may be far below plan (H2, untested); exec-summary headline rewritten at gate 2 to stop short of this until it is.
**Secondary risk flagged at gate 2:** franchising kill (H3) rests on 3 operator interviews only; needs one independent source (workplan #2b) before the combined business case relies on it.
**Next decision needed from the client:** none yet — next is data: pilot-store delivery order data and comparable-chain benchmarks for workplan #3 (see research/delivery-order-growth.md).


## File written by the run: engagement/brightwell/02-hypotheses.md

# Hypotheses

**Current answer (v2, 2026-10-02):** Fund corporate catering and online delivery; no franchising.

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Catering can reach at least EUR 2.5m revenue by 2031 | high | medium | order data + 12 office interviews | below EUR 1.5m in both estimates | confirmed (EUR 2.5-3.3m) |
| H2 | Delivery orders can grow at least 15% a year for five years | high | high | pilot-store order data, comparable chains | below 8% a year | open |
| H3 | Franchising adds at least EUR 4m by 2031 within the margin floor | medium | high | 3 franchise-operator interviews | royalties push store margin below 14% | killed 2026-10-01 (single evidence family — see gate 2 review, triangulate before workplan #5) |
| H4 | Suburban stores can be lifted above 14% margin | low | medium | store P&L | no store above 14% after rent reset | open |

**Change log:** v1 → v2: franchising killed after operator interviews. Gate 2 review 2026-10-14: kill rests on 3 interviews only; needs one independent source before the combined business case closes it out for good.


## File written by the run: engagement/brightwell/03-ghost-deck.md

# Ghost deck v2

| # | Section | Action title | Status |
|---|---|---|---|
| 1 | Executive summary | Catering adds a confirmed EUR 2.5-3.3m; delivery could add more if order growth clears 15%/year (test pending) | hypothesis |
| 2 | 1. Catering | Office catering tripled without sales effort and can reach EUR 3m by 2031 | proven |
| 3 | 2. Delivery | High-street stores can carry a profitable delivery business | hypothesis |
| 4 | 3. Franchising (ruled out) | Franchising was ruled out: operator royalties push store margin below the 14% floor | proven |
| 5 | 4. Stores | Suburban expansion does not pay back under current rents | partly |

**Change log:** v1 → v2: page 4 rewritten from "franchising adds EUR 4m" to "franchising ruled out", following H3 killed 2026-10-01 (see 02-hypotheses.md). Action title and status corrected from "hypothesis" to "proven" (interview evidence; see workplan #2). Gate 2 review 2026-10-14 (reviews/gate2-v2.md): p.1 headline rewritten to stop short of the unconfirmed "EUR 6m+" figure until H2 is tested.


## File written by the run: engagement/brightwell/04-workplan.md

# Workplan v2

| # | Analysis | Tests | Effort (days) | Due | Status |
|---|---|---|---|---|---|
| 1 | Catering bottom-up and top-down sizing | H1 | 3 | 2026-09-26 | done |
| 2 | Franchise operator interviews | H3 | 2 | 2026-10-01 | done |
| 2b | Franchise kill triangulation: one independent source (royalty benchmarks or a second interview round) | H3 | 1 | 2026-10-24 | open (added, gate 2 review 2026-10-14) |
| 3 | Delivery order growth: pilot-store data and comparable chains | H2 | 4 | 2026-10-20 | open |
| 4 | Suburban store rent-reset scenario | H4 | 2 | 2026-10-24 | open |
| 5 | Combined business case | all | 3 | 2026-10-30 | open |

**Change log:** gate 2 review 2026-10-14 (reviews/gate2-v2.md) added row 2b: the franchising kill (H3) rested on 3 operator interviews only and needs one independent source before workplan #5 closes it out.


## File written by the run: engagement/brightwell/research/delivery-order-growth.md

# Research: delivery order growth, 2026-10-14

**Hypothesis:** H2 — Delivery orders can grow at least 15% a year for five years (2026-2031)
**Kill criterion:** Below 8% a year
**Verdict:** open — no client data or desk research collected yet; this is the evidence plan and data/interview request for workplan row #3 (due 2026-10-20)
**So what:** This is the single highest-impact, highest-uncertainty branch left (H2) and the ghost-deck exec summary headline (03-ghost-deck.md, p.1) now explicitly waits on it; nothing below can be filled from memory without violating the no-invented-numbers rule.

## Decisive questions

| # | Question | Evidence families | What would support H2 | What would kill H2 |
|---|---|---|---|---|
| 1 | What has pilot-store delivery order volume/revenue actually done month over month since launch? | Client data | Trailing growth at or above ~1.2%/month compounding to 15%/yr | Flat or decelerating trend already below 8%/yr annualised |
| 2 | What delivery order growth did comparable bakery/QSR chains achieve in years 1-5 after launch, and did it decelerate (S-curve)? | Desk research (benchmarks) | Comparable chains sustained 15%+/yr past year 2 | Comparables show sharp deceleration after an initial pilot pop |
| 3 | What operational ceiling (oven/baking capacity, delivery radius, rider availability) caps order volume regardless of demand? | Client data, internal interviews | Capacity headroom well above the 5-year target volume | Capacity maxes out at a volume implying well under 15%/yr |
| 4 | What do aggregator-commission and packaging costs do to store-level margin as delivery share of revenue rises? | Client data (finance) | Delivery remains margin-floor-compliant (>14%) at scale | Margin falls below 14% before volume reaches the revenue target |
| 5 | Why do customers choose, or stop choosing, delivery (price premium, speed, minimum order)? | Customer interviews | Repeat/expanding usage, low price sensitivity | High churn after first order, strong price sensitivity |
| 6 | What do delivery-aggregator platforms report for demand trends in Brightwell's footprint (if Brightwell uses one)? | Desk research / platform data | Rising category demand in-footprint | Flat or declining category demand |

## Triangulation of decisive claims

Not yet possible — no data collected. Claim 1 (pilot-store trend) and claim 2 (comparable-chain outside view) are the two independent approaches planned for the 15%/8% threshold; both are needed before a verdict, per [triangulation](../../.claude/skills/strategy-engagement/references/triangulation.md) — a single source (e.g. the client's own pilot trend alone) would repeat the thin-evidence problem flagged for H3 at gate 2 (reviews/gate2-v2.md).

## Outside view

Not sized. No comparable-chain delivery growth figures are in hand; none should be stated from memory. This is itself a data/desk-research request (below).

## Counter-evidence

Not searched yet — becomes part of this branch once pilot data arrives (look specifically for stores where delivery growth stalled or reversed, not just averages).

## Assumptions and gaps

| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| Pilot-store delivery growth trend | missing | none | Pilot-store order data, workplan #3 | Brightwell ops/finance |
| Comparable-chain delivery growth (outside view) | missing | none | Desk research on bakery/QSR chains with delivery programs | Research team |
| Delivery-channel margin (commission, packaging, labour) | missing | none | Store-level delivery P&L from finance | Brightwell finance |
| Operational capacity ceiling | missing | none | Oven/kitchen capacity and delivery-radius data per pilot store | Brightwell ops |

## Data requests

| What | Format | Why it matters (which claim) | Fallback if missing | Owner |
|---|---|---|---|---|
| Pilot-store delivery orders and revenue, weekly, since launch, by store | CSV/Excel | Claim 1 — establishes actual growth trajectory, the deciding test for the 15%/8% threshold | Store-manager estimate (weak; label as such) | Brightwell ops/finance |
| Store-level delivery P&L: aggregator commission %, packaging cost, delivery labour cost | CSV/Excel or finance report | Claim 4 — tests whether delivery stays margin-floor-compliant at scale | Industry commission-rate assumption, wide range, flagged ASSUMPTION | Brightwell finance |
| Kitchen/oven capacity and delivery radius per pilot store | Store ops data sheet | Claim 3 — tests whether a demand-side 15%/yr is even deliverable | Qualitative ops-manager judgement, flagged weak | Brightwell ops |
| List of comparable bakery/QSR delivery programmes and any published growth figures | Desk research (requires web access) | Claim 2, outside view | None — if unavailable, state no comparable found and widen the range | Research team |
| Aggregator platform demand trend for Brightwell's footprint, if used | Platform dashboard export | Claim 6 | Omit and rely on claims 1-2 only | Brightwell ops / aggregator account manager |

## Interview guide: pilot-store managers

**Hypotheses tested:** H2
**Target interviewees:** 5-8 managers across all current delivery-pilot stores, including at least one store where delivery has underperformed or was paused, not only the best performers (likely dissenter)

### Opening (2 min)
Purpose: understanding how the delivery pilot has actually gone, not evaluating the manager. Notes used for the growth strategy workplan only.

### Core questions
1. Walk me through last week's delivery orders store by store — how many, compared to a month ago and three months ago?
2. What happened the week delivery volume jumped or dropped the most since launch? What caused it?
3. When you've been at or near kitchen capacity, what did you do — turn away delivery orders, delay in-store customers, or something else? How often does that happen?
4. What has an aggregator or delivery partner told you about commission, fees, or changes to the terms since you started?
5. Tell me about a customer who stopped ordering delivery. What did they say, if anything?

### Close
- What should I have asked?
- Who else should I talk to (a store that tried and stopped, a top performer)?
- Can you share the store's weekly order log directly?

---

## Interview guide: delivery customers

**Hypotheses tested:** H2
**Target interviewees:** 10-15 customers split across frequent orderers, one-time/lapsed orderers, and non-adopters who tried once and stopped (likely dissenters)

### Opening (2 min)
Purpose: understanding how people actually use bakery delivery. Confidential, used for internal planning only.

### Core questions
1. Walk me through the last time you ordered delivery from [store]. What prompted it that day?
2. What happened after — did you order again within the next two weeks? Why or why not?
3. What did that order cost you, including any delivery fee, versus walking in?
4. Tell me about a time you considered ordering delivery and didn't. What stopped you?

### Close
- What should I have asked?
- Who else orders delivery from here that I should talk to?

---

## Interview summary

Not run yet — template ready for use once interviews are scheduled.

| Hypothesis | Interviews | Support | Contradict | Nuance | Representative evidence |
|---|---|---|---|---|---|
| H2 | 0 of ~13-23 planned | | | | |


## File written by the run: engagement/brightwell/reviews/gate2-v2.md

# Partner review: hypotheses v2, ghost deck v2, workplan v2, 2026-10-14, gate 2

**Verdict:** Release with fixes

**One-line reason:** The structure is sound and MECE (two funded moves, two ruled-out alternatives), but the exec summary headline is not yet tied to confirmed analysis, and the franchising kill rests on one evidence family.

## Findings

| # | Severity | Perspective | Check | Where (page/section) | Problem | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | Logician | 6 | Ghost deck p.1 | Headline "EUR 6m+ by 2031" is asserted while only catering (EUR 2.5–3.3m, confirmed) is tied to analysis; delivery's contribution (H2) is still open with high uncertainty and could land near zero if H2 is killed at 8%/yr. The team risks anchoring on 6m before the deciding test runs. | Rewrite p.1 title to carry only the confirmed number plus a labelled range for delivery, e.g. "Catering adds a confirmed EUR 2.5–3.3m; delivery could add EUR X–Ym if order growth clears 15%/yr (test pending)." Revisit once workplan #3 reports. |
| 2 | Major | Evidence Auditor | 10 | Ghost deck p.4 / hypotheses H3 | Franchising is being closed out ("proven", killed) on the strength of 3 operator interviews only — one evidence family. A board-level option should not be ruled out permanently on stated intent from 3 counterparties alone. | Before the combined business case (workplan #5) is finalised, triangulate with one independent source (e.g. published franchise-royalty benchmarks for comparable bakery/QSR chains, or a second interview round with operators who declined) or explicitly note in the synthesis that this kill rests on a single, thin evidence base. |
| 3 | Minor | Decision Maker | 3 | Ghost deck p.1 | At ghost-deck stage amounts are not yet decision-ready (expected before analysis is done) but should be flagged so the status table doesn't read as more settled than it is. | Carried forward via 00-status.md "Biggest open risk" line; no separate fix needed now. |

## Premortem

1. H2 (delivery) comes in below the 8%/yr kill threshold after the pilot-store data is in, and the EUR 6m+ headline the team has been repeating since the ghost deck draft is hard to walk back credibly with the board.
2. The franchising kill is challenged by a board member who knows a competitor franchising profitably; the team has only 3 interviews to defend it.
3. Suburban stores (H4) stays "partly" through to synthesis because the rent-reset scenario (workplan #4) is deprioritised in favour of delivery and catering, leaving an unresolved page in the final deck.

## What is good and must survive the rewrite

- The hypothesis table's numeric thresholds and kill criteria (H1–H4) are specific and were set before testing.
- The ghost-deck story, read title-only, is now MECE: the two funded moves (catering, delivery) and the two ruled-out alternatives (franchising, suburban) cover the full option set from the problem statement.
- Catering sizing (H1) triangulates order data with 12 interviews — keep this as the evidence bar for the remaining branches.

