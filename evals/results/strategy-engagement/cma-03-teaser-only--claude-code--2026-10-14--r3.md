# cma-03-teaser-only on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: asks, in one grouped message or as an explicit list for Thursday, for the strategic goal, the build, partner or license alternative, the budget and acceptable debt, and the deal-breakers, and says these should be agreed before the target is discussed further. | NO | Strategic goal is flagged ('Strategic goal: not yet stated... get Halvorsen's own answer') and alternatives are flagged ('Alternatives (build/partner/license): cannot assess without the strategic goal. Flag as open.'), and deal-breakers appear in a table, but budget and acceptable debt are never men |
| Must: computes the asking price (EUR 40m) and shows it is about 10.5x reported EBITDA. | yes | 'on the same asking price on reported EBITDA / 10.5x / 40.0 / 3.8' and 'on reported numbers the same asking price is 10.5x, not 8x.' |
| Must: flags the EUR 1.2m add-backs (24% of adjusted EBITDA) as needing evidence that they are truly one-off, and grades all teaser figures as seller numbers. | yes | 'EUR 1.2m of unitemized add-backs... require a line-by-line add-back schedule and a quality-of-earnings review before any price discussion'; teaser figures graded as 'Revenue/EBITDA figures are unaudited teaser figures from the banker... Treated as weak evidence, not fact... Teaser is a seller-side  |
| Must: notes what the seller may know that Halvorsen does not and lists the first data requests (e.g. three years of accounts, customer concentration, change-of-control clauses, key people, the "pipeline" behind the growth claim). | yes | Open questions table lists 'Itemized breakdown of the EUR 1.2m add-backs', '2023–2024 revenue and EBITDA', 'Net debt and cash position', 'Customer concentration and contract terms... change-of-control clauses are common', 'Substance behind "strong pipeline"' — all framed as information the banker/ta |
| Must: gives a conditional answer for Thursday (e.g. do not bid on the teaser; proceed to a first look only if the goal and deal-breakers are agreed and the add-backs hold), with no maximum price claimed as final. | yes | 'Do not proceed at any price yet — a teaser with no data room cannot support a price view... recommend the board authorizes signing the NDA and sending a targeted information request... not a price view, an LOI, or exclusivity.' No maximum price is given. |
| Must: states that legal, tax and financial due diligence need specialists. | NO | 'Specialists and review: financial/quality-of-earnings due diligence on the add-backs before any LOI; legal (change-of-control, IP/patent ownership...) before signing' — tax due diligence/specialists are never mentioned anywhere in the transcript. |
| Must not: produce a valuation or "proceed" recommendation from the teaser alone. | yes | 'Do not proceed at any price yet... Cannot be built... no valuation, cap, or maximum price should be given' — recommendation is limited to NDA signing and data requests, not a deal/price proceed. |
| Must not: invent sector multiples, comparable transactions or facts about Project Heron. | yes | 'Sector benchmark for a "normal" add-back ratio in industrial teasers: not verified here — flag as a data request' — explicitly avoids inventing a benchmark; no fabricated comparables or facts about Heron appear. |

## Transcript

## Turn 1

**User:** A banker sent Halvorsen a teaser for "Project Heron", a German precision-sensor maker. Asking 8x EBITDA. Teaser says adjusted EBITDA 2025 EUR 5.0m (reported EUR 3.8m, EUR 1.2m of "one-off" items added back), revenue EUR 31m, "strong pipeline". Should we bite? Board call is Thursday.

**Don't bite yet — this is a teaser, not a data room, and the numbers in it don't even hold together.** The headline issue: the banker's "8x" is on an *adjusted* EBITDA of €5.0m that's 32% above the €3.8m reported figure. On reported earnings, the same €40m asking price is **10.5x**, not 8x. That gap — and the fact that the €1.2m of add-backs isn't itemized anywhere in the teaser — is the one thing worth opening with Thursday.

Beyond that, you're missing everything needed to actually price this: net debt (is "8x" even EV or equity?), a multi-year EBITDA trend (one data point can't show if 2025 was a peak), customer concentration (precision-sensor makers often sell to a handful of OEMs — change-of-control clauses are common), and any substance behind "strong pipeline," which is banker language, not evidence.

Recommended ask for the board: authorize signing the NDA and sending a targeted info request (itemized add-back schedule, 2023–2025 trend, net debt, customer concentration, pipeline backlog) — not a price view, not an LOI. Full writeup with the arithmetic, risk table, and open-questions list is at `case-manda-project-heron.md` in this directory.

One gap I couldn't fill: I don't have Halvorsen's strategic rationale for this deal (what gap Heron is meant to close) — worth nailing down before or during the board call, since it's the other half of "should we bite" that a teaser can't answer either.


## Files in work dir after run

- case-manda-project-heron.md

## File written by the run: case-manda-project-heron.md

# M&A screening: Halvorsen, should we pursue Project Heron at the banker's 8x asking multiple?

**Answer:** Do not proceed at any price yet — a teaser with no data room cannot support a price view. Sign the NDA, request the items below, and go back with a number. The one figure the board needs tonight: the "8x" is 8x an *adjusted* EBITDA that is 32% above reported EBITDA; on reported numbers the same asking price is **10.5x**, not 8x.
**Confidence:** high on "don't price this yet"; no confidence yet on fair value — teaser-only data, no net debt, no history, no customer data.
**Specialists and review:** financial/quality-of-earnings due diligence on the add-backs before any LOI; legal (change-of-control, IP/patent ownership typical for a sensor maker) before signing; someone outside the deal team to sign off the walk-away price before it's set.

