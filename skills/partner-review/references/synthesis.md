# Synthesis

## Purpose

Turn a pile of findings into a few conclusions and one recommendation the decision maker can act on. Analysis says what is true; synthesis says what it means for this client and what to do. Most weak final documents fail here: they report findings in the order they were found and leave the thinking to the reader.

## Entry criteria

- The high-impact hypotheses have been tested ([Hypothesis-Driven Approach](hypothesis-driven-approach.md)).
- Findings exist with sources: analysis outputs, interview summaries, model results.

## Step by step

1. **List findings** as full sentences, one per line, each with its source. "Revenue fell" is not a finding; "Spare-part revenue fell 14% from 2022 to 2025 while the installed base grew 6% (ERP export)" is.
2. **Apply the [So-What Test](so-what-test.md) to each finding.** Ask "so what for the decision?" until the answer names an implication for the client. Findings with no implication move to the appendix.
3. **Group implications** into three to five themes. Each group must make one point, and the groups must not overlap ([MECE](mece.md)).
4. **Write one conclusion per group** as a full sentence that could serve as a slide title ([Action Titles](action-titles.md)).
5. **Derive the recommendation.** It must follow from the conclusions, answer the problem statement directly, and say who does what by when.
6. **Check the logic upward and downward** ([Pyramid Principle](pyramid-principle.md)). Upward: do the conclusions together prove the recommendation? Downward: is every conclusion supported by enough evidence? Fix gaps before writing slides.
7. **State what would change the answer.** Name the two or three facts that, if they turned out different, would flip the recommendation. This shows confidence and honesty at once.
8. **Write the one-paragraph answer** in plain language. If it does not fit in one paragraph, the synthesis is not done.

## Inputs needed

- Problem statement, final hypothesis list, all findings with sources.

## Output produced

- Synthesis pyramid: recommendation, three to five conclusions, supporting findings.
- One-paragraph answer.
- Sensitivity note: what would change the answer.

## Exit criteria

- The recommendation answers the problem statement question word for word.
- Every conclusion passes the so-what test and is supported by at least two independent pieces of evidence, or is flagged as weakly supported.
- The pyramid has no orphan findings in the main line.
- The one-paragraph answer exists and a non-expert understands it.

## Common mistakes

- **Chronological reporting.** "First we looked at X, then Y" describes the project, not the answer.
- **Summary instead of synthesis.** Restating findings shorter is not synthesis. Synthesis adds the implication.
- **Recommendation that does not follow.** Conclusions about the market, recommendation about the organisation.
- **Too many messages.** Twelve conclusions means none of them is important.
- **Hiding uncertainty.** Presenting a 55% confidence answer as certain. Partners and boards forgive stated uncertainty; they do not forgive surprises.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps findings: (1) 52% of the 60,000 installed pumps are older than eight years and not under contract (ERP). (2) Plant managers report downtime costs of EUR 4,000 to EUR 40,000 per failure (12 interviews). (3) Two of three lost customers left over repair response time (interviews). (4) Alder's list prices are 6% below the two main competitors for comparable pumps (price benchmark). (5) Polish market is 78% held by two local players (trade data). So-what chain for finding 1: "Large uncontracted base" → "Untapped service revenue" → "Service contracts at 40% take-up add about EUR 12.5m by 2030". Conclusions: A. Service contracts are the largest growth lever (findings 1-3). B. Prices can rise without losing volume (finding 4 plus interview evidence). C. Poland is not attractive before 2029 (finding 5). Recommendation: "Fund a service-contract offer with a 48-hour response guarantee and raise list prices 4% in 2027; revisit Poland in 2029." What would change it: take-up below 25%, or a competitor matching response times first.

## Output template

```markdown
# Synthesis: <question in one line>

**One-paragraph answer:**

**Recommendation:** <who does what by when>

| Conclusion (action title) | Supporting findings (source) | Evidence strength |
|---|---|---|
| A. | 1 (<source>), 2 (<source>) | strong / medium / weak |
| B. | | |
| C. | | |

**What would change the answer:**
1. If <fact> turns out <different>, then <consequence>.

**Findings moved to appendix (no so-what for this decision):**
-
```

## Related

- [Storyline and Ghost Deck](storyline.md), [Pyramid Principle](pyramid-principle.md), [So-What Test](so-what-test.md), [Unanswered So-What](unanswered-so-what.md), [Logic Gaps](logic-gaps.md), [Executive Summary](executive-summary.md)
