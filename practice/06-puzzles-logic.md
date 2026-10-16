# Set 06: Puzzles and logic

**Week 6** · 7 problems · target time 50 min · moves: M8, M10, M14, M17

> Write a **guess** in the margin before working anything out, then solve on paper. No computer, just like the exam: trace code by hand. Check answers in `notebooks/06_puzzles_logic.ipynb` (spoiler-free checker). Read `solutions/06-puzzles-logic.md` only after you've checked.

---

### 6.1 Robot vacuum parity [3 pts]

A robot vacuum cleans a room divided into a 5 × 5 grid of cells. Cells are labelled (row, column), from (0, 0) in the top-left corner to (4, 4) in the bottom-right corner.

- Each move takes the robot one cell up, down, left or right. There are no diagonal moves.
- It never enters a cell it has already visited.
- It starts at (0, 0) and must finish at its charging dock at (0, 1), right next to the start.

**Output:** The maximum number of cells the robot can visit, counting both the start cell and the end cell.

---

### 6.2 Trace the loop [2 pts]

Trace this code by hand. Don't run it.

```python
x = 0
for i in range(1, 6):
    for j in range(i, 6):
        if (i + j) % 3 == 0:
            x += i * j
        else:
            x -= 1
print(x)
```

**Output:** What is printed?

---

### 6.3 Design a path-quality score [3 pts]

A delivery robot gives each candidate path a quality score $Q(d, n)$. Here $d \ge 0$ is the path length in metres (any real number) and $n \ge 0$ is the number of turns (a whole number). The team wants $Q$ to obey four rules:

- **R1.** $Q = 1$ if and only if $d = 0$ and $n = 0$.
- **R2.** $0 < Q \le 1$ always.
- **R3.** $Q$ strictly decreases when $d$ increases (with $n$ fixed), and when $n$ increases (with $d$ fixed).
- **R4.** One extra turn costs exactly as much as 2 extra metres: $Q(d, n+1) = Q(d+2, n)$ for all $d$ and $n$.

> **Background:** "X if and only if Y" makes two promises: if Y is true then X is true, **and** if X is true then Y is true. "Strictly decreases" means the value gets smaller; staying the same is not allowed. $e \approx 2.718$. The function $e^x$ is always positive, $e^0 = 1$, and $e^x$ gets bigger as $x$ gets bigger.

**Output (select all that apply):** Which formulas satisfy all four rules?

- **A.** $Q = \dfrac{1}{1 + d + 2n}$
- **B.** $Q = e^{-(d + n/2)}$
- **C.** $Q = 1 - \dfrac{d + 2n}{10}$
- **D.** $Q = e^{-d} \cdot e^{-2n}$
- **E.** $Q = \dfrac{1}{1 + 2dn}$
- **F.** $Q = \dfrac{2}{1 + e^{d + 2n}}$

---

### 6.4 Which cards to flip? [2 pts]

An AI lab keeps one card for each model it has trained. One side of a card says whether the model was **Deployed** or **Not deployed**. The other side says whether it **Passed** or **Failed** the safety test.

The lab's rule: **"If a model is deployed, then it passed the safety test."**

Four cards lie on the table. You can see one side of each:

| Card | A | B | C | D |
|---|---|---|---|---|
| Visible side | Deployed | Not deployed | Passed | Failed |

**Output:** Which cards must you turn over to check whether these four models follow the rule? Give the smallest set that is guaranteed to catch any violation.

---

### 6.5 Decode the robot language [3 pts]

Here are five sentences in an invented robot language, with their English translations.

| | Robot language | English |
|---|---|---|
| (1) | robo veln mor | The robot builds the car. |
| (2) | mina robon taki | The girl saw the robot. |
| (3) | karobo minan tak | The robots see the girl. |
| (4) | mina kaveln mori | The girl built the cars. |
| (5) | robo minan taki | The robot saw the girl. |

**Output:**
(a) Which of these means "The robots built the car."?

- **A.** karobo veln mori
- **B.** robo kaveln mori
- **C.** karobo veln mor
- **D.** karobon vel mori
- **E.** veln karobo mor
- **F.** karobo kaveln mori

(b) Translate into the robot language: "The girls saw the cars."

---

### 6.6 Find the rule [2 pts]

A hidden function $f$ takes a string of bits (0s and 1s) and returns a whole number:

| Input | 0110 | 1111 | 1010 | 0001 | 1001 |
|---|---|---|---|---|---|
| $f$ | 2 | 0 | 3 | 1 | 2 |

**Output:** $f(0101101)$. One simple rule fits all five examples. Make sure yours does.

---

### 6.7 LLM reality check [3 pts]

You run a small LLM offline on a laptop. It has no internet and no tools: no calculator, no code execution and no search. You type each task below in as a prompt.

**Output (select all that apply):** Which tasks is it most likely to get **wrong**?

- **A.** Count how many times the letter "r" appears in "strawberry".
- **B.** Label a product review as positive or negative.
- **C.** Translate "good morning" into Hindi.
- **D.** Report the final score of yesterday's cricket match.
- **E.** Summarise a paragraph you give it.
- **F.** Detect whether a headline contains a quotation.
