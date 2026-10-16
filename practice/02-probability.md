# Set 02: Probability & Bayes

**Week 2** · 6 problems · target time 45 min · moves: M2, M16, M18

> Write a guess first. Solve on paper. Check in `notebooks/02_probability.ipynb`.

---

### 2.1 The AI-essay detector [3 pts]

A detector flags **95%** of AI-written essays. It also wrongly flags **4%** of human-written essays. In a class, **10%** of essays are AI-written.

**Output:**
(a) An essay is flagged. Report ⌊100 × P(AI-written)⌋.
(b) The teacher runs a *second, independent* detector with the same rates on that essay, and it flags it too. Report ⌊100 × P(AI-written)⌋ now.

---

### 2.2 The late robot [3 pts]

A delivery robot reaches the 3rd floor by lift (L) or by stairs (S).
- The lift works with probability 0.7. When it works, the robot takes L with probability 0.9 and S otherwise. When the lift is broken, the robot always takes S.
- P(late | L) = 0.1.
- P(late | S, lift working) = 0.3.
- P(late | S, lift broken) = 0.5, because the stairs get crowded.

**Output:** The robot was late. Report ⌊100 × P(lift was broken | late)⌋.

---

### 2.3 Naive Bayes by hand [3 pts]

> **Background (Bernoulli Naive Bayes):** Each email is described by which words it contains. For class $c$, $P(\text{email}\mid c) = \prod_w P(w \mid c)^{x_w}\,(1-P(w\mid c))^{1-x_w}$, where $x_w = 1$ if word $w$ is present. Then $P(c \mid \text{email}) \propto P(c)\,P(\text{email} \mid c)$.

Training data: 4 spam and 6 ham emails. Fraction of emails in each class that contain each word:

| Word | Spam | Ham |
|---|---|---|
| free | 3/4 | 1/6 |
| meeting | 1/4 | 4/6 |
| win | 2/4 | 1/6 |

A new email contains **free** and **win** but **not meeting**.

**Output:**
(a) Report ⌊100 × P(spam | email)⌋.
(b) Redo (a) with **Laplace smoothing**: $P(w\mid c) = \dfrac{\text{count}+1}{N_c+2}$.

---

### 2.4 Best of three [3 pts]

$P(R \text{ beats } S) = \dfrac{1}{1+10^{(S-R)/400}}$, and games are independent with no draws.

**Output:**
(a) Give P(a 1800-rated player beats a 1600-rated player) to 3 decimal places.
(b) They play best-of-3: first to 2 wins. Report ⌊100 × P(the 1800 player wins the series)⌋.
(c) In one sentence: why does a longer series help the stronger player?

---

### 2.5 Does the AI tutor help? [3 pts]

Pass rates for 200 students in two schools:

| School | Used tutor | Passed | Didn't use | Passed |
|---|---|---|---|---|
| X | 100 | 85 | 20 | 18 |
| Y | 20 | 5 | 60 | 32 |

**Output:** Which statement is supported by the data?
A. The tutor raises pass rates in both schools.
B. Overall, tutor users pass more often, but within each school non-users pass more often.
C. Overall, non-users pass more often.
D. Tutor use and passing are independent.
E. The data proves the tutor lowers pass rates.

---

### 2.6 Charging or working [3 pts]

Each hour a robot is either **Working (W)** or **Charging (C)**. If it is working, it keeps working with probability 0.8 and goes to charge with probability 0.2. If it is charging, it returns to work with probability 0.6 and keeps charging with probability 0.4.

**Output:**
(a) It is working now. Report ⌊100 × P(working two hours from now)⌋.
(b) Report ⌊100 × the long-run fraction of hours spent working⌋.
