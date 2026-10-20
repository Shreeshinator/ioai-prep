# Connections: the same idea in different clothes

A **connection** means two different-looking problems are solved using the same underlying move.

A single insight only helps on the problem where you learned it. The real skill is noticing that a new problem is an *old idea in disguise*. Each theme below shows up in several places. When you meet a theme for the second time, come here, add the new place, and write one sentence on *why* it's the same idea.

| Theme | Where it appears | The shared idea |
|---|---|---|
| **Mean vs median** | 1.4 (RMSE vs MAE) · 5.1 (charger) · 3.2 (k-means centroid) · Jan 18 Godown | Squared loss → mean; absolute loss → median; worst-case loss → midrange. The median ignores outliers. |
| **Conditioning on the true class** | 1.1 (prevalence) · 1.2 (AUC) · 2.1–2.3 (Bayes) · Jan 18 B1 Q4–Q5 | TPR/FPR = P(prediction \| truth) and don't depend on the class mix. Precision = P(truth \| prediction) does. Bayes converts one into the other. |
| **Only the order matters** | 1.2 (AUC) · 4.4 (P@k) · 3.1 (k-NN uses nearest, not exact distances) · Jan 18 B1 Q4 | Any monotone transform leaves these unchanged. |
| **Fixed points and iteration** | 2.6 (Markov chain) · 4.2 (PageRank) · 5.4 (recurrence) · 3.2 (k-means repeats until nothing changes) · Jan 18 V-67 | Repeat an update until it stops changing. At the fixed point, inflow = outflow. |
| **Differences and telescoping** | 4.5 (kernels) · 6.6 (bit changes) · 5.4 (differences of a sequence) · Jan 18 B3 | [1, −1] is a difference. Summing differences leaves only the ends. |
| **Equal marginal gains** | 5.2 (budget) · Jan 18 Catalyst · 2.6 (balance of flows) | At the best split, moving one unit from one use to the other doesn't help. |
| **Invariants give bounds** | 6.1 (grid colouring) · Jan 18 Pikachu · 1.1 (ROC unchanged) · 4.1 (idf = 0 for words in every doc) | Find what *can't* change, and the answer is boxed in before you compute. |
| **s = Xw (linear algebra)** | Jan 18 B4 · 3.5 (PCA scatter matrix) · 5.7 (solving for parameters) · 4.2 (PageRank as a matrix) | A table of numbers times a list of weights. Solving for weights means solving equations. |
| **Kill with a counterexample** | 6.3 · 6.4 (Wason) · Jan 18 Smart Search · Jan 18 B3 kernels | Proving something is always true is hard; one failing example is enough to rule an option out. |

## Synthesis questions (one per Sunday teach-back)

1. Why do ROC invariance and Bayes' rule come from the same fact? (Weeks 1–2)
2. k-means moves each centroid to the *mean* of its points. If it used the *median* instead, what loss would it be minimising? (Weeks 1, 3, 5)
3. PageRank, a Markov chain and the V-67 outbreak are all "apply the same update every step". What's different about the long-run behaviour of each? (Weeks 2, 4, 5)
4. Why does the kernel [1, −2, 1] detect *acceleration* in B3 and *dips* in 4.5? Are those the same thing? (Week 4)
5. Pikachu (colouring) and 1.1 (ROC unchanged under prevalence) both use something that *can't change*. What is the invariant in each? (Weeks 1, 6)
