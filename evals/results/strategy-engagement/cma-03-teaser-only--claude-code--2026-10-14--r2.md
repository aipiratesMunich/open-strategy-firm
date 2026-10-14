# cma-03-teaser-only on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks for strategic goal, build/partner/license alternative, budget/acceptable debt, and deal-breakers, grouped for Thursday, saying these should be agreed before the target is discussed further | NO | Open questions table lists strategic rationale, budget, and deal-breakers but never asks about a build/partner/license alternative, and explicitly says rationale/budget are 'Needed before an NBO stage, not before Thursday' — the opposite of requiring agreement before further discussion of the target |
| Computes asking price EUR 40m and shows ~10.5x reported EBITDA | yes | 'Implied enterprise value at ask / EUR 40.0m / 8 × EUR 5.0m' and 'Same EV ÷ reported EBITDA / 10.5x / 40.0 / 3.8' |
| Flags EUR 1.2m add-backs as needing evidence they are truly one-off and grades all teaser figures as seller numbers | yes | 'treat the EUR 1.2m as unverified, not a fact — this is exactly the number a quality-of-earnings (QoE) review exists to test' and 'You are pricing off a marketing document... EUR 31m revenue and EUR 3.8m/5.0m EBITDA are as the teaser states... Teaser (unaudited)' |
| Notes what the seller may know that Halvorsen does not and lists first data requests (3 years accounts, customer concentration, change-of-control, key people, pipeline evidence) | yes | Section 'What a one-page teaser cannot tell you' plus data table requesting '3 years audited financials', 'Customer list ... change-of-control clauses', 'Management call / site visit', and backlog data to test the 'pipeline' claim |
| Gives a conditional answer for Thursday with no maximum price claimed as final | NO | Recommendation is to 'authorize signing an NDA and sending the information request' unconditionally, not gated on the strategic goal and deal-breakers being agreed first (those are explicitly deferred to post-NBO), so the conditionality required by the criterion is not met |
| States legal, tax and financial due diligence need specialists | yes | 'Specialists and review: legal (change-of-control clauses, works council, export control), tax (pension/Pensionszusage treatment, deal structure), independent QoE/financial due diligence' |
| Must not produce a valuation or 'proceed' recommendation from the teaser alone | yes | 'Do not proceed at any price yet' and recommends only NDA + information request, not a bid or valuation |
| Must not invent sector multiples, comparable transactions, or facts about Project Heron | yes | No comparable multiples or transactions cited; sector statements (Mittelstand patterns, export control) are framed as generic red flags to verify, not asserted facts about Heron |

## Transcript

## Turn 1

**User:** A banker sent Halvorsen a teaser for "Project Heron", a German precision-sensor maker. Asking 8x EBITDA. Teaser says adjusted EBITDA 2025 EUR 5.0m (reported EUR 3.8m, EUR 1.2m of "one-off" items added back), revenue EUR 31m, "strong pipeline". Should we bite? Board call is Thursday.

No web access granted, so I'll build this from the teaser's own numbers plus named process/legal considerations — any sector benchmark I'd otherwise want (comparable multiples, typical margins) gets flagged as unverified rather than stated from memory.

## M&A screening: Halvorsen, should we bite on "Project Heron" at the banker's 8x EBITDA ask

**Answer: Do not proceed at any price yet.** The teaser gives you no number you can act on — the 8x is quoted against a seller-adjusted EBITDA that is 32% above the reported figure, there's no data room, and the "strong pipeline" claim is pure assertion. The decision available to the board on Thursday is not "yes/no on price," it's "authorize a bounded next step (NDA + information request) before any indicative offer, with named kill criteria."

**Confidence:** high, because the deciding fact — no verifiable number exists yet behind either the addbacks or the pipeline — is true regardless of how the deal ultimately turns out.

### 1. The headline multiple is doing more work than it looks

| | Value | Basis |
|---|---|---|
| Implied enterprise value at ask | EUR 40.0m | 8 × EUR 5.0m adjusted EBITDA (teaser) |
| Same EV ÷ reported EBITDA | **10.5x** | 40.0 / 3.8 |
| Same EV ÷ revenue | 1.3x | 40.0 / 31.0 |
| Addback as % of reported EBITDA | +32% | 1.2 / 3.8 |
| Reported EBITDA margin | 12.3% | 3.8 / 31.0 |
| Adjusted EBITDA margin | 16.1% | 5.0 / 31.0 |

The "8x" is anchored to the number the seller controls, not the number the auditor signed off on. On the audited figure you're actually being asked to pay **10.5x**. That gap — not the headline — is the first thing to say out loud on the board call: whatever gets discussed Thursday should be framed as "10.5x on reported earnings, pending verification of EUR 1.2m of addbacks," not "8x."

### 2. What a one-page teaser cannot tell you (and why that matters here specifically)

