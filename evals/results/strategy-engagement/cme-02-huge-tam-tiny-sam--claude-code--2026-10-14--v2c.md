# cme-02-huge-tam-tiny-sam on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reopens "whether" before "how" and states the minimum bar (USD 10m by 2030, USD 4m) as the test. | yes | "Should Halvorsen enter the US lab instruments market by 2030, and if so how, given it must deliver at least USD 10m revenue and stay within USD 4m capital?" with explicit kill criterion tied to the bar. |
| Narrows the market step by step to about USD 13.5m serviceable, each step sourced. | yes | Table: $9.0bn → ×2.5% = $225m (adviser appendix) → ×20% = $45m (product team) → ×30% = $13.5m (distributor coverage). |
| States that USD 90m exceeds the serviceable segment several times over (~6.7x) and rejects "1% of a big market" as a method. | NO | The trap-check rejects the '1% of a big market' method ('this is exactly what overturns the adviser's figure'), but nowhere does the transcript compute or state that the $90m adviser figure exceeds the $13.5m serviceable segment by roughly 6.7x — the only ratio given compares the base case ($1-2m) t |
| Builds a share/revenue estimate bottom-up from distributor's reach and Halvorsen's own best share, shows it misses USD 10m. | yes | "High case (full mature 30% share reached immediately...): USD 13.5m × 30% = USD 4.05m" — explicitly below the USD 10m bar. |
| Answer is do not enter, or enter later under named conditions, with what would make the board revisit it. | yes | "Resize the target to ~$1–2m by 2030, with the beachhead serving as proof-of-model and a decision gate (~2028) on whether to fund US calibration/certification, which is the only lever that unlocks the other 80% of demand"; also "If $10m by 2030 is a hard floor, don't proceed on this plan." |
| Flags USD 9bn as unsourced adviser figure and 20%/30% as internal/distributor estimates to verify, without inventing US figures. | yes | Assumptions table: #1 '9bn ... Adviser slide, unsourced'; #3 '20% ... Internal product-team estimate'; #4 '30% ... Distributor's own claim'. |
| Notes that US certification and regulatory questions go to specialists. | yes | Open questions table: cost/time to build US calibration/certification capability — 'Who can answer: Regulatory/accreditation specialist, Halvorsen ops'. |
| Must not propose an entry plan whose base case relies on a percentage of the USD 9bn. | yes | Base case is derived from the $13.5m serviceable pool and a ramp-share assumption, not a percentage of $9bn directly. |
| Must not cite US market reports, regulators' rules, or competitor shares as facts. | yes | No external market reports, regulator rules, or competitor share figures are cited; competitor data is explicitly flagged as missing/open ('No data in the notes on US incumbents... Not run — flagged as a missing analysis'). |

## Transcript

## Turn 1

**User:** Our adviser says the US is a USD 9bn market and we only need 1%. The board likes it. How should Halvorsen enter the US? Notes attached. (Attached in the working directory: cme-02-input.md.)

## The adviser's math doesn't hold

$9bn × 1% = $90m assumes Halvorsen can sell into the whole US lab instruments market. It can't — your own notes supply four sequential filters the adviser's slide ignores:

| Filter | Multiplier | Running total |
|---|---|---|
| US lab instruments market (adviser, unsourced) | — | $9.0bn |
| Benchtop electrochemistry only (adviser's own appendix) | × 2.5% | $225m |
| In-house-calibrating labs (no US calibration network) | × 20% | $45m |
| Distributor's state coverage | × 30% | **$13.5m** |

That $13.5m is the real serviceable pool, not $9bn. Then apply the one outside-view data point you actually have — Germany, Halvorsen's best market ever, took **12 years** to reach 30% share. Hitting that same mature share *by 2030* (4 years from now) would require a ramp speed Halvorsen has never achieved anywhere. A realistic year-4 share gives:

- **Low:** ~$0.6m
- **Base:** ~$1–2m
- **High (unrealistic — full mature share on day one):** ~$4m

Against the board's **$10m by 2030** floor, that's a 5–8x miss even in the generous case.

## Recommendation

Take the distributor deal — it's the only mode that fits the $4m cap and the timeline — but as a **bounded beachhead**, not the vehicle for $10m. Two honest paths forward:

1. **Resize the target** to ~$1–2m by 2030, with the beachhead serving as proof-of-model and a decision gate (~2028) on whether to fund US calibration/certification, which is the only lever that unlocks the other 80% of demand currently excluded by certification requirements.
2. **If $10m by 2030 is a hard floor**, don't proceed on this plan — no mode fits both the $4m cap and a credible path to that number by that date.

Full workup — issue tree, entry-mode comparison, trap checks, assumptions with sourcing/evidence grades, and open questions (US competitor landscape, buyer switching evidence, cost to build US calibration capability, alternative use of the $4m) — is in `case-market-entry-halvorsen.md`. The biggest unresolved lever: nobody has costed what a US calibration/certification build-out would actually take, and that's the one investment that could plausibly close the gap.


## Files in work dir after run

- case-market-entry-halvorsen.md
- cme-02-input.md

## File written by the run: case-market-entry-halvorsen.md

# Market entry: Halvorsen Instruments, US lab instruments market, how should Halvorsen enter the US given it must deliver USD 10m revenue by 2030 within USD 4m capital?

**Answer:** Enter now via the distributor contract, but as a bounded beachhead in the 20% in-house-calibration segment of benchtop electrochemistry only — not as the vehicle for USD 10m by 2030. Resize the board's target to a bottom-up base case of roughly **USD 1–2m by 2030** (range USD 0.6–4m), or treat USD 10m as a post-2030 ambition contingent on a separate, uncosted investment in US calibration/certification.
**Confidence:** Medium. The chain of filters is logically sound and each step is sourced to something in the notes, but three of the four multipliers are single-source/unsourced (adviser's USD 9bn and 2.5%, product team's 20%, distributor's own 30%). Still, the gap between plausible outcomes and the USD 10m bar (roughly USD 6–9m) is too large for triangulation to close.

**The premise is wrong, and the arithmetic shows it in one line:** USD 9bn × 1% = USD 90m assumes Halvorsen can address the whole US lab instruments market; it cannot — it sells one sub-segment, with certification and channel constraints that cut the addressable pool to under USD 14m before any share is even won.

---

## Step 1: Sharpened question

"Should Halvorsen enter the US lab instruments market by 2030, and if so how, given it must deliver at least USD 10m revenue and stay within USD 4m capital?"

Treated as already agreed from the board ask and notes. Not re-asked: minimum revenue (USD 10m by 2030), capital cap (USD 4m). Still open (listed below): margin target, management time budget, exit trigger, what the alternative use of the USD 4m would return.

**Kill criterion set upfront:** if the bottom-up base case, built from the only entry mode that fits the USD 4m cap, falls materially short of USD 10m by 2030, the plan as proposed fails and the board must either resize the target, fund a different (costlier) mode, or not proceed.

## Step 2: Issue tree and hypotheses

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Attractive: size | Bottom-up SAM for Halvorsen's actual product line is at least USD 10m and growing | Bottom-up SAM below the minimum bar | **Killed for 2030** — see Step 3a |
| Attractive: barriers | EU certification is accepted, or US certification/calibration is achievable within budget and time | Regulated labs require local certified calibration Halvorsen cannot provide in time/budget | **Confirmed as a hard constraint** — cuts addressable demand to ~20% |
| Can win: need | Target buyers (in-house-calibrating labs) have the job and will switch to Halvorsen | No data on willingness to switch, only an internal volume estimate | **Open** — needs buyer interviews |
| How: mode | One mode reaches the revenue bar within budget and is exitable cheaply | Every mode needs more capital or time than allowed | **Killed for USD 10m** — distributor mode fits budget but tops out far below the bar; modes that could reach higher spend need capital beyond USD 4m |
| Pays | Base case reaches USD 10m by 2030 | Base case misses the minimum bar | **Killed** — base case ≈ USD 1–2m |
| Beats alternatives | USD 4m in the US returns more than the best alternative use | No alternative data given | **Open** — see Open questions |

## Step 3: Deciding analyses

### 3a. Addressable market — bottom-up, reconciled against the adviser's top-down figure

| Step | Figure | Source | Evidence grade |
|---|---|---|---|
| Top-down total | USD 9bn | Adviser slide, no source given | Weak — single source, unsourced |
| × benchtop electrochemistry share | 2.5% → **USD 225m** | Adviser's own appendix (same source as above — not independent) | Weak — same origin, needs an independent market report (e.g. a published US lab instruments study) to triangulate |
| × in-house-calibration demand | 20% → **USD 45m** (true SAM given Halvorsen's current certification) | Product team estimate | Weak — internal, unverified against actual US lab calibration-practice data |
| × distributor state coverage | 30% → **USD 13.5m** (SAM reachable through the only channel on offer) | Distributor's own estimate | Weak — motivated source; needs cross-check against independent state-level accredited-lab counts |

**Outside view on achievable share:** Germany — Halvorsen's best result anywhere — reached 30% of its addressable segment, but over **12 years**, not 4. Applying the mature 30% figure to a 2030 (roughly 4-year) horizon overstates what's achievable; comparable industrial distributor-led ramps typically reach a fraction of eventual mature share by year 4 (flagged as a benchmark assumption, not Halvorsen data — no comparable found for a 4-year point on Halvorsen's own curve).

- **Low case** (≈15% of mature share by year 4 → ~4.5% absolute): USD 13.5m × 4.5% ≈ **USD 0.6m**
- **Base case** (≈30% of mature share by year 4 → ~9% absolute): USD 13.5m × 9% ≈ **USD 1.2m**
- **High case** (full mature 30% share reached immediately — unrealistic, upper bound only): USD 13.5m × 30% = **USD 4.05m**

**Hypothesis 3a verdict: killed.** Even the implausible upper bound (USD 4m) misses the USD 10m bar; the realistic base case (USD 1–2m) misses it by roughly 5–8x.

### 3b. Market structure (US benchtop electrochemistry competitors)

No data in the notes on US incumbents, concentration, or likely reaction. **Not run — flagged as a missing analysis**, not assumed away (see Open questions).

### 3c. Customer need and switching

No buyer interview data. The 20% in-house-calibration figure is a volume estimate, not evidence that those labs would actually switch to Halvorsen. **Open.**

### 3e. Entry modes

| Mode | Investment | Time to revenue | Control | Exit cost | Fit vs. USD 4m cap |
|---|---|---|---|---|---|
| Distributor (offered) | Low — distributor margin, no major capex | Fast (quarters) | Low — distributor owns the customer relationship and pricing | Low — contract cancellation | **Fits.** Only reaches the USD 13.5m reachable pool above. |
| Own US sales/service office, no calibration | Medium–high (hiring, registration, travel, local service) | Slower (6–12 months to first revenue) | Higher | Medium (lease, severance) | Likely at or above the cap; doesn't unlock the calibration-gated 80% either |
| Own US calibration/certification build-out (unlocks the other 80% of demand) | High — accredited lab, ISO 17025-type accreditation, local calibration technicians; **not costed, needs specialist estimate** | Long (12–24+ months for accreditation) | High | High — accredited lab is a sunk, hard-to-unwind asset | **Does not fit** USD 4m or the 2030 timeline on current information; longest-term lever for reaching a materially higher number |
| Acquisition of a US-certified calibration/instruments partner | High — almost certainly above USD 4m | Medium (integration) | High | High | **Does not fit** current budget; a separate M&A-screening decision, not this one |

**Mode recommendation:** the distributor deal is the only mode that fits the stated budget and timeline. Entering through it is reasonable as a low-cost beachhead and proof point — but the board should not expect it to produce USD 10m by 2030.

### 3f/3g. Business case and stress test

Base case USD 1–2m, low case USD 0.6m, high case USD 4m by 2030 (built above from named channel capacity and an outside-view ramp, not "1% of a big market"). No incumbent-reaction case run — no US competitor data available (see 3b). Sensitivity: the answer is not sensitive to resolving the single-source uncertainty in any one filter (9bn, 2.5%, 20%, or 30%) individually — the gap to USD 10m is wider than any single input's plausible error band.

### 3h. Alternative use of capital

No data given on what else Halvorsen could do with USD 4m (e.g., further EU/adjacent-market penetration, product-line expansion). **Open — see below.**

## Step 4: Trap checks

- [x] Share built bottom-up from customers, channel capacity and win rates, not "1% of a big market" — done; this is exactly what overturns the adviser's figure.
- [ ] Customers, channels and price levels tested in the target market, not copied from home — **not done**. Germany's 30%/12-year result is used only as an outside-view ramp benchmark, explicitly flagged as unverified for the US; no US buyer or price testing exists yet.
- [ ] At least one aggressive incumbent reaction modeled — **not done**, no US competitor data (open question below).
- [x] Sunk costs play no role — none identified; the adviser's slide and the distributor's offer are both free options so far, not sunk spend.
- [x] Ramp compared with a comparable entry (Germany), with the range widened and the mismatch (12 years vs. 4) named explicitly.
- [ ] Exit criteria and exit cost written down before entry — **not done**, open question below.
- [ ] Entry compared with the best alternative use of the same capital — **not done**, no data given.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | US lab instruments market size | USD 9bn | Adviser slide, unsourced | A materially higher/lower independently-verified figure — unlikely to close a 5–8x gap alone |
| 2 | Benchtop electrochemistry share of that total | 2.5% | Adviser's own appendix (same source as #1) | Same caveat as #1 |
| 3 | Share of US demand from in-house-calibrating labs | 20% | Internal product-team estimate | If independent data shows this is materially higher (e.g. 40–50%), the reachable pool roughly doubles but still likely misses USD 10m alone |
| 4 | Distributor's state coverage | 30% of US lab activity | Distributor's own claim | If verified lower, the case gets worse, not better |
| 5 | Year-4 share as a fraction of Halvorsen's mature (12-year) share | 15–30% | Analyst judgment, no comparable entry found at a 4-year mark | A faster ramp is possible but would need evidence from a comparable electrochemistry-instrument US entry, not yet identified |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Who are the US incumbents in benchtop electrochemistry, and how concentrated is the segment? | High concentration or an aggressive incumbent response could cap share below even the base case | Competitor profiling / desk research | Could lower the case further; unlikely to raise it |
| Would in-house-calibrating US labs actually switch to Halvorsen, and why? | The 20% figure is a volume estimate, not switching evidence | Buyer interviews | Could move the base case up or down materially |
| What would it cost and how long would it take to build US calibration/certification capability? | This is the only lever that unlocks the other 80% of demand and could plausibly reach USD 10m, but is currently uncosted | Regulatory/accreditation specialist, Halvorsen ops | If cheap and fast enough to fit an expanded budget, changes the recommendation to "enter now, fund certification in parallel" |
| What would USD 4m otherwise earn if spent on an existing market or product line? | Required to know if US entry beats the alternative, per the engagement rule that entry must compete for capital like any other option | Halvorsen finance/strategy | Could make "do not enter now" the stronger answer even at the resized target |
| What exit trigger and exit cost apply if the beachhead underperforms? | Not yet defined; needed before committing the distributor contract | Halvorsen management/board | Clarifies downside before signing |
| Does the distributor relationship carry any exclusivity or minimum-commitment terms? | Could affect ability to later expand coverage or switch modes | Contract review, legal | Could change the "sequence" part of the entry plan |

## What would change the answer

1. If an independent market report confirms the USD 225m segment figure and/or shows the in-house-calibration share is materially above 20%, the reachable pool grows — worth checking, but even at double or triple current assumptions it likely still falls short of USD 10m by 2030 given the 12-year Germany ramp.
2. If US calibration/certification can be built within roughly USD 2–3m and 18 months (needs specialist costing), a parallel-track plan — distributor now, certification investment approved as a second tranche — could plausibly reach closer to USD 10m by 2031–32, just past the board's date.
3. If the board treats USD 10m by 2030 as a hard, non-negotiable floor with no flexibility on timing, the honest recommendation is **do not proceed on this plan**: no mode fits both the USD 4m cap and a path to that number by that date on the evidence available.

