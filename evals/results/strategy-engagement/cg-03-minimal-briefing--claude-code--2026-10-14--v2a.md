# cg-03-minimal-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes the gap (EUR 9m, about 29%) and the required growth rate (about 9% a year from 2026 to 2029), and contrasts it with the flat history. | yes | 'roughly +€9m, +29% cumulative, ~8.9%/yr CAGR needed — against a trend that's currently running at ~0%' |
| Asks a short, grouped set of questions the user can answer, no more than about three rounds, and proceeds without waiting if the user has no more data. | yes | Lists B2B/B2C, product range, geography, reason for target, capital/margin constraints, and 'first things I'd ask for are: 3 years of revenue by customer/segment, market growth data... and why growth has been flat' — while still delivering the full hypothesis-driven analysis in the same turn rather  |
| Produces an issue tree that starts from the gap, with branches for momentum, core (market vs share, price, existing customers), adjacencies and portfolio, each with a hypothesis and a kill criterion. | yes | Ranked hypotheses table includes rows for momentum case, market-vs-share, existing customer wallet-share leak, price/mix, adjacency, and portfolio sum — each with a kill criterion. |
| Keeps inorganic moves out of scope or names them as ruled out by the board. | yes | 'the board has ruled out M&A, so the full gap must be organic' / 'with M&A off the table, 100% of it has to come from organic levers.' |
| States the analysis order (momentum case and market vs share split first). | yes | Priority column marks momentum case as 'Test first' and market-vs-share split as 'High' priority, immediately after. |
| Gives a provisional answer or the most likely shape of the answer, explicitly labelled as hypotheses, with confidence low and the reason. | yes | 'Day-one answer (hypothesis):' section states 'No single lever plausibly carries €9m... Base-case sum... probably closes 60–80% of the gap — closing all of it by 2029 without M&A is a stretch.' |
| Open-questions table in the skill's format (question, why it matters, who can answer, effect on the answer). | NO | Only a prose paragraph ('What I don't know yet that would change this a lot: whether the business is B2B or B2C...') is given — no table with question/why/who/effect columns appears anywhere in the transcript. |
| Does not invent textile market growth rates, competitor names, or benchmark figures as facts. | yes | All figures given (60–80%, 3–5%, €3–5m) are explicitly framed as hypotheses/estimates, not asserted market facts; no competitor names or market growth rates are stated. |
| Does not deliver a generic list of growth frameworks or ideas unconnected to the EUR 9m gap. | yes | All hypotheses (wallet-share recovery, price/mix, adjacency) are explicitly sized against and tied to closing the €9m/29% gap. |

## Transcript

## Turn 1

**User:** Pellworth Textiles. Revenue 31m in 2026, flat for years. Board wants 40m by 2029. No M&A. That's all I've got right now, what's your take?

Quick framing first: with revenue flat at ~€31m for years and a board target of €40m by 2029, that's roughly **+€9m, +29% cumulative, ~8.9%/yr CAGR** needed — against a trend that's currently running at ~0%. That's a real reacceleration, not a rounding error, and with M&A off the table, 100% of it has to come from organic levers.

**Day-one answer (hypothesis):** No single lever plausibly carries €9m in textiles. My working bet is a portfolio of three: (1) wallet-share recovery in the existing customer base — the cheapest growth, since "flat" often hides customers already buying adjacent products/services from competitors; (2) a disciplined price/mix move where list prices sit below delivered value; (3) one well-chosen adjacency (new category, channel, or export geography). Base-case sum of those probably closes 60–80% of the gap — closing all of it by 2029 without M&A is a stretch, and the board should see that honestly now rather than find out in 2029.

**Ranked hypotheses, with kill criteria:**

| # | Hypothesis | Kill criterion | Priority |
|---|---|---|---|
| 1 | Momentum case is genuinely flat/declining → gap is ~€9m (29%) by 2029 | Gap <€2m → it's a different problem (defend the core) | Test first |
| 2 | The served market is roughly flat, not shrinking — flatness is a share/mix problem, not a market problem | Market shrinking >3%/yr → reframe as core-defense | High |
| 3 | A meaningful slice of the installed customer base buys adjacent product/service lines elsewhere | Addressable leak <€3m → demote | High |
| 4 | List prices/mix sit below achievable value on part of the range | Prices already at ceiling vs. comps → kill | Medium |
| 5 | At least one adjacency (new category, channel, e.g. export/DTC) can add >€3m with a right to win | Segment too small or entrenched competitors → kill | Medium |
| 6 | Two or three levers close ≥70% of the gap in base case | Base case sums <50% → reopen the target with the board | Last |

**Ghost deck (SCQA):**
- **S:** Pellworth's revenue has sat near €31m for several years.
- **C:** The board wants €40m by 2029 — a 29% increase — and has ruled out M&A, so the full gap must be organic.
- **Q:** Which combination of organic levers can close this gap, and is the target realistic in three years?
- **A (hypothesis):** Wallet-share recovery + price/mix + one adjacency likely close most, not all, of the gap — the board needs a range, not a single promised number.

Candidate page titles (all hypotheses, unverified):
1. "Flat revenue has been masking share loss in a steady market, not a demand collapse."
2. "A chunk of the cheapest growth — €3–5m — is probably already walking out the door to competitors via the existing customer base."
3. "Part of the range is underpriced relative to value delivered; a low-risk price/mix move is worth 3–5%."
4. "One adjacency can add a real slice, but it needs sizing before anyone trusts the number."
5. "The kept levers likely close over half the gap but probably not all of it by 2029 — that remaining gap needs to go to the board now."

**What I don't know yet that would change this a lot:** whether the business is B2B or B2C, what's actually in the product range, geographic footprint, why the board picked €40m/2029 specifically (investor commitment? refinancing covenant? succession?), and the capital/margin constraints the plan has to respect. If you want to go further, the first things I'd ask for are: 3 years of revenue by customer/segment, market growth data for your category, and whatever's known about why growth has been flat — losing share vs. a genuinely flat market need opposite fixes.

Want me to run this as a proper quick case (adds sizing, assumptions table, open questions) or push further into a full engagement?


## Files in work dir after run


