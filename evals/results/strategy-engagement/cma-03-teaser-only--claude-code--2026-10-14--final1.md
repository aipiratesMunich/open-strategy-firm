# cma-03-teaser-only on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (5/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks for strategic goal, build/partner/license alternative, budget and acceptable debt, and deal-breakers, grouped for Thursday, to be agreed before further target discussion | NO | Only asks 'why is buying better than building or partnering?' and lists deal-breakers; no mention of budget, financing capacity, acceptable debt/leverage, or a license alternative anywhere in the transcript. |
| Computes asking price (EUR 40m) and shows ~10.5x reported EBITDA | yes | "Implied EV if 8x × adjusted / ~EUR 40m" ... "40m / 3.8m ≈ 10.5x reported EBITDA" |
| Flags EUR 1.2m add-backs as needing evidence of being truly one-off, and grades all teaser figures as seller numbers | yes | "EUR 1.2m of add-backs ... that's a lot of the 'price' riding on items you haven't seen itemized"; "Confidence: low, because every input is seller/banker-supplied and unverified" |
| Notes what the seller may know that Halvorsen does not and lists first data requests (accounts, customer concentration, change-of-control, key people, pipeline evidence) | yes | "Sellers' teasers almost always mean adjusted, which is the more favourable reading for the seller"; requests 3 years of accounts, customer concentration, 'legal on change-of-control and IP terms', owner/key-person role, and pipeline backlog/win-rate data |
| Gives a conditional answer for Thursday with no maximum price claimed as final | yes | "Proceed to IOI stage only under conditions — do not clear a price at the board call... No valuation, cap or maximum price can be set from a teaser alone." |
| States that legal, tax and financial due diligence need specialists | NO | Only "financial due diligence (QoE)... legal on change-of-control and IP terms" are mentioned; tax due diligence is never mentioned anywhere in the transcript. |
| Must not produce a valuation or 'proceed' recommendation from the teaser alone | yes | "No valuation, cap or maximum price can be set from a teaser alone"; recommendation is explicitly conditional, not an unconditional proceed. |
| Must not invent sector multiples, comparable transactions, or facts about Project Heron | NO | "the EV/Revenue implied (~1.3x) isn't obviously rich for precision sensors" asserts an unsupported sector-multiple judgment before disclaiming it was unverified. |

## Transcript

## Turn 1

**User:** A banker sent Halvorsen a teaser for "Project Heron", a German precision-sensor maker. Asking 8x EBITDA. Teaser says adjusted EBITDA 2025 EUR 5.0m (reported EUR 3.8m, EUR 1.2m of "one-off" items added back), revenue EUR 31m, "strong pipeline". Should we bite? Board call is Thursday.

**Bottom line for Thursday: don't price it, push back on it.**

You only have a teaser — no data room, no CIM, no management meeting. That's not enough to set a price, so the honest answer isn't "yes/no on 8x," it's "send the deal team back for three things before anyone discusses a number":

1. **The EBITDA bridge.** EUR 1.2m of add-backs on EUR 3.8m reported EBITDA is a 32% uplift — that's a lot of the "price" riding on items you haven't seen itemized. If 8x is quoted against the adjusted EUR 5.0m (standard teaser convention), implied EV is ~EUR 40m, which is really ~**10.5x on the reported number** until the add-backs are proven. Ask the banker which EBITDA the 8x is actually against, get the bridge line-by-line, and get 3 years of history, not one.
2. **Customer concentration and key-person risk.** Totally unknown at this stage, and both are standard deal-breakers in a EUR 31m German Mittelstand sensor business.
3. **What "strong pipeline" actually means.** It's sales copy until there's backlog/win-rate data behind it.

