# Set 04 solutions: Ranking, retrieval & convolution

> Make a real attempt first (10–15 min per problem). Then open **one** hint, try again, and only then open the next. If a word or symbol in a problem is new to you, open Hint 1 straight away: notation is not something to struggle with. You can check a final answer without spoilers in `notebooks/04_ranking_signals.ipynb`.

---

### 4.1 TF-IDF ranking

<details><summary>Hint 1: understand the question</summary>

The score adds up one contribution per *query* word, and the query has only two words: "robot" and "motor". So "arm", "vision" and "camera" don't matter at all. For each of the two query words, which two numbers does the formula need from the table?
</details>

<details><summary>Hint 2: the key idea</summary>

Each query word gets a weight, its idf, which depends on how many documents contain it: the fewer documents, the bigger the weight. Work out the two weights first. Then each document's score is

(times "robot" appears) × idf(robot) + (times "motor" appears) × idf(motor).
</details>

<details><summary>Hint 3: set it up</summary>

- df counts **documents**, not occurrences. "robot" is in D1, D2 and D4, so df(robot) = 3, even though D1 says it twice.
- With N = 4: idf(robot) = log₂(4/3) and idf(motor) = log₂(4/2).
- Make a table with one row per document and columns: count of "robot", count of "motor", score.
</details>

<details><summary>Answer</summary>

(a) **D3 > D4 > D1 > D2** (b) idf = **0**. A word in every document can't tell documents apart, so it shouldn't affect the ranking.
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: what log₂ means.** log₂(x) is the power you raise 2 to in order to get x. So log₂ 2 = 1 (because 2¹ = 2), log₂ 4 = 2, log₂ 8 = 3, and log₂ 1 = 0 (because 2⁰ = 1). Two facts you'll use:
- log₂(a/b) = log₂ a − log₂ b, because dividing powers of 2 subtracts the exponents (2⁵ ÷ 2² = 2³).
- log₂ 3 ≈ 1.585 (check: 2^1.585 ≈ 3). It sits between log₂ 2 = 1 and log₂ 4 = 2, as it should.

**Step 2: the pieces of the score.** Use exactly the formula in the background box, not a version you remember from elsewhere (move **M1: read the definition, not your memory**). Here tf is a raw count and the log is base 2.
- **tf(t, d)**, the *term frequency*, is how many times word t appears in document d. Example: tf(robot, D1) = 2, because D1 is "robot arm robot arm".
- **df(t)**, the *document frequency*, is how many documents contain t at least once. Example: df(robot) = 3 (D1, D2, D4).
- **idf(t)** = log₂(N/df(t)), the *inverse document frequency*. It is big for rare words and small for common ones. With N = 4, a word in 1 document gets log₂ 4 = 2, and a word in 2 documents gets log₂ 2 = 1.

So a document scores high when it uses the query words often (tf) **and** those words are rare (idf).

**Step 3: idf of the two query words** (N = 4).
- robot is in D1, D2, D4, so df = 3 and idf = log₂(4/3) = log₂ 4 − log₂ 3 ≈ 2 − 1.585 = **0.415**.
- motor is in D3, D4, so df = 2 and idf = log₂(4/2) = log₂ 2 = **1**.

**Step 4: score each document.**

| Doc | tf(robot) | tf(motor) | Score = tf(robot) × 0.415 + tf(motor) × 1 |
|---|---|---|---|
| D1 | 2 | 0 | 0.830 |
| D2 | 1 | 0 | 0.415 |
| D3 | 0 | 2 | **2.000** |
| D4 | 1 | 1 | 1.415 |

Ranking: **D3 > D4 > D1 > D2**.

Stop and notice: D3 wins even though it never says "robot". "motor" is rarer (2 documents instead of 3), so each "motor" is worth more than twice as much as each "robot".

**Step 5: (b) a word in every document.** Then df = N, so idf = log₂(N/N) = log₂ 1 = **0**. Its contribution, tf × 0, is zero however often it appears. That is sensible: a word like "the" appears everywhere, so knowing a document contains it tells you nothing about whether that document matches better than another.

**What to remember:** TF-IDF score = (how often a query word appears) × (how rare it is across documents). Rare words dominate the ranking, and a word in every document has idf 0.

**Common trap:** counting *occurrences* instead of *documents* for df. "robot" appears 4 times in total, which would give idf(robot) = log₂(4/4) = 0 and a different ranking.
</details>

---

### 4.2 PageRank, one step at a time

<details><summary>Hint 1: understand the question</summary>

