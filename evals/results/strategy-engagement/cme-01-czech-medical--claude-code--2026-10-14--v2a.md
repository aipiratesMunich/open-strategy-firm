# cme-01-czech-medical on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/13 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question with the minimum bar (EUR 6m, 8% EBIT by 2030, EUR 5m) and kill criteria before analysing. | yes | "Decision question: ... must deliver at least EUR 6m revenue and 8% EBIT margin within EUR 5m capital, with an exit decision at end-2029" (Step 1), followed by a kill-criteria hypothesis table (Step 2) before the deciding analyses (Step 3). |
| Sizes the segment top-down (~EUR 31.5m) and bottom-up (~EUR 25.7m) and explains/flags the difference. | yes | "Top-down: ... = EUR 31.5m ... Bottom-up: ... = EUR 25.65m ... the gap (~EUR 5.85m) is plausibly hospitals/labs plus pharmacies outside the 3 regions." |
| Builds the ramp from reps x win rate and arrives at ~EUR 4.0m-4.6m revenue in 2030, below the EUR 6m bar. | yes | "3 reps × 40 wins/year ... 2030 ... 425.8 ... EUR 4.05m"; zero-churn case "480 accounts (EUR 4.56m) — below the 631.6 accounts (EUR 6m) the bar requires." |
| Computes 2030 EBIT margin below 8% (~1%-5%). | yes | "EUR 0.06m (~1.5% margin)" in the base case table, below the 8% bar. |
| Models at least one aggressive incumbent reaction using the 2024 price-cut evidence and reports its effect. | yes | "Low case (incumbent reacts as it did in 2024 ... 30 wins/rep/year instead of 40 ... 2030 accounts ≈319, revenue ≈EUR 3.03m, EBIT ≈ −EUR 0.25m" |
| States that the EUR 120k study is sunk and plays no role. | yes | "the EUR 120k study and the interviewed-but-unhired country manager are sunk — they carry no weight in the recommendation"; trap check "[x] Sunk costs (EUR 120k study, interviewed candidate) play no role." |
| Compares with the Austrian alternative per euro of capital, and flags that alternative as a management estimate to test. | yes | "~17.5% EBIT-to-capital at run-rate, against ~1.2% for the Czech base case ... The Austria estimate is itself a single-comparable management estimate and should be held to the same evidence standard as the Czech numbers." |
| Does not approve the briefed 3-rep plan; answer is do not enter/enter later/enter under conditions with a stage gate, and says what would make the board revisit it. | yes | "Do not approve the current plan (3 reps from 2027) ... Approve a rescoped, gated entry: fund a 2027 one-region pilot ... if the pilot clears ... scale to ~5 reps ... If the pilot fails ... exit." Plus a "What would change the answer" section. |
| Compares at least two entry modes (e.g. own office, partner/distributor, acquisition of a local courier) on cost, speed, control and exit cost. | NO | The analysis only compares headcount scaling (3 reps vs 5 reps) and the Austria capital-allocation alternative; no mention of partner/distributor, acquisition, or any alternative entry mode anywhere in the document. |
| Writes exit criteria and exit cost. | NO | Exit criteria are defined ("pilot win-rate below 32 accounts/rep/year by end-2027; or end-2029 run-rate below EUR 5m"), but exit cost is not computed — instead it is listed as an unanswered open question: "What would wind-down cost if Kestrel exits at end-2029 ... exit cost isn't quantified anywhere |
| Flags that Austrian win rates and prices may not transfer to the Czech market and names the test. | yes | "the entire plan copies the Austria win-rate (40/rep/yr) and churn (8%) onto a Czech market Kestrel has never sold in ... Fix before committing: a 2027 pilot (1 region, 1–2 reps) to measure actual first-year win rate." |
| Must not: recommend unconditional entry on the strength of the EUR 210m headline. | yes | The EUR 210m top-down figure is used only as a sizing cross-check, and the final answer is a conditional, gated pilot, not unconditional entry. |
| Must not: invent Czech regulatory requirements, competitor names, or wage levels as facts. | yes | Regulatory items are flagged for specialists ("Czech entity setup, driver/courier employment classification, and cross-border VAT/transfer pricing ... need local legal and tax review"), competitors are referred to generically as "Incumbent A/B," and cost figures (EUR 85k/rep, EUR 0.9m depot) are tak |

## Transcript

## Turn 1

**User:** Work the Kestrel Czech entry case from the briefing. Quick case, answer page for the board. (Attached in the working directory: cme-01-input.md.)

