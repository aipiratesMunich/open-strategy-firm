# cg-03-minimal-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (3/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes the gap (EUR 9m, about 29%) and the required growth rate (about 9% a year from 2026 to 2029), and contrasts it with the flat history. | NO | Assistant only says 'Three years, ~9% CAGR from a flat base, organic only' — gives the growth rate but never states the EUR 9m gap or the ~29% figure. |
| Asks a short, grouped set of questions the user can answer, no more than about three rounds, and proceeds without waiting if the user has no more data. | NO | Only two loosely related open questions are asked conversationally ('why flat' and 'what's actually been flat — unit volume, price realization, or mix') — not a grouped set covering revenue by product/customer/region, margin floor, capital, decision-maker/timing, or market vs. share loss. |
| Produces an issue tree that starts from the gap, with branches for momentum, core (market vs share, price, existing customers), adjacencies and portfolio, each with a hypothesis and a kill criterion. | NO | No issue tree is present anywhere in the transcript; the assistant merely offers to 'run this properly as a strategy engagement' rather than producing one. |
| Keeps inorganic moves out of scope or names them as ruled out by the board. | yes | "Three years, ~9% CAGR from a flat base, organic only" acknowledges the user's 'No M&A' constraint. |
| States the analysis order (momentum case and market vs share split first). | NO | No statement of analysis sequencing or prioritization appears in the transcript. |
| Gives a provisional answer or the most likely shape of the answer, explicitly labelled as hypotheses, with confidence low and the reason. | NO | No provisional answer or hypothesis-labelled day-one answer is given; the response ends with clarifying questions only. |
| Open-questions table in the skill's format (question, why it matters, who can answer, effect on the answer). | NO | No table of any kind appears in the transcript. |
| Must not invent textile market growth rates, competitor names, or benchmark figures as facts. | yes | No market growth rates, competitor names, or benchmark figures are asserted. |
| Must not deliver a generic list of growth frameworks or ideas unconnected to the EUR 9m gap. | yes | The response stays focused on diagnostic questions about Pellworth's own flat revenue rather than delivering a generic framework list. |

## Transcript

## Turn 1

**User:** Pellworth Textiles. Revenue 31m in 2026, flat for years. Board wants 40m by 2029. No M&A. That's all I've got right now, what's your take?

Three years, ~9% CAGR from a flat base, organic only — that's a real step-change, not a budget nudge, so the first question is *why* flat: is this a shrinking core market you're treading water in, or a healthy market where you've been losing share/pricing discipline? Those point to very different plays — the first needs a new growth vector (adjacent segment, channel, or product line), the second might be fixable with pricing and go-to-market alone, and conflating them is how boards end up funding the wrong initiative.

What's actually been flat — is it unit volume, price realization, or mix shifting while total stays put? That'll tell me which lever is worth pressure-testing first. If you want, I can run this properly as a strategy engagement (problem statement, growth hypotheses, evidence) rather than just riffing.


## Files in work dir after run