The sum in the formula runs over pages q that link **to** p. Which pages link to C, and how many outgoing links does each of them have?
</details>

<details><summary>Hint 2: the key idea</summary>

"Update all pages simultaneously" means every new value is computed from the **old** values only (all 0.25 at the start). Think of building a new array from the old one, not updating in place.

For (b), ask: who links to D? What does that leave in D's formula?
</details>

<details><summary>Hint 3: set it up</summary>

- Teleport share: (1 − 0.85)/4 = 0.0375.
- C gets links from A (A has 2 out-links), B (1 out-link) and D (1 out-link).
- For (b): call the final values A, B, C, D. Write one equation per page with the same values on both sides, and use the fact that the four values add up to 1.
</details>

<details><summary>Answer</summary>

(a) **568** (b) **C** (≈0.394, with A close behind at ≈0.373); PR(D) = **0.0375**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: what PageRank measures.** Picture a *random surfer*. At each tick they are on some page.
- With probability 0.85 they click one of that page's outgoing links, chosen at random.
- With probability 0.15 they get bored and *teleport* to any of the N pages, chosen at random.

PR(p) is the long-run fraction of time the surfer spends on page p. The 0.85, the chance of following a link, is called the **damping** factor d.

Now read the formula with this picture:
- (1 − d)/N is the chance of landing on p by teleporting. Here 0.15/4 = **0.0375**.
- d × PR(q)/out(q) is the chance that the surfer was on q, clicked a link, and picked the one to p. Here out(q) is the number of outgoing links from q. Example: if q has PR 0.4 and 2 out-links, it sends 0.85 × 0.4/2 = 0.17 to each of its two targets.

**Step 2: list the incoming links.** The problem lists links by sender. The formula needs them by receiver, so flip the list around:

| Page | Linked from | Out-links of each sender |
|---|---|---|
| A | C | C: 1 |
| B | A | A: 2 |
| C | A, B, D | A: 2, B: 1, D: 1 |
| D | nobody | none |

**Step 3: (a) one iteration, using only the old values (0.25 each).**

PR(C) = 0.0375 + 0.85 × (0.25/2 + 0.25/1 + 0.25/1) = 0.0375 + 0.85 × 0.625 = 0.0375 + 0.53125 = 0.56875.

⌊1000 × 0.56875⌋ = ⌊568.75⌋ = **568**.

Check by computing the others too:
- A = 0.0375 + 0.85 × 0.25 = 0.25
- B = 0.0375 + 0.85 × 0.25/2 = 0.14375
- D = 0.0375 (nothing links to it)

Total = 0.25 + 0.14375 + 0.56875 + 0.0375 = 1. The total stays at 1 because every page has at least one out-link, so no rank leaks away.

**Step 4: (b) PR(D).** Nobody links to D, so the sum in its formula is empty, and every update gives PR(D) = (1 − d)/N = **0.0375**. It drops from 0.25 to 0.0375 at the first update and can never change after that, because nothing in its formula depends on the other pages. In surfer terms, the only way to arrive at D is by teleporting.