I worked the Kestrel Czech case and wrote the quick-case file to `case-market-entry-kestrel-czech.md`. Headline finding: **the plan as currently scoped (3 reps from 2027) mathematically can't hit the board's bar** — Kestrel's own account math (40 wins/rep/year, 8% churn, €9,500/account, from the Austria benchmark) lands at ~426 accounts / **€4.05m revenue / ~1.5% EBIT margin** by 2030, against a €6m/8% bar. Even with zero churn, 3 reps over 4 years caps out at 480 accounts — short of the ~632 needed.

The gap is a headcount-sizing problem, not a capital or market-size problem: peak cash need stays under ~€1.5m either way, well inside the €5m cap. A rescoped plan (~5 reps) clears both bars on paper (€6.7m revenue, ~10.3% margin), but that rests entirely on an untested assumption — Austria's win-rate transferring unchanged into a Czech market where the two incumbents (55% share) have already cut price 12% against a new entrant in 2024.

**Recommendation:** don't approve the current 3-rep plan; fund a 2027 one-region pilot to test real win-rate, gate scaling to 5 reps on clearing ~32 accounts/rep/year, and set a hard exit trigger at end-2029 (<€5m revenue run-rate). The Austria two-region extension (€2m → €3.5m/10% EBIT) is the safer capital-efficient fallback (~17.5% EBIT/capital yield vs ~1.2% for the current Czech base case) and isn't mutually exclusive with the pilot.

The file includes the full quick-case workup — triangulated market sizing, trap checks, low/base/high business case, alternative-use-of-capital comparison, assumptions, and open questions (regional incumbent share, hospital/lab segment, exit/wind-down cost, legal/tax specialist flags) — ending in a one-page board answer section.


## Files in work dir after run

- case-market-entry-kestrel-czech.md
- cme-01-input.md

## File written by the run: case-market-entry-kestrel-czech.md

# Market entry: Kestrel Logistics, Czech Republic medical same-day, quick case

*Fictional company and figures, invented for evaluation. Working file for the January 2027 board paper.*

## Step 1: Sharpen the question

Decision question: **"Should Kestrel enter the Czech medical same-day market by 2030, given it must deliver at least EUR 6m revenue and 8% EBIT margin within EUR 5m capital, with an exit decision at end-2029 if the bar is missed?"**

The brief already gives a bar, a capital limit, and an exit checkpoint, so no blocking round of questions is needed. Three clarifications are still open and listed in Open Questions rather than held: regional incumbent share (vs. the 55% national figure), hospital/lab segment size, and wind-down cost. Two things are explicitly **not** reasons to enter: the EUR 120k study and the interviewed-but-unhired country manager are sunk — they carry no weight in the recommendation below.

## Step 2: Hypotheses and kill criteria

| Branch | Hypothesis | Kill criterion | Verdict |
|---|---|---|---|
| Attractive: size | Addressable medical segment ≥ EUR 6m achievable share | Bottom-up SAM too small or inconsistent with top-down | Confirmed — segment ~EUR 25–31m, big enough; not the binding constraint |
| Attractive: structure | No player holds a blocking share | Two incumbents hold 55%, with a demonstrated 12% price-cut reaction to a 2024 entrant | Reshaped — moderate concentration, but reaction risk is real and unmodelled in the plan |
| Can win: capacity | Planned sales capacity (3 reps, 2027) can reach EUR 6m by 2030 | Account math falls short of the bar | **Killed** — reaches only ~EUR 4.05m |
| Pays | Base case clears 8% EBIT margin by 2030 | Margin below 8% in base case | **Killed** — ~1.5% margin in base case |
| Beats alternative | Czech entry returns more per euro of capital than the Austria extension | Alternative returns more for less capital | Confirmed against current plan — Austria alternative wins on a run-rate EBIT/capital basis |

## Step 3: Deciding analyses

### a. Addressable market (sizing, triangulated)
- Top-down: CZ B2B same-day delivery EUR 210m/yr × 15% medical share = **EUR 31.5m** (whole country, pharmacies + hospitals + labs).
- Bottom-up: 2,700 pharmacies in the 3 target regions × EUR 9,500/pharmacy = **EUR 25.65m** (pharmacies only, 3 regions, excludes hospitals/labs).
- These aren't the same scope (nationwide-all-medical vs. 3-regions-pharmacy-only), but the magnitudes are consistent — the gap (~EUR 5.85m) is plausibly hospitals/labs plus pharmacies outside the 3 regions. **Weak-to-medium evidence**: the per-pharmacy figure rests on a 60-pharmacy self-reported survey, and hospitals/labs are uncounted. The segment is large enough that size is not the binding constraint — the next two analyses are.

