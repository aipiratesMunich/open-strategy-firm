# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (2/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes | NO | "**Verdict:** Return" — the memo was returned, not released. |
| No Blocker findings | NO | Finding #1 is explicitly listed as "Blocker" severity. |
| At most two Major findings, each with a concrete, defensible reason | NO | Six findings are rated "Major" (#2 order-value sourcing, #3 no catering benchmark, #4 scale/kill threshold gap, #5 thin suburban evidence, #6 price-increase arithmetic, #7 no sales motion named) — exceeds the two-Major cap. |
| Names what is good and must survive | yes | "## What is good and must survive" lists six specific strengths (e.g. "The primary recommendation is genuinely actionable...", "Delivery growth is checked against two external comparables..."). |
| Must not demand a named framework, more length, or more slides | yes | No finding asks for a specific framework, additional length, or more slides; fixes requested are substantive (numbers, owners, dates), not formatting/length demands. |
| Must not flag the stated uncertainty or explicit assumptions as weaknesses | NO | Finding #5 penalizes the memo for explicitly scoped, stated evidence ("one year... 2025 P&L only") as a weakness rather than accepting the disclosed scope, and the premortem (#3) treats the memo's own disclosed one-year data point as an unaddressed risk rather than crediting the disclosure. |
| Must not claim numbers do not tie when they actually do | NO | The review's "Numbers that do not tie" table flags the 3% price increase (~EUR1.1m vs. implied ~EUR1.86m) as an unexplained ~EUR0.76m gap, but the reference set establishes 1.1 + 0.9 = 2.0 (< 12.7/4) as a figure that does tie, meaning this flagged discrepancy is a false positive rather than a real i |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: Brightwell 2027 catering/delivery memo, gate 3

**Verdict:** Return
**In one line:** The memo's second ask — "revisit the 2031 target or the margin floor" — is not actionable (no target number, no date, no owner) and its sole justification mischaracterizes the franchising evidence as "weakest" when three real operator offers are actually solid primary evidence.

**Question the draft must answer:** Which 2027 growth moves should the board fund, and how should it resolve the resulting gap to the 2031 target? (given)
**Answer the draft gives:** Fund catering (EUR1.2m) and a delivery pilot (EUR0.3m); don't fund suburban or franchising; revisit the 2031 target rather than the margin floor.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Decision Maker / Logician | "What it adds up to" | "Revisit the target" names no new number, owner, or date, and its only stated reason — the lower-floor options carry "the weakest evidence" — doesn't hold for franchising, which rests on three real operator offers (decent primary evidence), not weak evidence. | Board approves a vague mandate to "revisit" EUR80m with no actual number on the table, and may later discover franchising was dismissed on a mischaracterized basis — reopening a decision it thought was closed. | State the recommended new target (or range) and a date to bring it to the board. Separate the franchising rejection into its real reasons (strategic fit, brand/control risk of royalties) from an evidence-quality claim that doesn't survive scrutiny. |
| 2 | Major | Evidence Auditor | "Why catering" | The EUR190 median order value feeding the bottom-up revenue estimate comes from 12 interviewed managers, not from the sales/transaction data already cited for order counts (3,100→9,000), which almost certainly contains actual order values. | A CFO asks why a quantitative input to a multi-million-euro estimate uses n=12 when stronger data exists; if real average order value is materially different, the EUR2.9m base case (and the 5.3m/8.5%/12.7m figures built on it) moves. | Recompute average order value from transaction data; use the interview median only to sanity-check, not source, the figure. |
| 3 | Major | Skeptical CFO | "Why catering" | No comparable-company benchmark is given for the catering ramp-up (unlike delivery, which cites two regional chains' 10–14% growth), so the board cannot judge whether EUR2.9m by 2031 is realistic. | The larger of the two investments (EUR1.2m) rests entirely on internal triangulation with no outside check on execution risk. | Add at least one comparable: a competitor's or another regional bakery's central-kitchen catering ramp, or industry B2B-catering growth benchmarks. |
| 4 | Major | Logician | "Why a delivery pilot" vs. "What would change our view" | The pilot's stated scale threshold is 60 orders/day; the kill threshold is below 50 orders/day. No decision rule is given for 50–59. | If the pilot lands in that range, the board and Operations have no pre-agreed answer on whether to scale, extend, or kill — reopening the argument the kill-criteria section was meant to pre-empt. | Reconcile to one threshold, or state explicitly what happens in the gap zone (e.g., extend six months). |
| 5 | Major | Evidence Auditor | "Why not suburban stores or franchising" | Suburban rejection rests on one year, one aggregate number (13.1% vs. 14.0% floor, 2025 P&L only) — no trend, no store-level spread, no explanation of the 0.9pp gap. | This thin evidence is exactly what the memo leans on to argue the board should move the target rather than the floor (see #1); if the gap is noise or improving, the premise weakens. | Show 2–3 years of suburban margin trend and the store-level spread before using it to justify a strategic choice. |
| 6 | Major | Skeptical CFO | "What it adds up to" | 3% price increase is valued at ~EUR1.1m, but 3% of today's EUR62m revenue is ~EUR1.86m — a ~40% gap with no bridge shown (elasticity, scope, competitive response). | A board member doing the mental math (3% × 62m ≈ 1.9m) will conclude the memo's arithmetic doesn't hold up, and discount confidence in the other figures by association. | Add one sentence showing the bridge (e.g., volume loss from the two discount competitors, or scope limited to certain stores/products). |
| 7 | Major | Premortem | Not addressed anywhere | Catering's entire historical growth happened "without any sales effort." The plan now depends on converting prospects into signed framework agreements within six months, but no sales hire, process, or capability is named anywhere in the memo. | This is the single most likely way the catering move underperforms, and the memo gives the board no visibility into whether it's being managed. | Add one line naming who builds and runs the B2B sales/contracting motion for catering, and when. |
| 8 | Minor | Outsider | "What would change our view" | "Framework agreements" appears only here; it's never introduced in "Why catering." | A reader has to infer what the catering go-to-market motion actually is. | Introduce the term once in the catering section. |
| 9 | Minor | Outsider | "Why a delivery pilot" | "(about EUR0.6m, a separate board decision...)" is ambiguous — unclear if EUR0.6m is rollout cost, investment, or something else. | Minor re-reading required; doesn't change the current ask. | Add two words: "about EUR0.6m rollout cost." |
| 10 | Minor | Skeptical CFO | "Why catering" | Payback ("pays back in the fourth year") uses undiscounted cash contribution. | Immaterial at this scale/horizon; won't flip the decision. | Label the payback as nominal/undiscounted, one phrase. |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| 3% price increase impact | Stated: ~EUR1.1m | Implied by 3% × EUR62m current revenue | EUR1.1m vs. ~EUR1.86m nominal — ~EUR0.76m unexplained |
| Delivery pilot scale/kill thresholds | "Why delivery" §: scale at 60 orders/day | "What would change our view" §: kill below 50 orders/day | No stated rule for 50–59 orders/day |

Everything else headline (EUR2.9m + EUR2.4m = EUR5.3m; 5.3/62 = 8.5%; 80 − 67.3 = EUR12.7m; the year-by-year catering contribution math) ties correctly.

## Missing outside view

- **Catering revenue ramp:** no comparable company or project benchmark given (delivery has one; catering doesn't). Need a reference point for how fast a bakery/food-service central kitchen has scaled B2B catering elsewhere.
- **Suburban store economics:** no benchmark for what comparable regional chains' suburban-format stores earn, to judge whether 13.1% is a Brightwell-specific or format-wide issue.

## Premortem

1. Catering demand was passive ("grew... without any sales effort"); converting it into signed framework agreements requires an active B2B sales motion the memo never staffs or plans for — the 40% six-month target is missed for execution reasons, not demand reasons.
2. In-store cannibalization from delivery shows up gradually, after the 12-month pilot and the 3% check have already passed, and only becomes visible once rolled out to all 18 stores — by which point it's a company-wide margin problem.
3. Office attendance (catering's structural driver) plateaus or reverses after 2027; the memo's only reassurance is one year of data (24% Q2–Q2 growth), with no scenario tested for a demand reversal against the EUR1.2m capex and EUR0.35m/year fixed cost it commits to.

## What is good and must survive

- The primary recommendation is genuinely actionable: named amounts, owners, start dates for both funded moves.
- The rejection of suburban/franchising is reasoned, not just asserted, and tied to an explicit, named floor.
- Catering sizing triangulates bottom-up and top-down independently and lands on a mid-range base case rather than the top of the range.
- Delivery growth is checked against two external comparables (10–14% range) — exactly the outside-view discipline catering is missing.
- Pre-committed falsification criteria ("what would change our view") exist for both moves — most memos skip this entirely.
- The memo is honest about the EUR12.7m gap rather than hiding it, and surfaces the real second decision instead of pretending the two funded moves solve everything.

## What "fixed" looks like

"We recommend the board fund two reversible 2027 moves — a EUR1.2m catering central kitchen and a EUR0.3m delivery pilot — and lower the 2031 group revenue target from EUR80m to roughly EUR67–70m rather than cut the 14% margin floor. Closing the full EUR12.7m gap would require suburban stores or franchising; franchising's margin hit is well evidenced by three independent operator offers but remains strategically unattractive, and suburban economics rest on one year of data we have not yet stress-tested over a longer trend. We will bring a retested suburban-margin view and a franchising recommendation back to the board in [date] before asking it to revisit the floor itself."


## Files in work dir after run

- pr-03-input.md
