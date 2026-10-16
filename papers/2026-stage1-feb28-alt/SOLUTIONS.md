# INAIO 2026 Stage 1 — Alternate paper (28 Feb) — Solutions (unofficial)

Unofficial: computed by us and checked numerically with `verify.py`. No official key has been published. If you find a mistake, open an issue.

Grade yourself with the **answer table** first. Re-attempt anything you missed **before** reading its worked solution.

For each question you missed, struggle for 10–15 minutes, then open **one** hint at a time, with about 5 minutes between hints. If two hints don't unlock it, the gap is in your knowledge, not your effort, so read the full solution.

## Answer table

| Section | Question | Points | Answer |
|---|---|---|---|
| A1 | 1. Cracking the Imperial Glyphs | 3 | **E** (土造蘋果甜) |
| A1 | 2. Filtering Fakes with Faulty Oracle | 3 | **F** {F1, F3, F6} |
| A1 | 3. Smart Professor Search | 3 | **C** |
| A1 | 4. Recursive V-67 Outbreak | 3 | **D** (102) |
| A1 | 5. Pikachu's Path to Victory | 3 | **E** (15) |
| A2 | 1. The Phulera Godown Showdown | 3 | **15** |
| A2 | 2. The Blind Board Gambit | 3 | **31** |
| A2 | 3. The Crude Curve Forecast | 3 | **49** |
| A2 | 4. The Catalyst Constraint | 3 | **45** |
| A2 | 5. The Pit-Stop Paradox | 3 | **15** |
| B1 | Q1 False alarms in ICU prediction | 1 | **43** (42 is also defensible; see the solution) |
| B1 | Q2 Inpatient triaging | 1 | **90** |
| B1 | Q3 Optimal operating point | 2 | **Option 5** (Point E) |
| B1 | Q4 Effect of score adjustment | 1 | **Option 2** (improves consistently) |
| B1 | Q5 Diagnosing a ROC shift | 1 | **Option 3** (new predictive features) |
| B1 | Q6 Architectures and losses (select all) | 2 | **Options 3 and 5** (Claims 3 and 5) |
| B1 | Q7 Expected misclassification cost | 2 | **13** |
| B2 | Q1 DCG@5 | 1 | **10** |
| B2 | Q2 Strategy A vs B at k = 8 | 1 | **Option 4** (B improves both) |
| B2 | Q3 Maximising DCG | 2 | **Option 3** [D1, D8, D5, D9] |
| B2 | Q4 Optimal scoring function | 3 | **Option 4** (Score_D only) |
| B2 | Q5 PI-Recall@5 | 3 | **30** |
| B3 | Q1 Convolution with padding and stride | 1 | **A** [4, 7, 8] |
| B3 | Q2 Smoothness vs fluctuations (select all) | 2 | **D, F** |
| B3 | Q3 Acceleration (select all) | 2 | **E, F** |
| B3 | Q4 Spike detection (select all) | 2 | **E, F** |
| B3 | Q5 Symmetry detection (select all) | 3 | **B, D, F** |
| B4 | Q1 Reverse-engineering the weights | 4 | **36** |
| B4 | Q2 Optimal pruning pair | 3 | **13** |
| B4 | Q3 Bias correction | 3 | **65** |

## Hints and worked solutions

### A1.1 Cracking the Imperial Glyphs (3 pts)

<details><summary>Hint 1: understand the question</summary>

The target is "The soil makes the apple sweet." Which of the eight example sentences has the same shape (*something* makes *something* have a *quality*)? And which word in the target never appears in any example?

</details>

<details><summary>Hint 2: the key idea</summary>

Match words to glyphs by where they occur. A glyph that appears in exactly the sentences containing "sweet", and nowhere else, must mean "sweet". Do this for each word you need, then copy the word order from the sentence with the same shape.

</details>

<details><summary>Hint 3: set it up</summary>

Write sentence 5 glyph by glyph under its English words: "Does the tree make the apple beautiful?" = 樹造蘋果美？ Now swap in your own words.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: build a mini-dictionary from co-occurrence.** For each English word, find the glyph that appears in exactly the same sentences.
- 蘋果 appears in sentences 1, 2, 3, 4, 5 and 8: exactly the ones with "apple". So 蘋果 = apple.
- 甜 appears only in sentence 8, the only one with "sweet". So 甜 = sweet.
- 造 appears only in sentence 5, the only one with "make". So 造 = make.
- In the same way: 樹 = tree, 美 = beautiful, 很 = very, 宮 = palace, 塗 = paints, 山 = mountain.
- "Soil" appears in no example, so its glyph can't be any glyph you've already seen. The only unseen glyph in the options is 土.

**Step 2: find the word order.** Sentence 5 is 樹 造 蘋果 美 = tree / make / apple / beautiful. The pattern is [doer] 造 [thing] [quality], with the quality at the end. Sentence 7 confirms this: 山 塗 宮 黑 = mountain / paints / palace / black.

**Step 3: fill in the pattern.** soil + make + apple + sweet = 土造蘋果甜.

**Step 4: check the options.**
- A uses 山, which already means mountain.
- B adds 很 (very).
- C and F put 蘋果 first, which would make the apple the doer.
- D uses 塗 (paints) and 宮 (palace).
- **E** matches exactly.

**What to remember:** *M17 Align and decode.* Line up each sentence with its glyphs, decode words by where they co-occur, and copy the word order from the example with the same structure. A word you've never seen must map to a glyph you've never seen.

**Common trap:** picking A because it "looks complete". 山 already means mountain, so it can't also mean soil.

</details>

---

### A1.2 Filtering Fakes with Faulty Oracle (3 pts)

<details><summary>Hint 1: understand the question</summary>

For each feature, ask: does the model have everything it needs inside its input (the headline and the article body)? Or does it have to count letters, guess, or know facts about the world?

</details>

<details><summary>Hint 2: the key idea</summary>

Look at what is special about this oracle: it is text-only, it sees the article body, and it can search the web. Which features does that make easy? Then check which options contain one of those easy features.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: sort the features by what the model has to do.**

| Feature | What the model must do | Reliable here? |
|---|---|---|
| F1 Character count | count characters | **No.** LLMs read *tokens* (chunks of several letters), not individual letters, so counting characters is a known weakness. A one-line program counts exactly anyway. |
| F2 Publication year | find a date | Mostly yes: web retrieval can look up when the story appeared. |
| F3 Political leaning of the likely outlet | guess the outlet, then guess its leaning | **No.** It is a guess built on a guess, "leaning" is subjective, and the model's own bias leaks in. |
| F4 Article–headline consistency | compare two texts it has been given | **Yes.** Everything needed is in the prompt. This is reading comprehension, which LLMs do well. |
| F5 Language ID | recognise French | Yes. It will say "fr" almost every time. That makes it a useless feature, but not an unreliable one. |
| F6 Named outlet | name the publisher | **No.** This invites made-up answers (*hallucination*). Fake stories are copied across many sites, so even a web search can surface the wrong source. |
| F7 Topic | classify the topic | Yes. |
| F8 Quote present | spot quotation marks or "said X" | Yes. |

**Step 2: read off the set.** The unreliable features are {F1, F3, F6}, which is option **F**.

**Step 3: fast cross-check.** Every option except F contains F4, the most clearly reliable feature here. So even if you're unsure about F2 or F6, F4 alone rules out A–E.

**What to remember:** *M14 LLM reality check.* Ask "is the answer inside the prompt?" LLMs are good at reading and comparing text they're given. They are weak at counting characters (because of tokens) and at guessing facts that aren't there. Retrieval fixes lookups, not guesswork.

**Common trap:** reusing your Jan 18 reasoning. There the model was offline and multimodal, so the year was pure guesswork and F4 compared an image with text. Here, retrieval and the article body change which features are reliable.

</details>

---

### A1.3 Smart Professor Search (3 pts)

<details><summary>Hint 1: understand the question</summary>

The five rules are five tests. Instead of hunting for the "best" formula, can you find, for each wrong option, one pair of profiles that breaks one rule?

</details>

<details><summary>Hint 2: the key idea</summary>

Run three quick tests on every option:
1. Two identical profiles: the score must be exactly 1.
2. Different departments, e.g. CS vs CE: the score must be 0.
3. A name typo vs a title typo of the same size: the name typo must give the lower score.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Definitions.**
- NED = 1 − ED/(longer length). It is 1 for identical strings and smaller the more they differ. For example, NED("Alice", "Alicf") = 1 − 1/5 = 0.8.
- exp(x) means $e^x$, where e ≈ 2.718. exp(0) = 1, and exp of a negative number lies between 0 and 1.
- Write $u_n = 1 - \text{NED}(n, n')$ for how wrong the name is and $u_t = 1 - \text{NED}(t, t')$ for the title. Both are 0 when the field matches.

**Step 1: identical profiles (rules 1 and 5).** Here $u_n = u_t = 0$.
- A gives (1 + 1)/2 = 1 ✓. B, C and D give exp(0) = 1 ✓.
- E gives 2·1 + 1 = **3** ✗. F gives $e^0 + e^0$ = **2** ✗. Both also break rule 5 (score must be at most 1).