### b. Market structure (Five Forces lens)
Two local players hold ~55% of the medical segment; the remaining ~45% is fragmented. Moderate, not extreme, concentration — on its own this would not kill entry. But the one hard data point in the brief is behavioral, not structural: when a new carrier entered in 2024, the larger incumbent cut price ~12% for six months. That is the single most decision-relevant fact in the market study and it is **not reflected anywhere in Kestrel's own account-math plan**. Trap: "ignoring incumbent reaction" (see Step 4).

### c. Entry business case — Kestrel's own account math (the deciding analysis)

Planning convention from the brief: revenue in a year = pharmacy accounts in force at year-end × EUR 9,500. Accounts in force = prior year × (1 − 8% churn) + new wins. Austria benchmark: 40 new wins/rep/year. Plan: 3 reps from 2027.

**Base case (plan as written, Austria productivity assumed to transfer unchanged):**

| Year | New wins (3 reps × 40) | Accounts in force (year-end) | Revenue | Fixed cost (depot 0.9m + 3×85k) | EBIT (30% gross margin − fixed) |
|---|---|---|---|---|---|
| 2027 | 120 | 120.0 | EUR 1.14m | EUR 1.155m | −EUR 0.81m |
| 2028 | 120 | 230.4 | EUR 2.19m | EUR 1.155m | −EUR 0.50m |
| 2029 | 120 | 332.4 | EUR 3.16m | EUR 1.155m | −EUR 0.21m |
| 2030 | 120 | **425.8** | **EUR 4.05m** | EUR 1.155m | **+EUR 0.06m (~1.5% margin)** |

Result: **the plan as scoped cannot reach the board's bar.** Even with zero churn, 3 reps × 40 wins/year × 4 years = 480 accounts max (EUR 4.56m) — below the 631.6 accounts (EUR 6m) the bar requires. With the stated 8% churn, the plan lands at 426 accounts / EUR 4.05m, **33% short of revenue** and far short of margin (1.5% vs 8% required). This is not a market-attractiveness problem; it is a sales-capacity sizing problem.

Reverse-engineering the capacity needed: to reach 631.6 accounts by end-2030 at the same 40-wins/8%-churn assumptions requires **~4.5 reps**, not 3. Peak cumulative cash need across the ramp stays under ~EUR 1–1.5m either way (see Low/Base/High table below) — well inside the EUR 5m cap. **Capital is not the constraint here; the headcount plan is.**

