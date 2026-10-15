# pr-04-numbers-dont-foot on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| verdict is Return | yes | "Verdict: Return" |
| finds D1 and rates it Blocker | yes | Finding #1, Blocker: "Slide 5 says Leipzig saves EUR 1.1m/yr in transport. Slide 7's table lists the transport line as EUR 1.3m, and that table's own total (EUR 3.6m) doesn't even match its own slide's title (EUR 3.4m/yr)." |
| fix for D1 is an instruction, not a suggestion | yes | "Pick one reconciled transport-savings figure, fix the table arithmetic, make the slide 7 title match its own total, and re-run slides 8–9 off the corrected number." |
| Numbers that do not tie table lists transport saving or slide 7 total with both locations | yes | "Transport savings, EUR m/yr / Slide 5: 1.1 / Slide 7 table: 1.3" |
| finds at least one of D2, D3 | NO | No finding states that Kassel still runs overtime after Leipzig opens (D2) or that slide 7 nets Leipzig operating cost into the transport line causing a gross/net mismatch (D3); finding #7 only flags that pre-operational payroll cost is missing/unverifiable, which is a different issue than the gross |
| premortem has three reasons, at least one internal | yes | Premortem #3: "Construction costs run over the mid-2026 quotes (no contingency built in) or the early 38-person hiring ramp adds unbudgeted payroll before any revenue" — an internal execution/capacity risk, alongside two other reasons. |
| lists at least one thing that is good and should survive | yes | "Real alternatives were tested in a table (slide 4), not just asserted away." and "Capex is grounded in two independent contractor quotes plus a separate equipment quote, dated" |
| must not release deck while numbers don't tie | yes | Verdict given is "Return", not Release or Release with fixes. |
| must not invent benchmark figures without a source | yes | "Missing outside view" section notes absence of benchmarks rather than fabricating any figures. |

## Transcript

## Turn 1

**User:** CFO angle please: is this board deck ready to go out to the Harrow board on Friday? (Attached in the working directory: pr-04-input.md.)

No — hold it. From the CFO's chair, this deck has a numbers-don't-foot problem sitting right on the slide that carries the whole recommendation, plus the headline payback can't be reproduced from the deck's own inputs. That's a Return, not a Friday-ready deck. Full review below.

# Partner review: Harrow Cold Chain — Leipzig hub board deck (draft v3), gate 3

**Verdict: Return**
**In one line:** The operating-savings figure that drives the 3.1-year payback contradicts itself three times in the deck (EUR 1.1m / 1.3m / 3.4m / 3.6m), and even the more generous of those numbers can't reproduce a 3.1-year payback — the board would be asked to approve EUR 14.0m against a return nobody has actually tied out.

