# Partner Review Checklist

## What it catches

Everything that would embarrass the team in front of the client: a question that was never answered, conclusions that do not follow, numbers that do not tie, evidence that would not survive one sharp question, slides that bury the message. The partner's job is not to improve the draft line by line. It is to decide whether it can leave the room, and if not, to say exactly why.

## When to apply

- **Gate 1, after framing:** problem statement only. Is this the right question?
- **Gate 2, after structuring:** issue tree, hypotheses, ghost deck, workplan. Will this plan answer the question?
- **Gate 3, before release:** any document, deck, memo or model that leaves the team. Can the client act on this, and will it survive their sharpest person?

Apply the full list at gate 3. At gates 1 and 2, apply sections A and B only.

## Checks

Run the review in five passes, each from one reviewer perspective. Each pass reads the whole draft. If your agent can run sub-tasks in parallel, run the five passes independently and in parallel so they do not influence each other; otherwise run them in order and do not revise earlier findings while doing later passes.

**A. The Decision Maker (question and answer)**
1. Does the first page answer the problem statement question directly, in one sentence?
2. Is the recommendation specific: who does what, by when, with what resources?
3. Would the decision maker know what to approve after reading only the executive summary?
4. Does every main section change or support the decision? (See unanswered so what.)

**B. The Logician (structure)**
5. Do the action titles, read alone in order, tell the full story?
6. Do the supporting points together prove the point above them, with nothing missing and nothing overlapping? (See [Logic Gaps](logic-gaps.md).)
7. Does the recommendation follow from the conclusions, or does it jump?
8. Are alternatives the client will think of addressed and ruled out with reasons?

**C. The Evidence Auditor (proof)**
9. Does every number have a source, a date and a unit?
10. Are the key claims supported by at least two independent kinds of evidence? (See [Weak Evidence](weak-evidence.md).)
11. Are assumptions flagged as assumptions, not presented as facts?
12. Has anyone looked for evidence against the answer, and is it shown?

**D. The Skeptical CFO (numbers and model)**
13. Do the numbers tie across pages, executive summary and model?
14. Is the base case realistic compared with what similar companies or projects actually achieved (outside view)?
15. Does the answer survive the downside case? Is it stated what would flip it?
16. Does the model pass [Model Red Flags](model-red-flags.md)?

**E. The Outsider (clarity)**
17. Could a smart person outside the industry follow the story without a glossary?
18. Does each slide pass slide quality red flags?
19. Is the length right: main line short, detail in the appendix?

**Closing: premortem.** Imagine the client followed the recommendation and it failed badly two years later. Write the three most likely reasons. If any of them is not addressed in the draft, raise it as a finding.

**Decision-quality check on the team** (for gate 3 on high-stakes recommendations): Is there a sign the team fell in love with the day-one answer, anchored on the client's own numbers, or ignored a dissenting interview? Note it if so.

## Severity

Severity follows the consequence for the decision, not the check number:

- **Blocker:** the draft, as written, would mislead the decision maker or cannot support the decision. Typical cases: the question is not answered, the recommendation is not actionable, a key number is wrong or does not tie, the answer collapses in a plausible downside that the draft hides, the conclusion does not follow.
- **Major:** the decision can be taken, but a sharp board member would expose a real weakness: a key claim with one kind of evidence, a base case above what comparables achieved, a missing alternative, an unaddressed premortem risk.
- **Minor:** improves the document without changing the decision: sourcing details, labels, wording, a sample description.

Calibration before the verdict:

1. Merge findings that share one root cause into one finding.
2. For each Blocker ask: "Would a demanding but fair partner stop the meeting for this?" If not, downgrade it.
3. For each Major ask: "Would the answer or the board's confidence in it change if this were fixed?" If not, downgrade it to Minor.
4. A request for more analysis than the decision needs is not a finding. Asking for payback on a small, reversible pilot is usually Minor; on a large, irreversible investment it is Major.

Verdict rules: any open Blocker means **Return**. Majors alone mean **Return** only if together they change the recommendation or the decision maker's confidence in it; say which ones and why. Otherwise **Release with fixes** (Majors listed) or **Release**. A draft that answers the question with tied numbers, triangulated key claims and stated uncertainty should normally come back as Release with fixes.

## False alarms

- A recommendation with stated uncertainty is not weak. Hidden uncertainty is.
- Short is not shallow. A three-page memo that answers the question beats a forty-page deck.
- Using the client's own data is fine if it is labelled and sense-checked; it is only a problem if it is the sole support for a claim the client disputes.
- An assumption is acceptable when it is flagged, reasoned and its impact is tested in the sensitivity.
- Do not demand frameworks. A finding is not weaker because no named framework produced it.

## Worked example

*Fictional example. Company, figures and people are invented.*

Draft executive summary for Alder Pumps: "Our analysis of the market shows significant potential in services. Customers value reliability. We recommend exploring service opportunities and considering international expansion." Review:

- Blocker (check 1): Does not answer the question "Which two growth moves should the board fund?" No moves, no amounts.
- Blocker (check 2): "Exploring" and "considering" are not actions. Name the offer, the budget, the owner, the date.
- Major (check 10): "Customers value reliability" rests on interviews only; add the installed-base and lost-customer data.
- Major (check 8): International expansion appears without the Poland market-share finding that killed it.
- Premortem: "Take-up stays below 20% because sales has no incentive to sell contracts" is not addressed.

Verdict: **Return**. Rewrite the summary around "Fund a EUR 6m service offer with 48-hour response and a 4% price increase; no Poland before 2029."

## Output template

```markdown
# Partner review: <document>, <date>, gate <1/2/3>

**Verdict:** Return / Release with fixes / Release

**One-line reason:**

## Findings
| # | Severity | Perspective | Check | Where (page/section) | Problem | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Decision Maker | 1 | p.1 | | |

## Premortem
1.
2.
3.

## What is good and must survive the rewrite
-
```

## Related

- [Logic Gaps](logic-gaps.md), [Weak Evidence](weak-evidence.md), unanswered so what, slide quality red flags, [Model Red Flags](model-red-flags.md), [Engagement Lifecycle](engagement-lifecycle.md)