**Low case** (incumbent reacts as it did in 2024, and Austria win-rate doesn't fully transfer to an unfamiliar, competitively-held market: 30 wins/rep/year instead of 40, 3 reps):
2030 accounts ≈319, revenue ≈EUR 3.03m, EBIT ≈ −EUR 0.25m (negative margin). Misses the bar by a wide margin.

**High case** (plan rescoped to 5 reps from 2027, Austria productivity holds unchanged):
2030 accounts ≈709, revenue ≈EUR 6.74m, fixed cost EUR 1.325m, EBIT ≈EUR 0.70m (**10.3% margin — clears both bars**). Peak cumulative cash need ≈EUR 1.0m (trough end-2028), full payback on a cumulative basis essentially by end-2030. Still well inside the EUR 5m cap.

| | Base (3 reps) | Low (3 reps, incumbent reaction) | High (5 reps) |
|---|---|---|---|
| Revenue 2030 | EUR 4.05m | EUR 3.03m | EUR 6.74m |
| EBIT margin 2030 | ~1.5% | negative | ~10.3% |
| Peak cumulative cash need | ~EUR 1.5m | >EUR 1.5m (worse, not sized precisely) | ~EUR 1.0m |
| Clears EUR 6m / 8% bar? | No | No | Yes |

The swing factor is headcount and win-rate, not capital headroom — both low and high cases sit well under the EUR 5m cap.

### d. Compared with the alternative use of capital

Austria head's offer: EUR 2m → ~EUR 3.5m revenue, 10% EBIT by 2030 (management estimate, based on the 2024 Salzburg-region extension — a real, in-market comparable, not a cross-border guess).
- Run-rate EBIT 2030: EUR 0.35m on EUR 2m capital → **~17.5% EBIT/capital yield**.
- Czech base case (3 reps): EUR 0.06m EBIT on up to EUR 5m capital → **~1.2% yield**.
- Czech high case (5 reps, bar cleared): EUR 0.70m EBIT on ~EUR 1–1.3m actually deployed → **~55–70% yield**, i.e. if Kestrel commits to fixing the headcount gap, Czech entry could outperform the Austria alternative — but only if the untested assumption (Austria win-rate transfers unchanged into a market with entrenched, price-cutting incumbents) holds.
- The Austria estimate is itself a single-comparable management estimate and should be held to the same evidence standard as the Czech numbers, not treated as a safe default.

## Step 4: Trap checks

- [x] Share built bottom-up from accounts, reps and win rates, not "1% of a big market." — done in Step 3c.
- [ ] **Customers, channels and price tested in the target market, not copied from home.** Open — the entire plan copies the Austria win-rate (40/rep/yr) and churn (8%) onto a Czech market Kestrel has never sold in, against incumbents with an entrenched 55% share. No Czech-specific win-rate evidence exists. **Fix before committing:** a 2027 pilot (1 region, 1–2 reps) to measure actual first-year win rate before scaling to 3+ reps.
- [ ] **At least one aggressive incumbent reaction modelled.** Open in the base case — fixed in the Low case above, which shows the bar is missed by more, not less, once the 2024 precedent (12% price cut on new entry) is factored in.
- [x] Sunk costs (EUR 120k study, interviewed candidate) play no role in the recommendation.
- [ ] **Ramp compared with a true outside-view comparable.** No cross-border entry comparable exists in the brief; the only comparable (Austria/Salzburg) is a domestic regional extension, not a foreign-market entry, so it understates the risk. Range widened accordingly (Low/Base/High above); flagged as a gap, not filled from memory.
- [x] Exit criteria defined before entry (see Answer Page).
- [x] Entry compared with the best alternative use of the same capital (Step 3d).

## Step 5: Answer page

---

# Market entry: Kestrel Logistics, Czech Republic medical same-day, enter by 2030?

**Answer:** Do not approve the current plan (3 reps from 2027) — it misses the board's bar. Approve a **rescoped, gated entry**: fund a 2027 one-region pilot (1–2 reps) to test real Czech win-rate and incumbent reaction; if the pilot clears ~80% of the Austria win-rate (≥32 accounts/rep/year) by end-2027, scale to ~5 reps total — still under EUR 1.3m peak cash need, well inside the EUR 5m cap — targeting EUR 6.7m / ~10% EBIT by 2030. If the pilot fails that threshold, or by end-2029 the business is not tracking to ≥EUR 5m 2030 run-rate (~553 accounts), exit and redirect capital to the Austria two-region extension (EUR 2m → EUR 3.5m revenue / 10% EBIT by 2030) instead.

**Confidence:** Medium. High confidence that the current 3-rep plan mathematically misses the bar — that comes straight from Kestrel's own account-math convention and Austria benchmarks, with no favorable assumption needed. Lower confidence on whether a rescoped 5-rep plan would actually clear the bar, because it rests on an untested assumption: that Austria's rep productivity transfers unchanged into a Czech market with two incumbents who have already shown they'll cut price ~12% against a new entrant. A one-region pilot resolves this before the full capital commitment.

**Specialists and review:** Czech entity setup, driver/courier employment classification, and cross-border VAT/transfer pricing for the new depot need local legal and tax review before the pilot is funded, not after. A partner-style review of this account-math model (especially the win-rate and churn transfer assumptions) should happen before it goes to the board.

## Minimum bar agreed with the board
- Revenue ≥ EUR 6m and EBIT margin ≥ 8% by 2030; capital up to EUR 5m; exit decision at end-2029 if off track.
- Kill criteria set here: pilot win-rate below 32 accounts/rep/year by end-2027; or end-2029 run-rate below EUR 5m (~553 accounts).

## Is the market attractive?
| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Addressable size and growth | ~EUR 25.65m (bottom-up, pharmacies, 3 regions) vs. ~EUR 31.5m (top-down, whole medical segment) — consistent order of magnitude, large enough | Market study 2026 (60-pharmacy survey; top-down 15% of EUR 210m) | Pass, with weak-evidence flag on the per-pharmacy figure |
| Concentration and incumbents | Two players hold ~55%; no per-region split known | Market study 2026 | Pass, but see reaction risk below |
| Incumbent reaction | Larger incumbent cut price ~12% for 6 months against a 2024 entrant | Market study interviews | **Risk, not modelled in the plan — now modelled in Low case** |
| Barriers and regulation | Not assessed in the brief | — | Open — flag for legal/regulatory specialist |

## Can we win?
| Factor | Kestrel (Czech, planned) | Incumbent A/B (combined ~55% share) |
|---|---|---|
| Win rate | Assumed = Austria's 40/rep/yr — **unverified in Czech market** | Entrenched relationships; price-cut precedent shows willingness to defend share |
| Cost structure | 70% variable, depot EUR 0.9m, reps EUR 85k each | Unknown |
| Brand/relationships | None yet in Czech Republic | Established |

## Business case (base / low / high)
| | Base (3 reps) | Low (3 reps + incumbent reaction) | High (5 reps, pilot confirms win-rate) |
|---|---|---|---|
| Revenue 2030 | EUR 4.05m | EUR 3.03m | EUR 6.74m |
| EBIT margin 2030 | ~1.5% | negative | ~10.3% |
| Peak cumulative investment | ~EUR 1.5m | >EUR 1.5m (not fully sized) | ~EUR 1.0m |
| Payback (cumulative basis) | Not reached by 2030 | Not reached | ~End of 2030 |
| Clears the board's bar? | No | No | Yes |

## Compared with the alternative use of capital
The Austria two-region extension (EUR 2m capital → ~EUR 3.5m revenue / 10% EBIT by 2030, estimated from the 2024 Salzburg extension) returns roughly 17.5% EBIT-to-capital at run-rate, against ~1.2% for the Czech base case and a speculative ~55–70% for the Czech high case if the win-rate assumption holds. The Austria option is the safer, capital-light default; the Czech option can beat it only if the rescoped plan and its central assumption survive the pilot. They are not mutually exclusive at this capital scale — both fit inside envelopes well under EUR 5m — so the realistic choice is "Austria now, Czech pilot in parallel," not strictly either/or.

## What would change the answer
1. If the 2027 pilot shows a Czech win-rate at or above ~32 accounts/rep/year (80% of Austria's), scale to 5 reps and the board's bar becomes reachable — proceed.
2. If the incumbent reaction turns out weaker than the 2024 precedent (e.g., no retaliatory price cut), the Low case collapses toward Base/High and the entry case strengthens.
3. If regional incumbent share in the 3 target regions is far above the 55% national figure, kill the plan regardless of pilot win-rate — reaction risk would dominate.
4. If Austria's own Salzburg-extension case underperforms its estimate when it actually runs, revisit the alternative-use-of-capital comparison — it currently favors Austria partly on an unproven management estimate too.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Austria win-rate transfers to Czech Republic | 40 new accounts/rep/year | Austria 2023–25 average (own data) | Pilot shows materially lower (or higher) Czech win-rate |
| 2 | Churn unchanged in a new market | 8%/year | Austria own data | Czech churn runs higher (unfamiliar brand, weaker service relationships early on) |
| 3 | Revenue-per-account unchanged under competitive pressure | EUR 9,500/pharmacy/year | Market study survey (60 pharmacies) | Incumbent price war compresses achievable pricing below this |
| 4 | Fixed-cost structure scales linearly with reps | Depot EUR 0.9m + EUR 85k/rep | Own data | Depot has step-function capacity limits not captured here |
| 5 | Incumbent reaction to Kestrel mirrors the 2024 precedent | 12% price cut, 6 months, applied as ~6% annual drag in Low case | Market study interviews (one historical instance) | Reaction is stronger/longer, or absent entirely |
| 6 | Hospitals/labs excluded from the revenue plan | EUR 0 attributed, pharmacy-only build | Account math is pharmacy-only by convention | Kestrel later adds a hospital/lab sales motion — upside not counted here |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is incumbent share within the 3 target regions specifically (vs. 55% national)? | National concentration may understate or overstate local reaction risk | Market study author / a targeted regional survey | Could kill or de-risk the plan independent of the account math |
| What is the size of the hospital/lab medical-courier segment? | Survey only covered pharmacies; this is unpriced upside or a separate sales motion with its own economics | Market study author / new primary research | Could close part of the revenue gap without more reps |
| What would wind-down cost if Kestrel exits at end-2029 (lease break, severance, customer handover)? | Board asked for "a way out" — exit cost isn't quantified anywhere in the brief | Finance / Austria ops (lease and HR terms) | Changes the true downside of the "pilot then scale" path vs. not entering at all |
| Is the Czech depot/entity subject to local licensing, courier employment law, or VAT/transfer-pricing rules that add cost or delay? | Not assessed in the brief; could change fixed cost or timeline | Local legal/tax counsel | Could shift fixed-cost assumptions or push the ramp back a year |
| How firm is the Austria/Salzburg comparable behind the alternative's EUR 3.5m/10% estimate? | It's a single management estimate, same evidence standard the Czech case is held to | Head of Austria / Salzburg P&L actuals | Narrows or widens the capital-efficiency gap used to rank the two options |