**Step 5: (b) which page wins at convergence?** "Convergence" means the values have stopped changing, so the same numbers appear on both sides of each equation. With D = 0.0375:
- A = 0.0375 + 0.85·C (C's only link goes to A)
- B = 0.0375 + 0.85·A/2 = 0.0375 + 0.425·A
- A + B + C + D = 1, so A + B + C = 0.9625

You can rank them before solving anything:
- B < A, because B gets only half of A's rank (times 0.85) plus the same teleport share.
- A < C exactly when 0.0375 + 0.85C < C, i.e. 0.0375 < 0.15C, i.e. C > 0.25.
- Could C be 0.25 or less? Then A ≤ 0.0375 + 0.85 × 0.25 = 0.25 and B ≤ 0.0375 + 0.425 × 0.25 = 0.14375, so A + B + C ≤ 0.64375. But they must add up to 0.9625. That's a contradiction, so C > 0.25, and **C is the highest**.

To get the numbers, substitute A into B, then both into the sum:
- B = 0.0375 + 0.425 × (0.0375 + 0.85C) = 0.0534375 + 0.36125C
- A + B + C = (0.0375 + 0.85C) + (0.0534375 + 0.36125C) + C = 0.0909375 + 2.21125C = 0.9625
- C = 0.8715625 / 2.21125 ≈ **0.394**, then A = 0.0375 + 0.85 × 0.394 ≈ **0.373** and B ≈ 0.196.

A is close behind C because C sends *all* of its rank to A.

**What to remember:** PageRank is the time share of a random surfer. Incoming links bring rank, split by the sender's number of out-links. A page with no incoming links sits at the teleport floor (1 − d)/N forever.

**Common trap:** updating in place, i.e. using the new A and B while computing C in the same round. That gives PR(C) = 0.478, so 478 instead of 568. A second trap is guessing the winner from early iterations. After two iterations A is ahead (≈0.521 against C ≈0.298); the values swing back and forth before they settle.
</details>

---

### 4.3 DCG and the best swap

<details><summary>Hint 1: understand the question</summary>

nDCG needs two lists: the ranker's order [3, 2, 3, 0, 1], and the *ideal* order, which is the same relevances sorted from highest to lowest. What is the ideal order?
</details>

<details><summary>Hint 2: the key idea</summary>

The discount 1/log₂(i+1) depends only on the position i, not on which document sits there. Compute the five discounts once and reuse them for both lists.

For (b): a swap only touches two positions, so only two terms of the sum change.
</details>

<details><summary>Hint 3: set it up</summary>

For a swap of positions i and i+1, write the two affected terms before the swap and after it. Subtract and factor the result. When is it positive, and when is it big?
</details>

<details><summary>Answer</summary>

(a) **97** (b) swap **positions 2 and 3**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: what DCG measures.** Each result has a relevance score (here 3 = great, 0 = useless). People read from the top, so a relevant result at position 1 is worth more than the same result at position 5. DCG (*discounted cumulative gain*) adds up the relevances, each multiplied by a **discount** 1/log₂(i+1) that shrinks with the position i.

**nDCG** (*normalised* DCG) divides by the DCG of the best possible order of the same results. A perfect ranking scores exactly 1, so rankings of different queries can be compared. Tiny example: relevances [1, 2] have DCG = 1 + 2(0.631) = 2.262; the ideal [2, 1] has DCG = 2 + 0.631 = 2.631; nDCG = 2.262/2.631 = 0.86.

**Step 2: the five discounts.** (log₂ was defined in 4.1. For position 5, log₂ 6 = log₂ 2 + log₂ 3, because 6 = 2 × 3 and multiplying powers of 2 adds the exponents.)

| Position i | log₂(i+1) | Discount 1/log₂(i+1) |
|---|---|---|
| 1 | log₂ 2 = 1 | 1 |
| 2 | log₂ 3 ≈ 1.585 | 0.6309 |
| 3 | log₂ 4 = 2 | 0.5 |
| 4 | log₂ 5 ≈ 2.322 | 0.4307 |
| 5 | log₂ 6 ≈ 2.585 | 0.3869 |

**Step 3: DCG of the ranker's list [3, 2, 3, 0, 1].**

DCG = 3(1) + 2(0.6309) + 3(0.5) + 0(0.4307) + 1(0.3869) = 3 + 1.2618 + 1.5 + 0 + 0.3869 ≈ 6.149.

**Step 4: DCG of the ideal list.** Sort the relevances: [3, 3, 2, 1, 0].

Ideal DCG = 3(1) + 3(0.6309) + 2(0.5) + 1(0.4307) + 0 = 3 + 1.8927 + 1 + 0.4307 ≈ 6.323.

**Step 5: (a)** nDCG = 6.149/6.323 ≈ 0.972, and ⌊100 × 0.972⌋ = **97**.

**Step 6: (b) what one adjacent swap does.** This is move **M12: ranking-metric mechanics**. Write relᵢ for the relevance at position i and discᵢ for its discount. Only positions i and i+1 change.
- Before: relᵢ·discᵢ + relᵢ₊₁·discᵢ₊₁
- After: relᵢ₊₁·discᵢ + relᵢ·discᵢ₊₁
- After − before = relᵢ₊₁(discᵢ − discᵢ₊₁) − relᵢ(discᵢ − discᵢ₊₁) = **(relᵢ₊₁ − relᵢ) × (discᵢ − discᵢ₊₁)**

The second bracket is always positive, because discounts shrink down the list. So a swap helps exactly when the lower item is more relevant, and it helps more when the relevance gap is bigger and when the discount gap is bigger. Discount gaps are biggest near the top.

| Swap | Relevances | Relevance gap | Discount gap | Change in DCG |
|---|---|---|---|---|
| 1↔2 | 3, 2 | −1 | 1 − 0.6309 = 0.3691 | −0.369 |
| 2↔3 | 2, 3 | +1 | 0.6309 − 0.5 = 0.1309 | **+0.131** |
| 3↔4 | 3, 0 | −3 | 0.5 − 0.4307 = 0.0693 | −0.208 |
| 4↔5 | 0, 1 | +1 | 0.4307 − 0.3869 = 0.0438 | +0.044 |

The best swap is **positions 2 and 3**. A swap doesn't change the ideal list (it's the same set of relevances), so the best swap for DCG is also the best for nDCG.

