# cme-01-czech-medical on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (12/13 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States decision question with minimum bar and kill criteria before analysing | yes | Title and 'Minimum bar agreed' section state 'at least EUR 6m and EBIT margin at least 8%... by 2030', 'Capital: up to EUR 5m', and exit trigger, all placed before the market/business-case analysis. |
| Sizes segment top-down (~31.5m) and bottom-up (~25.7m), explains/flags difference | yes | 'Top-down: medical/pharmacy segment ≈ EUR 210m × 15% = EUR 31.5m/yr. Bottom-up... 2,700 pharmacies × EUR 9,500 = EUR 25.65m/yr... the gap is a red flag' and later flags hospitals/labs as the likely explanation. |
| Builds ramp from reps x win rate, arrives ~EUR 4.0-4.6m revenue in 2030, below EUR 6m bar | yes | 'Accounts(t) = Accounts(t−1) × (1 − 8% churn) + (reps × 40 new accounts/yr)'... 'Revenue 2030: EUR 4.04m' in the base 3-rep case, explicitly below the EUR 6m bar. |
| Computes 2030 EBIT margin below 8% (~1-5%) | yes | 'EBIT margin 2030: 1.4%' in the base case table. |
| Models at least one aggressive incumbent reaction using 2024 price-cut evidence and reports effect | yes | 'In 2024, when a new carrier entered, the larger incumbent cut prices ~12% for 6 months'... Low case: 'Revenue ≈ EUR 3.7–3.8m... EBIT margin negative-to-flat'. |
| States EUR 120k study is sunk and plays no role | yes | 'Sunk cost (EUR 120k study) and an interviewed-not-hired candidate play no role in this recommendation — they are spent/optional, not reasons to enter.' |
| Compares with Austrian alternative per euro of capital, flags it as a management estimate to test | yes | 'EUR 0.35m EBIT on EUR 2m capital (17.5%)... is a management estimate based on one precedent... should be tested the same way before being taken as given.' |
| Does not approve the briefed 3-rep plan; answer is do-not-enter/enter-later/conditional with stage gate and revisit trigger | yes | 'Do not approve the Czech entry as currently planned... approve a capped pilot... with a hard go/no-go gate in 2028 before any commitment to the 5-rep design' and 'What would change the answer' section. |
| Compares at least two entry modes (own office, partner/distributor, acquisition) on cost, speed, control, exit cost | NO | The analysis only varies scale of Kestrel's own hiring plan (3-rep vs 5-rep vs 1-rep pilot); no mention of a partner/distributor or acquisition-of-local-courier entry mode anywhere in the document. |
| Writes exit criteria and exit cost | yes | Exit criteria: 'board's own end-2029 checkpoint'; exit cost explicitly addressed: 'exit cost not quantifiable from the data given (no wind-down/lease/severance figures) — flagged as an assumption gap' plus an open question on wind-down cost. |
| Flags that Austrian win rates/prices may not transfer to Czech market and names the test | yes | Assumption #1: 'Czech win rate per rep equals Austrian average... Would change if Czech pilot shows materially higher or lower'; pilot explicitly designed 'to generate real Czech win-rate and realised-price data'. |
| Does not recommend unconditional entry on the EUR 210m headline | yes | Recommendation is 'Do not approve the Czech entry as currently planned'; the EUR 210m/31.5m figures are used only for sizing, not as grounds for unconditional entry. |
| Does not invent Czech regulatory requirements, competitor names, or wage levels as facts (may flag for specialists) | yes | Regulatory certification is hedged ('typically needs... needs local regulatory counsel before any commitment') and tabled as 'Open / unknown — specialist needed'; competitors are referred to generically as 'Incumbent A+B', not invented names. |

## Transcript

## Turn 1

**User:** Work the Kestrel Czech entry case from the briefing. Quick case, answer page for the board. (Attached in the working directory: cme-01-input.md.)

The analysis contradicts the plan as tabled: the 3-rep Czech entry Kestrel's own briefing describes reaches only ~EUR 4.0m revenue and 1.4% EBIT margin by 2030 — missing both board bars, not by a little.

**Answer:** Don't approve the Czech entry as planned. Fund the proven EUR 2m Austria expansion instead, and if the board wants to keep Czech alive, do it as a small capped pilot (1 rep, 1 region) to test the win-rate/pricing assumptions before committing to the 5-rep design that the same math says *would* clear both bars by 2030.

