# cg-01-revenue-gap on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question in the skill's form (gap EUR140m→175m by 2030, EUR15m capital, no acquisitions, EBIT margin ≥10%, board March 2027) | yes | Header: 'which levers close the gap from EUR 140m to EUR 175m revenue by 2030, within EUR 15m capital and a 10% group EBIT margin floor, no acquisitions?' plus 'Bring the board a revised, de-risked plan for March 2027' |
| Computes a momentum case of about EUR 140-141m and a gap of about EUR 34m using the CFO convention | yes | 'Total momentum 2030 ≈ EUR 140.7m → gap to EUR 175m = EUR 34.3m' with CAGR continuation per 'CFO convention' |
| Separates market growth from share change and states Kirkby lost share in both lab instruments and process sensors | yes | Table: 'Lab instruments ... Losing share'; 'Process sensors ... Losing share — growing, but slower than the market' |
| Sizes the core (share recovery, price) and installed base (service coverage) before the software adjacency, each with base case/range/evidence grade | NO | Only price and installed-base levers are sized; a share-recovery lever (e.g. holding/regaining share) is never quantified — 'Process sensors share recovery / Not sized ... No data' is left as an 'Open question', and no equivalent lab-instrument share-recovery case is computed at all |
| Installed-base lever about EUR 4.3m at 50% coverage (or consistent alternate coverage level) | yes | 20% take-up → EUR3.72m at ~48% total coverage, 30% take-up → EUR5.58m at ~54.5% coverage; interpolating the stated range to 50% coverage lands at ≈EUR4.3m, consistent with the given arithmetic (14,300×rate×EUR1,300) |
| Treats EUR15m software figure as unsupported: widens range or kills it, names a comparison that would settle it, without inventing one | yes | 'Hypothesis killed as a committed base-case lever, kept as an option pending validation' requiring '2-3 customer pilots or signed LOIs, and a search for comparable adjacent-market software launches to benchmark ramp-up' |
| Shows profit next to revenue for every kept lever and checks the 10% EBIT floor | yes | Levers table has 'EBIT effect' column for each kept lever; 'Margin check' section computes 12.4% and 14.6% against the '10% floor' |
| Shows the remaining gap openly after base-case levers and says how it is closed or accepted | yes | 'Sum of kept levers (base case): EUR 8.6m; remaining gap: EUR 25.7m (EUR 10.7m even if software's unvalidated EUR 15m is fully credited); how we close or accept it: ...' |
| Answer line names specific levers with amounts and investment, plus a confidence level with one reason | yes | 'reset lab-instrument list prices ... ~EUR 3.0m revenue ... near-zero investment ... convert part of the uncontracted installed base ... ~EUR 5.6m revenue ... modest sales/ops investment'; 'Confidence: low-medium, because the two core levers rest on reasonable but unverified take-up/elasticity assum |
| Assumptions table and open-questions table in the skill's format | yes | Both '## Assumptions' and '## Open questions' tables present with the expected columns (#, Assumption, Value used, Basis, Would change the answer if / Question, Why it matters, Who can answer, Effect on the answer) |
| Must not close the gap by stretching assumptions (e.g. full share recovery plus EUR15m software at base case with no range) | yes | Document explicitly leaves 'remaining gap: EUR 25.7m' open rather than assuming software or full share recovery into the base case |
| Must not invent market data, competitor prices, or benchmark ramp-up rates | yes | Market growth figures (lab +3%/yr, sensors +6%/yr) are consistent with the underlying cumulative 2023-25 figures rather than invented; software ramp-up explicitly not assumed: 'no comparable launch data was available in this pack to benchmark the ramp-up, and none should be assumed from memory' |

## Transcript

## Turn 1

**User:** Work the Kirkby growth case from the briefing pack. Quick case, no engagement folder. I need the answer page for the CEO. (Attached in the working directory: cg-01-input.md.)