**What to remember:** DCG = sum of relevance × position discount. An adjacent swap changes DCG by (relevance gap) × (discount gap), so the most valuable fix is an out-of-order pair near the top.

**Common trap:** treating both "out of order by 1" swaps (2↔3 and 4↔5) as equally good. The relevance gaps match, but the discount gap near the top is about three times bigger. A second trap is using log₂(i) instead of log₂(i+1): position 1 would then divide by log₂ 1 = 0, which tells you that you've misread the definition.
</details>

---

### 4.4 Where to cut the list

<details><summary>Hint 1: understand the question</summary>

Cutting at k means you keep only the top k results. How many of those k are relevant? Call that count hits(k). Precision and recall both start from hits(k), but each divides by something different. What does each one divide by?
</details>

<details><summary>Hint 2: the key idea</summary>

Prove the bonus identity first, then use it. Once you have F1@k = 2·hits(k)/(k + R), ask what happens to the top and the bottom of that fraction when k goes up by 1, (i) when the next result is relevant and (ii) when it isn't.
</details>

<details><summary>Hint 3: set it up</summary>

Write h for hits(k). Substitute P@k = h/k and R@k = h/R into 2·P·R/(P + R). Put the two fractions in the denominator over the common denominator kR before you divide.
</details>

<details><summary>Answer</summary>

**k = 4** (F1 = 2/3 ≈ 0.667)
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the definitions.** Cutting at k means you keep the top k results.
- **hits(k)** = the number of relevant results among the top k.
- **Precision at k**: P@k = hits(k)/k. Of what you kept, what fraction is relevant?
- **Recall at k**: R@k = hits(k)/R, where R = 5 is the total number of relevant documents. Of all relevant documents, what fraction did you keep?
- **F1** = 2·P·R/(P + R), called the *harmonic mean* of P and R. It is high only if *both* are high. Example: P = 1 and R = 0.2 give F1 = 0.4/1.2 = 0.333, far below their ordinary average of 0.6.

Tiny example, k = 3: the top 3 are positions 1, 2, 3, and the relevant ones among them are 1 and 3, so hits(3) = 2. Then P@3 = 2/3 and R@3 = 2/5.

(One of the 5 relevant documents never appears in the 10 results, so recall can reach at most 4/5.)

**Step 2: the identity, one step at a time.** Write h for hits(k).
- Numerator: 2 × (h/k) × (h/R) = 2h²/(kR).
- Denominator: h/k + h/R. Over the common denominator kR this is hR/(kR) + hk/(kR) = h(R + k)/(kR).
- Divide. Dividing by a fraction means multiplying by its flip: [2h²/(kR)] × [kR/(h(k + R))]. The kR cancels, one h cancels, and you are left with

F1@k = **2h/(k + R)**.

(If h = 0, then P and R are both 0 and F1 is taken to be 0. The formula also gives 0.)

Check at k = 3: 2 × 2/(3 + 5) = 0.5. Directly: 2(2/3)(2/5) ÷ (2/3 + 2/5) = (8/15) ÷ (16/15) = 0.5. They match.

**Step 3: what the identity tells you.** This is move **M12: ranking-metric mechanics**. Each time k goes up by 1:
- the bottom, k + R, always goes up by 1;
- the top, 2h, goes up by 2 only if the new result is relevant.

So after a miss, F1 always falls (same top, bigger bottom). The best k therefore can't be a miss. It must be a hit position: 1, 3, 4 or 8. Check just those four:

| k | hits | F1 = 2h/(k + 5) |
|---|---|---|
| 1 | 1 | 2/6 = 0.333 |
| 3 | 2 | 4/8 = 0.5 |
| 4 | 3 | 6/9 = **0.667** |
| 8 | 4 | 8/13 = 0.615 |

Best: **k = 4**.

The full table, as a check:

| k | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| hits | 1 | 1 | 2 | 3 | 3 | 3 | 3 | 4 | 4 | 4 |
| F1 | 0.333 | 0.286 | 0.5 | **0.667** | 0.6 | 0.545 | 0.5 | 0.615 | 0.571 | 0.533 |