Full answer page with the arithmetic, business case (base/low/high), trap checks, assumptions and open questions is written to `case-market-entry-kestrel.md` in the working directory.

Key finding: the 3-rep plan fails because the fixed depot cost (EUR 0.9m/yr) swamps a slow-ramping book — it wouldn't clear EUR 6m revenue until ~2033. A 5-rep version clears both bars in 2030 within the capital cap, but requires capturing ~26% of all pharmacies in the three target regions against incumbents holding 55% share who've already shown they'll price-war a new entrant — an assumption nothing in the data actually tests.


## Files in work dir after run

- case-market-entry-kestrel.md
- cme-01-input.md

## File written by the run: case-market-entry-kestrel.md

# Market entry: Kestrel Logistics, Czech Republic (medical same-day delivery), should Kestrel enter by the January 2027 board, and if so how, given it must deliver at least EUR 6m revenue and 8% EBIT margin by 2030 within EUR 5m capital?

**Answer:** Do not approve the Czech entry as currently planned. On Kestrel's own account economics, the proposed 3-rep plan delivers only about **EUR 4.0m revenue (33% short of the EUR 6m bar) and a 1.4% EBIT margin (vs. the 8% bar) by 2030**, and would not clear the revenue bar until roughly 2033 — three years late. Fund the proven EUR 2m Austria regional expansion now. Keep a Czech option open only as a small, capped pilot (1 rep, 1 region, ~EUR 0.3–0.5m, 12–18 months) to test whether the win-rate and price-per-account assumptions actually hold in the Czech market before committing to the 5-rep design that the same economics say *would* clear both bars.