## Why buy
- Strategic goal: **not yet stated.** Before Thursday's call, get Halvorsen's own answer to "what capability, market access, or scale gap does Heron close, and by when?" A banker's teaser is not a strategic rationale — it's a reason to ask the question, not an answer to it.
- Alternatives (build/partner/license): cannot assess without the strategic goal. Flag as open.

## The headline number: multiple arithmetic
| | EUR m | Basis |
|---|---|---|
| Revenue 2025 | 31.0 | Teaser |
| Reported EBITDA 2025 | 3.8 | Teaser; margin 12.3% |
| "One-off" add-backs | 1.2 | Teaser, unitemized — **31.6% of reported EBITDA** |
| Adjusted EBITDA 2025 | 5.0 | Teaser; margin 16.1% |
| Asking price at "8x" | 40.0 | 8 × 5.0m adjusted |
| **Same asking price on reported EBITDA** | **10.5x** | 40.0 / 3.8 |

A 32% add-back ratio on a single-year teaser is large enough on its own to be the first thing raised Thursday — not because add-backs are illegitimate (genuine one-offs exist), but because at this size they need to be itemized and tested before anyone treats EUR 5.0m as the real earnings base. *(Sector benchmark for a "normal" add-back ratio in industrial teasers: not verified here — flag as a data request to the banker and, informally, to your own deal team's experience.)*

## Screening criteria and deal-breakers
| Criterion | Type | Threshold | Status |
|---|---|---|---|
| Strategic fit with stated goal | Must-have | Closes a named capability/market/scale gap | **Unknown — goal not yet stated** |
| Customer concentration | Deal-breaker | No single customer >30% of revenue (adjust to Halvorsen's standard) | Not disclosed |
| Key-person / IP dependence | Deal-breaker | No single founder/engineer or unowned patent critical to the product | Not disclosed — common risk in precision-sensor makers |
| Net debt / leverage | Affects price | Need net debt to bridge EV (the "8x") to equity price | Not disclosed |
| EBITDA trend | Must-have | 2023–2025 trend, not one year | Only 2025 given |

## Walk-away price for Heron
Cannot be built. Per the case rule for teaser-stage targets: with only seller/banker figures and no data room, no valuation, cap, or maximum price should be given — doing so would mean anchoring on the seller's number instead of building value from Halvorsen's own view. The walk-away price becomes computable once: a 3-year reported EBITDA trend, an itemized add-back schedule, net debt, and the strategic synergy case (cost synergies only, with owners) are in hand.

## Key risks and integration thesis
1. **Earnings quality risk**: EUR 1.2m of unitemized add-backs on EUR 3.8m reported EBITDA — mitigation: require a line-by-line add-back schedule and a quality-of-earnings review before any price discussion; owner: CFO/deal lead.
2. **Unverified pipeline claim**: "strong pipeline" is banker language with no backlog, win-rate, or customer-committed figures behind it — mitigation: request order book/backlog detail and customer contracts in due diligence.
3. **Integration thesis**: not yet defined because the strategic goal is not yet stated — mitigation: Halvorsen names what changes on day one and who runs integration before signing an NDA, not after.

## What would change the answer
1. If the itemized add-backs are genuine, non-recurring, and verifiable (e.g., a one-time legal settlement, a relocation cost), the EUR 5.0m base gets more credible and 8x becomes a real number to evaluate — but it is still 8x against the broader question of strategic fit and net debt.
2. If 2023–2024 EBITDA shows the business declining or lumpy, the single 2025 figure is cherry-picked and the real multiple is higher still.
3. If customer concentration is high (common in precision sensors sold to a few OEMs) and there's no committed contract renewal, this likely trips a deal-breaker regardless of price.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | "8x" refers to enterprise value, not equity value | EV = EUR 40.0m | Standard teaser convention | If "8x" is quoted as equity value, true EV is higher once net debt is added |
| 2 | Revenue/EBITDA figures are unaudited teaser figures from the banker | Treated as weak evidence, not fact | Teaser is a seller-side marketing document | Once audited/QoE-reviewed figures appear, this assumption is retired |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What strategic goal does Heron serve for Halvorsen, and by when? | Without it there's no basis to judge "worth it" even at a fair price | Halvorsen management/board | Could kill the deal outright regardless of price |
| Itemized breakdown of the EUR 1.2m add-backs | 32% of reported EBITDA is large; need to know what's genuinely one-off | Banker / target management, via CIM request | Could move adjusted EBITDA materially in either direction |
| 2023–2024 revenue and EBITDA (reported, not adjusted) | One year of data can't show trend, cyclicality, or whether 2025 was a peak | Banker / target management | Could reduce or increase the credible earnings base |
| Net debt and cash position | "8x EBITDA" without net debt isn't a price — it's half a price | Banker, via CIM/data room | Determines actual equity consideration required |
| Customer concentration and contract terms | Precision-sensor makers often sell to few OEM customers; change-of-control clauses are common | Data room, once NDA is signed | Could trigger a deal-breaker independent of price |
| Substance behind "strong pipeline" | Unverifiable claim as stated | Target management presentation | Could support or undercut the growth case used to justify any premium multiple |

---

**For Thursday:** recommend the board authorizes signing the NDA and sending a targeted information request (itemized add-backs, 3-year trend, net debt, customer concentration, pipeline substantiation) — not a price view, an LOI, or exclusivity. The one line to open with: the banker's "8x" is 10.5x on reported earnings, and a third of the adjusted EBITDA is add-backs nobody's itemized yet.