Stop and notice: the hit at position 8 does raise F1 (from 0.5 at k = 7 to 0.615), but four slots were spent to get it, so it can't climb back to 0.667.

**What to remember:** F1@k = 2·hits(k)/(k + R). Every miss lowers it, so the best cut is always right after a hit, and you only need to compare those positions.

**Common trap:** dividing recall by the list length (10) instead of the number of relevant documents (5), or picking k = 8 because it has the most hits. More hits raises recall, but F1 also pays for every slot you keep.
</details>

---

### 4.5 Convolution, done the exam's way

<details><summary>Hint 1: understand the question</summary>

Write the definition out in full for the smallest case, k = 2 and i = 1: y₁ = h₁x₂ + h₂x₁. Which kernel entry multiplies the *later* x? And how many outputs fit if the kernel can't hang off either end?
</details>

<details><summary>Hint 2: the key idea</summary>

- (b): the kernel [1, −2, 1] is a "difference of differences". Can you rewrite each output as (one neighbouring difference) − (the previous one)?
- (c): a chain like (b − a) + (c − b) + (d − c) collapses to d − a. Can you write S as a chain like that?
</details>

<details><summary>Hint 3: set it up</summary>

For (c), let dᵢ = xᵢ₊₁ − xᵢ be the step from one value to the next. Show that each output is yᵢ = dᵢ₊₁ − dᵢ. Then write y₁ + y₂ + y₃ + y₄ in a column and see what cancels.
</details>

<details><summary>Answer</summary>

(a) **[4, −3, 5]** (b) **[7, −4, −5, 8]**, **2** positive. A positive entry means a local dip: the middle value sits below the average of its two neighbours. (c) **6**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: convolution vs correlation, on a tiny example.** Both slide a short list of weights (the *kernel* h) along the signal x, multiply matching entries, and add. The only difference is which way round the kernel faces. Take x = [1, 2, 4] and h = [10, 1]:
- **Correlation** (no flip) lays h down as written. Windows (1, 2) and (2, 4) give 10·1 + 1·2 = 12 and 10·2 + 1·4 = 24, so [12, 24].
- **Convolution** (flip) reverses h to [1, 10] first: 1·1 + 10·2 = 21 and 1·2 + 10·4 = 42, so [21, 42].

The big weight 10 lands on the *left* item of each window in correlation and on the *right* item in convolution.

**Step 2: read the exam's definition** (move **M1: read the definition, not your memory**). $y_i = \sum_{j=1}^{k} h_j\, x_{i+k-j}$. For k = 2 this is $y_i = h_1 x_{i+1} + h_2 x_i$, so h₁ multiplies the *later* x. This is the flipping kind: convolution. With no padding and stride 1, a window of length k fits n − k + 1 times, so y has n − k + 1 entries.

**Step 3: (a)** n = 4 and k = 2, so there are 3 outputs. With h = [1, −1]: $y_i = 1\cdot x_{i+1} + (-1)\cdot x_i = x_{i+1} - x_i$. This is the **first difference**: how much x changes from one entry to the next.
- y₁ = 7 − 3 = 4
- y₂ = 4 − 7 = −3
- y₃ = 9 − 4 = 5