**Confidence:** Medium — high confidence that the 3-rep plan as tabled fails (this follows directly from Kestrel's own stated unit economics, not from contested market data); low confidence on whether any rescoped Czech entry would work, because it rests on an untested transfer of the Austrian win rate and a thin 60-pharmacy survey. Would change if a Czech pilot shows reps can win accounts at a rate and realised price close to the Austrian figures.

**Specialists and review:** (1) Regulatory/compliance — medical/pharma courier work typically needs cold-chain and Good Distribution Practice-type certification; the market study does not address this — needs local regulatory counsel before any commitment. (2) Labour/HR — hiring Czech sales reps and depot staff triggers local labour-law and possibly works-council questions — needs local HR/legal input. (3) This business case should go through a standard finance/partner review before it reaches the board paper.

## Minimum bar agreed (from the briefing)
- Revenue at least EUR 6m and EBIT margin at least 8% in the Czech business by 2030
- Capital: up to EUR 5m
- Exit trigger: a "way out" if the bar is missed by end of 2029 (treated here as a checkpoint — see Open questions on what exactly is measured at that date)
- Sunk cost (EUR 120k study) and an interviewed-not-hired candidate play no role in this recommendation — they are spent/optional, not reasons to enter.

## Is the market attractive?

| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Addressable size | Top-down: medical/pharmacy segment ≈ EUR 210m × 15% = **EUR 31.5m/yr**. Bottom-up (pharmacies only, 3 target regions): 2,700 pharmacies × EUR 9,500 = **EUR 25.65m/yr**. The two triangulate roughly (pharmacy-only bottom-up is ~81% of the top-down *total* medical segment, which should also include hospitals/labs — the gap is a red flag, see Assumptions) | 2026 market study | Pass on size alone — either figure is several times the EUR 6m bar |
| Concentration | Two local players hold ~55% combined, leaving ~45% open (≈ EUR 14.2m top-down / EUR 11.5m bottom-up contestable) | Market study | Caution, not an automatic kill — material open segment, but... |
| Incumbent reaction | In 2024, when a new carrier entered, the larger incumbent cut prices ~12% for 6 months | Study interviews (single instance) | Confirmed risk — must be modelled (see Low case) |
| Barriers / regulation | Not addressed in the study (cold-chain/GDP-type certification typical in pharma logistics) | — | Open / unknown — specialist needed |

## Can we win?

| Factor | Kestrel | Incumbent A+B (combined) |
|---|---|---|
| Share today | 0% | ~55% of medical segment, entrenched relationships |
| Win rate evidence | 40 new accounts/rep/yr, 8% churn — **Austria actuals, 2023–2025**, not yet tested in Czech market | Demonstrated willingness to defend share with a ~12% price cut against a new entrant (2024) |
| Cost base | Variable cost ~70% of revenue (Austria); depot fixed cost ~EUR 0.9m/yr (Czech estimate, basis not stated) | Unknown |

**Verdict: unproven.** The only evidence for how fast Kestrel can win accounts in the Czech Republic is its Austrian track record — a classic home-market transfer risk, especially against incumbents who have already shown they will cut price to defend share.

## Business case (base / low / high), 2030

Planning convention per the briefing: revenue in a year = pharmacy accounts in force at year-end × EUR 9,500. Accounts build as: Accounts(t) = Accounts(t−1) × (1 − 8% churn) + (reps × 40 new accounts/yr). Fixed cost = EUR 0.9m depot + (reps × EUR 85k).

| | **Base: 3 reps (as tabled)** | **Low: 3 reps + incumbent price reaction** | **High: 5 reps (rescoped)** |
|---|---|---|---|
| Accounts, end 2027 / 28 / 29 / 30 | 120 / 230 / 332 / 425 | similar, revenue haircut below | 200 / 384 / 553 / 709 |
| Revenue 2030 | **EUR 4.04m** | ≈ EUR 3.7–3.8m (illustrative; a 12% price cut for 6 months during the 2028 ramp pushes the whole curve down and out) | **EUR 6.74m** |
| EBIT margin 2030 | **1.4%** | negative-to-flat | **10.3%** |
| Cumulative EBIT 2027–30 (cash-burn proxy) | −EUR 1.46m | worse | ≈ breakeven (−EUR 0.04m) |
| Year revenue bar (EUR 6m) is reached | ~2033 (6.6 years into the ramp) | later still | 2030 |
| Year margin bar (8%) is reached | ~2032 | later | 2030 |
| End-2029 checkpoint (rev / margin) | EUR 3.15m / −6.6% | worse | EUR 5.26m / +4.8% — close but still short of EUR 6m/8% |

**Base case: both bars missed, decisively, and not close by 2030.** The structural problem is fixed-cost absorption: the EUR 0.9m depot cost is too large relative to a 3-rep ramp's revenue until well past 2030. **High case (5 reps): both bars cleared in 2030, inside capital (~EUR 1m peak cash tied up, well under EUR 5m)** — but it requires capturing ~709 pharmacy accounts, i.e. ~26% of all 2,700 pharmacies in the three target regions, against incumbents holding 55% combined share. That share-capture rate is not evidenced anywhere in the data provided; it is a mechanical consequence of transplanting the Austrian win rate onto a bigger sales team, not a tested finding.

## Compared with the alternative use of capital

The Head of Austria's proposal — EUR 2m for two more Austrian regions, ≈EUR 3.5m revenue at 10% EBIT (EUR 0.35m) by 2030 — is a management estimate based on one precedent (the 2024 Salzburg extension), so it carries the same "weak/single-data-point" evidence grade as the Czech case and should be tested the same way before being taken as given. On the numbers as stated, EUR 0.35m EBIT on EUR 2m capital (17.5%) in a market Kestrel already knows, with a team and playbook it has already run once, is a materially lower-risk use of the same board-approved capital pool than committing to an unproven ~26%-share-capture assumption in a new country against incumbents who have already shown they will price-fight a new entrant. The rescoped 5-rep Czech plan is mathematically more capital-efficient on paper (~EUR 1m peak burn for EUR 0.70m 2030 EBIT), but that comparison is only as good as the untested share assumption behind it — it is a higher-risk, higher-reward option, not a safer one.

**Recommendation:** fund Austria now; do not approve the 3-rep Czech plan; if the board wants to keep the Czech option alive, approve a capped pilot (1 rep, 1 region, ~EUR 0.3–0.5m, 12–18 months) to generate real Czech win-rate and realised-price data, with a hard go/no-go gate in 2028 before any commitment to the 5-rep design. This uses only a fraction of the EUR 5m ceiling and leaves the rest uncommitted until the pilot has an answer.

## Trap checks

- [x] Share built bottom-up from named accounts and win rates, not "1% of a big market" — done above; it is this bottom-up build that reveals the 3-rep plan fails and the 5-rep plan needs an aggressive 26% share.
- [ ] Customers, channels and price levels tested in the Czech market — **not done**; the 9,500/account figure and 40-accounts/rep win rate are Austrian-sourced or a thin 60-pharmacy survey. Flagged as the central open risk.
- [x] At least one aggressive incumbent reaction modelled — 12% price cut case included (Low case).
- [x] Sunk costs (EUR 120k study, interviewed candidate) excluded from the recommendation.
- [ ] Ramp compared with comparable entries — no outside comparable entry data was provided; range widened and the gap flagged.
- [x] Exit criteria named — board's own end-2029 checkpoint; exit cost not quantifiable from the data given (no wind-down/lease/severance figures) — flagged as an assumption gap.
- [x] Compared with the best alternative use of the same capital — Austria, above.

## What would change the answer
1. If a Czech pilot shows reps winning accounts at a rate and price close to the Austrian figures (not just the untested transfer), the 5-rep case becomes a credible "enter" — revisit with real data in 2028.
2. If the hospital/lab segment (not covered by the survey) turns out to be large and less contested than the pharmacy segment, the addressable base — and therefore the credibility of the 5-rep share assumption — would be larger than modelled here.
3. If the 12% incumbent price-cut precedent turns out to be an outlier (not the norm for this competitor), the Low case risk is smaller than assumed.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Czech win rate per rep equals Austrian average | 40 new accounts/rep/yr | Kestrel Austria actuals 2023–2025 | Czech pilot shows materially higher or lower — directly rescales every year of the ramp |
| 2 | Churn rate transfers unchanged | 8%/yr | Kestrel Austria actuals | Czech churn higher (e.g. due to incumbent defence) — slows net account growth further |
| 3 | Average pharmacy spend transfers to the Czech book | EUR 9,500/account/yr | Market study survey of 60/2,700 pharmacies (2.2% sample) | Real figure is lower (survey likely skews to above-average spenders) — every revenue figure above shrinks proportionally |
| 4 | Czech depot fixed cost | EUR 0.9m/yr | Planning estimate in the briefing, basis not detailed | Actual cost is materially higher or lower — directly moves the margin break-even point |
| 5 | Variable cost ratio transfers | 70% of revenue | Kestrel Austria actuals | Czech fuel/courier/vehicle costs differ — moves achievable margin at any revenue level |
| 6 | Incumbent reaction size/duration | −12% price for 6 months | Single 2024 precedent (study interviews) | Reaction is larger, longer, or targeted specifically at Kestrel — Low case understates the risk |
| 7 | Austria alternative's return | EUR 3.5m revenue / 10% EBIT by 2030 on EUR 2m capital | Head of Austria's estimate, based on one precedent (2024 Salzburg extension) | Salzburg-style ramp does not repeat in the next two regions — alternative is less attractive than it looks, though still lower-risk than Czech |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is the EUR 5m Czech capital cap and the EUR 2m Austria ask drawn from the same budget, or separate pools? | Determines whether Austria and a Czech pilot can both be funded simultaneously, or whether it's a strict either/or | CFO / board | If separate pools, fund both in parallel; if one pool, Austria should go first given its lower risk |
| What exactly triggers the "way out" at end of 2029 — must the full 2030 bar already be hit, or is 2029 just a progress checkpoint against a 2030 target? | Changes how the board should read the end-2029 numbers in both the base and high case | Board (it set the bar) | If the full bar must be hit by end-2029, even the 5-rep case (EUR 5.26m/4.8%) falls short and the Czech option looks weaker still |
| What pharma/medical courier certification (cold-chain, GDP-equivalent) does Czech regulation require, and how long does approval take? | Not covered by the market study; could be a hard gate on timing or on which mode of entry is viable | Local regulatory counsel | A long or uncertain approval process could rule out the 2027 start date Kestrel is planning around |
| What does the hospital/lab segment look like (size, incumbents, buying process)? | The market study only surveyed pharmacies; hospitals/labs are part of the EUR 31.5m top-down medical figure but entirely unsized bottom-up | Commission a follow-up study / local country-manager candidate | Could materially raise or lower the addressable base behind both the top-down and bottom-up size estimates |
| What wind-down cost would Kestrel face if it exits Czech at or after the 2029 checkpoint (lease, severance, customer handover)? | Needed to size the real downside of the entry decision | Finance / local counsel on Czech labour law | A high wind-down cost makes the "small pilot first" path even more clearly preferable to committing to 3 or 5 reps up front |
| Why was a country-manager candidate already interviewed before the board has decided whether to enter at all? | Signals momentum/sunk-cost pressure on this decision that should not influence it | Whoever ran that process | None on the numbers — but worth naming explicitly so the board does not treat it as a reason to proceed |

