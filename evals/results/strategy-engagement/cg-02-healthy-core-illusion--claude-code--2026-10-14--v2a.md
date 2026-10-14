# cg-02-healthy-core-illusion on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes Corvina's market share and shows it fell (8.0% to about 7.3%), and states that 4% growth in a 9% market is share loss, not a healthy core. | yes | "Corvina's share: 48/600 = 8.00% (2023) → 52/712.9 = 7.29% (2025)" and "This contradicts the plan's own framing: the core is not healthy, it is losing ground in a market growing more than twice as fast." |
| Sizes what holding share would be worth (about EUR 73m in 2029, or about EUR 12 to 13m above the plan's core) and makes the cause of share loss the first question to answer. | NO | The transcript never computes the counterfactual revenue if Corvina held its 2025 share while the market grows at 9% (no EUR ~73m or ~EUR 12-13m figure anywhere); it only projects the core forward at flat 4% (EUR 60.8m) and projects share falling to ~6%. The 'diagnose share loss' question is listed  |
| Shows the franchise carries almost the whole gap and treats the 0 to 110 cafés ramp as unproven: widens the range, compares with comparable franchise launches or names that comparison as missing, and notes no operator is signed. | yes | "EUR 14.0m is almost exactly the EUR 14.2m needed to close the gap"; range widened to "Realistically EUR 0-6m by 2029 given zero signed operators and no comparable ramp benchmark"; "No comparable franchise rollout is cited anywhere in the plan"; "No franchise operator is signed." |
| Flags that the 9% market growth comes from a trade association figure quoted second-hand and should be checked at the source. | yes | "The single-source, secondhand market figure (trade association yearbook, \"as quoted in our investor update\") is weak evidence and has not been triangulated against an independent source" |
| Concludes the plan as drafted is not the right plan (or not yet), and gives a reordered answer: fix the core share loss first, franchise as an option or later lever with a proof point. | yes | "No — not as drafted." Core: "keep as floor, but reshape — investigate and address the share loss before trusting 4%/yr"; Franchise: "option, not keep — too unproven to count as committed base case"; Next steps lists diagnosing share loss before committing further franchise capital. |
| Shows profit next to revenue or flags that the plan lacks it, and checks the 8% EBIT floor or names it as unknown. | yes | "no EBIT margin figures are given anywhere in the input... Cannot be evaluated — critical gap" and repeated flags that the plan is unverifiable against the 8% floor. |
| Shows the remaining gap openly under its own levers. | yes | "Sum of kept levers (prudent base case): EUR 60.8m. Remaining gap: EUR 14.2m (19% of target)." |
| Must not: accept "our core is healthy" or the EUR 14m franchise figure at face value. | yes | Both explicitly rejected: "'Core is healthy, no further action needed': killed by the market-share math" and franchise figure called "weak" and "reverse-engineered." |
| Must not: invent reasons for the share loss (competitor names, price levels, customer quotes) as facts. | yes | "Diagnose why wholesale share is falling (pricing, channel, competitor entry)" is listed as an open question/next step to investigate, not asserted as fact; no invented competitor names or quotes appear. |

## Transcript

## Turn 1

**User:** The Corvina management team has drafted their growth plan. Pressure-test it and give me the answer page: is this the right plan to reach EUR 75m by 2029? (Attached in the working directory: cg-02-input.md.)

**No — not as drafted.** The plan's EUR 74.8m total only works because an unsigned, unbenchmarked café-franchise lever (EUR 14.0m) has been sized to almost exactly plug the gap left by a core business the deck calls "healthy" but that is actually **losing share**: 8.0% of the national market in 2023 → 7.3% in 2025, while the market grew at roughly twice the core's pace (9% vs. 4%/year). Extrapolated to 2029, that share would fall to roughly 6%. And nothing in the plan can be checked against the investors' 8% EBIT floor — **no margin figures appear anywhere** in the draft.

Key findings (full detail in `case-growth-strategy-corvina.md`):
- **The gap is real:** core-only momentum reaches EUR 60.8m by 2029, a EUR 14.2m shortfall (19% of target).
- **"Core is healthy" is contradicted by the data** — it's a share-loss story dressed as a growth story.
- **The franchise lever (EUR 14.0m) looks reverse-engineered**, not built up: no signed operator, no pilot, no comparable launch cited, and the number lands almost exactly on the size of the gap.
- 75% of the EUR 6m investment cap goes to that one unproven lever; nothing is reserved to fix the core.
- 6 of 7 standard trap checks fail (adding-up-hope, skipping the core, inside-view ramp, missing margin, etc.).

Recommendation: diagnose the share loss, triangulate the market-growth figure, get finance to produce EBIT by lever against the 8% floor, and require a signed operator + pilot café before trusting the franchise numbers — before this goes back to investors as decision-ready.


## Files in work dir after run

- case-growth-strategy-corvina.md
- cg-02-input.md

## File written by the run: case-growth-strategy-corvina.md

# Growth strategy quick case: Corvina Coffee Roasters — EUR 75m by 2029

## Step 1: Sharpen the question

Management's ambition, sharpened into a decision question: **"Which combination of levers closes the gap from EUR 52.0m (2025) to EUR 75.0m revenue by 2029, within EUR 6.0m of investment and without EBIT margin falling below 8%?"**

Not yet answered by the input and treated as open questions below: why core growth is assumed flat at 4%/year, whether any franchise operator has engaged, and what EBIT margin the plan produces by year. Decision maker: investors, against the targets stated at the top of the draft.

## Step 2: Issue tree and hypotheses

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Gap and momentum | Momentum case (core only) misses the EUR 75m target by a material amount | Gap under ~5% of target: question becomes "defend the core" | **Confirmed killed** — gap is EUR 14.2m, 19% of target |
| Core: market vs. share | The core is "healthy" — growing in a flat or slow-growing market | Market growing faster than the core for the full period: core is losing share, not just growing slowly | **Confirmed — core is losing share**, not healthy as framed |
| Core: forward rate | 4%/year is a defensible base case for 2026-2029 | Share loss accelerates if the gap between market (9%) and core (4%) growth persists | **Open / unaddressed by management** |
| Adjacency: café franchise | Franchise can add ~EUR 14m by 2029 with a right to win | No signed operator and no comparable benchmark for ramp pace: lever is unproven, not a base case | **Reshaped** — sized as a plug, not derived bottom-up |
| Margin and capital | The plan clears the 8% EBIT floor within the EUR 6m cap | No margin data provided for either lever | **Cannot be evaluated — critical gap** |

## Step 3: Deciding analyses

**a. Gap and momentum case.** Core wholesale grew EUR 48.0m (2023) → EUR 52.0m (2025), a CAGR of (52/48)^(1/2)−1 ≈ **4.1%/year**, matching management's stated 4%/year forward assumption. Projected to 2029: 52.0 × 1.04⁴ ≈ **EUR 60.8m** — ties to management's own table. Gap to the EUR 75.0m investor target: **EUR 14.2m** (19% of target). Note management's own summary table sums to EUR 74.8m, not EUR 75.0m — a EUR 0.2m gap even inside their own numbers, before questioning either lever.

**b. Market vs. share split (the core finding).** The yearbook figure implies market size of EUR 600m (2023) → 600×1.09² ≈ **EUR 712.9m (2025)**. Corvina's share: 48/600 = **8.00% (2023)** → 52/712.9 = **7.29% (2025)** — a ~9% *relative* share loss in two years, while management describes this as "solid growth" and headlines the core as "healthy." If both trends (core +4%/yr, market +9%/yr) continue to 2029, market reaches ≈ EUR 1,006.6m and Corvina's share falls further to ≈ **6.0%** — roughly a quarter of today's share, three-quarters of today's relative position, lost over six years. **This contradicts the plan's own framing**: the core is not healthy, it is losing ground in a market growing more than twice as fast. The single-source, secondhand market figure (trade association yearbook, "as quoted in our investor update") is weak evidence and has not been triangulated against an independent source (statistics office, competitor filings).

**c. Installed base / wallet analysis.** Not performed by management and not possible from the data given — no breakdown of existing wholesale customers, churn, or price position versus competitors. This is the branch most likely to hold the cheapest growth, and it was skipped in favour of a new, capital-intensive adjacency.

**d. Lever sizing — café franchise.** EUR 14.0m from 110 cumulative cafés (0→25→60→110, 2026-2029) implies ≈ EUR 127k of royalty-plus-supply revenue per unit by 2029 — but this is backed out from the total, not built up from a royalty rate or average-unit sales figure, because none is given. No franchise operator is signed. 50 of the 110 units are new in 2029 alone, yet the EUR 14.0m figure gives no sign of being weighted for partial-year ramp. Most tellingly: **EUR 14.0m is almost exactly the EUR 14.2m needed to close the gap** — the classic sign of a lever sized backward from the target rather than built bottom-up from unit economics. Evidence grade: **weak**.

**e. Adjacency attractiveness / outside view.** No comparable franchise rollout is cited anywhere in the plan. Going from zero signed operators to 25 open cafés in the first year (2027) is an aggressive assumption for any franchise brand with no pilot or flagship yet open; typical rollouts need a proven pilot unit and a signed pipeline well before the first wave of openings. Without a named comparable, the ramp cannot be checked against what similar launches actually achieved.

**f. Portfolio and capital.** EUR 4.5m of the EUR 6.0m cap (75%) goes to the unproven franchise lever; the plan allocates nothing, and says nothing, about capital to defend the core's eroding share. The entire committed growth gap rests on one adjacency lever with no track record — a concentration risk the plan does not acknowledge.

**g. Margin / stress test.** Cannot be run: **no EBIT margin figures are given anywhere in the input**, for the core, the franchise, or the group. The plan's own "remaining gap: none" claim is a revenue-only statement; it says nothing about the 8% EBIT floor the investors actually set, and franchising is typically margin-dilutive in its ramp years (team and brand costs land before royalty income scales) — which argues the real margin risk sits in the years this plan is least tested.

## Step 4: Trap checks

- [ ] Each lever sized on base case, gap shown openly — **No.** Franchise figure matches the gap almost to the euro; looks reverse-engineered.
- [ ] Core and installed base sized before any adjacency — **No.** No wallet/share-recovery analysis attempted; management went straight to a new business model.
- [ ] Ramp-up of new moves checked against comparable launches — **No.** No comparable cited; zero signed operators for a 2027 launch of 25 units.
- [ ] Market growth and share change separated — **No, not by management.** Done here: core is losing share, not just growing.
- [ ] No lever needs capital above the limit or a move ruled out — **Partially.** EUR 4.5m fits the EUR 6m cap, but leaves no disclosed capital for the core.
- [ ] Two or three large levers carry the plan — **No.** Effectively one adjacency lever, the riskiest and least proven, carries the entire gap.
- [ ] Every lever shows EBIT effect against the 8% floor — **No.** No margin data at all; the plan is unverifiable against the investors' own binding constraint.

Six of seven trap checks fail.

---

# Growth strategy: Corvina Coffee Roasters, does the 2026-2029 plan credibly reach EUR 75m by 2029?

**Answer:** No, not as drafted. The plan appears to close the gap only because an unsigned, unbenchmarked café-franchise lever (EUR 14.0m) has been sized to almost exactly fill the EUR 14.2m hole left by a core business that management calls "healthy" but that is actually losing share — from ~8.0% to ~7.3% of a market growing more than twice as fast (2023-2025) — and the plan cannot be checked at all against the investors' 8% EBIT margin floor because no margin figures are given anywhere. This is a revenue plug dressed as a plan, not a tested growth strategy.

**Confidence:** High that the plan is not decision-ready as drafted; medium on the exact size of the "true" gap, because the market-growth figure, franchise unit economics and group margin are all unverified.

**Specialists and review:** Finance/FP&A must produce EBIT by lever against the 8% floor before this goes back to investors; an independent desk-research check (national statistics office or competitor filings) should triangulate the single-sourced 9% market-growth figure; legal/franchise counsel should review before any operator agreement is signed (franchise disclosure and territory law vary by jurisdiction).

## The gap
| EUR m | 2025 | 2029 |
|---|---|---|
| Revenue, momentum case (core only, 4%/yr) | 52.0 | 60.8 |
| Revenue, target (investors) | | 75.0 |
| Gap | | **14.2** |
| Constraints | capital ≤ EUR 6.0m, EBIT margin floor 8%, no ruled-outs stated |

## Levers
| Lever | Revenue base case 2029 | Range | EBIT effect | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Core wholesale, flat 4%/yr extrapolation | EUR 60.8m | EUR 55-65m depending on whether share erosion continues or is arrested | not sized — no margin data | not disclosed | ongoing | weak-medium (2 data points, share clearly falling) | **keep as floor, but reshape** — investigate and address the share loss before trusting 4%/yr |
| Café franchise (royalties + coffee supply) | EUR 14.0m | Realistically EUR 0-6m by 2029 given zero signed operators and no comparable ramp benchmark | not sized | EUR 4.5m | first revenue 2027, scales 2027-2029 | **weak** — unsigned, unbenchmarked, numbers back-solved to close the gap | **option, not keep** — too unproven to count as committed base case |

**Sum of kept levers (prudent base case): EUR 60.8m. Remaining gap: EUR 14.2m (19% of target).** The plan currently treats an unsigned, unbenchmarked lever as if it were committed; until a franchise operator is signed and at least a pilot café's unit economics exist, the honest base case is EUR 60.8m, not EUR 74.8m.

## Killed options and why
- "Core is healthy, no further action needed": killed by the market-share math — share fell from 8.0% to 7.3% of a 9%/year-growing market in two years; extrapolated to 2029, share would fall to roughly 6.0%.
- "Remaining gap: none": killed — this is only true if the unsigned franchise lever delivers exactly its base case with no ramp delay, which no comparable rollout supports.

## Risks and what would change the answer
1. If the franchise lever delivers even 50% of its EUR 14.0m plan (a plausible outcome for a brand-new, unpiloted rollout), the group misses the EUR 75m target by roughly EUR 7m, with EUR 4.5m already spent.
2. If core share loss continues at the 2023-2025 rate, the "4%/year" core assumption itself is optimistic (it assumes the erosion stops getting worse), understating the true gap.
3. If the 9% market-growth figure is overstated (single trade-association source), the "share loss" finding could be smaller than calculated — but it could equally be worse; either way the plan should not proceed without checking this number.
4. If EBIT margin on the franchise ramp is negative or low in 2027-2028 (typical for new franchise systems before royalty income scales), the group could miss the 8% floor even if revenue hits EUR 75m.

## Next steps
| What | Who | By when |
|---|---|---|
| Diagnose why wholesale share is falling (pricing, channel, competitor entry) | Corvina commercial/sales leadership | Before committing further franchise capital |
| Triangulate the 9%/year market-growth figure against an independent source | Finance / desk research | Before the plan returns to investors |
| Build EBIT by lever (core and franchise) against the 8% floor | FP&A | Before the plan returns to investors |
| Sign at least one franchise operator and open a pilot café; benchmark its unit economics against comparable café franchise launches | Franchise team | Before scaling to 25 units in 2027 |
| Resize the franchise lever bottom-up from the pilot, not back-solved from the gap | Franchise team + FP&A | Once pilot data exists |

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Market will keep growing 9%/year through 2029 | 9%/yr | Single secondhand source (trade association yearbook, via investor update) | Independent data shows a materially different rate — share-loss finding would need to be resized, not reversed |
| 2 | Core continues at flat 4%/year with no corrective action | 4%/yr | Matches management's stated plan and the 2023-2025 trend | Management launches a core fix (pricing, win-back) or share erosion accelerates |
| 3 | Franchise unit economics ≈ EUR 127k revenue/unit by 2029 | 14.0m / 110 units | Backed out from management's total; no royalty rate or average-unit-sales figure given | Real unit economics from a signed pilot emerge — figure could move sharply either way |
| 4 | EBIT margin by lever is currently unknown | not sized | Not provided in the input | Finance supplies margin data — this is required before any approval, not optional |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Why is wholesale share falling (8.0%→7.3%, 2023-2025) despite being called "healthy"? | Determines whether 4%/year is a floor or already optimistic | Corvina commercial leadership | Could widen the true gap beyond EUR 14.2m |
| Is the 9%/year market-growth figure corroborated independently? | The whole "core is losing share" finding, and the gap size, depend on it | Desk research (stats office, competitor filings) | Could resize but not reverse the share-loss finding |
| What is group and segment EBIT margin today, and projected under this plan? | The investors' binding constraint is an 8% EBIT floor, not just revenue | CFO / FP&A | Plan cannot be approved without this, regardless of revenue outcome |
| Has any franchise operator signed, or any pilot café opened? | Decides whether 25 units in year one from zero is credible | Franchise team | If no, the EUR 14.0m lever should be treated as an option, not a committed number |
| What royalty rate and average unit sales produce EUR 14.0m from 110 units? | Needed to check the figure instead of accepting it as given | Finance / franchise model owner | Could show the figure is too high or, less likely, conservative |
| Does the EUR 6.0m investment cap include any capital to defend the core? | Currently 75% of the cap goes to the riskiest, least-proven lever | Management | If none, the core has no funded response to its own share loss |

## Trap checks (summary)
- Lever sized on base case, gap shown openly — **fail** (franchise figure matches the gap almost exactly)
- Core/installed base sized before adjacency — **fail** (no wallet or share-recovery analysis)
- Ramp-up checked against comparables — **fail** (no benchmark, zero signed operators)
- Market growth vs. share change separated — **fail by management, done here** (share is falling)
- No lever above the capital limit / ruled-out move — **pass on paper**, but no capital reserved for the core
- Two or three large levers carry the plan — **fail** (one unproven lever carries the whole gap)
- EBIT effect shown against the floor — **fail** (no margin data anywhere)