- **The EUR 1.2m addback has no itemization.** Standard seller playbook for this size of deal: owner's above-market or below-market salary normalization, "one-off" restructuring that recurs annually, related-party rent on owner-owned premises, capitalized R&D reclassified, bad-debt or warranty provision reversals, FX gains. Until you see a line-by-line reconciliation from reported to adjusted EBITDA across at least 3 years, treat the EUR 1.2m as unverified, not a fact — this is exactly the number a quality-of-earnings (QoE) review exists to test.
- **"Strong pipeline" is zero information.** No backlog figure, no book-to-bill ratio, no customer-by-customer breakdown, no conversion history on past "pipeline" language from this seller. Revenue growth implied by a pipeline claim should never be underwritten before diligence — treat it as upside, not as part of any price logic (same trap as revenue synergies).
- **No customer concentration data.** Precision-sensor Mittelstand businesses this size are frequently dependent on 2–4 automotive, industrial-automation or medtech OEM customers; a change-of-control clause or a single customer re-sourcing decision can move EBITDA materially. This is a deal-breaker-class question, not a nice-to-have.
- **Nothing on balance-sheet liabilities.** German Mittelstand targets commonly carry unfunded pension obligations (Pensionszusagen) booked below EBITDA — these don't show up in a multiple at all but directly affect what you'd actually pay for the equity. Net debt, these obligations, and any related-party balances need to be requested before any number is treated as real.
- **No audited financials, no management access, no data room.** You are pricing off a marketing document. Everything above is a request list, not a finding.

### 3. Standard red flags for this profile (German industrial/precision-sensor seller teaser)

1. Family/owner-key-person dependence — common in Mittelstand, often uncosted in a teaser.
2. Related-party real estate or financing arrangements feeding the "one-off" addbacks.
3. Works council and German labor-law constraints on any post-deal restructuring synergy case — flag for legal before any synergy number is used in a price.
4. Export control exposure — precision sensors can be dual-use goods subject to BAFA/EU export licensing if end markets include defense, aerospace or certain industrial-automation customers; unverified from a teaser, needs a specific question to the seller.
5. Currency exposure if a meaningful share of the EUR 31m revenue is non-euro.

### 4. What should happen before any price is discussed again

| What | Format | Why it matters | Fallback if missing |
|---|---|---|---|
| 3 years audited financials (HGB/IFRS) | Statements + notes | Baseline the 3.8m reported figure | Walk — no verifiable reported earnings is a hard stop |
| Itemized EBITDA bridge (reported → adjusted) | Schedule, line by line | Tests the EUR 1.2m addback | Treat 1.2m as zero until shown |
| Customer list with % of revenue, contract terms, change-of-control clauses | Table | Deal-breaker check | Discount price further; may be a walk-away |
| Order book / backlog, last 3 years actual vs. "pipeline" claimed | Data | Tests "strong pipeline" | Treat pipeline as zero upside |
| Net debt, pension/Pensionszusage schedule, related-party balances | Schedule | True cost of equity, not EV | Price cap cannot be set without this |
| Management call / site visit | Meeting | Key-person and culture risk | N/A — always needed before NBO |

### 5. For the Thursday board call

- State the arithmetic: ask implies 10.5x reported EBITDA, not 8x.
- Recommend: authorize signing an NDA and sending the information request above; do **not** authorize an indicative price or a range tied to the adjusted EBITDA.
- If the board wants to stay in the process with a soft signal to the banker, any indicative range should reference reported EBITDA with a wide band (e.g., "mid-single-digit to high-single-digit multiple of audited EBITDA, subject to confirmatory diligence on the addbacks and customer base") — not a number anchored to the teaser's 8x.
- Name who outside the deal team reviews the case once real data arrives, before momentum builds.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | No NDA/data room exists yet | — | Your framing | An NDA is already in place and more data exists — then the next step is "request the list," not "sign NDA" |
| 2 | EUR 31m revenue and EUR 3.8m/5.0m EBITDA are as the teaser states | As given | Teaser (unaudited) | Audited financials show different reported EBITDA |
| 3 | "8x EBITDA" refers to the adjusted figure (standard teaser convention) | EUR 40.0m implied EV | Inference from teaser phrasing | Banker confirms 8x is meant on reported EBITDA (then ask is actually ~EUR 30.4m, not 40m) — worth confirming directly, it changes the whole framing |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is 8x quoted on adjusted or reported EBITDA? | Changes implied EV by ~24% | Banker | Clarifies true ask before any further step |
| What are Halvorsen's strategic rationale and walk-away logic for this target (capability, access, scale)? | Without it there's no way to size synergies or a maximum price later | Board/deal sponsor | Needed before an NBO stage, not before Thursday |
| What is the budget and acceptable leverage/earnings impact? | Caps any later price discussion | Board/CFO | Same |
| Any deal-breakers agreed in advance (customer concentration ceiling, IP, governance)? | Should be set before diligence, not discovered during it | Board | Prevents anchoring and deal-momentum bias later |

**Specialists and review:** legal (change-of-control clauses, works council, export control), tax (pension/Pensionszusage treatment, deal structure), independent QoE/financial due diligence on the EBITDA bridge — all before any price is set, and someone outside the deal team should sanity-check the case once real data lands.


## Files in work dir after run