**Step 2: different departments (rule 2).** A, C, D, E and F multiply by the indicator $\mathbf{1}_{d=d'}$, which is 0 ✓. B multiplies by NED(d, d′) instead, and NED("CS", "CE") = 1 − 1/2 = 0.5. So B gives a positive score for different departments ✗.

**Step 3: name vs title (rule 4).** Compare a mismatch of the same size u in the name or in the title.
- A: the name typo gives 1 − u/2, and so does the title typo. They hurt equally, but the name should hurt more ✗.
- C: the name typo gives $e^{-2u}$, the title typo gives $e^{-u}$. Since 2u > u, $e^{-2u} < e^{-u}$, so the name typo hurts more ✓.
- D: the weights are swapped, so the title typo hurts more ✗.

**Step 4: confirm C.** C equals 1 only when both NEDs are 1 (identical strings) and the departments match. It always lies between 0 and 1. ED doesn't care about order, so C is symmetric. Answer: **C**.

**What to remember:** *M10 Kill options with counterexamples.* Don't try to prove the right option is right. Find one small example that breaks each wrong one; three quick tests usually leave one standing.

**Common trap:** D looks almost the same as C. Check which NED carries the factor 2: the heavier weight must be on the name.

</details>

---

### A1.4 Recursive V-67 Outbreak (3 pts)

<details><summary>Hint 1: understand the question</summary>

The question asks for $R_3$, not for the number of infectious people. What gets added to R each day? Which numbers do you actually need for that?

</details>

<details><summary>Hint 2: the key idea</summary>

Make a table with one row per day: N, M and R at the start of the day, then X. Fill it row by row, applying the three steps in order.

</details>

<details><summary>Hint 3: set it up</summary>

The update rules, with $X_t = 2N_t + (2 + 4t)M_t$:
- $N_{t+1} = N_t/2 + \tfrac34 X_t$
- $M_{t+1} = M_t/2 + \tfrac14 X_t$
- $R_{t+1} = R_t + N_t/2 + M_t/2$

Day 0 uses t = 0.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: turn the story into update rules.** During day t, $X_t$ new people are infected. Half of the people who were infectious at the start of the day recover, and the new infections join the pool for tomorrow. A rule like this, which computes each day's numbers from the previous day's, is called a *recurrence*. The rules are in Hint 3.

**Step 2: tabulate.**

| Day t | $N_t$ | $M_t$ | $R_t$ | mutant rate 2 + 4t | $X_t$ |
|---|---|---|---|---|---|
| 0 | 8 | 8 | 0 | 2 | 16 + 16 = 32 |
| 1 | 4 + 24 = 28 | 4 + 8 = 12 | 0 + 4 + 4 = 8 | 6 | 56 + 72 = 128 |
| 2 | 14 + 96 = 110 | 6 + 32 = 38 | 8 + 14 + 6 = 28 | 10 | 220 + 380 = 600 |
| 3 | 55 + 450 = 505 | 19 + 150 = 169 | 28 + 55 + 19 = **102** | | |

**Step 3: shortcut check.** Each day, half of everyone infectious at the start recovers. So $R_3 = \tfrac12[(8 + 8) + (28 + 12) + (110 + 38)] = \tfrac12(16 + 40 + 148) = 102$. Notice that $X_2 = 600$ never affects $R_3$.

Answer: **D (102)**.

**What to remember:** *M9 Tabulate recurrences.* Write the update rule once, then fill a table one row at a time. Before computing, ask what the answer actually depends on: here $R_3$ needs only the infectious counts on days 0, 1 and 2.

**Common trap:** starting the mutant rate at t = 1 (which gives a rate of 6 on day 0), or letting newly infected people recover on the day they were infected.

</details>

---

### A1.5 Pikachu's Path to Victory (3 pts)

<details><summary>Hint 1: understand the question</summary>

There are 16 pads but only six answer options. Before searching for a long path, can you rule some counts out without drawing anything?

</details>

<details><summary>Hint 2: the key idea</summary>

Colour the board like a chessboard. What does every knight move do to the colour? Then look at the four corners: how many knight moves lead into each one?

</details>

<details><summary>Hint 3: set it up</summary>

Compare the colours of (0,0) and (3,3). Then notice that corners (0,3) and (3,0) each have only two knight neighbours, (1,1) and (2,2). What happens if a path passes through both of these corners?

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: parity (colouring).** Colour square (r, c) white if r + c is even and black if it's odd. A knight move changes r + c by 1 ± 2 or −1 ± 2, which is always odd, so every move flips the colour. Start (0,0) has sum 0 (white) and goal (3,3) has sum 6 (white). Going from white to white takes an even number of moves, so the number of pads (moves + 1) is **odd**. That rules out 10, 12, 14 and 16, leaving 13 or 15.

**Step 2: an upper bound from the corners.** List each corner's knight neighbours:
- (0,0) and (3,3): only (1,2) and (2,1).
- (0,3) and (3,0): only (1,1) and (2,2).

A pad in the middle of a path needs two path-neighbours: one to arrive from and one to leave to. So if (0,3) is in the middle of the path, the path contains (1,1) – (0,3) – (2,2). If (3,0) is in the middle as well, the path also contains (1,1) – (3,0) – (2,2). Together these make a closed loop (1,1) → (0,3) → (2,2) → (3,0) → (1,1), and a path that never revisits a pad can't contain a loop. Neither corner can be the start or the end, because those are (0,0) and (3,3). So at most one of (0,3) and (3,0) is used, giving **at most 15 pads**.

**Step 3: show that 15 is reachable.** One path, written as (row, column):

(0,0) → (1,2) → (2,0) → (3,2) → (1,3) → (0,1) → (2,2) → (0,3) → (1,1) → (2,3) → (3,1) → (1,0) → (0,2) → (2,1) → (3,3)

That's 15 pads; only (3,0) is skipped. Spot-check a move: (1,2) → (2,0) is 1 down and 2 left ✓.

A full computer search in `verify.py` finds paths of 3, 7, 9, 11, 13 and 15 pads, never an even number, and never 16. Answer: **E (15)**.

**What to remember:** *M8 Parity / colouring.* Colour the board. If every move flips the colour, the parity of the path length is fixed. Then look at squares with few neighbours (corners): a square with only two neighbours forces both of them into the path.

**Common trap:** answering 16 ("visit everything"). A full tour fails for two separate reasons: parity and the corners.

</details>

---

### A2.1 The Phulera Godown Showdown (3 pts)

<details><summary>Hint 1: understand the question</summary>

Each godown is the answer to "where is the total cost smallest?" Do the x and y parts of each cost interact, or can you find the best x and the best y separately?

</details>

<details><summary>Hint 2: the key idea</summary>

For Sachivji: imagine moving x a little to the right. How many fields get closer, and how many get further away?

For Pradhanji: try a few values of u (say 100, 115 and 130) and see which gives the smallest cost. Then look for the reason.

</details>

<details><summary>Hint 3: set it up</summary>

For Itakura–Saito, expand the total cost using ln(x/u) = ln x − ln u. Then compare it with 4 × IS(m, u), where m is the mean of the four x-values.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Definitions.**
- *argmin*: the input that makes an expression smallest. For example, the argmin of (x − 3)² is x = 3.
- *Manhattan (L1) distance*: |Δx| + |Δy|, the distance you travel along a street grid.
- *Median*: the middle value. With an even count, any value between the two middle values counts.
- *ln* (natural log): ln(e^a) = a, ln 1 = 0, and ln(a/b) = ln a − ln b.
- *Itakura–Saito (IS) divergence*: IS(p, u) = p/u − ln(p/u) − 1. It measures how far u is from p using their ratio: it is 0 when p = u and grows as p/u moves away from 1.
- ⌊D⌋ means round down: ⌊15.9⌋ = 15 and ⌊15⌋ = 15.

**Step 1: split x from y.** Both costs are (a part depending only on x) + (a part depending only on y), so you can minimise each part on its own.

**Step 2: Sachivji (L1).** The x-values sorted are 40, 80, 120, 220. Pick x between 80 and 120 and move it right by a small amount δ. Fields 40 and 80 get further away (+2δ), while 120 and 220 get closer (−2δ), so the cost doesn't change. To the left of 80, three fields lie to your right, so moving right lowers the cost. Beyond 120, moving left lowers it. So every x in [80, 120] is best: the median range. The note says to take the middle, so $x_S$ = 100. The y-values sorted are 20, 80, 120, 180, giving the range [80, 120] and $y_S$ = 100. So $G_S$ = (100, 100).

**Step 3: Pradhanji (IS), first by trial.** If you don't know the trick, try numbers. The x-cost is Σ [x_i/u − ln(x_i/u) − 1]:

| u | total x-cost |
|---|---|
| 100 | 0.769 |
| 115 | **0.728** |
| 130 | 0.757 |

The best value, 115, is exactly the mean of 40, 120, 220 and 80. Here is why that's no coincidence.

**Step 4: Pradhanji, the reason.** Let m = mean, so Σ x_i = 4m. Then

Σ [x_i/u − ln x_i + ln u − 1] = 4m/u + 4 ln u − Σ ln x_i − 4.

Add and subtract 4 ln m:

= 4[m/u − ln(m/u) − 1] + (4 ln m − Σ ln x_i) = 4·IS(m, u) + (a number that doesn't involve u).

So minimising the total cost is the same as minimising IS(m, u). The problem tells you IS ≥ 0, and it equals 0 only when u = m: the function r − ln r − 1 is 0 at r = 1 and positive elsewhere (r = 0.5 gives 0.19 and r = 2 gives 0.31). So $u = m$ = 115.

For y, the mean of 180, 80, 120 and 20 is 400/4 = 100. So $G_P$ = (115, 100).

**Step 5: the distance.** D = √(15² + 0²) = 15 exactly, so ⌊D⌋ = **15**.

**What to remember:** *M6 What does the argmin pick?* A sum of absolute distances is minimised by the median, and a sum of squared distances by the mean. Divergences like IS (and Jan 18's generalised KL), measured from the data point to the candidate, are also minimised by the mean. Identify the statistic first; the arithmetic is then one line.

**Common trap:** assuming a "fancy" divergence picks something exotic, or ignoring the note and using an endpoint (80 or 120) instead of 100.

</details>

---

### A2.2 The Blind Board Gambit (3 pts)

<details><summary>Hint 1: understand the question</summary>

There are two stages. First, Anand *chooses* his line-up using an average over three possible Gukesh line-ups. Then the match is *played* against the actual line-up. Which line-up belongs to which stage?

</details>

<details><summary>Hint 2: the key idea</summary>

First build the 3×3 table of single-game win probabilities (each Anand player against each Gukesh player). Then you need the probability of winning at least 2 of 3 independent games, written in terms of p1, p2 and p3.

</details>

<details><summary>Hint 3: set it up</summary>

P(at least 2 of 3) = p1p2 + p1p3 + p2p3 − 2p1p2p3. Compute it for each of Anand's six orders against each of Gukesh's three possible orders, then average across the three.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: single games.** P(an Anand player rated R beats a Gukesh player rated S) = 1/(1 + 10^((S − R)/400)). Useful powers: 10^0.25 ≈ 1.778, 10^0.5 ≈ 3.162, 10^0.75 ≈ 5.623 and 10^1.5 ≈ 31.62.

| Anand player | vs A (2100) | vs B (1800) | vs C (1600) |
|---|---|---|---|
| X (2000) | 0.360 | 0.760 | 0.909 |
| Y (1700) | 0.091 | 0.360 | 0.640 |
| Z (1500) | 0.031 | 0.151 | 0.360 |

**Step 2: at least 2 of 3.** Winning all three has probability p1p2p3. Winning exactly two has probability p1p2(1 − p3) + p1(1 − p2)p3 + (1 − p1)p2p3. Adding these and simplifying gives p1p2 + p1p3 + p2p3 − 2p1p2p3.

**Step 3: a rough shortlist.** Z beats A only 3% of the time and B 15%, so Z's board is almost always lost, which means Anand must win both of the other boards. Board 3 has A in two of the three possible line-ups, so Z belongs on board 3. That suggests (X, Y, Z) or (Y, X, Z). A rough guess can mislead, though, so compute everything.

**Step 4: the full table** (probability that Anand wins the match):

| Anand (boards 1, 2, 3) | vs (B, C, A) | vs (C, A, B) | vs (C, B, A) | average |
|---|---|---|---|---|
| X, Y, Z | 0.499 | 0.209 | 0.346 | 0.351 |
| X, Z, Y | 0.326 | 0.346 | 0.209 | 0.293 |
| **Y, X, Z** | 0.346 | **0.312** | 0.499 | **0.386** |
| Y, Z, X | 0.295 | 0.499 | 0.312 | 0.369 |
| Z, X, Y | 0.209 | 0.295 | 0.326 | 0.277 |
| Z, Y, X | 0.312 | 0.326 | 0.295 | 0.311 |

Only six different numbers appear. Each match is a set of three pairings, and different line-ups often produce the same set, so by hand you need far fewer than 18 calculations.

Worked example, (Y, X, Z) against (C, A, B): the pairings are Y–C, X–A and Z–B, so p = (0.640, 0.360, 0.151). Then p1p2 = 0.2304, p1p3 = 0.0966, p2p3 = 0.0543 and p1p2p3 = 0.0348. Total = 0.3813 − 2(0.0348) = 0.3118.

**Step 5: answer.** Anand picks (Y, X, Z), which has the highest average. Against the actual line-up (C, A, B), p = 0.3118, so ⌊100p⌋ = **31**.

Notice: had Anand known the actual line-up, he would have picked (Y, Z, X) and won with probability 0.499. Not knowing costs him about 19 percentage points.

**What to remember:** *M16 Elo & series.* Build the single-game table first, then use P(≥2 of 3) = p1p2 + p1p3 + p2p3 − 2p1p2p3. Keep the decision stage (averaging over the possibilities) separate from the evaluation stage (the actual line-up).

**Common trap:** using the actual line-up while choosing. That uses information Anand doesn't have; you'd pick (Y, Z, X) and answer 49.

</details>

---

### A2.3 The Crude Curve Forecast (3 pts)

<details><summary>Hint 1: understand the question</summary>

The model has six pieces that switch on at different times. Between months 0 and 18, which pieces are on? Can you find some parameters from that window alone?

</details>

<details><summary>Hint 2: the key idea</summary>

Treat the dashed lines as switch-on times. Find the period of the cosine from the peaks and dips, then use the months where the cosine is exactly +1 or −1.

</details>

<details><summary>Hint 3: set it up</summary>

Guess that the cosine has a period of 12 months: peaks at 0 and 12, a dip at 6. Then t = 0, 6 and 12 give three equations in A, B and E.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Definitions.**
- *Heaviside step* h(t − τ): 0 before time τ and 1 from τ onwards, like a switch. So D·h(t − 18) adds D from month 18 on.
- $e^{-x}$ shrinks fast: $e^{-1} \approx 0.37$ and $e^{-6} \approx 0.0025$. So $C(1 - e^{-(t-\tau_C)})$ rises from 0 to almost C within a few months of $\tau_C$.
- $F(t - \tau_F)h(t - \tau_F)$ is a ramp that starts at $\tau_F$ with slope F.
- $E\cos(2\pi t/\tau_E)$ repeats every $\tau_E$ months, swinging between +E and −E.

**Step 1: before month 18.** Only A + Bt + E cos(2πt/τ_E) is switched on. The curve peaks at 0 and 12 and dips at 6, so $\tau_E$ = 12: the cosine is +1 at months 0 and 12 and −1 at month 6.
- t = 0: A + E = 58
- t = 6: A + 6B − E = 45
- t = 12: A + 12B + E = 64

Subtract the first equation from the third: 12B = 6, so B = 0.5. Then the second gives A − E = 45 − 3 = 42. Combined with A + E = 58: A = 50 and E = 8.

Check t = 18⁻: 50 + 9 + 8 cos(3π) = 59 − 8 = 51 ✓.

**Step 2: the jump at 18.** The price drops from 51 to 26, so D = −25 and $\tau_D$ = 18. Check t = 24: 50 + 12 − 25 + 8 = 45 ✓. Check t = 30: 50 + 15 − 25 − 8 = 32 ✓.

**Step 3: the fast climb after 30.** This is the exponential recovery, so $\tau_C$ = 30. At t = 36: 50 + 18 − 25 + 8 + C(1 − e^{−6}) = 51 + 0.9975C = 71, so C ≈ 20. Check t = 42: 50 + 21 − 25 − 8 + 20 = 58 ✓.

**Step 4: after 42.** The peaks stop rising (71 at both 36 and 48), so a downward ramp starts at $\tau_F$ = 42. At t = 48: 50 + 24 − 25 + 8 + 20 + 6F = 77 + 6F = 71, so F = −1. Check t = 54: 50 + 27 − 25 − 8 + 20 − 12 = 52 ✓. Check t = 60: 50 + 30 − 25 + 8 + 20 − 18 = 65 ✓.

**Step 5: t = 75.** cos(2π·75/12) = cos(12.5π) = cos(π/2) = 0. The recovery term is 20(1 − e^{−45}), which is 20 for all practical purposes.

P(75) = 50 + 37.5 + 20 − 25 − 33 + 0 = 49.5, so ⌊P(75)⌋ = **49**.

`verify.py` fits all six parameters by least squares to the twelve labelled points, trying every assignment of the dashed lines to τ_C, τ_D and τ_F. The assignment above is the only one that fits (error 0.001 vs 393 for the next best), and it also gives 49.

**What to remember:** *M13 Read parameters off a graph.* Work window by window, since only some terms are on in each window. Use the months where the periodic term is ±1 or 0, solve small linear systems, and check every other labelled point.

**Common trap:** forgetting that the trend B keeps going after the ramp starts (the net slope after month 42 is B + F = −0.5, not −1), or taking the cosine at t = 75 as ±1 instead of 0.

</details>

---

### A2.4 The Catalyst Constraint (3 pts)

<details><summary>Hint 1: understand the question</summary>

How much catalyst would each pathway want if catalyst were unlimited? Is 5 moles enough for both?

</details>

<details><summary>Hint 2: the key idea</summary>

If the budget is too small for both, you should use all of it. Then $c_B = 5 - c_A$, and the total yield becomes a quadratic in $c_A$ alone.

</details>

<details><summary>Hint 3: set it up</summary>

Substitute $c_B = 5 - c_A$ into $10c_A - 2c_A^2 + 20c_B - 3c_B^2$ and expand.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: read the formula.** Here a = 2 and b = 3 multiply the *squared* term (the inhibition), so $d_A = 10c_A - 2c_A^2$ and $d_B = 20c_B - 3c_B^2$.

**Step 2: does the budget bind?** A quadratic −kc² + mc peaks at c = m/(2k). Pathway A alone would peak at 10/4 = 2.5, and B at 20/6 ≈ 3.33. Together they want 5.83 > 5. Below its peak each pathway's yield is still rising, so any catalyst you held back would be better given to one of them. Use all 5.

**Step 3: substitute and expand.**

total = $10c_A - 2c_A^2 + 20(5 - c_A) - 3(5 - c_A)^2$
= $10c_A - 2c_A^2 + 100 - 20c_A - 75 + 30c_A - 3c_A^2$
= $-5c_A^2 + 20c_A + 25$.

This peaks at $c_A$ = 20/10 = 2, so $c_B$ = 3. Total = −20 + 40 + 25 = 45.

**Step 4: check with marginal gains.** The *marginal gain* is the extra yield from one more tiny amount δ of catalyst. For A: 10(c + δ) − 2(c + δ)² − (10c − 2c²) = (10 − 4c)δ − 2δ² ≈ (10 − 4c)δ. For B it is about (20 − 6c)δ. At (2, 3) both equal 2δ, so moving catalyst from one pathway to the other can't help.

The individual yields are $d_A$ = 20 − 8 = 12 and $d_B$ = 60 − 27 = 33, so ⌊d_A + d_B⌋ = **45**.

**What to remember:** *M7 Equal marginal gains (check if the constraint binds).* First compare each option's unconstrained peak with the budget. If the budget binds, split it so that the last bit of catalyst earns the same in both pathways.

**Common trap:** using a = 2 and b = 3 as the *linear* coefficients, as in Jan 18's version ($d_A = a\,c_A - 2c_A^2$). Read the formula, not your memory.

</details>

---

### A2.5 The Pit-Stop Paradox (3 pts)

<details><summary>Hint 1: understand the question</summary>

You want P(neither pitted | H wins). The bar means "given that". Which races go in the bottom of the fraction, and which in the top?

</details>

<details><summary>Hint 2: the key idea</summary>

Imagine 10,000 races. Split them by safety car, then by strategy, then count how many end in a Hamilton win.

</details>

<details><summary>Hint 3: set it up</summary>

There's no safety car in 6,000 races and a safety car in 4,000. In the 6,000, "neither pits" happens 50% of the time (3,000 races), and Hamilton wins 20% of those.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: why counts?** P(A | B) = (number of cases with both A and B) ÷ (number of cases with B). Counts make this mechanical.

**Step 2: count all 10,000 races.**

| Safety car? | Strategy | Races | P(H wins) | H wins |
|---|---|---|---|---|
| No (6,000) | Neither | 0.50 × 6000 = 3000 | 0.20 | 600 |
| No | Only V | 1500 | 0.85 | 1275 |
| No | Only H | 600 | 0.10 | 60 |
| No | Both | 900 | 0.50 | 450 |
| Yes (4,000) | Neither | 0.05 × 4000 = 200 | 0.40 | 80 |
| Yes | Only V | 400 | 0.15 | 60 |
| Yes | Only H | 200 | 0.90 | 180 |
| Yes | Both | 3200 | 0.55 | 1760 |

**Step 3: divide.** Hamilton wins 600 + 1275 + 60 + 450 + 80 + 60 + 180 + 1760 = 4465 races. Of those, neither driver pitted in 600 + 80 = 680. So P = 680/4465 = 0.1523 and ⌊100P⌋ = **15**.

**What to remember:** *M2 Natural frequencies.* Turn every probability into a count out of 10,000. A conditional probability is then "count in the top group ÷ count in the bottom group". A hidden variable like the safety car just adds more rows.

**Common trap:** ignoring the safety-car split, or answering with P(neither pitted) before you learned that Hamilton won: 0.6 × 0.5 + 0.4 × 0.05 = 0.32.

</details>

---

### B1 Q1 False alarms in ICU prediction (1 pt)

<details><summary>Hint 1: understand the question</summary>

"Flagged for ICU" includes two kinds of patient. What are they, and which numbers in the performance table tell you how many of each there are?

</details>

<details><summary>Hint 2: the key idea</summary>

Turn rates into counts. Of the 1,000 patients, how many are actually ICU and how many are not?

</details>

<details><summary>Hint 3: set it up</summary>

ICU patients who get flagged = sensitivity₃ × 150. Non-ICU patients who get flagged = (1 − specificity₃) × 850.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Definitions.** Sensitivity of a class = the fraction of that class that gets caught. Specificity₃ = the fraction of non-ICU patients correctly *not* flagged as ICU, so 1 − specificity₃ is the fraction of non-ICU patients wrongly flagged (the *false-positive rate*, FPR).

**Step 1: counts.** ICU = 15% of 1,000 = 150. Non-ICU = 850.

**Step 2: flagged patients.** ICU patients flagged: 0.80 × 150 = 120. Non-ICU patients flagged: (1 − 0.89) × 850 = 93.5.

**Step 3: the fraction.** x = 93.5/(120 + 93.5) = 93.5/213.5 = 0.4379, so ⌊100x⌋ = **43**.

Stop and notice: a system that is "80% sensitive and 89% specific" still gets 44% of its ICU flags wrong, because there are 850 non-ICU patients for every 150 ICU patients.

**An alternative answer: 42.** The paper's numbers don't quite fit together. Suppose you build the full 3×3 table (see Q7) from the sensitivities and the two egregious counts, and use specificity₁ = 0.90 to split class 2's errors. Then the non-ICU patients flagged as ICU number 25 + 65 = 90, not 93.5, and x = 90/210 = 0.4286, giving 42.

The cause is rounding: the specificities are printed to 2 decimals. For example, the table forces specificity₂ = 575/650 = 0.8846, which the paper prints as 0.88. `verify.py` checks every whole-number table that matches all the printed figures: two give 43 and one gives 42.

We give 43 because it uses the class-3 figures exactly as printed, which is the standard one-mark method. 42 is also defensible.

**What to remember:** *M5 Rates → counts.* "Of the flagged, how many are wrong?" divides by a *predicted* count, so it depends on how common each class is. Convert each rate into a count within its own group, then add.

**Common trap:** answering 1 − specificity₃ = 11% or 1 − sensitivity₃ = 20%. Neither divides by the number of flagged patients.

</details>

---

### B1 Q2 Inpatient triaging (1 pt)

<details><summary>Hint 1: understand the question</summary>

"Actually needs hospitalisation" means actual class 2 or 3, i.e. actual *not class 1*. "Correctly identified as needing hospitalisation" means predicted *not class 1*. Does any definition in the background box describe exactly that?

</details>

<details><summary>Hint 2: the key idea</summary>

Reread the definition of specificity, with class 1 as the positive class.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: translate.** Hospitalised means not class 1. The question asks: of the patients who are actually not C1, what fraction were predicted not C1? A C2 patient sent to the ICU, or a C3 patient sent to the ward, still counts as "correctly identified as needing hospitalisation".

**Step 2: match a definition.** That is word for word specificity₁: of the actual non-C1 patients, the fraction correctly identified as non-C1. So x = 0.90 and the answer is **90**.

**Step 3: check with counts.** Using the table from Q7, 500 patients need hospital care. The only ones sent home are 40 (from C2) + 10 (from C3) = 50, and (500 − 50)/500 = 0.90 ✓.

**What to remember:** *M1 Read the definition, not your memory.* Before computing, rewrite the question as "of [actual group], what fraction were [predicted group]?" Then check whether one of the given metrics is exactly that.

**Common trap:** using the class-2 and class-3 sensitivities, (245 + 120)/500 = 73%. That only counts patients placed in exactly the right ward.

</details>

---

### B1 Q3 Optimal operating point for ICU detection (2 pts)

<details><summary>Hint 1: understand the question</summary>

Missing an ICU patient costs 8, and an unnecessary admission costs 1. At each point, how many of each mistake happen per 1,000 patients?

</details>

<details><summary>Hint 2: the key idea</summary>

Convert TPR and FPR into counts using 150 ICU patients and 850 non-ICU patients.

</details>

<details><summary>Hint 3: set it up</summary>

Cost per 1,000 patients = 8 × 150 × (1 − TPR) + 1 × 850 × FPR.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Definitions.** TPR = the fraction of ICU patients flagged (the sensitivity). FPR = the fraction of non-ICU patients flagged. An *ROC curve* plots TPR against FPR as you slide the threshold t₂; each point on it is one threshold setting.

**Step 1: the two kinds of mistake.** Missed ICU patients = 150(1 − TPR), at 8 each, costing 1200(1 − TPR). Unnecessary admissions = 850 × FPR, at 1 each.

**Step 2: tabulate.**

| Point | FPR | TPR | 1200(1 − TPR) | 850 × FPR | Cost per 1,000 |
|---|---|---|---|---|---|
| A | 0.02 | 0.52 | 576 | 17 | 593 |
| B | 0.05 | 0.68 | 384 | 42.5 | 426.5 |
| C | 0.08 | 0.76 | 288 | 68 | 356 |
| D | 0.11 | 0.80 | 240 | 93.5 | 333.5 |
| E | 0.14 | 0.86 | 168 | 119 | **287** |
| F | 0.22 | 0.91 | 108 | 187 | 295 |

The minimum is **Point E (option 5)**. Point D is the current operating point (sensitivity 0.80, specificity 0.89), and it isn't the best.

**Step 3: why E and not F?** Moving from E to F raises TPR by 0.05, saving 1200 × 0.05 = 60, but raises FPR by 0.08, costing 850 × 0.08 = 68. That's a net loss. Moving from D to E saves 72 and costs 25.5, so that step is worth it.

**What to remember:** *M5 Rates → counts.* Expected cost = (cost of a miss) × (number of positives) × (1 − TPR) + (cost of a false alarm) × (number of negatives) × FPR. Prevalence (how common ICU cases are) matters for cost, even though it doesn't change the ROC curve itself.

**Common trap:** forgetting prevalence and minimising 8(1 − TPR) + FPR. That picks F (0.94 vs E's 1.26).

</details>

---

### B1 Q4 ROC curve: effect of score adjustment (1 pt)

<details><summary>Hint 1: understand the question</summary>

In the Jan 18 paper, applying a monotone function to the score left the ROC curve unchanged. Is $s_{new}$ a function of $s_{old}$ alone? Can two patients with the same old score end up with different new scores?

</details>

<details><summary>Hint 2: the key idea</summary>

The ROC curve depends only on how ICU and non-ICU scores are *ordered* relative to each other. Ask who gets pushed up by 1.5 and who gets pushed down, and compare the ICU group with the non-ICU group.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Definitions.**
- *Monotone increasing* function: if a > b then f(a) > f(b), so the order of scores is unchanged. Squaring positive numbers is an example.
- *Conditional independence*, P(b | s_old, y) = P(b | y): once you know whether a patient is ICU, their old score tells you nothing more about their test result. In other words, the test is genuinely new evidence.

**Step 1: is this just a rescaling?** No. The shift depends on b, not only on $s_{old}$. Two patients with an old score of 3.0 end up at 4.5 (b = 1) and 1.5 (b = 0). So the order of patients can change, and so can the ROC curve. That rules out option 1.

**Step 2: which direction?** Among ICU patients, 85% test positive and move up 1.5, while 15% move down: an average shift of 1.5 × (0.85 − 0.15) = +1.05. Among non-ICU patients, only 12% test positive (specificity 0.88): an average shift of 1.5 × (0.12 − 0.88) = −1.14. So the two groups move apart by about 2.2 score units.

Because b is independent of $s_{old}$ within each group, this is new information, not the old information counted twice. At any FPR you choose, you now catch more ICU patients, so the curve moves toward the top-left everywhere. That's **option 2**.

**Step 3: rule out the rest.**
- Option 3: the test is informative (85% vs 12%), so it can't make things worse here.
- Option 4: "δ exceeds the SD" is an invented condition; a small δ helps a little and a larger one helps more.
- Option 5: there's no reason for the gain to appear only on one side of the curve.
- Option 6: the independence assumption is given precisely so that you don't need the joint distribution.

`verify.py` checks this numerically. It assumes each class's scores follow a bell curve (the *binormal* model), fits that to the six points in the figure, and applies the shift. At every FPR the new TPR is at least the old one, whatever the scale of the scores, and the AUC rises from 0.93 to about 0.96–0.97.

**A technical caveat (why option 6 isn't absurd).** A fixed shift isn't guaranteed to help for *every* possible score distribution. Suppose the old score already separated the classes perfectly, but with a gap smaller than 1.5. Then some non-ICU patients who test positive leapfrog ICU patients who test negative, and the curve gets worse (`verify.py` shows the AUC falling from 1.0 to 0.98). The question's wording ("independent predictive information") clearly points to option 2, and option 2 holds for any realistic curve like the one drawn.

**What to remember:** *M4 ROC invariances.* The ROC curve only sees the order of scores across the two classes. Monotone transforms, prevalence and thresholds don't change it. Adding genuinely new information changes the order, and in the useful direction.

**Common trap:** answering "unchanged" by pattern-matching on Jan 18. That transform was monotone; this one isn't.

</details>

---

### B1 Q5 Diagnosing a ROC curve shift (1 pt)

<details><summary>Hint 1: understand the question</summary>

Each option describes a change. For each one, ask: does it change the scores themselves, or only who is in the cohort, how many patients there are, or where the cut-off sits?

</details>

<details><summary>Hint 2: the key idea</summary>

TPR is computed inside the ICU group only, and FPR inside the non-ICU group only. A change can move the whole curve only if it changes how much the two groups' scores overlap.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: go through the options.**
1. ICU prevalence rises from 15% to 22%. TPR and FPR are each computed within one class, so the class mix doesn't matter. Same curve.
2. Lowering t₂ moves you to a different point *on the same curve* (higher TPR and higher FPR). It doesn't create a new curve.
3. Adding two predictive features changes the scoring function itself. With more information, ICU and non-ICU scores overlap less, and the whole curve moves up and to the left ✓.
4. Taking the square root of every score is monotone (it keeps the order), so the curve is the same. This is the lesson of Jan 18 Q4.
5. A bigger cohort means less random wobble, but no systematic shift in one direction.
6. Randomly dropping some ICU patients leaves the remaining ICU patients with the same score distribution. Same curve, just fewer patients.

Answer: **option 3**.

`verify.py` simulates every option. The AUC stays at about 0.928 for options 1, 4, 5 and 6 and jumps to 0.981 only when features are added.

**What to remember:** *M4 ROC invariances.* The ROC curve measures how well the scorer separates the classes. Prevalence, thresholds, sample size, random subsampling within a class and monotone rescaling leave it unchanged. Only a better (or worse) scorer moves it.

**Common trap:** option 2. Lowering a threshold slides you along the curve; it never lifts the curve.

</details>

---

### B1 Q6 Comparing classifier architectures and loss functions (2 pts, select all)

<details><summary>Hint 1: understand the question</summary>

Most claims use words like "always", "any" or "strictly". For each claim, can you build one small situation where it fails?

</details>

<details><summary>Hint 2: the key idea</summary>

For Claim 1, trace one patient through the cascade Y: can it ever end up with two answers, or with none? For the loss claims, compare how fast each loss grows for a point far on the wrong side, and ask what value each loss is minimised by.

</details>

<details><summary>Hint 3: set it up</summary>

Take a point with y·f(x) = −5 and compute its squared loss and its hinge loss. Then consider a group of patients of whom 70% are positive: which single score minimises their average logistic loss, and which minimises their average hinge loss?

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Definitions.**
- *Loss*: a penalty for one prediction. Training picks the model with the smallest total loss.
- *Margin* y·f(x): positive means the point is on the right side of the boundary; large means confidently right.
- *Outlier*: a training point far on the wrong side, such as a mislabelled patient.
- *Calibrated*: when the model says "70%" for a group of patients, about 70% of them really are positive.
- *Sigmoid* σ(f) = 1/(1 + e^(−f)) turns a score into a probability between 0 and 1. With it, log(1 + e^(−f)) = −ln σ(f).

**Claim 1: false.** In Z, three pairwise classifiers vote, and you can get "C1 beats C2, C2 beats C3, C3 beats C1": a three-way tie that needs a rule to break it (`verify.py` finds such cycles). But Y is a *cascade*. The first classifier decides "C1 or not", and only if the answer is "not" does the second decide C2 vs C3. Every patient gets exactly one label, so no post-processing is needed. The claim says "Y *and* Z", so it is false.

In Jan 18, Y was two independent classifiers that could contradict each other. Making Y a cascade is exactly what flips this claim.

**Claim 2: false.** "Strictly greater on any dataset" falls to a single counterexample: a dataset that Y's two boundaries classify perfectly. Z can't beat 100%.

**Claim 3: true.** X is one score with two cut-offs, so classes 1 < 2 < 3 are ordered along one line. Squared loss treats the class number as a target, so predicting 3 for a class-1 patient costs (3 − 1)² = 4, more than predicting 2 (cost 1); it naturally respects the order. Hinge loss is built for two classes (±1) and has no notion of how far apart classes are.

On outliers: a point with margin −5 costs (1 − (−5))² = 36 under squared loss but only 1 − (−5) = 6 under hinge loss, so one bad point pulls a squared-loss model much harder.

**Claim 4: false.** This is the reverse of the outlier comparison above: squared loss grows like distance², hinge loss like distance. Squared loss even penalises points that are *too* correct: margin 3 costs (1 − 3)² = 4.

**Claim 5: true.** Take a group of identical-looking patients, 70% of whom are positive. The average logistic loss of predicting probability q is −0.7 ln q − 0.3 ln(1 − q):

| q | 0.6 | 0.7 | 0.8 |
|---|---|---|---|
| average logistic loss | 0.632 | **0.611** | 0.639 |

It is lowest at q = 0.7, the true rate, which is what makes logistic outputs calibrated. Hinge loss behaves differently: the average 0.7·max(0, 1 − f) + 0.3·max(0, 1 + f) is lowest at f = 1 whether the true rate is 0.6, 0.7 or 0.9. Hinge loss learns which side a patient is on, not how likely they are to be positive.

**Claim 6: false**, since Claims 3 and 5 hold.

Answer: **options 3 and 5**.

**What to remember:** *M15 Linear-classifier mechanics*, together with *M10 Kill options with counterexamples*. Know three facts cold: squared loss is sensitive to outliers (it grows quadratically); hinge loss gives a boundary but no probabilities; logistic loss is minimised by the true probability. For claims about architectures, trace one example through the system.

**Common trap:** ticking Claim 1 from memory of Jan 18. Read how Y is defined this time.

</details>

---

### B1 Q7 Expected misclassification cost (2 pts)

<details><summary>Hint 1: understand the question</summary>

The cost needs the full 3×3 table of counts (actual class × predicted class). Which cells can you fill in straight away?

</details>

<details><summary>Hint 2: the key idea</summary>

Each actual-class row must add up to that class's size. The sensitivities give the diagonal and the two "egregious" counts give two corners. Then one specificity splits the last row.

</details>

<details><summary>Hint 3: set it up</summary>

- Row C1 (500): 420 correct and 25 sent to ICU, so 55 go to the ward.
- Row C3 (150): 120 correct and 10 sent home, so 20 go to the ward.
- Row C2 (350): 245 correct, leaving 105 errors split between "home" and "ICU". Specificity₁ = 0.90 tells you how many non-C1 patients were sent home.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: sizes and the diagonal.** The class sizes are 500, 350 and 150. The diagonal (sensitivity × size) is 420, 245 and 120.

**Step 2: rows C1 and C3**, as in Hint 3.

**Step 3: row C2.** Specificity₁ = 0.90, so of the 500 non-C1 patients, 10% = 50 were predicted C1 (sent home). Ten of those are from C3, so 40 are from C2. That leaves 105 − 40 = 65 C2 patients sent to the ICU.

| Actual \ Predicted | C1 | C2 | C3 | Total |
|---|---|---|---|---|
| C1 | 420 | 55 | 25 | 500 |
| C2 | 40 | 245 | 65 | 350 |
| C3 | 10 | 20 | 120 | 150 |

**Step 4: weight by cost.** 55×10 + 25×100 + 40×50 + 65×20 + 10×500 + 20×100 = 550 + 2500 + 2000 + 1300 + 5000 + 2000 = 13,350. Per patient that is 13.35, so ⌊x⌋ = **13**.

**Robustness.** As noted in Q1, the specificities are rounded, so this isn't the only table that fits the data. If you split row C2 using specificity₃ instead (C2→C3 = 93.5 − 25 = 68.5, C2→C1 = 36.5), the cost is 13.245. Every reasonable completion rounds down to 13.

**What to remember:** *M3 Fill the whole table.* Rows of actual classes must add up to the class sizes. Sensitivities give the diagonal, and specificities pin down the column totals. Once the 3×3 table is full, any cost or benefit question is just a weighted sum.

**Common trap:** mixing the two conventions. The background confusion matrix puts *predicted* classes in rows ($F_{C_i,C_j}$ means actual $C_j$ predicted as $C_i$), but the cost table puts *actual* classes in rows. Label your table "actual \ predicted" before multiplying. If you transpose it, you get 23.

</details>

---

### B2 Q1 DCG@5 calculation (1 pt)

<details><summary>Hint 1: understand the question</summary>

DCG adds up each chocolate's relevance divided by a discount that depends on its position. What are the relevances of the five chocolates, in this order?

</details>

<details><summary>Hint 2: the key idea</summary>

Write out the discount log₂(i + 1) for positions i = 1 to 5, then make a three-row table: position, relevance, discount.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Definition.** log₂ n is the power you raise 2 to in order to get n. For example, log₂ 4 = 2 because 2² = 4, and log₂ 3 ≈ 1.585.

**Step 1: relevances.** In the order D5, D3, D1, D9, D8 they are 3, 0, 10, 2, 5.

**Step 2: discounts.** log₂ 2, log₂ 3, log₂ 4, log₂ 5, log₂ 6 = 1, 1.585, 2, 2.322, 2.585.

**Step 3: add up.** DCG@5 = 3/1 + 0/1.585 + 10/2 + 2/2.322 + 5/2.585 = 3 + 0 + 5 + 0.861 + 1.934 = 10.796, so ⌊DCG@5⌋ = **10**.

**What to remember:** *M12 Ranking-metric mechanics.* Make a table of position, relevance and discount, then add relevance ÷ discount. Memorise log₂ 3 ≈ 1.585, log₂ 5 ≈ 2.32 and log₂ 6 ≈ 2.585.

**Common trap:** dividing by log₂ i instead of log₂(i + 1) (position 1 would then divide by 0), or using the natural log.

</details>

---

### B2 Q2 Comparison of ranking strategies (1 pt)

<details><summary>Hint 1: understand the question</summary>

Precision@8 and recall@8 both start from the same count: how many relevant chocolates land in the top 8. What is that count under each strategy?

</details>

<details><summary>Hint 2: the key idea</summary>

Rank all 10 chocolates under each strategy, breaking ties by the lower ID. Then count the relevant ones in the first eight.

</details>

<details><summary>Hint 3: set it up</summary>

Under Strategy A, four chocolates score 2 (which ones?). The other six tie at 0 and go in ID order.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: classify the chocolates.**
- Both Cocoa and Hazelnut: D1, D2, D5, D8.
- Exactly one of them: D3 (C), D4 (H), D7 (C), D9 (H), D10 (H).
- Neither: D6.
- Relevant: D1, D5, D8, D9, so R = 4.

**Step 2: Strategy A.** The ranking is D1, D2, D5, D8 (score 2), then D3, D4, D6, D7, D9, D10 (score 0, in ID order). The top 8 are D1, D2, D5, D8, D3, D4, D6, D7, which contain 3 relevant chocolates (D1, D5, D8). P@8 = 3/8 and R@8 = 3/4.

**Step 3: Strategy B.** The ranking is D1, D2, D5, D8 (score 2), then D3, D4, D7, D9, D10 (score 1), then D6 (score 0). The top 8 are D1, D2, D5, D8, D3, D4, D7, D9, which contain 4 relevant chocolates. P@8 = 4/8 and R@8 = 4/4.

**Step 4: compare.** B raises both precision and recall: **option 4**.

**What to remember:** *M12 Ranking-metric mechanics.* At a fixed k, precision and recall share the same numerator (relevant chocolates in the top k), so they always move together. One can rise while the other falls only when k changes.

**Common trap:** missing that D9 gets into the top 8 only under B, because D6 drops to a score of 0. Under A, D6 and D9 tie at 0, and D6 wins on ID.

</details>

---

### B2 Q3 Maximising DCG (2 pts)

<details><summary>Hint 1: understand the question</summary>

Which chocolate do you most want in position 1, where the discount is smallest?

</details>

<details><summary>Hint 2: the key idea</summary>

Look at two neighbouring positions. If a more relevant chocolate sits behind a less relevant one, does swapping them raise DCG?

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: relevances.** D1 = 10, D8 = 5, D5 = 3, D9 = 2.

**Step 2: the swap argument.** Take positions i < j with discounts $d_i < d_j$, and put relevance a at i and b at j. The DCG contribution is a/d_i + b/d_j. Swapped, it is b/d_i + a/d_j. The difference (original − swapped) is (a − b)(1/d_i − 1/d_j). Since 1/d_i > 1/d_j, the original order is better exactly when a > b. So the most relevant chocolate should always come first: sort by relevance, giving D1, D8, D5, D9 = **option 3**.

**Step 3: check.** 10/1 + 5/1.585 + 3/2 + 2/2.322 = 10 + 3.155 + 1.5 + 0.861 = 15.516. The closest rival is option 5, with D5 and D9 swapped, at 15.447.

**What to remember:** *M12 Ranking-metric mechanics.* DCG is maximised by sorting in decreasing relevance, because swapping any out-of-order pair always helps. Use the relevance values, not just relevant vs not relevant.

**Common trap:** option 1, [D1, D5, D8, D9], which is sorted by chocolate ID rather than by relevance.

</details>

---

### B2 Q4 Optimal scoring function (3 pts)

<details><summary>Hint 1: understand the question</summary>

Precision@3 = (relevant chocolates in the top 3) ÷ 3. For each scoring function, which three chocolates come out on top?

</details>

<details><summary>Hint 2: the key idea</summary>

Make one table with a row per chocolate and a column per scoring function. Compute all 40 numbers, then read off each top 3 using the ID tie-break.

</details>

<details><summary>Hint 3: set it up</summary>

min(1, w_i) = 1 for every weight here, so Score_B simply counts how many ingredients a chocolate has.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the score table** (W = 3, 3, 1, 1; Σd = number of ingredients).

| Chocolate | C H K M | A = Σd·w | B = Σd | C = A − Σd | D = A/(1 + Σd) | Relevance |
|---|---|---|---|---|---|---|
| D1 | 1 1 0 0 | 6 | 2 | 4 | 2 | 10 |
| D2 | 1 1 1 1 | 8 | 4 | 4 | 1.6 | 0 |
| D3 | 1 0 1 1 | 5 | 3 | 2 | 1.25 | 0 |
| D4 | 0 1 1 1 | 5 | 3 | 2 | 1.25 | 0 |
| D5 | 1 1 0 1 | 7 | 3 | 4 | 1.75 | 3 |
| D6 | 0 0 1 1 | 2 | 2 | 0 | 0.67 | 0 |
| D7 | 1 0 0 0 | 3 | 1 | 2 | 1.5 | 0 |
| D8 | 1 1 0 0 | 6 | 2 | 4 | 2 | 5 |
| D9 | 0 1 1 0 | 4 | 2 | 2 | 1.33 | 2 |
| D10 | 0 1 0 0 | 3 | 1 | 2 | 1.5 | 0 |

**Step 2: the top 3 under each function.**
- A: D2 (8), D5 (7), D1 (6, ahead of D8 on ID). 2 relevant, so 2/3.
- B: D2 (4), then D3 and D4 (3, ahead of D5 on ID). 0 relevant, so 0/3.
- C: a four-way tie at 4 (D1, D2, D5, D8); ID order gives D1, D2, D5. So 2/3.
- D: D1 (2), D8 (2), D5 (1.75). 3 relevant, so 3/3.

Answer: **Score_D only (option 4)**.

Why D wins: dividing by (1 + number of ingredients) penalises "everything" chocolates like D2, which score high on raw sums but have no ticket.

**What to remember:** *M12 Ranking-metric mechanics.* Build the full score table once, then apply the tie-break exactly as written. Normalising by size (as Score_D does) stops items that "have everything" from dominating.

**Common trap:** forgetting D2 in Score_C's four-way tie. If you take D1, D5, D8, C looks as good as D; but D2 has a lower ID than D5 and D8, so it takes a top-3 slot.

</details>

---

### B2 Q5 Position-based inspection effects (3 pts)

<details><summary>Hint 1: understand the question</summary>

PI-Recall@5 counts only relevant chocolates in the top 5, but weights each by the chance Charlie actually looks at its position. What is the Score_A ranking?

</details>

<details><summary>Hint 2: the key idea</summary>

You already computed Score_A in Q4. List the top 5 with their positions and inspection probabilities, then divide by the total number of relevant chocolates.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the ranking.** Score_A with ties by ID: D2 (8), D5 (7), D1 (6), D8 (6), D3 (5), D4 (5), … The top 5 are D2, D5, D1, D8, D3.

**Step 2: weighted hits.** The relevant chocolates sit at positions 2, 3 and 4 (D5, D1, D8). Their inspection probabilities are 0.6, 0.4 and 0.2, which sum to 1.2.

**Step 3: divide by R.** There are R = 4 relevant chocolates in total (D1, D5, D8, D9). PI-Recall@5 = 1.2/4 = 0.30, so ⌊100 × 0.30⌋ = **30**.

**What to remember:** *M12 Ranking-metric mechanics.* PI-Recall weights each hit by how likely the user is to see it, then divides by *all* relevant items, including ones outside the top k like D9. The answer lands exactly on an integer (30), so compute with fractions (12/40) rather than rounded decimals.

**Common trap:** dividing by the number of relevant chocolates in the top 5 (3) instead of R = 4, which gives 40.

</details>

---

### B3 Q1 Convolution with custom kernel (1 pt)

<details><summary>Hint 1: understand the question</summary>

The background box says convolution has three steps. Which one is easiest to forget? And how many outputs should you get with padding 1, a kernel of length 2 and stride 2?

</details>

<details><summary>Hint 2: the key idea</summary>

First write out the padded series. Then reverse the kernel. Then slide it two places at a time.

</details>

<details><summary>Hint 3: set it up</summary>

Padded series: [2, 1, 3, 2, 4, 2]. Reversed kernel: [1, 2]. The windows start at positions 1, 3 and 5.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: pad with the value 2 (not 0).** [2, 1, 3, 2, 4, 2].

**Step 2: reverse h = [2, 1].** You get [1, 2].

**Step 3: slide with stride 2** over positions 1–2, 3–4 and 5–6:
- [2, 1]: 1×2 + 2×1 = 4
- [3, 2]: 1×3 + 2×2 = 7
- [4, 2]: 1×4 + 2×2 = 8

y = [4, 7, 8], which is **A**.

**What to remember:** *M1 Read the definition, not your memory.* This paper's convolution reverses the kernel, as its own worked example shows. Write the padded series out in full, then slide.

**Common trap:** each slip lands on a listed option. Not reversing gives [5, 8, 10] (C); padding with 0 instead of 2 gives [2, 7, 4] (B).

</details>

---

### B3 Q2 Signal smoothness vs fluctuations (2 pts, select all)

<details><summary>Hint 1: understand the question</summary>

"Constant signal → S = 0" is a condition on the kernel alone. What must the three kernel numbers add up to? Which options survive that test?

</details>

<details><summary>Hint 2: the key idea</summary>

Instead of computing every $y_i$, write S = y₁ + y₂ + y₃ for a general signal [x₁, …, x₅] and count how many times each x appears. Most terms cancel.

</details>

<details><summary>Hint 3: set it up</summary>

For h = [1, −2, 1]: y₁ = x₁ − 2x₂ + x₃, y₂ = x₂ − 2x₃ + x₄, y₃ = x₃ − 2x₄ + x₅. Add them up.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: constant signals.** If every x equals c, each output is c(h₁ + h₂ + h₃), so the kernel must sum to 0. B [2, −3, 2] sums to 1, so it's out. All the others sum to 0.

**Step 2: the telescoping trick.** For D [1, −2, 1], adding the three outputs gives S = x₁ − x₂ − x₄ + x₅ = (x₅ − x₄) − (x₂ − x₁), i.e. the last step minus the first step. Every middle value cancels, because each one meets all three kernel numbers once and they sum to 0. This kind of cancellation is called *telescoping*.
- x = [2, 4, 6, 8, 10]: S = (10 − 8) − (4 − 2) = 0, small ✓.
- z = [2, 6, 3, 10, 4]: S = (4 − 10) − (6 − 2) = −10, large ✓.

F [−2, 4, −2] is −2 × D, so S(x) = 0 and S(z) = 20 ✓.

**Step 3: the others.** With the reversal, $y_i = h_1x_{i+2} + h_2x_{i+1} + h_3x_i$.

| Kernel | S simplifies to | S(x) | S(z) | Verdict |
|---|---|---|---|---|
| A [1, 0, −1] | (x₄ + x₅) − (x₁ + x₂) | 12 | 6 | the smooth signal scores higher ✗ |
| C [1, 1, −2] | (2x₄ + x₅) − (2x₁ + x₂) | 18 | 14 | the smooth signal scores higher ✗ |
| E [0, −1, 1] | x₁ − x₄ | −6 | −8 | measures only net rise ✗ |

E needs a closer look. Its sizes (6 vs 8) barely differ, and S = x₁ − x₄ only measures how much the signal rose. A steeper smooth ramp such as [2, 5, 8, 11, 14] gives S = −9, bigger than z's. E detects trend, not fluctuation.

Answer: **D and F**.

**What to remember:** *M11 Kernels telescope.* When you add up all outputs of a zero-sum kernel, the middle of the signal cancels and only the edges remain. Write S in terms of the first and last values and each option takes seconds. A kernel and its multiples (D and F) behave alike, so in "select all" questions, look for pairs.

**Common trap:** ticking E because 8 > 6. An "is z bigger?" test isn't enough; the smooth signal must give a *small* S, and E's S grows with the slope.

</details>

---

### B3 Q3 Signal acceleration (2 pts, select all)

<details><summary>Hint 1: understand the question</summary>

"Constant velocity → S = 0" must hold for *every* straight-line signal, such as [0, 1, 2, 3, 4] and [5, 5, 5, 5, 5]. What two conditions does that put on the kernel?

</details>

<details><summary>Hint 2: the key idea</summary>

Use the telescoping from Q2. Which kernel's S turns into "last step − first step"? Then check the sign on the decelerating and accelerating signals.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: straight lines.** Constant signals need h₁ + h₂ + h₃ = 0, and the ramp [0, 1, 2, 3, 4] must also give S = 0. This eliminates three options:
- D [0, 1, −2] sums to −1, so it fails on constants.
- A [−1, 0, 1]: $y_i = x_i - x_{i+2}$ = −2 on the ramp at every position, so S = −6 ✗.
- C [1, −1, 0]: $y_i = x_{i+2} - x_{i+1}$ = the velocity = 1, so S = 3 ✗.

The survivors B, E and F are all multiples of [1, −2, 1].

**Step 2: the sign.** From Q2, [1, −2, 1] gives S = (last step) − (first step).
- x is decelerating, with steps 4, 3, 2, 1: S = 1 − 4 = −3 < 0 ✓.
- w is accelerating, with steps 1, 2, 3, 4: S = 4 − 1 = 3 > 0 ✓.

So E works, and F = 3E gives −9 and 9 ✓. B = −E flips both signs ✗.

Answer: **E and F**.

**What to remember:** *M11 Kernels telescope.* [1, −2, 1] is the *second difference* ("the change in the change"), and summed over a signal it becomes last step − first step. Positive multiples keep the sign; negative multiples flip it.

**Common trap:** B [−1, 2, −1] passes the constant-velocity test but has the wrong sign.

</details>

---

### B3 Q4 Spike detection (2 pts, select all)

<details><summary>Hint 1: understand the question</summary>

$S^{abs}$ adds absolute values, so nothing can cancel between positions. For the smooth z to give $S^{abs}$ = 0, what must every single $y_i$ be?

</details>

<details><summary>Hint 2: the key idea</summary>

Every $y_i$ must be 0 on any straight line, constant or ramp. Try a general kernel [h₁, h₂, h₃] on [1, 1, 1] and on [0, 1, 2], and see what conditions you get.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: each output must vanish on straight lines.** On constants this needs h₁ + h₂ + h₃ = 0. On a ramp $x_i = i$: $y_i = h_1(i + 2) + h_2(i + 1) + h_3 i = (h_1 + h_2 + h_3)i + (2h_1 + h_2)$, so you also need 2h₁ + h₂ = 0. Together these give h₂ = −2h₁ and h₃ = h₁: the kernel must be a multiple of [1, −2, 1].

**Step 2: check the options.** E [−1, 2, −1] and F [1, −2, 1] are multiples. A, B, C and D are not. For example, A gives 6 at every position on z, and C gives 2 at every position.

**Step 3: check the spike.** F on x = [1, 2, 8, 2, 1, 2], using $y_i = x_{i+2} - 2x_{i+1} + x_i$: the outputs are 8 − 4 + 1 = 5, 2 − 16 + 2 = −12, 1 − 4 + 8 = 5 and 2 − 2 + 2 = 2. So $S^{abs}$ = 5 + 12 + 5 + 2 = 24, which is large ✓. E gives the same absolute values.

Answer: **E and F**.

**What to remember:** *M11 Kernels telescope*, and its partner rule: with absolute values nothing telescopes, so each output must vanish on its own. Being zero on every straight line forces the kernel to be a multiple of [1, −2, 1]. The absolute value hides the sign of the multiple, so both E and F work.

**Common trap:** A [1, 1, −2] and C [2, −3, 1] sum to 0, so they kill constants. But they don't kill ramps: on z they give 6 and 2 at every position.

</details>

---

### B3 Q5 Symmetry detection (3 pts, select all)

<details><summary>Hint 1: understand the question</summary>

A length-4 kernel on a length-4 signal gives just one output. Write that one number in terms of x₁, x₂, x₃ and x₄ (remember the reversal).

</details>

<details><summary>Hint 2: the key idea</summary>

Every symmetric signal has the form [a, b, b, a]. Plug that in and ask when the output is 0 for every a and b.

</details>

<details><summary>Hint 3: set it up</summary>

y = h₁x₄ + h₂x₃ + h₃x₂ + h₄x₁. With x = [a, b, b, a], this becomes y = (h₁ + h₄)a + (h₂ + h₃)b.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the single output.** y = h₁x₄ + h₂x₃ + h₃x₂ + h₄x₁.

**Step 2: symmetric signals.** For [a, b, b, a], y = (h₁ + h₄)a + (h₂ + h₃)b. This is 0 for every a and b only if h₄ = −h₁ and h₃ = −h₂. Such a kernel is *anti-symmetric*: reading it backwards flips every sign.

**Step 3: check the options.**

| Option | h₁ + h₄ | h₂ + h₃ | y on z = [1, 2, 3, −1] | Passes? |
|---|---|---|---|---|
| A [1, 1, 1, −1] | 0 | 2 | | ✗ |
| B [1, −1, 1, −1] | 0 | 0 | −1 − 3 + 2 − 1 = −3 | ✓ |
| C [−1, 2, 1, 1] | 0 | 3 | | ✗ |
| D [2, 1, −1, −2] | 0 | 0 | −2 + 3 − 2 − 2 = −3 | ✓ |
| E [1, −1, −1, 0] | 1 | −2 | | ✗ |
| F [1, 0, 0, −1] | 0 | 0 | −1 + 0 + 0 − 1 = −2 | ✓ |

Answer: **B, D and F**.

**A note on "asymmetric → y ≠ 0".** No single kernel can promise y ≠ 0 for *every* asymmetric signal. One output number can't track two separate mismatches (x₁ vs x₄ and x₂ vs x₃) at once. For example, F only compares x₁ with x₄, so [1, 0, 5, 1] gives 0 even though it isn't symmetric. The output box asks for kernels that output zero on symmetric signals, so judge the options on that, plus the nonzero output on z.

**What to remember:** *M10 Kill options with counterexamples.* Plug a *general* symmetric signal [a, b, b, a] into the output formula; the condition on the kernel (anti-symmetry) drops out in one line, and one look at each option finishes the job.

**Common trap:** expecting a symmetry detector to be a *symmetric* kernel. A symmetric kernel gives y = 2h₁a + 2h₂b, which is not 0. It is the anti-symmetric kernel that cancels symmetric signals.

</details>

---

### B4 Q1 Reverse engineering the weights (4 pts)

<details><summary>Hint 1: understand the question</summary>

Each of X's first four rows contains a single 1. What does that tell you about s₁, s₂, s₃, s₄ and the weights?

</details>

<details><summary>Hint 2: the key idea</summary>

Read off the weights you can directly, then use a row with two or three 1s to find the missing one. Fill in the "?" scores and apply the rule "predict 1 only if the score is > 0".

</details>

<details><summary>Hint 3: set it up</summary>

For $s^{(A)}$: w₁ = 2, w₃ = −1 and w₄ = −1, and row 5 says w₁ + w₂ = −1.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: what s = Xw means.** $s_i$ is the sum of the weights wherever row i of X has a 1. Rows 1–4 pick out w₁, …, w₄ individually; row 5 gives w₁ + w₂; row 6 gives w₁ + w₃ + w₄.

**Step 2: option A.** s = [2, ?, −1, −1, −1, ?], so w₁ = 2, w₃ = −1 and w₄ = −1. Row 5: 2 + w₂ = −1, so w₂ = −3. The missing scores are s₂ = −3 and s₆ = 2 − 1 − 1 = 0.

The predictions are [1, 0, 0, 0, 0, 0] against labels y = [1, 0, 0, 0, 0, 1]. Example 6 scores exactly 0, which predicts class 0, but y = 1. Accuracy 5/6.

**Step 3: option B.** s = [3, −5, ?, −1, ?, 1], so w₁ = 3, w₂ = −5 and w₄ = −1. Row 6: 3 + w₃ − 1 = 1, so w₃ = −1. The missing scores are s₃ = −1 and s₅ = 3 − 5 = −2.

The predictions are [1, 0, 0, 0, 0, 1] = y. Accuracy 6/6.

**Step 4: the answer.** $w^* = (3, -5, -1, -1)$, so $\lVert w^* \rVert^2 = 9 + 25 + 1 + 1$ = **36**.

**What to remember:** *M15 Linear-classifier mechanics.* A score is the sum of the weights an example "switches on". Rows with a single 1 hand you weights directly; then use the mixed rows. The threshold is strict: a score of exactly 0 is class 0.

**Common trap:** counting A's example 6 (score 0) as correct. Both options then reach 6/6, and "choose the option with higher accuracy" no longer has an answer. Also check what is asked: ‖w‖² here, not the ℓ1 norm from Jan 18 (which would be 10).

</details>

---

### B4 Q2 Finding the optimal pruning strategy (3 pts)

<details><summary>Hint 1: understand the question</summary>

Before pruning anything, what is each example's score, and how accurate is the model? Which examples are "on the edge", with a score near 0?

</details>

<details><summary>Hint 2: the key idea</summary>

Look at w₇. What does pruning feature 7 change? Then work out what pruning one more feature does to its own example and to example 7, which uses every feature.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the original scores.** Because w₇ = 0, column 7 never matters (that's why the problem says at least one weight is 0).
- Examples 1–5: (−1)(−1) = 1 > 0, so they predict 1 ✓.
- Example 6: 1 × 1 = 1, so it predicts 1 ✓.
- Example 7: five terms of 1 × (−1) plus 5 × 1 gives −5 + 5 = 0, so it predicts 0 ✓ (y = 0).

The accuracy is 7/7, so pruning can only make things worse. The goal is to lose as little as possible.

**Step 2: what removing each feature does.**
- Feature 7: nothing changes (w₇ = 0).
- Feature j ∈ {1, …, 5}: example j drops from 1 to 0 and now predicts 0 ✗. Example 7 loses a −1 term, rises to 1 and predicts 1 ✗. Cost: 2 examples.
- Feature 6: example 6 drops to 0 ✗. Example 7 loses its +5 and falls to −5, still class 0 ✓. Cost: 1 example.

**Step 3: pick the pair.** Two features must go. The best pair is {6, 7}, which loses only example 6, for 6/7. Every other pair loses at least 2. So $j^* + k^*$ = **13**.

**What to remember:** *M15 Linear-classifier mechanics.* Pruning feature j changes only the examples where feature j is nonzero, and by exactly $w_j x_{ij}$. List who gets hurt for each feature; a zero weight is a free prune.

**Common trap:** reporting the product (42) out of habit. Jan 18 asked for $j^* \cdot k^*$; this paper asks for the sum.

</details>

---

### B4 Q3 Bias correction for improved performance (3 pts)

<details><summary>Hint 1: understand the question</summary>

After pruning {6, 7}, which example is wrong, and which way does its score need to move? Could shifting every score by the same b break an example that is currently right?

</details>

<details><summary>Hint 2: the key idea</summary>

For each example, write the range of b that makes it correct, using the strict rule "> 0 means class 1". Then intersect the ranges.

</details>

<details><summary>Hint 3: set it up</summary>

The pruned scores are [1, 1, 1, 1, 1, 0, −5]. Examples 1–5 need 1 + b > 0, example 6 needs 0 + b > 0, and example 7 needs −5 + b ≤ 0.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: one condition per example** (b is an integer).
- Examples 1–5 (y = 1): 1 + b > 0, so b ≥ 0.
- Example 6 (y = 1): b > 0, so b ≥ 1.
- Example 7 (y = 0): −5 + b ≤ 0, so b ≤ 5.

**Step 2: intersect.** b = 1, 2, 3, 4 and 5 all give 7/7. (b = 0 gives 6/7, and any negative b gives 1/7.)

**Step 3: apply the tie-break.** "Choose the largest b" gives $b^*$ = 5. At b = 5, example 7 scores exactly 0, which is class 0, so it's still correct.

**Step 4: the answer.** $(j^* + k^*) \times |b^*|$ = 13 × 5 = **65**.

**What to remember:** *M15 Linear-classifier mechanics*, plus *M1 Read the definition, not your memory.* A shared bias shifts every score by the same amount: turn each example into an inequality on b and intersect them. Then apply the tie-break rule exactly as written.

**Common trap:** using Jan 18's tie-break (smallest |b|), which gives $b^*$ = 1 and an answer of 13. Or thinking b = 5 fails because example 7's score becomes 0; a score of 0 is class 0, which is correct.

</details>

---

## Where this paper differs from Jan 18

- **Formulas were quietly rewired, so read them instead of pattern-matching.** In the catalyst problem, the substrate amounts now multiply $c^2$ ($d_A = 10c_A - a\,c_A^2$) instead of being linear coefficients. In V-67, the mutant rate grows with the day (2 + 4t), and the question asks for $R_3$, which never needs the last day's infections. The crude curve uses a cosine instead of a sine and adds a downward ramp after month 42. The pit-stop problem conditions on a safety car instead of rain and asks about "neither pitted".
- **The godown and knight problems keep their skeleton with new details.** Itakura–Saito replaces the generalised KL divergence, but both are minimised by the mean, so the answer is exactly 15. The knight board shrinks to 4×4: parity removes the even options, and the two "other" corners cap the path at 15 pads.
- **The LLM oracle changed, and so did the answer.** The model is now text-only, with web retrieval and the article body. Publication year (F2) becomes a lookup and article–headline consistency (F4) becomes reading comprehension. F is the only option without F4.
- **B1 needs more care.** Q1 needs counts, and the printed specificities are rounded, so the answer can be 43 or 42 depending on method. Q3 uses costs instead of a bed limit. Q4 is not a monotone transform, so this time the ROC curve does change. In Q6, Y is now a cascade, which makes Claim 1 false.
- **Several questions are "select all that apply".** These are B1 Q6 and B3 Q2–Q5. In B3, the right kernel usually appears alongside a scalar multiple of itself ([1, −2, 1] with [−2, 4, −2] or [3, −6, 3]), so expect pairs. The sign of the multiple matters only when S must be positive or negative (Q3), not when it must be zero or you take absolute values (Q4).
- **B4's traps sit on the boundaries.** Q1 asks for ‖w‖², and option A hides a score of exactly 0 (class 0). Q2 asks for $j^* + k^*$ instead of the product. Q3's tie-break now picks the *largest* b, and b = 5 works only because a score of exactly 0 counts as class 0.
