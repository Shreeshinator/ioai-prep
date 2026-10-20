# Moves: names for ideas you'll discover

A **move** is a reusable solving action: when you see a cue in a new question, you use the same action again.

> **Don't memorise this page.** Each move is something you should *find yourself* while solving the linked problems. Come here **after** you've met a move, to put a name on it. Then write it in **your own words** under "Moves I own" in `log/ERROR_LOG.md`. A move you only read about won't fire in the exam; one you discovered will.

Each entry gives: **Cue** (what in a question should make you think of it) · **Idea** · **Why it's true** · **Where you meet it**.

---

### M1. Read the definition, not your memory
- **Cue:** any "Background" box, or any definition printed in the question.
- **Idea:** the paper's definition wins, even when it differs from what you know. Underline every convention before you read the questions.
- **Why:** the examiners deliberately pick unusual conventions. On Jan 18:
  - the confusion matrix had **rows = predicted**
  - "convolution" **flipped** the kernel (PyTorch doesn't)
  - the classifier threshold was **strict** (> 0), and one row scored exactly 0
  - ties were broken by ID
  - answers were ⌊100x⌋, not rounded
- **Where:** 1.5, 4.5, 4.6 · Jan 18 B1, B3, B4.

### M2. Natural frequencies
- **Cue:** "given that", false alarm rates, priors, tests, sensors.
- **Idea:** imagine 1,000 cases. Fill a table of counts. Keep the rows consistent with what you observed, then divide.
- **Why:** Bayes' rule is exactly "zoom into the rows where the evidence is true". The table *is* the formula.
- **Where:** 1.1, 2.1–2.3 · Jan 18 Pit-Stop.

### M3. Fill the whole table
- **Cue:** partial facts about a confusion matrix (sensitivities, specificities, a few off-diagonal cells, class sizes).
- **Idea:** count the unknown cells and the facts you have. Fill cells in order, so that each new fact leaves exactly one unknown. Use the facts you didn't need as **free checks**.
- **Where:** 1.5 · Jan 18 B1 (all seven parts reuse one table).

### M4. ROC invariances
- **Cue:** "how does the ROC curve / AUC change if…"
- **Idea:** ROC and AUC depend only on the **order** of scores *within each true class*. So they don't change under monotone increasing transforms or when the class mix (prevalence) changes. Precision *does* change with prevalence.
- **Why:** TPR divides by "truly positive" and FPR by "truly negative". Neither denominator mixes the classes.
- **Where:** 1.1, 1.2 · Jan 18 B1 Q4, Q5.

### M5. Rates → counts
- **Cue:** capacity limits, "at most K per day", budgets.
- **Idea:** count = rate × size of the group the rate refers to. Flagged = TPR × (#positives) + FPR × (#negatives).
- **Where:** 1.3 · Jan 18 B1 Q3.

### M6. What does the argmin pick?
- **Cue:** "place X to minimise total…", or MAE vs RMSE.
- **Idea:**

  | Minimise | Answer |
  |---|---|
  | Σ\|x − aᵢ\| | **median** (any point in the middle interval) |
  | Σ(x − aᵢ)² | **mean** |
  | max\|x − aᵢ\| | **midpoint of the extremes** |
  | KL-type divergences | often **mean** |

  L1 in 2-D splits into each coordinate separately.
- **Why:** nudge x a little and count how many terms get better vs worse (median), or find the bottom of the parabola (mean).
- **Where:** 1.4, 5.1 · Jan 18 Godown.

### M7. Equal marginal gains (check whether the constraint binds)
- **Cue:** "allocate a shared resource between two uses".
- **Idea:**
  1. Find each use's unconstrained best. If together they fit in the budget, you're done.
  2. If not, the optimum spends the whole budget, and the **extra gain per unit** is equal in both uses.
- **Why:** if one use gained more per unit, moving a unit to it would raise the total.
- **Where:** 5.2 · Jan 18 Catalyst.

### M8. Parity / colouring
- **Cue:** "maximum number of cells / moves / pads", grids, alternating steps.
- **Idea:** colour the board. If every move changes colour, the path alternates colours, which caps how many cells of each colour you can visit. That gives an upper bound before any searching.
- **Where:** 6.1 · Jan 18 Pikachu.

### M9. Tabulate recurrences
- **Cue:** "each day…", "at the start of day t".
- **Idea:** write the update rule once in symbols, then one row per day in a table. For a one-variable linear rule x → a·x + b, shift by the fixed point x* = b/(1 − a) to get a geometric sequence.
- **Where:** 5.4 · Jan 18 V-67.

### M10. Kill options with counterexamples
- **Cue:** "which function / kernel / design satisfies these rules?"
- **Idea:** make a grid of rules × options. For each option, find **one** input that breaks one rule. Good killer inputs: swapped arguments (symmetry), huge values (range), the "if and only if" case, and which side gets the bigger weight.
- **Where:** 6.3 · Jan 18 Smart Search, B3.

### M11. Kernels telescope
- **Cue:** sums of convolution outputs; "constant signals → 0".
- **Idea:**

  | Kernel | Acts like |
  |---|---|
  | [1, −1] | first difference (velocity) |
  | [1, −2, 1] | second difference (acceleration / curvature) |
  | [−1, 2, −1] | spike detector |

  Kernels with Σh = 0 send constant signals to 0. The total S = Σy collapses to a few end values of the signal.
- **Where:** 4.5, 6.6 · Jan 18 B3.

### M12. Ranking-metric mechanics
- **Cue:** precision@k, recall@k, DCG.
- **Idea:**
  - P@k and R@k only count hits in the top k.
  - DCG weights each relevance by 1/log₂(position + 1), which is 1, 0.63, 0.5, 0.43, …
  - Swapping two neighbours changes DCG by Δrelevance × Δdiscount.
  - F1@k = 2·hits/(k + R).
- **Where:** 4.3, 4.4 · Jan 18 B2.

### M13. Read parameters off a graph
- **Cue:** a formula with unknown parameters, plus a plot with labelled points.
- **Idea:** match each parameter to one visible feature of the graph:

  | Graph feature | Gives you |
  |---|---|
  | distance between repeats | period |
  | change between two points at the *same phase* | trend |
  | size of a jump | step |
  | difference between a high and a low point | amplitude |

  Solve two or three small equations, then check against a point you didn't use.
- **Where:** 5.7 · Jan 18 Crude Curve.

### M14. LLM reality check
- **Cue:** "a small offline model is used to…"
- **Idea:** LLMs read **tokens**, not letters, so counting characters is unreliable. Without retrieval they can't know facts they weren't trained on, and they'll invent an answer instead of saying so. Pattern tasks (tone, topic, language) are fine.
- **Where:** 6.7 · Jan 18 Faulty Oracle.

### M15. Linear-classifier mechanics
- **Cue:** s = Xw + b, pruning, bias.
- **Idea:**
  - A row of X with a single 1 reveals one weight directly.
  - Pruning feature j only changes rows where xⱼ ≠ 0.
  - A bias shifts every score equally, so find the window of b values that fixes the most rows.
- **Where:** Jan 18 B4.

### M16. Elo and series
- **Cue:** ratings; "wins at least 2 of 3".
- **Idea:** P = 1/(1 + 10^(Δ/400)), where Δ is the opponent's rating minus yours.

  | Your lead (rating points) | 100 | 200 | 400 |
  |---|---|---|---|
  | P(you win) | 0.64 | 0.76 | 0.91 |

  For series, enumerate the win/loss sequences. Longer series amplify the favourite's edge.
- **Where:** 2.4 · Jan 18 Blind Board.

### M17. Align and decode
- **Cue:** an unknown language, glyphs or codes with translations.
- **Idea:** line up sentences that share a word to isolate it. Form a hypothesis about word order and markers, then test it on **every** sentence.
- **Where:** 6.5 · Jan 18 Imperial Glyphs.

### M18. Confounders
- **Cue:** "does X cause Y?" from observational data; group-level vs overall rates.
- **Idea:** a trend in the totals can reverse inside every group (Simpson's paradox). Correlation in observational data doesn't prove causation.
- **Where:** 2.5.