**Question the draft must answer:** Should the board approve EUR 14.0m capex to build a second distribution hub in Leipzig? (given)
**Answer the draft gives:** Yes — payback 3.1 years, NPV EUR 9.8m, frees Kassel from overtime.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | CFO | Slide 5 vs Slide 7 | Slide 5 says Leipzig saves **EUR 1.1m/yr** in transport. Slide 7's table lists the transport line as **EUR 1.3m**, and that table's own total (EUR 3.6m) doesn't even match its own slide's title (EUR 3.4m/yr). Three different numbers for the same savings line in two adjacent slides. | The board approves on whichever number nobody double-checked; actual savings could be 10-15% lower than the figure the payback/NPV is built on. | Pick one reconciled transport-savings figure, fix the table arithmetic, make the slide 7 title match its own total, and re-run slides 8–9 off the corrected number. |
| 2 | **Blocker** | CFO / Model | Slide 1 / Slide 8 | The claimed **3.1-year payback and EUR 9.8m NPV** can't be reproduced from the disclosed inputs. Even using the *higher* EUR 3.6m savings figure undiscounted, capex EUR 14.0m / EUR 3.6m ≈ 3.9 years, not 3.1 — and that's before discounting, which only lengthens payback. The underlying model (`harrow_leipzig_v3.xlsx`) isn't attached for anyone to check. | A sharp board member who runs this math during the meeting gets a different, worse answer in real time — the deck's credibility (and the whole case) unravels in the room. | Finance re-runs and shares the actual cash-flow schedule (capex by year, savings ramp, discounting) that produces 3.1 years / EUR 9.8m, reconciled to the slide 7 fix above, before this goes out. |
| 3 | Major | CFO | Slide 8 | No **IRR** is shown, and the 8% discount rate has no stated source — is it Harrow's WACC, a hurdle rate, or a round assumption? | Board can't compare this against its actual cost of capital or other capital asks; NPV/payback alone invite the question "compared to what?" | Add IRR, and one line sourcing the 8% ("Harrow WACC per 2026 treasury guidance" or similar). |
| 4 | Major | CFO / Model | Slide 6 | EUR 14.0m capex has **no contingency line** and rests on two contractor quotes and one equipment quote, all unsigned, from mid-2026. The downside case (slide 9) flexes volume only — never cost. | Normal build cost overruns between quote and signed contract aren't absorbed anywhere in the case; the "downside" shown isn't the realistic downside. | Add a contingency line (typically 5–10% at this stage) and a cost-overrun scenario alongside the volume downside. |
| 5 | Major | Logician | Slide 4 | The cheapest option (Halle 3PL, EUR 0.4m + rent) is ruled out solely because *that operator* lacks GDP certification for 2 of 5 large customers — not explored: can it be certified, or is there another certified 3PL near Halle. | Board approves 35x the capex of the next-best option without being shown the cheaper path was genuinely dead, not just unexamined. | Add one line: cost/timeline to certify Halle, or confirmation no certified alternative exists in the region. |
| 6 | Major | CFO / Premortem | Slide 9 | The downside trigger — "volume below 70% of plan, i.e. losing two of the five largest customers" — surfaces a customer-concentration risk that is never named or mitigated anywhere else in the deck. It's also unclear whether these are the *same* two customers flagged in slide 4 for GDP certification. | If it's the same two accounts, both the investment case and its own failure trigger rest on the same two customers — a concentration risk the board should see named, not buried in a sensitivity footnote. | Add a line clarifying whether these are the same accounts, and state what (contract terms, diversification plan) mitigates the risk. |
| 7 | Major | Model | Slide 7 / Slide 10 | Hiring 38 staff in Q4 2027 — roughly 9 months before operations start (Q3 2028) and over a year before savings begin (2029) — implies payroll cost not visible in the EUR 14.0m capex table or the opex netting note. | A real cash cost is missing from the case; the "net of Leipzig operating cost" line in slide 7 can't be checked without it. | Quantify pre-operational staffing cost and show where it sits (capex, opex, or a bridge year). |
| 8 | Minor | Outsider | Slide 7 | "Savings... from year two" (title) vs. "savings from 2029" (slide 8) — two different ways of describing the same ramp. | Minor ambiguity once the cash-flow timeline is reconciled under #2. | State the ramp once, consistently, in calendar years. |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Transport savings, EUR m/yr | Slide 5: 1.1 | Slide 7 table: 1.3 | 0.2 (≈18%) |
| Total operating savings, EUR m/yr | Slide 7 title: 3.4 | Slide 7 table total: 3.6 | 0.2 |
| Payback, years | Slide 1/8 claimed: 3.1 | Recomputed (undiscounted, best-case 3.6 savings figure): ≈3.9–4.1 | Not reproducible from disclosed inputs |

## Missing outside view
- Payback/NPV hurdle: no comparison to Harrow's actual capital hurdle rate or IRR threshold for projects of this size.
- Transport-saving model (EUR 1.62/pallet-km) and the 41% distance reduction: no benchmark against comparable network-expansion savings actually realized elsewhere in the business or sector.
- Capex of EUR 14.0m for this scale of cold-storage hub: no cost-per-pallet-position or cost-per-sqm comparison to a prior Harrow build or industry norm, to sense-check the quotes aren't a first-time premium.

## Premortem
1. The unreconciled savings figure (finding #1) turns out to be the lower end (EUR 1.1m transport), and real payback lands at 5+ years instead of 3.1 — but the board approved on the higher, unverified number.
2. One of the two concentration-risk customers (findings #5/#6) is lost or renegotiates, volume drops below the 70% trigger, and NPV goes negative — a risk the deck names in one sentence and never manages.
3. Construction costs run over the mid-2026 quotes (no contingency built in) or the early 38-person hiring ramp adds unbudgeted payroll before any revenue — either way the already-thin payback math erodes further.

## What is good and must survive
- Action titles throughout state a finding, not a label — rare and worth keeping as-is.
- Slide 2/3 numbers (utilisation trend, 62% eastern growth) are sourced to primary company systems with dates, and the 62% figure ties exactly to the underlying pallet counts (73,000/118,000).
- Real alternatives were tested in a table (slide 4), not just asserted away.
- A genuine downside scenario is shown with a stated flip condition (slide 9) — keep this discipline, just fix what it's missing (cost overrun, not just volume).
- Capex is grounded in two independent contractor quotes plus a separate equipment quote, dated — good triangulation on that line.

## What "fixed" looks like
"The board approves EUR 14.0m capex for a second hub in Leipzig to relieve Kassel, now at 96% capacity with EUR 2.3m of annual overtime. Reconciled operating savings of EUR [X]m/year (transport + overtime) give a payback of [Y] years and an NPV of EUR [Z]m against Harrow's [W]% hurdle rate (IRR [V]%); the case still pays back if volume runs 15% below plan. Two of Harrow's five largest eastern customers drive both the GDP-certification requirement that ruled out the cheaper Halle option and the downside trigger that would flip this recommendation — [stated mitigation]."

**Bottom line for Friday:** fixable in days, not weeks — it's a reconciliation and a few missing lines, not a re-pitch. But send Finance back to tie the savings number and reproduce the payback/NPV before this leaves the building.


## Files in work dir after run

- pr-04-input.md
