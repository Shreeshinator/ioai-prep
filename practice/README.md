# Practice sets

Original problems in the exam's style. Every answer has been checked numerically.

| Set | Week | Topic | Notebook |
|---|---|---|---|
| [01](01-metrics.md) | 1 | Evaluation metrics | `notebooks/01_metrics.ipynb` |
| [02](02-probability.md) | 2 | Probability & Bayes | `notebooks/02_probability.ipynb` |
| [03](03-algorithms-by-hand.md) | 3 | Algorithms by hand | `notebooks/03_algorithms.ipynb` |
| [04](04-ranking-retrieval.md) | 4 | Ranking, retrieval & convolution | `notebooks/04_ranking_signals.ipynb` |
| [05](05-math-optimization.md) | 5 | Optimisation, recurrences, graphs | `notebooks/05_math_optimization.ipynb` |
| [06](06-puzzles-logic.md) | 6 | Puzzles, logic, LLM sense | `notebooks/06_puzzles_logic.ipynb` |

## How to work a problem

1. **Guess first.** Before computing, write a guess (a number or an option) in the margin. Comparing guesses to answers over the weeks is how you *measure* your intuition getting better.
2. **Paper, not code.** Aim for the target time shown in each set's header. The exam has no computer.
3. **Check without spoilers.** Use `prep.check("1.2a", your_answer)` in the matching notebook. It says "correct" or "not yet", never the answer.
4. **Stuck? Climb the hint ladder** in `solutions/`, one rung at a time. Struggle for 10–15 min before Hint 1, and about 5 min between hints.
5. **Log it.** Write every miss in `log/ERROR_LOG.md`: what happened, which category, and what you should have noticed.
6. **Make a variant.** Change one number, predict what happens to the answer, then check. Writing your own problems builds intuition faster than solving more of ours.

## Adding problems

Follow `AUTHORING.md`: problem in `0X-*.md`, hint ladder in `solutions/0X-*.md`, a numeric check, and a hashed answer via `python notebooks/prep.py add <id> <answer>`.
