# Set 04: Ranking, retrieval & convolution

**Week 4** · 6 problems · target time 45 min · moves: M1, M11, M12

> Check in `notebooks/04_ranking_signals.ipynb`.

---

### 4.1 TF-IDF ranking [3 pts]

> **Background:** $\text{tf}(t,d)$ = number of times term $t$ appears in document $d$. $\text{idf}(t) = \log_2(N/\text{df}(t))$, where $N$ is the number of documents and df is the number of documents containing $t$. Score$(d) = \sum_{t \in \text{query}} \text{tf}(t,d)\cdot \text{idf}(t)$.

| Doc | Text |
|---|---|
| D1 | robot arm robot arm |
| D2 | robot vision camera |
| D3 | arm motor motor |
| D4 | robot motor arm vision |

**Output:**
(a) Rank the documents for the query **"robot motor"**.
(b) A word that appears in *every* document gets what idf, and why is that sensible?

---

### 4.2 PageRank, one step at a time [3 pts]

> **Background:** $PR(p) = \frac{1-d}{N} + d\sum_{q \to p} \frac{PR(q)}{\text{out}(q)}$, with $d = 0.85$. Start with $PR = 1/N$ for every page and update all pages simultaneously.

Links: A→B, A→C, B→C, C→A, D→C ($N = 4$).

**Output:**
(a) Report ⌊1000 × PR(C)⌋ after **one** iteration.
(b) Which page has the highest PageRank at convergence? What is PR(D) at convergence, and why can't it ever change?

---

### 4.3 DCG and the best swap [3 pts]

> **Background:** $\text{DCG}@k = \sum_{i=1}^{k} \frac{\text{rel}_i}{\log_2(i+1)}$. nDCG = DCG ÷ DCG of the ideal (sorted) order.

A ranker returns relevances `[3, 2, 3, 0, 1]` in positions 1–5.

**Output:**
(a) Report ⌊100 × nDCG@5⌋.
(b) You may swap **one adjacent pair**. Which swap increases DCG the most?

---

### 4.4 Where to cut the list [3 pts]

A search returns 10 results. The relevant ones are at positions **1, 3, 4, 8**. There are **5** relevant documents in total.

**Output:** Which $k$ maximises F1@k = 2·P@k·R@k / (P@k + R@k)? Bonus: show that F1@k = 2·hits(k) / (k + R).

---

### 4.5 Convolution, done the exam's way [3 pts]

> **Background (as on Jan 18):** $y_i = \sum_{j=1}^{k} h_j\, x_{i+k-j}$. Equivalently: reverse the kernel, slide it, multiply and sum. No padding, stride 1, unless stated.

**Output:**
(a) $x = [3, 7, 4, 9]$, $h = [1, -1]$. Give $y$.
(b) $x = [5, 2, 6, 6, 1, 4]$, $h = [1, -2, 1]$. Give $y$, and how many entries are positive? What does a positive entry mean about the signal there?
(c) For (b), compute $S = \sum y_i$ **without** computing $y$, using only the first two and last two values of $x$.

---

### 4.6 Flip or not? [2 pts]

PyTorch's `Conv1d` and NumPy's `np.correlate` **do not** reverse the kernel. `np.convolve` **does**.

**Output:** For $x = [1, 2, 3, 4]$ and $h = [1, 0, -1]$, give the output of the exam's convolution and of a no-flip correlation. How are they related?