So y = **[4, −3, 5]**. (Without the flip you'd get [−4, 3, −5], every sign wrong.)

**Step 4: (b)** n = 6 and k = 3, so there are 4 outputs. $y_i = h_1 x_{i+2} + h_2 x_{i+1} + h_3 x_i = x_{i+2} - 2x_{i+1} + x_i$. The kernel [1, −2, 1] reads the same backwards, so the flip makes no difference here.

| i | Window (xᵢ, xᵢ₊₁, xᵢ₊₂) | yᵢ |
|---|---|---|
| 1 | (5, 2, 6) | 5 − 4 + 6 = 7 |
| 2 | (2, 6, 6) | 2 − 12 + 6 = −4 |
| 3 | (6, 6, 1) | 6 − 12 + 1 = −5 |
| 4 | (6, 1, 4) | 6 − 2 + 4 = 8 |

So y = **[7, −4, −5, 8]**, with **2** positive entries.

Check: the first differences of x are [−3, 4, 0, −5, 3]. Taking differences of *those* gives [7, −4, −5, 8], the same. So [1, −2, 1] computes the **second difference**: the change in the change.

**Step 5: what a positive entry means.** Rearrange: $y_i = (x_i + x_{i+2}) - 2x_{i+1}$ = 2 × [(average of the two neighbours) − (middle value)]. A positive y means the middle value sits *below* the average of its neighbours: a local **dip**, where the curve bends upward like a valley. Window (5, 2, 6): 2 is well below 5.5, so y = 7. A negative y means a bump, where the curve bends downward.

**Step 6: (c) the sum without computing y.** First, the way anyone could do it: write S = y₁ + y₂ + y₃ + y₄ and count the total weight each x gets.

| | x₁ | x₂ | x₃ | x₄ | x₅ | x₆ |
|---|---|---|---|---|---|---|
| y₁ | +1 | −2 | +1 | | | |
| y₂ | | +1 | −2 | +1 | | |
| y₃ | | | +1 | −2 | +1 | |
| y₄ | | | | +1 | −2 | +1 |
| **Total** | +1 | −1 | 0 | 0 | −1 | +1 |

Every middle value meets all three kernel weights once, so its total is 1 − 2 + 1 = 0. Only the two values at each end survive:

S = x₁ − x₂ − x₅ + x₆ = (x₆ − x₅) − (x₂ − x₁) = (4 − 1) − (2 − 5) = 3 + 3 = **6**.

Check: 7 − 4 − 5 + 8 = 6.

**Step 7: the same thing as a telescoping sum** (move **M11: kernels telescope**). A *telescoping sum* is a chain where each term cancels part of the next, like (b − a) + (c − b) + (d − c) = d − a. With the steps dᵢ = xᵢ₊₁ − xᵢ, Step 4's check says yᵢ = dᵢ₊₁ − dᵢ. So

S = (d₂ − d₁) + (d₃ − d₂) + (d₄ − d₃) + (d₅ − d₄) = d₅ − d₁,

the last step minus the first step: 3 − (−3) = 6.

**What to remember:** read the convolution definition before you compute, because the exam's version flips the kernel. If a kernel's weights add up to 0, then every middle value cancels when you sum the outputs, and only the ends of the signal survive.

**Common trap:** sliding [1, −1] without flipping it, out of CNN habit, which gives [−4, 3, −5].
</details>

---

### 4.6 Flip or not?

<details><summary>Hint 1: understand the question</summary>

Write out the first output, y₁, both ways with k = 3. In the exam's formula, which x does h₁ multiply? In the no-flip version, which x does h₁ multiply?
</details>

<details><summary>Hint 2: the key idea</summary>

Convolution is correlation with the kernel reversed. So reverse h = [1, 0, −1] and compare the result with the original h. What do you notice?
</details>

<details><summary>Answer</summary>

exam: **[2, 2]**; correlation: **[−2, −2]**; they differ by sign here because $h$ is antisymmetric (reversing it gives −h)
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the exam's convolution** (move **M1: read the definition, not your memory**). With k = 3: $y_i = h_1 x_{i+2} + h_2 x_{i+1} + h_3 x_i = x_{i+2} - x_i$. Output length is 4 − 3 + 1 = 2.
- y₁ = x₃ − x₁ = 3 − 1 = 2
- y₂ = x₄ − x₂ = 4 − 2 = 2

So the exam's output is **[2, 2]**. That makes sense: x rises by 1 per step, so over two steps it rises by 2.

**Step 2: correlation (no flip).** $y_i = h_1 x_i + h_2 x_{i+1} + h_3 x_{i+2} = x_i - x_{i+2}$.
- 1 − 3 = −2
- 2 − 4 = −2

So the correlation output is **[−2, −2]**.

**Step 3: why they are related.** Convolution with h is the same as correlation with h reversed. Reversed, [1, 0, −1] becomes [−1, 0, 1], which is exactly −h. A kernel with this property (reversing it gives its negative) is called **antisymmetric**. So convolution = correlation with −h = −(correlation with h), and the outputs are exact negatives of each other.
- If h is **symmetric** (it reads the same backwards, like [1, −2, 1] in 4.5), the two operations give identical outputs.
- For a general kernel, like [10, 1] in 4.5 Step 1, the outputs are neither equal nor opposite: [21, 42] against [12, 24].

**What to remember:** convolution = correlation with the kernel reversed. The two agree for symmetric kernels and differ by a sign for antisymmetric ones. On the exam, use the formula printed on the paper.

**Common trap:** your CNN intuition is for correlation, because PyTorch's `Conv1d` doesn't flip. If you slide the kernel as written on the exam, every antisymmetric kernel gives you the wrong sign.
</details>