Separately: the EV/Revenue implied (~1.3x) isn't obviously rich for precision sensors, but I didn't verify that against current comparable deals (web search wasn't available this session) — flag that as still open before anyone calls the multiple cheap or expensive.

Also worth 30 seconds at the board call: nobody's stated *why* Halvorsen wants this target strategically. A fair price on a target that doesn't serve a named goal is still a no.

Full write-up with the issue tree, red-flag detail, and an open-questions table for the banker is at `case-manda-project-heron.md` in this directory.


## Files in work dir after run

- case-manda-project-heron.md

## File written by the run: case-manda-project-heron.md

# M&A screening: Halvorsen, should we bite on "Project Heron" at 8x EBITDA?

**Answer:** Proceed to IOI stage only under conditions — do not clear a price at the board call. Go back to the banker for the EBITDA bridge and three data points (one-off breakdown, customer concentration, pipeline backlog/conversion) before anyone commits to a number. No valuation, cap or maximum price can be set from a teaser alone.
**Confidence:** low, because every input is seller/banker-supplied and unverified (teaser stage, no data room, no management access yet).
**Specialists and review:** financial due diligence (QoE) on the EBITDA bridge before any binding offer; legal on change-of-control and IP terms once a CIM is available; someone outside the deal team to sign off the walk-away price before signing.

## Why buy

Not stated in the brief. Before Thursday, the board should be able to answer: what strategic goal does Heron serve (capability, customer access, geography, technology), and why is buying better than building or partnering? A "strong pipeline" teaser line is not a strategic rationale — it's sales copy. *Open question, see below.*

## The headline math

| Metric | Value | Source | Note |
|---|---|---|---|
| Revenue 2025 | EUR 31.0m | Teaser | ASSUMPTION: unaudited |
| Reported EBITDA 2025 | EUR 3.8m | Teaser | Reported margin 12.3% |
| Add-backs | EUR 1.2m | Teaser, "one-off" | 32% of reported EBITDA — large relative to base |
| Adjusted EBITDA 2025 | EUR 5.0m | Teaser | Adjusted margin 16.1% |
| Asking multiple | 8x EBITDA | Banker | Ambiguous which EBITDA it's applied to |
| Implied EV if 8x × adjusted | ~EUR 40m | Calculated | EV/Revenue ≈ 1.3x |
| Implied multiple if priced off reported instead | 40m / 3.8m ≈ **10.5x reported EBITDA** | Calculated | The number that matters until the add-backs are proven |

The EV/Revenue of ~1.3x is not obviously rich for a precision-sensor maker — the real exposure is entirely in whether that EUR 1.2m of add-backs survives diligence, not in the headline multiple. Confirm with the banker which EBITDA the 8x is quoted against; sellers' teasers almost always mean adjusted, which is the more favourable reading for the seller.

## Quality-of-earnings red flags (the thing to press on Thursday)

1. **Size of the adjustment.** EUR 1.2m of add-backs on EUR 3.8m reported EBITDA is a 32% uplift. That is large enough that the 8x "price" is materially a function of items nobody outside the seller has seen itemized yet.
2. **"One-off" is doing a lot of work.** Teasers routinely bundle recurring costs (management fees, family-business salary normalization, recurring restructuring, bad debt) into "one-off." Ask for the full bridge, item by item, with the year each item hit and whether it recurred in any of 2022–2024.
3. **No multi-year EBITDA shown.** One year of reported and adjusted figures is not enough to tell if EUR 1.2m is genuinely non-recurring or a pattern. Request at least three years of both reported and adjusted EBITDA.
4. **"Strong pipeline" is unverified sales language.** Revenue of EUR 31m with margin expansion claimed via pipeline growth needs backlog, win rates, and customer-by-customer detail — not a teaser adjective. Treat it as weak evidence until seen ([Weak Evidence](../.claude/skills/strategy-engagement/references/weak-evidence.md) grade: unverified).
5. **Customer concentration unknown.** Precision-sensor businesses this size often carry concentration risk (a handful of OEM/industrial customers). This is a standard deal-breaker check and is completely open at teaser stage.
6. **Owner/key-person dependence unknown.** Common in a EUR 31m German Mittelstand business; ask about management depth and any owner who exits at close.

## Screening criteria and deal-breakers (set these before the next call, not after)

| Criterion | Type | Threshold |
|---|---|---|
| Customer concentration | Deal-breaker | No single customer >30% of revenue (adjust to board's risk appetite) |
| Key-person dependence | Deal-breaker | Business must be sellable/runnable without the founder/owner post-close |
| EBITDA bridge quality | Deal-breaker | Add-backs must be itemized and independently plausible; unexplained add-backs are excluded from the price basis |
| Strategic fit | Must-have | Closes a named capability/market gap for Halvorsen — TBD, see open questions |
| IP / regulatory | Deal-breaker | No unresolved IP ownership or pending litigation (precision-sensor IP is often the actual asset) |

## What would change the answer

1. If the EBITDA bridge shows the EUR 1.2m is genuinely one-off (e.g., a single litigation settlement or a one-time facility move, clearly dated) and does not recur across prior years, the adjusted number gains credibility and 8x on EUR 5.0m becomes a reasonable starting point for negotiation.
2. If customer concentration exceeds the board's threshold or a top customer carries a change-of-control clause, this should kill the deal regardless of price.
3. If the strategic rationale can't be named in one sentence, the right answer is "no" independent of the financials — a reasonable price on a target that doesn't serve a stated goal is still a bad deal.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 8x is quoted against adjusted EBITDA | EV ≈ EUR 40m | Standard teaser convention | Banker confirms it's off reported EBITDA — then the ask is actually ~10.5x reported |
| 2 | EUR 31m revenue and EUR 3.8m reported EBITDA are unaudited teaser figures | As stated | Teaser only | Audited accounts show different reported figures |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What strategic goal does Heron serve, and why acquire vs. build/partner? | Not stated in the brief; a good price on the wrong target is still a no | Halvorsen board/management | Could kill the deal independent of financials |
| Full itemized EBITDA bridge for the EUR 1.2m, with 3 years of reported and adjusted history | Single biggest QoE risk in the teaser | Banker / seller (next CIM stage) | Could move the effective multiple from 8x to ~10.5x+ |
| Customer concentration (top 5 customers, % of revenue, contract terms) | Standard M&A deal-breaker; sensor OEM relationships are often concentrated | Banker / seller | Could be an outright deal-breaker |
| Owner/key-person role and post-close plan | Mittelstand succession risk | Banker / seller | Affects integration risk and price |
| Backlog/pipeline detail behind "strong pipeline" claim | Currently just sales language | Banker / seller | Could support or undercut the growth case |
| Is 8x EBITDA rich or cheap for precision-sensor deals in this size bracket right now? | Needed to judge if the ask is market or aggressive | Banker (ask for comparable transactions) / outside data | Not verified in this session — flag as needed before IOI |

## Recommendation for Thursday

Tell the board: this is a teaser, not a basis for a price decision. The headline 8x looks plausible on revenue multiple terms, but roughly a quarter of the "price-setting" EBITDA is unverified add-backs — that's the conversation to have with the banker before an IOI, not after. Authorize the deal team to request the EBITDA bridge, 3-year financials, and customer concentration data, and to get one sentence of strategic rationale on record, before any number is discussed with the seller.

