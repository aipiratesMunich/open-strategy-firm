# pr-03: A good memo (false-alarm test)

## Prompt

> Partner review please. This memo goes to the Brightwell CEO tomorrow.

Input file: `pr-03-input.md`

## What this case tests

The memo is sound: it answers the question, the recommendation is specific, numbers tie, evidence is triangulated and uncertainty is stated. A good partner releases it, possibly with minor fixes. A weak reviewer invents problems to look rigorous.

## Pass criteria

- Must: verdict is **Release** or **Release with fixes**.
- Must: no Blocker findings.
- Must: every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo.
- Must: names what is good and must survive.
- Must not: demand a named framework, more length, or more slides.
- Must not: flag the stated uncertainty or the explicit assumptions as weaknesses.
- Must not: claim numbers do not tie (they do: 2.9 + 2.4 = 5.3; 5.3 / 62 = 8.5%; 80 - 62 - 5.3 = 12.7; 0.32 x 1.6 - 0.35 = 0.16 and so on, cumulative 0.93 after three years and 1.44 after four, so payback in year four; 1.1 + 0.9 = 2.0 < 12.7 / 4).
