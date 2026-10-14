# Evals

Each skill has at least three cases in `evals/<skill>/`. A case file holds:

- **Prompt:** exactly what the user types.
- **Input files:** anything the prompt refers to, in the same folder.
- **Pass criteria:** observable checks. A run passes when every "must" holds and no "must not" occurs.
- **Planted defects** (review skills only): the errors deliberately built into the input, so recall can be scored.

Runs are recorded in `evals/results/<skill>/<case>--<agent>--<date>.md` with the agent, model, full output and a pass/fail line per criterion.

All companies, people and figures in eval inputs are fictional.