Answer page written to `case-growth-strategy-kirkby.md`. Headline finding: the head of strategy's software bet is wrong as the answer — even taken at full, unvalidated face value (EUR 15m), the plan still misses the board's EUR 175m target by ~EUR 10.7m, since momentum alone only reaches EUR 140.7m (lab instruments decline offsets process-sensor growth) against a EUR 34.3m gap.

The data shows Kirkby is losing share in **all three** segments against growing served markets — not facing market saturation. That points to two cheap, fast, margin-accretive core fixes instead: a 4% lab-instrument price reset (~EUR 3.0m, near-zero cost since it's priced 7% below competitors for no stated reason) and converting part of the 65% uncontracted installed base to service contracts (~EUR 5.6m at 30% take-up). Together these close only ~25% of the gap but need under EUR 2m of capital and keep EBIT margin well above the 10% floor (rising to ~14.6%). I've recommended gating the software's EUR 9m behind a real pilot rather than committing it on an unverified slide claim.

Open items worth your attention before the March 2027 board meeting are flagged in the file — notably that process sensors (the fastest-growing, highest-margin segment) has no sized lever yet due to missing price/competitor data, and the 22,000-unit installed base figure doesn't fully reconcile against the EUR 20m service line.


## Files in work dir after run

- case-growth-strategy-kirkby.md
- cg-01-input.md

## File written by the run: case-growth-strategy-kirkby.md

# Growth strategy: Kirkby Analytical, which levers close the gap from EUR 140m to EUR 175m revenue by 2030, within EUR 15m capital and a 10% group EBIT margin floor, no acquisitions?

**This contradicts the head of strategy's premise:** even if the process analytics software hits its own unvalidated EUR 15m target in full, the plan still misses the board's EUR 175m goal by roughly EUR 10-11m. Software cannot be "the answer" on its own — and its EUR 15m/EUR 9m figures rest on no customer interviews, pilots or comparable launches, the weakest evidence in the whole pack, yet it claims 60% of the capital budget.

**Answer:** Fund two core-fix levers first — reset lab-instrument list prices toward parity with competitors (+4%, ~EUR 3.0m revenue by 2030, near-zero investment, flows ~100% to EBIT) and convert part of the uncontracted installed base to Kirkby service contracts (~30% take-up, ~EUR 5.6m revenue by 2030 at the segment's 24% margin, modest sales/ops investment). Together these close only ~25% of the gap (EUR 8.6m of EUR 34.3m) but need under EUR 2m of capital and raise group EBIT margin, not risk it. Gate the software bet behind a EUR 1-2m pilot (customer LOIs, 2-3 reference pilots) before committing the remaining EUR 9m; do not book its EUR 15m into the base case until that evidence exists. Bring the board a revised, de-risked plan for March 2027 and flag now that, on current evidence, the EUR 175m target likely needs either a bigger core push (deeper price reset, higher contract take-up) or an accepted miss of ~EUR 10-25m depending on how software performs.

**Confidence:** low-medium, because the two core levers rest on reasonable but unverified take-up/elasticity assumptions, and the single largest lever in the existing plan (software) has no supporting evidence at all; this would firm up with actual price-elasticity and contract win-rate data, and with pilot results for the software offer.

**Specialists and review:** no legal/tax/regulatory question is load-bearing for this decision; flag for completeness: (1) contracts/legal review of service-contract terms before a push to convert uncontracted instruments (liability, SLAs); (2) data-privacy/IP review before any process analytics software pilot that touches customer process data.

## The gap

| | 2025 | 2030 |
|---|---|---|
| Revenue, momentum case (segment CAGR 2023-25 continued) | 140 | 140.7 |
| Revenue, target | 140 | 175 |
| Gap | — | **34.3** |
| Constraints | capital EUR 15m, EBIT margin floor 10%, ruled out: acquisitions |

**Momentum case arithmetic** (CFO convention: continue each segment's 2023-25 CAGR to 2030):
- Lab instruments: 82→80 over 2023-25 = CAGR -1.23%/yr → 80 × (0.9877)^5 ≈ **EUR 75.2m**
- Process sensors: 38→40 = CAGR +2.60%/yr → 40 × (1.0260)^5 ≈ **EUR 45.5m**
- Service: 20→20→20 = CAGR 0% → **EUR 20.0m** (flat)
- Total momentum 2030 ≈ **EUR 140.7m** → gap to EUR 175m = **EUR 34.3m**

Revenue has looked "stuck," but that masks three different stories, confirmed next.

## Market vs. share (hypothesis: core is losing share, not a saturated market)

| Segment | Kirkby CAGR 2023-25 | Served market growth | Share trend |
|---|---|---|---|
| Lab instruments | -1.23%/yr | +3%/yr | **Losing share** — shrinking in a growing market |
| Process sensors | +2.60%/yr | +6%/yr | **Losing share** — growing, but slower than the market |
| Service | 0%/yr | +4%/yr | **Losing share** — flat in a growing market |

**Hypothesis confirmed in all three segments**: the market is not the constraint; Kirkby is underperforming its own served markets everywhere. Per the playbook, this means the core and installed base — not an unrelated adjacency — hold the fastest, cheapest growth, and should be sized before the software bet.

## Installed base and wallet (lever: service contract conversion)

- 22,000 instruments in the field; 35% (7,700) under a Kirkby contract at EUR 1,300/instrument/yr (≈EUR 10.0m of the EUR 20m service line; the rest is parts/repairs, much of it likely from the uncontracted base).
- 65% (14,300) uncontracted — service manager confirms most go to independent shops or run with no contract, i.e. real convertible demand exists.
- **Lever, base case 30% take-up of the uncontracted base**: 14,300 × 30% × EUR 1,300 = **EUR 5.58m** revenue by 2030, at the segment's 24% EBIT margin → **EUR 1.34m EBIT**.
  - Range: 20% take-up → EUR 3.72m; 45% take-up → EUR 8.37m.
  - Evidence: **weak-medium** — no Kirkby-specific win-rate/conversion data; take-up rate is an assumption benchmarked against comparable installed-base plays, not Kirkby history.

**Hypothesis confirmed, reshaped to a range**: the installed base is a real, low-capital lever, sized at EUR 3.7m-8.4m depending on take-up.

## Price position (lever: lab-instrument price reset)

- Kirkby lab instruments list ~7% below the two main competitors, with "no volume reason recorded" — i.e. the discount looks unearned, not a deliberate value trade-off.
- **Lever, base case +4% reset** (mirrors a defensible partial close, leaving Kirkby ~3% below competitors as a buffer against demand response): 4% × EUR 75.2m (2030 momentum revenue) = **EUR 3.0m** revenue, flowing almost entirely to EBIT since it is a pure price move on existing volume.
  - Range: +2% (conservative) → EUR 1.5m; +7% (full close) → EUR 5.3m.
  - Evidence: **medium** — the price gap itself is a measured fact; the assumption that volume holds through the increase is untested (no elasticity data, no pilot).

**Hypothesis confirmed, reshaped to a range**: price is a near-zero-capital, margin-accretive lever, but the "no volume impact" assumption needs a test (e.g. a phased or regional rollout) before betting the full gap on it.

## Process analytics software (adjacency — gate, do not commit)

- Head of strategy's claim: EUR 15m revenue by 2030 on EUR 9m investment. No customer interviews, no pilots, no comparable launches cited.
- Outside view: no comparable launch data was available in this pack to benchmark the ramp-up, and none should be assumed from memory. This is exactly the "inside view on a new move" trap — a plan built on the plan's own logic, not on evidence.
- **Hypothesis killed as a *committed base-case lever*, kept as an option pending validation.** It should not enter the base-case revenue sum until at least: 2-3 customer pilots or signed LOIs, and a search for comparable adjacent-market software launches to benchmark ramp-up.
- Even if granted at full face value (EUR 15m, no discount for the missing evidence), the portfolio still misses the target — see Levers table. That is the decisive fact: the target problem is not "is software worth it," it is "the core levers plus even a fully-trusted software number don't reach EUR 175m."

## Levers

| Lever | Revenue base case (2030) | Range | EBIT effect | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Lab instrument price reset (+4%) | EUR 3.0m | EUR 1.5m-5.3m | ~+EUR 3.0m (near 100% flow-through) | ~EUR 0m | Immediate | Medium | **Keep** |
| Service-contract conversion (30% take-up of uncontracted base) | EUR 5.6m | EUR 3.7m-8.4m | ~+EUR 1.3m (at 24% margin) | ~EUR 1-2m (sales/ops capacity, assumption) | 1-3 years | Weak-medium | **Keep** |
| Process analytics software | EUR 0 in base case (claimed EUR 15m unvalidated) | EUR 0 (no pilot) to EUR 15m (if claim holds) | Unknown — no cost/margin data given | EUR 9m (per slide) | 2027+ pilot, scale after | **Weak** | **Option — pilot-gate, do not fund in full now** |
| Process sensors share recovery | Not sized | — | — | — | — | No data (no price/competitor benchmark given for sensors) | **Open question** |

**Sum of kept levers (base case):** EUR 8.6m; **remaining gap:** EUR 25.7m (EUR 10.7m even if software's unvalidated EUR 15m is fully credited); **how we close or accept it:** take the core levers now (low capital, margin-accretive), run the software pilot in 2027 with a small tranche of the EUR 9m, and bring the board either a larger core push (deeper price reset, higher contract take-up, a sized sensors lever once data exists) or a reset target/timeline — rather than carrying an unvalidated EUR 15m as if it were decided.

## Margin check

Momentum 2030 EBIT (segment margins held flat): Lab 75.2×9%=6.8m, Sensors 45.5×13%=5.9m, Service 20×24%=4.8m → EUR 17.5m / EUR 140.7m = **12.4%**, already above the 10% floor.
With the two kept levers: revenue EUR 149.3m, EBIT ≈ EUR 21.8m → **margin ≈14.6%**. The 10% floor is not the binding constraint in this plan — the revenue gap is. There is margin headroom to absorb a weaker-than-planned software outcome without breaching the floor.

## Killed options and why
- **Software as the primary, committed lever**: killed in that role — its own numbers, taken at face value, still leave the plan ~EUR 10.7m short, and the numbers have zero supporting evidence (no interviews, pilots, or comparables). Kept only as a pilot-gated option.
- **Acquisitions**: out of scope per the board's own rule-out; not evaluated.

## Risks and what would change the answer
1. If price elasticity is worse than assumed (volume falls when the discount is removed), the price lever's EUR 3.0m base case could turn negative — a phased/regional test should run before a full reset.
2. If service-contract take-up lands below 20% (independent shops prove sticky), the installed-base lever shrinks toward EUR 3.7m or less, widening the gap further.
3. If the software pilot fails to validate demand, the EUR 9m should not be spent, and the board should be told the honest gap (EUR 25.7m) rather than a plan that assumes it away.
4. Process sensors is losing share against a 6%-growing market with no lever identified yet — this is the largest un-investigated branch and could hold more upside than software if a price/competitive-position study (like the one done for lab instruments) is run there.

## Next steps
| What | Who | By when |
|---|---|---|
| Commission a price-elasticity test (phased/regional) for the lab-instrument reset | Commercial/sales lead | Q1 2027 |
| Size the uncontracted-base conversion pipeline with real win-rate data, not an assumed take-up rate | Service manager | Q4 2026 |
| Run a process analytics software validation (2-3 customer pilots or LOIs; search comparable launches) before committing beyond a small pilot tranche of the EUR 9m | Head of strategy | Before March 2027 board meeting |
| Commission a price/competitor study for process sensors, mirroring the lab-instruments comparison | Commercial/sales lead | Q1 2027 |
| Reconcile the 22,000-unit installed base and the EUR 1,300 contract rate against the full EUR 20m service line (contracts vs. parts/repairs split) | Finance / service manager | Q4 2026 |

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Momentum convention taken literally (CAGR continuation to 2030) | As per CFO convention | Agreed with CFO | Any segment's underlying trend inflects (e.g. sensors market matures) |
| 2 | +4% lab-instrument price increase does not materially reduce volume | EUR 3.0m base case | Price gap has "no volume reason recorded," implying limited risk | Elasticity test shows volume loss, or competitors reprice in response |
| 3 | 30% take-up of the uncontracted installed base is achievable within the plan period | EUR 5.58m base case | Directional analogy to comparable installed-base conversion plays; no Kirkby-specific data | Actual sales pipeline/win-rate data comes in above or below this |
| 4 | New service-contract revenue carries the existing 24% segment margin | EUR 1.34m EBIT from the lever | No separate cost data for new vs. mature contracts | Contract-specific cost/margin data differs materially |
| 5 | Software revenue (EUR 15m) and investment (EUR 9m) figures are unvalidated and excluded from the base case | EUR 0 in base case; EUR 15m shown only as an upside scenario | Explicitly no customer interviews, pilots, or comparable launches cited in the source slide | Real pilot/LOI evidence or comparable-launch benchmarks become available |
| 6 | The 22,000-unit installed base is the full addressable universe for service-contract conversion (not split by lab instruments vs. sensors) | 14,300 uncontracted units | CRM figure given without a segment breakdown | The base is predominantly one segment, changing the addressable pool for this lever |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is process sensors' competitive price position and the reason it underperforms its 6%-growing market? | No lever has been sized for the second-largest and fastest-growing segment; could be larger than the software bet | Commercial/sales lead | Could add a second core-fix lever, reducing reliance on software |
| Would a price increase trigger competitor retaliation or a volume response? | Determines whether the EUR 3.0m base case or a wider range (down to EUR 1.5m or negative) applies | Commercial/sales lead, via a phased test | Narrows the price lever's range |
| What is the real conversion economics (win rate, cost of sales, contract length, margin) for moving uncontracted instruments onto Kirkby contracts? | The service manager's comment is qualitative; the 30% take-up is an assumption | Service manager / sales ops | Narrows the installed-base lever's range |
| Can the software claim be supported by any customer interviews, pilots, or comparable adjacent-market launches? | The entire EUR 15m/EUR 9m case currently has zero supporting evidence despite being 60% of the capital ask | Head of strategy | Determines whether software enters the base case at all, and at what level |
| Why is the 22,000-installed-base figure not reconciled against the EUR 20m total service revenue (only ~EUR 10m is explained by contract units × rate)? | Affects how much of the service line, and which future lever, the installed-base figure actually supports | Finance / service manager | Could change the addressable base for the conversion lever |

## Trap checks
- [x] **Adding up hope** — Each lever shown on its base case with a range; remaining gap (EUR 25.7m, or EUR 10.7m even crediting software in full) is stated openly, not closed by stretching assumptions.
- [x] **Skipping the core** — Market-vs-share split and installed-base/price levers were sized and confirmed as real, low-capital opportunities before evaluating the software adjacency.
- [ ] **Inside view on new moves** — Open. No comparable launch data exists in this pack to benchmark software ramp-up; flagged as a required validation step (pilot/LOIs/comparables) before the figure is used, rather than invented from memory.
- [x] **Market growth confused with share growth** — Explicitly separated per segment: Kirkby is losing share in a growing market in all three segments, not facing a saturated or shrinking market.
- [x] **Ignoring the constraints** — No lever uses acquisitions (ruled out); core levers need under EUR 2m of capital, leaving most of the EUR 15m available for a gated software pilot, well within the limit.
- [x] **Too many initiatives** — Two core levers (price, installed base) carry the plan; software is held as a single gated option, not stacked with many small initiatives.
- [x] **Revenue without margin** — Margin check shows group EBIT margin rising to ~14.6% under the kept levers, well above the 10% floor; the floor is not the binding constraint, the revenue gap is.

