# INAIO 2026 Stage 1 (18 Jan): Solutions (unofficial)

Unofficial: computed by us and checked numerically with `verify.py`. No official key has been published (as of Oct 2026).

> **Spoiler warning.** Take the paper timed (2 h) first. Grade with the answer table, then re-attempt every miss using the hint ladders before opening a full solution.

## Answer table

| Section | Question | Points | Answer |
|---|---|---|---|
| A1 | Cracking the Imperial Glyphs | 3 | **A** 樹造宮美 |
| A1 | Filtering Fakes with Faulty Oracle | 3 | **B** {F1, F2, F6} |
| A1 | Smart Student Search | 3 | **C** |
| A1 | Recursive V-67 Outbreak | 3 | **C** 281 |
| A1 | Pikachu's Path to Victory | 3 | **E** 25 |
| A2 | The Phulera Godown Showdown | 3 | **11** |
| A2 | The Blind Board Gambit | 3 | **43** |
| A2 | The Crude Curve Forecast | 3 | **92** |
| A2 | The Catalyst Constraint | 3 | **69** |
| A2 | The Pit-Stop Paradox | 3 | **86** |
| B1 | Q1 Missed ICU patients | 1 | **20** |
| B1 | Q2 Outpatient triaging | 1 | **85** |
| B1 | Q3 Operating point for ICU detection | 2 | **Option 3** (Point C) |
| B1 | Q4 Effect of score transformation | 1 | **Option 3** (unchanged) |
| B1 | Q5 Effect of distribution shift | 1 | **Option 3** (unchanged) |
| B1 | Q6 Designing an ordinal classifier | 2 | **Option 4** (Claims 1, 2, 4) \* |
| B1 | Q7 Triage benefits | 2 | **95** |
| B2 | Q1 Recall@k | 1 | **25** |
| B2 | Q2 Comparing ranking strategies | 1 | **Option 1** \* |
| B2 | Q3 Discounted cumulative gain | 2 | **Option 6** (none of the above) \* |
| B2 | Q4 Optimal scoring function | 3 | **Option 4** (Score_D only) |
| B2 | Q5 Position-based inspection | 3 | **27** |
| B3 | Q1 Convolution with custom kernel | 1 | **A** [8, 5, 11] |
| B3 | Q2 Smoothness vs fluctuations | 2 | **C** [1, −2, 1] |
| B3 | Q3 Signal acceleration | 2 | **C** [1, −2, 1] |
| B3 | Q4 Spikes in signals | 2 | **B** [−1, 2, −1] |
| B3 | Q5 Signal symmetry | 3 | **D** [1, −1, 1, −1] |
| B4 | Q1 Reverse engineering the weights | 4 | **5** |
| B4 | Q2 Optimal pruning | 3 | **42** |
| B4 | Q3 Bias correction | 3 | **43** |

Total: 70 points. \* = the question is ambiguous or arguable. The full solution explains the reading we used and why.

## Worked solutions

**How to use this.** Struggle for 10–15 minutes before opening Hint 1, then allow about 5 minutes between hints. If two hints don't unlock a question, the gap is in what you *know*, not in your effort: open the full solution, then go and do the practice problem it points to.

**Notation used all over the paper.** ⌊x⌋ ("floor of x") means round *down* to a whole number: ⌊86.52⌋ = 86 and ⌊92.0001⌋ = 92. So "report ⌊100x⌋" means "write x as a percentage and chop off the decimals". Every other term is defined inside the solution where it first matters.

---

### A1.1 Cracking the Imperial Glyphs

<details><summary>Hint 1: understand the question</summary>

You don't need to know any Chinese. Some English words appear in more than one sentence (apple, palace, tree, black, beautiful). Can you find the glyph that appears in exactly the same sentences as each of those words?

</details>

<details><summary>Hint 2: the key idea</summary>

Decode in two layers. First the **dictionary** (which glyph means which word). Then the **grammar**: compare "This is a *beautiful apple*" with "Does the tree make *the apple beautiful*?". Where does 美 (beautiful) go in each one, and why are they different?

</details>

<details><summary>Hint 3: set it up</summary>

Make a table with three columns: glyph, the rows it appears in, and the English word that appears in exactly those rows. Then write the target sentence by copying the pattern of the "Does the tree make the apple beautiful?" row and changing one word.

</details>

<details><summary>Answer</summary>

**A** 樹造宮美

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: build the dictionary by matching rows.** Number the six sentences 1–6 in the order given. For each glyph, list the rows it appears in, then find the English word that appears in exactly those rows.

| Glyph | Rows | English word in exactly those rows |
|---|---|---|
| 這 | 1, 2, 5 | "this is" / "there is" |
| 蘋果 | 1, 2, 3, 4 | apple (two glyphs for one word: the "no one-to-one correspondence" warning) |
| 樹 | 2, 4 | tree |
| 宮 | 3, 5, 6 | palace |
| 美 | 1, 4 | beautiful |
| 造 | 4 | make |
| 塗 | 6 | paint |
| 黑, 山 | 5, 6 (both!) | black, mountain |

The last row is the interesting one. 黑 and 山 appear in exactly the same rows, so matching rows can't tell them apart. Use **position** instead. In row 5 ("black mountain" = 黑山), the describing word comes first, just as in row 1 ("beautiful apple" = 美蘋果). So 黑 = black and 山 = mountain. Row 6 agrees: "The mountain paints…" starts with 山.

**Step 2: decode the grammar.** Now look at *where* words go, not just what they mean.
- **A describing word sits before its noun:** 美蘋果 (beautiful apple), 黑山 (black mountain), 綠蘋果 (green apples).
- **"X makes/paints Y into a state":** row 4 is 樹 造 蘋果 美 = tree · make · apple · beautiful. Row 6 is 山 塗 宮 黑 = mountain · paint · palace · black. The order is doer, action, thing acted on, *resulting state*. The result word comes **after** the object.
- **Questions:** row 4 has no glyph for "does". Only the ？ makes it a question, so the statement is the same string without ？.

**Step 3: build the target.** "The tree makes the palace beautiful" has exactly the shape of row 4, with apple swapped for palace:

樹 (tree) 造 (make) 宮 (palace) 美 (beautiful) → **A**.

**Step 4: check why each distractor is wrong.**
- B 宮造樹美: "the palace makes the tree beautiful" (doer and object swapped).
- C 樹美造宮: puts 美 between the doer and the action, which matches no pattern in the data.
- D 美樹造宮: "the beautiful tree makes a palace" (美 before 樹 describes the tree).
- E 樹造美宮: "the tree makes a *beautiful palace*". 美 before 宮 *describes* the palace, so this means the tree builds a palace that is beautiful. It is not the same as making an existing palace beautiful.
- F 宮美造樹: doer and object reversed again.

**What to remember:** *M17 Align and decode.* List the rows each symbol appears in and match it to the word with the same row pattern. When two symbols share a pattern, separate them by position. Decode the vocabulary first and the word order second. (Same move in new clothes: [practice set 06, problem 6.5](../../practice/06-puzzles-logic.md).)

**Common trap:** E (樹造美宮). It uses all the right words, but word order changes the meaning: before the noun, 美 *describes* it; after the object, 美 is the *result*.

</details>

---

### A1.2 Filtering Fakes with Faulty Oracle

<details><summary>Hint 1: understand the question</summary>

For each prompt, ask: can the model answer it just by *looking at* the headline and image in front of it? Or does it need something it doesn't have?

</details>

<details><summary>Hint 2: the key idea</summary>

Two facts about a small offline LLM:
1. It reads text as **tokens** (chunks of letters), not as individual letters.
2. It has **no internet** and a fixed training cutoff. Asked for a fact it doesn't know, it gives a confident guess instead of saying "I don't know".

Sort F1–F8 into "answer is in the input" and "needs letter-level access or outside facts".

</details>

<details><summary>Answer</summary>

**B** {F1, F2, F6}

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: two terms.**
- **Tokenization.** Before an LLM sees text, the text is chopped into *tokens*: common chunks of characters, each turned into a number. "Headline" might become ["Head", "line"], two tokens. The model sees the token numbers, not the letters inside them. So "count the characters" asks about something it can't directly see. This is why chatbots famously miscount the r's in "strawberry".
- **Hallucination.** When a model is asked something it doesn't know, it produces a plausible-sounding but invented answer instead of admitting it doesn't know.

**Step 2: go through the features one by one.**

| Feature | What it needs | Reliable from a small offline model? |
|---|---|---|
| F1 character count | exact letter-level counting | **No.** Tokenization hides the letters. |
| F2 publication year | knowing when the event happened, which may be after the training cutoff | **No.** It will guess a year. |
| F3 tone | reading the headline's wording | Yes: a judgement about the input |
| F4 image–headline match | looking at both inputs | Yes: what a multimodal model is built for |
| F5 language ID | reading the text (and it may answer "unk") | Yes |
| F6 news outlet | knowing which outlet ran this exact headline | **No.** It will name a plausible outlet. |
| F7 topic | reading the headline | Yes |
| F8 quote present? | reading for quote marks or "said" | Yes |

**Step 3: match to the options.** The unreliable set is {F1, F2, F6}. That is option **B**, and it is the only option containing all three. Every other option includes at least one feature the model handles well (F3, F4, F5, F7 or F8).

"Structurally unreliable" means wrong *because of how the model works*: tokens for F1, no outside knowledge for F2 and F6. It doesn't just mean "occasionally wrong". These features are worse than useless. The downstream classifier trains on invented numbers and may learn patterns that vanish in real use.

**What to remember:** *M14 LLM reality check.* Ask "is the answer in the input, or does it need letter-level access or facts the model was never given?" Offline LLMs are good at judging what's in front of them. They are bad at counting characters (tokenization) and at facts they don't have, which they invent confidently. (Practice: [set 06, problem 6.7](../../practice/06-puzzles-logic.md).)

**Common trap:** marking F5 (language ID) as unreliable because it sounds technical. The answer is right there in the input, and the prompt even gives the model an "unk" escape hatch.

</details>

---

### A1.3 Smart Student Search

<details><summary>Hint 1: understand the question</summary>

Don't ask which formula "looks best". There are five rules, and the right option must pass **all** of them. For each option, can you find one pair of IDs that breaks one rule?

</details>

<details><summary>Hint 2: the key idea</summary>

First pin down what the paper's JD measures. Compute JD(Aryan, Aryan) and JD(Aryan, Bob) from the formula. Does JD = 1 mean "identical" or "completely different"?

Then test each option quickly: rule 5 (can it go above 1?), rule 2 (different sections), rule 4 (which name has the bigger weight?), rule 3 (does swapping s and t change anything?).

</details>

<details><summary>Hint 3: set it up</summary>

Use s = (9C, Aryan, Shah) and t's that change exactly one thing: section 9D; first name "Arya"; last name "Sha". For option B, compute JD(9C, 9D) from the definition (the matching window here is ⌊2/2⌋ − 1 = 0).

</details>

<details><summary>Answer</summary>

**C**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: what the symbols mean.**
- **Edit distance** ED(x, y): the fewest single-letter insertions, deletions or substitutions that turn x into y. ED(Aryan, Arjun) = 2 (y→j, a→u). ED(x, x) = 0. Bigger means more different.
- **Jaro "distance"** JD(x, y). Here |x| is the length of x and m is the number of matching characters: the same letter, at most ⌊max(|x|,|y|)/2⌋ − 1 positions apart. t is half the number of matched characters that come in a different order.
  - JD(Aryan, Arya): window = ⌊5/2⌋ − 1 = 1. A, r, y, a match, and n has no partner, so m = 4 and t = 0. JD = (4/5 + 4/4 + 4/4)/3 = 2.8/3 = 0.933.
  - JD(MARTHA, MARHTA): window = 2. All 6 letters match, but T,H and H,T are in swapped order, so 2 are out of order and t = 1. JD = (1 + 1 + 5/6)/3 = 0.944.
  - Identical strings: m = |x| = |y| and t = 0, so JD = (1 + 1 + 1)/3 = **1**. No letters in common: JD = 0.

  So **despite its name, this JD is a similarity**: 1 means identical, 0 means nothing in common. (Many textbooks call 1 minus this the Jaro distance. The paper's formula is what counts.)
- **Indicator function** 𝟙_{c=c'}: equals 1 if c = c', otherwise 0. So 𝟙_{9C=9C} = 1 and 𝟙_{9C=9D} = 0. Multiplying by it forces the whole score to 0 whenever sections differ, which is exactly rule 2.
- **exp(u)** = e^u with e ≈ 2.718. exp(0) = 1. For negative u it lies between 0 and 1 and shrinks as u gets more negative: e^−1 ≈ 0.37, e^−2 ≈ 0.14.

**Step 1: F breaks rules 5 and 1.** For two identical IDs, F gives 2·1 + 1 = **3**, which is not in [0, 1] and not equal to 1.

**Step 2: B breaks rule 2.** B uses JD(c, c') where the others use the indicator. JD(9C, 9D): the window is ⌊2/2⌋ − 1 = 0, so letters must be in the same position. '9' matches and 'C' vs 'D' doesn't, so m = 1, t = 0 and JD = (1/2 + 1/2 + 1)/3 = **2/3**. Two students in different sections with identical names score 2/3 · e⁰ = 0.67, not 0. (B also puts the bigger weight on the last name, so it breaks rule 4 too.)

**Step 3: A and D break rule 4.**
- A averages the two names with equal weight ½. A one-letter slip costs the same in either name, but rule 4 needs first-name slips to cost *more*.
- D: one wrong letter in the first name multiplies the score by e^−1 ≈ 0.37, but one wrong letter in the last name multiplies it by e^−2 ≈ 0.14. Last-name mistakes hurt more, which is backwards.

**Step 4: E breaks rule 3 (symmetry).** E's weights 2|f'| and |l'| use the name lengths from t only, so swapping s and t changes the weights. Counterexample: s = (9C, Aryan, Shah), t = (9C, Aryan, Sha).

JD(Aryan, Aryan) = 1. For JD(Shah, Sha), the window is 1 and S, h, a match, so m = 3, t = 0 and JD = (3/4 + 1 + 1)/3 = 11/12 ≈ 0.917.
- Sim(s, t): weights 2·5 = 10 and |Sha| = 3, giving (10·1 + 3·0.917)/13 = 12.75/13 = **0.981**.
- Sim(t, s): weights 10 and |Shah| = 4, giving (10 + 4·0.917)/14 = 13.67/14 = **0.976**.

These are not equal. (E can also break rule 4: for "Al Venkataraman" the last-name weight 12 beats the first-name weight 2·2 = 4.)

**Step 5: check that C passes all five.**
- Rule 2: the indicator makes it 0 across sections.
- Rule 5: JD ≤ 1, so the exponent −2(1 − JD_f) − (1 − JD_l) is ≤ 0. That puts exp(…) in (0, 1], and multiplying by 0 or 1 keeps it in [0, 1].
- Rule 1: Sim = 1 needs the indicator to be 1 and the exponent to be 0, so both JDs must be 1. JD = 1 only when every letter matches in order, which means the names are identical.
- Rule 3: JD doesn't care which string comes first (m, t and the two m/length terms are the same either way), and neither does the indicator.
- Rule 4: a drop δ in the first name's JD multiplies the score by e^(−2δ). The same drop in the last name multiplies it only by e^(−δ). First-name mistakes cost more. ✓

| Option | Breaks rule | Witness |
|---|---|---|
| A | 4 | equal weights |
| B | 2 (and 4) | JD(9C, 9D) = 2/3 |
| **C** | none | |
| D | 4 | e^−1 vs e^−2: last name punished more |
| E | 3 (sometimes 4) | 0.981 vs 0.976 |
| F | 5 and 1 | identical IDs give 3 |

**What to remember:** *M10 Kill options with counterexamples*: every option must pass every rule, and one counterexample kills it. Also *M1 Read the definition, not your memory*: this "Jaro distance" is a similarity, where 1 means identical. (Practice: [set 06, problem 6.3](../../practice/06-puzzles-logic.md).)

**Common trap:** reading JD as a distance (0 = same). Then C looks as if it *rewards* mismatches, and you reject the right answer. Plug identical strings into the formula and you get 1.

</details>

---

### A1.4 Recursive V-67 Outbreak

<details><summary>Hint 1: understand the question</summary>

You need N₃ + M₃, the counts at the *start* of day 3. How many daily updates is that from the start of day 0? During one day, what happens to the 8 normal infectious people, and where do the new infections go?

</details>

<details><summary>Hint 2: the key idea</summary>

Write one update rule per group: "infectious tomorrow = still infectious from today + newly infected who join this group". Then fill a table one day at a time. Don't hunt for a closed formula.

</details>

<details><summary>Hint 3: set it up</summary>

N_{t+1} = ½N_t + ½X_t and M_{t+1} = ½M_t + ¼X_t, with X_t = 2N_t + 4M_t. Use a table with columns t, N, M, X.

</details>

<details><summary>Answer</summary>

**C** 281

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: follow one day.** At the start of day t there are N_t normal and M_t mutant infectious people.
- New infections: X_t = 2N_t + 4M_t.
- Of these, ½X_t become normal infectious and ¼X_t become mutant infectious. The other ¼X_t are removed at once and never infect anyone.
- Half of the people who were infectious at the *start* of the day recover, so ½N_t and ½M_t are still infectious.
- The newly infected don't recover on their first day, so all of them are infectious at the start of day t + 1.

So: **N_{t+1} = ½N_t + ½X_t** and **M_{t+1} = ½M_t + ¼X_t**. The removed group R never feeds back into anything, so you can ignore it.

**Step 2: tabulate.** "Start of day 3" means three updates: 0→1, 1→2, 2→3.

| t | N_t | M_t | X_t = 2N + 4M | N_{t+1} = N/2 + X/2 | M_{t+1} = M/2 + X/4 |
|---|---|---|---|---|---|
| 0 | 8 | 8 | 16 + 32 = 48 | 4 + 24 = 28 | 4 + 12 = 16 |
| 1 | 28 | 16 | 56 + 64 = 120 | 14 + 60 = 74 | 8 + 30 = 38 |
| 2 | 74 | 38 | 148 + 152 = 300 | 37 + 150 = 187 | 19 + 75 = 94 |
| 3 | 187 | 94 | | | |

N₃ + M₃ = 187 + 94 = **281**, option **C**.

**Step 3: sanity check.** Simplify the rules: N_{t+1} = 1.5N_t + 2M_t and M_{t+1} = 0.5N_t + 1.5M_t. Check day 1: 1.5·8 + 2·8 = 28 and 0.5·8 + 1.5·8 = 16. ✓ The total goes 16 → 44 → 112 → 281, growing about 2.5× per day. A quick estimate, 16 × 2.5³ ≈ 250, is in the right range.

**What to remember:** *M9 Tabulate recurrences.* For each group, write "next = stays + joins", then fill a table one row at a time. Three rows of arithmetic beat any clever formula. (Practice: [set 05, problem 5.4](../../practice/05-math-optimization.md).)

**Common trap:** forgetting that half of the existing infectious recover (writing N_{t+1} = N_t + ½X_t), or doing the wrong number of updates. "Start of day 3" is three updates after the start of day 0.

</details>

---

### A1.5 Pikachu's Path to Victory

<details><summary>Hint 1: understand the question</summary>

There are only 25 pads and each can be used once. Can any answer above 25 be right? So the real question is: can Pikachu land on all 25, and if not, what stops him?

</details>

<details><summary>Hint 2: the key idea</summary>

Colour the board like a chessboard. After one knight jump, does Pikachu land on the same colour or the other one? What colour are (0,0) and (4,4), and how many squares of each colour are there?

</details>

<details><summary>Hint 3: set it up</summary>

The path alternates colours and starts and ends on the same colour. How must the number of squares of each colour on the path compare? Then try to actually build a path. Tip: visit corners and edges early, because they have the fewest exits, and save (4,4) for last.

</details>

<details><summary>Answer</summary>

**E** 25

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the easy bound.** There are 25 pads and each can be landed on once, so the answer is at most 25. Option F (28) is impossible.

**Step 2: colouring.** Call square (r, c) *dark* if r + c is even and *light* if it is odd. A knight move changes one coordinate by 1 and the other by 2, so r + c changes by ±1 or ±3, always an odd number. So **every jump switches colour** and the path goes dark, light, dark, light, …

(0,0) has r + c = 0 and (4,4) has r + c = 8, so both are dark. A path that starts and ends on dark looks like D L D L … D, so it has **one more dark square than light**.

On a 5×5 board there are 13 dark squares and 12 light ones. The longest such path could use all 12 light and all 13 dark: 12 + 13 = 25. **Colouring does not rule out 25.**

(This check usually matters. If the target had been a light square, the path would contain equal numbers of each colour, at most 12 + 12 = 24, and 25 would be impossible. The colouring is a two-minute check before you invest time in building a path.)

**Step 3: build a path.** A bound is not an answer until you show a path that reaches it. Here is one. The number in each square is the order in which Pikachu lands there (row 0 at the top, column 0 on the left):

```
 1  20  15   8   3
14   9   2  21  16
19  22  13   4   7
10   5  24  17  12
23  18  11   6  25
```

To check it, confirm that each number k+1 is a knight's move from k. For example, 1 at (0,0) → 2 at (1,2) is one down, two right, and 24 at (3,2) → 25 at (4,4) is one down, two right. Also confirm that every number from 1 to 25 appears once. So all 25 pads can be activated: **E**.

**How to find such a path by hand.** Use Warnsdorff's rule: from where you stand, jump to the unvisited square that has the *fewest* onward jumps. Corners have only 2 exits, so you take them early instead of stranding them. Keep (4,4) for the last move, and if you get stuck, back up a few moves and choose differently. Following the rule blindly can strand you at 24 squares, so expect a little backtracking. A computer search finds 56 different 25-pad paths.

**What to remember:** *M8 Parity / colouring.* Colour the board so that every move flips the colour, then count colours to get an upper bound. A bound only becomes the answer once you exhibit a path that reaches it. (Practice: [set 06, problem 6.1](../../practice/06-puzzles-logic.md).)

**Common trap:** thinking the colouring *proves* 25 is reachable. It only shows that 25 isn't ruled out. The path in Step 3 is the proof.

</details>

---

### A2.1 The Phulera Godown Showdown

<details><summary>Hint 1: understand the question</summary>

Both formulas say "pick the point that makes this sum as small as possible". Look inside each sum. Can you split it into a part that depends only on x (or u) and a part that depends only on y (or v)? If so, you can solve each coordinate on its own.

</details>

<details><summary>Hint 2: the key idea</summary>

For Sachivji, take one coordinate: choose x to make |x − 40| + |x − 80| + |x − 120| + |x − 200| as small as possible. If you slide x one step to the right, how does the sum change? Count the points on each side of x.

For Pradhanji, the sum is a smooth bowl in u. Find where its slope is 0.

</details>

<details><summary>Hint 3: set it up</summary>

Sachivji: sort the x's (40, 80, 120, 200) and the y's (20, 80, 140, 180).

Pradhanji: use ln(x_i/u) = ln x_i − ln u, then throw away every piece that doesn't involve u. What is left?

</details>

<details><summary>Answer</summary>

**11**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: notation.**
- **argmin** over (x, y) of f means *the point* where f is smallest, not the smallest value. For example, the argmin over x of (x − 3)² is x = 3, while the minimum value is 0.
- **Manhattan (L1) distance:** |x − x_i| + |y − y_i|, the distance you travel along a grid of perpendicular roads.
- **ln** is the natural logarithm (log base e, where e ≈ 2.718). The facts used below are ln(a/b) = ln a − ln b, and that the slope of ln u at u is 1/u.
- **Pradhanji's formula is the generalised KL (Kullback–Leibler) divergence**, Σ[p ln(p/q) − p + q]. For one positive pair it is never negative, and it is 0 only when q = p. For example, p = 2, q = 1 gives 2 ln 2 − 2 + 1 = 0.386 > 0. So it behaves like a "distance" between p and q, although it isn't symmetric.

**Step 1: split by coordinate.** Sachivji's sum is Σ|x − x_i| + Σ|y − y_i|. The first part involves only x and the second only y, so you can minimise each on its own. Pradhanji's sum splits the same way into a u-part Σ[x_i ln(x_i/u) + (u − x_i)] and a v-part.

**Step 2: Sachivji's x.** f(x) = |x − 40| + |x − 80| + |x − 120| + |x − 200|. Slide x one unit to the right. Every point to the *left* of x gets 1 farther away (+1), and every point to the *right* gets 1 closer (−1).
- For x below 80, say x = 60: 1 point is on the left and 3 on the right, so the change is 1 − 3 = −2. Keep moving right.
- For x between 80 and 120: 2 on the left, 2 on the right, so the change is 0. The function is **flat** here.
- For x above 120: 3 on the left, 1 on the right, so the change is +2. Moving right now hurts.

So f is smallest everywhere on **[80, 120]**, the range between the two middle values (the *median range* of an even number of points). Check: f(80) = 40 + 0 + 40 + 120 = 200, f(100) = 60 + 20 + 20 + 100 = 200, f(120) = 200, but f(60) = 240.

The question's note says that when many points tie, you take the midpoint of the range, so x_S = **100**. For y, sorted 20, 80, 140, 180, the median range is [80, 140] and y_S = **110**. **G_S = (100, 110).**

**Step 3: Pradhanji's u.** Expand: g(u) = Σ[x_i ln x_i − x_i ln u + u − x_i]. The pieces x_i ln x_i and −x_i don't involve u, so they shift g up or down without moving its lowest point. Drop them:

g(u) = 4u − (Σx_i) · ln u + (constant).

The **slope** (derivative) of g at u is the rate at which g changes as u grows. At the bottom of a smooth bowl the slope is 0. The slope of 4u is 4 and the slope of ln u is 1/u, so

slope = 4 − (Σx_i)/u. Setting this to 0 gives **u = (Σx_i)/4, the mean.**

(The paper's way of writing the same equation is Σ(1 − x_i/u) = 0.)

Σx = 40 + 120 + 200 + 80 = 440, so u = 110. Σy = 180 + 80 + 140 + 20 = 420, so v = 105. **G_P = (110, 105).**

Is it really a minimum? For u below 110 the slope is negative (g is falling), and above 110 it is positive (g is rising), so 110 is the bottom. Numerically, the x-part is 66.0 at u = 100, 64.1 at u = 110 and 65.8 at u = 120.

**Step 4: the distance.** D = √((100 − 110)² + (110 − 105)²) = √(100 + 25) = √125 ≈ 11.18, so ⌊D⌋ = **11**.

**What to remember:** *M6 What does the argmin pick?* Absolute (L1) distance is minimised by the **median**, which is a whole range when the count is even. Squared error, and this KL divergence, are minimised by the **mean**. A sum that splits by coordinate can be minimised one coordinate at a time. (Practice: [set 05, problem 5.1](../../practice/05-math-optimization.md) and [set 01, problem 1.4](../../practice/01-metrics.md).)

**Common trap:** taking one median value (x = 80 or x = 120) instead of the midpoint of the median range, which the note asks for. Another trap is using straight-line (Euclidean) distance, which the question never mentions for Sachivji.

</details>

---

### A2.2 The Blind Board Gambit

<details><summary>Hint 1: understand the question</summary>

Anand chooses *before* he knows Gukesh's order. All he knows is that it's one of the 5 orders other than (A, B, C), each equally likely. Since the boards are interchangeable, only "who plays whom" matters. How many different "who plays whom" pairings are there?

</details>

<details><summary>Hint 2: the key idea</summary>

Brute force means 6 Anand orders × 5 Gukesh orders = 30 match calculations. Instead, fix one Anand order and let Gukesh run through **all 6** orders. Every possible pairing appears exactly once, so the total over all 6 is the **same number for every Anand order**. What does that tell you about maximising the total over the 5 allowed orders?

</details>

<details><summary>Hint 3: set it up</summary>

Total over the 5 allowed orders = (constant) − P(Anand wins against (A, B, C)). To make this as big as possible, Anand should pick the order that would do *worst* against (A, B, C). Compute P(Anand wins vs (A, B, C)) for all 6 of his orders.

</details>

<details><summary>Answer</summary>

**43**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: the rating formula.** P(R beats S) = 1/(1 + 10^((S−R)/400)) is the **Elo** formula. It depends only on the rating *difference*. Equal ratings give 1/(1 + 1) = 0.5. Being 400 points stronger gives 1/(1 + 0.1) = 0.91.

Only five differences (Anand's player minus Gukesh's) ever occur:

| Difference | −500 | −300 | −100 | +100 | +300 |
|---|---|---|---|---|---|
| P(Anand's player wins) | 0.053 | 0.151 | 0.360 | 0.640 | 0.849 |

By hand: 10^0.25 = √√10 ≈ 1.778, so P(+100) = 1/(1 + 1/1.778) = 0.640, and P(−100) = 1 − 0.640 = 0.360. Next, 10^0.75 = 10/1.778 = 5.62, so P(+300) = 1/(1 + 1/5.62) = 0.849. Finally 10^1.25 = 17.78, so P(−500) = 1/18.78 = 0.053.

**Step 1: probability of winning the match.** Anand needs at least 2 of 3 independent boards. List the outcomes with ≥ 2 wins (WWL, WLW, LWW, WWW), multiply along each and add. After simplifying:

P(≥ 2 wins) = p₁p₂ + p₁p₃ + p₂p₃ − 2p₁p₂p₃.

**Step 2: the symmetry shortcut.** Fix Anand's order, say (X, Y, Z). As Gukesh's order runs through all 6 permutations, the pairing (who faces whom) runs through all 6 possible pairings of {X, Y, Z} with {A, B, C}, each exactly once. So

sum over all 6 Gukesh orders of P(Anand wins) = K, **the same K for every Anand order.**

That means: sum over the 5 allowed orders = K − P(Anand wins against (A, B, C)). To maximise it, Anand should choose the order that would do **worst** against (A, B, C), the one order he knows he won't face. Intuitively, he "spends" his worst pairing on a matchup that can't happen.

**Step 3: each Anand order against (A, B, C).** Board 1 faces A = 2000, board 2 faces B = 1800, board 3 faces C = 1600.

| Anand's order | Pairings (rating difference) | p₁, p₂, p₃ | P(≥ 2 wins) |
|---|---|---|---|
| (X, Y, Z) | −100, −100, −100 | .360, .360, .360 | 0.295 |
| (X, Z, Y) | −100, −300, +100 | .360, .151, .640 | 0.312 |
| (Y, X, Z) | −300, +100, −100 | .151, .640, .360 | 0.312 |
| (Y, Z, X) | −300, −300, +300 | .151, .151, .849 | **0.241** |
| (Z, X, Y) | −500, +100, +100 | .053, .640, .640 | 0.434 |
| (Z, Y, X) | −500, −100, +300 | .053, .360, .849 | 0.337 |

Worked row, (Y, Z, X): p₁p₂ = 0.023, p₁p₃ = p₂p₃ = 0.128. The sum is 0.279, and subtracting 2 × 0.023 × 0.849 = 0.039 gives 0.241.

The smallest is (Y, Z, X), so **Anand plays (Y, Z, X)**. The column adds to K = 1.931, and his average over the 5 allowed orders is (1.931 − 0.241)/5 = 0.338. That is the best of the six; the 30-case brute force in `verify.py` agrees.

**Step 4: the real game.** Gukesh actually plays (C, A, B). Anand's (Y, Z, X) gives Y–C (+100), Z–A (−500), X–B (+100). That is the same pairing as the (Z, X, Y) row above, so you've already computed it:

p = 0.640·0.053 + 0.640·0.640 + 0.053·0.640 − 2·0.640·0.053·0.640 = 0.034 + 0.410 + 0.034 − 0.044 = **0.434**, and ⌊100p⌋ = **43**.

**What to remember:** *M16 Elo & series.* Elo win chance depends only on the rating difference, and "win ≥ 2 of 3" = p₁p₂ + p₁p₃ + p₂p₃ − 2p₁p₂p₃. A companion move: to average over "every case except one", compute "every case" (often a constant) and subtract the excluded one. (Practice: [set 02, problem 2.4](../../practice/02-probability.md).)

**Common trap:** letting Anand optimise against (C, A, B), which he doesn't know. He chooses using only the tip, and Gukesh's real order is used afterwards, to compute p.

</details>

---

### A2.3 The Crude Curve Forecast

<details><summary>Hint 1: understand the question</summary>

There are many unknowns, but each term in the model does one thing you can see on the graph. Which term makes the wiggles, which makes the slow climb, which makes the jump at t = 30, and which bends the curve after t = 48?

</details>

<details><summary>Hint 2: the key idea</summary>

Before t = 30, only A + Bt + E sin(2πt/T) is switched on. The distance between peaks gives T. At a labelled peak the sine is +1, and at a trough it is −1. Combine labelled points so that the parts you don't want cancel.

</details>

<details><summary>Hint 3: set it up</summary>

P(3) = 34, P(9) = 14, P(15) = 42. Compare P(15) with P(3): the sine is the same at both, so only Bt changed. After that, the jump at t = 30 gives D, t = 48 is where the C-term switches on, and you can read C from how far the curve after t = 48 sits below where it "should" be.

</details>

<details><summary>Answer</summary>

**92**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: the pieces.**
- **Heaviside step** h(t): 0 when t < 0 and 1 when t ≥ 0. So D·h(t − 30) is 0 before month 30 and D from month 30 on, like a switch that permanently adds D. Example: 20·h(t − 30) is 0 at t = 29 and 20 at t = 31.
- C(1 − e^(−(t−τ_C)))·h(t − τ_C) is 0 before τ_C. *At* τ_C it is C(1 − 1) = 0, so there is no jump. After that it rises quickly towards C: e^−1 ≈ 0.37 and e^−3 ≈ 0.05, so 3 months later it is already 95% of C. Think of it as a *smooth* step of size C.
- sin(2πt/T) repeats every T months, peaks at t = T/4 and bottoms out at t = 3T/4.

**Step 1: the period.** The peaks are at 3, 15, 27 and the troughs at 9, 21, so **T = 12**. As a check, the first peak should be at T/4 = 3. ✓

**Step 2: A, B, E from the part before t = 30.** Here P(t) = A + Bt + E sin(πt/6). The sine is +1 at t = 3, 15, 27 and −1 at t = 9, 21.
- P(15) − P(3) = 12B, because the sine terms are equal and cancel. 42 − 34 = 8, so **B = 2/3**.
- P(3) + P(9) = 2A + 12B, because +E and −E cancel. 34 + 14 = 48, so 2A = 48 − 8 and **A = 20**.
- E = P(3) − A − 3B = 34 − 20 − 2, so **E = 12**.

Check with points you didn't use: P(21) = 20 + 14 − 12 = 22 ✓, P(27) = 20 + 18 + 12 = 50 ✓, and P(0) = 20 ✓ (the graph starts at 20).

(Strictly, because of the upward trend the very top of each wave is a fraction of a month after t = 3. The labelled dots are the values *at* t = 3, 9, …, and those are what we used.)

**Step 3: D from the jump.** At t = 30 the price jumps from 40 to 60. The C-term starts at 0 (Step 0), so the jump must be the D-term: **D = 20, τ_D = 30**. Check: just before 30, P = 20 + 20 + 12 sin(5π) = 40. ✓

**Step 4: τ_C from the second dashed line.** It is at t = 48, labelled (48, 72.0). Check: P(48) = 20 + 32 + 0 + 20 + 12 sin(8π) = 72 ✓, exactly the label, which confirms the C-term is 0 at its switch-on. So **τ_C = 48**.

**Step 5: C from where the curve settles.** By about t = 51 the C-term is close to C. Without it, the model would give A + Bt + D + E·sin:
- at t = 60: 20 + 40 + 20 + 0 = 80, but the graph shows about 70, so C ≈ −10;
- at the trough near t = 57: 20 + 38 + 20 − 12 = 66, but the graph shows about 56, so C ≈ −10 again.

The two readings agree: **C = −10** (a market correction).

**Step 6: forecast.** 75 = 6 × 12 + 3, so t = 75 is at the same point of the cycle as t = 3, a peak where the sine is 1.

P(75) = 20 + (2/3)(75) − 10(1 − e^−27) + 20 + 12·1 = 20 + 50 − 10 + 20 + 12 + 10e^−27 = 92 + (a tiny positive number).

So ⌊P(75)⌋ = **92**. The tiny term is *positive*: −10(1 − e^−27) = −10 + 10e^−27, which is slightly *more* than −10. That's why the floor is 92 and not 91.

**What to remember:** *M13 Read parameters off a graph.* Give each term one job (wiggle, trend, jump, smooth step). Then combine labelled points so the unwanted terms cancel: P(15) − P(3) removes the sine, and so does P(3) + P(9). Check every parameter against a point you didn't use. (Practice: [set 05, problem 5.7](../../practice/05-math-optimization.md).)

**Common trap:** forgetting where t = 75 sits in the cycle. It's a peak, so the sine adds a full +12. Another trap is reading C off the graph at t = 49 or 50, before the smooth step has finished rising.

</details>

---

### A2.4 The Catalyst Constraint

<details><summary>Hint 1: understand the question</summary>

You have 5 moles of catalyst to split between the two pathways. If catalyst were unlimited, how much would each pathway want? Is 5 enough for both?

</details>

<details><summary>Hint 2: the key idea</summary>

Once you know the budget is tight, substitute c_B = 5 − c_A to get a single quadratic in c_A. Another way to see it: at the best split, one more drop of catalyst must be **equally useful** in both pathways.

</details>

<details><summary>Hint 3: set it up</summary>

d_A = 16c_A − 2c_A² and d_B = 24c_B − 3c_B². The extra D you get per extra mole of catalyst is 16 − 4c_A for pathway A and 24 − 6c_B for pathway B.

</details>

<details><summary>Answer</summary>

**69**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: plug in the numbers.** a = 16 and b = 24, so d_A = 16c_A − 2c_A² and d_B = 24c_B − 3c_B². Use these yield formulas exactly as given. They are the problem's model, so don't add chemistry rules the question didn't state.

**Step 2: what would each pathway want on its own?** d_A is a downward-opening parabola. Its peak is at c_A = 16/(2·2) = 4, where d_A = 32. d_B peaks at c_B = 24/(2·3) = 4, where d_B = 48. Together they would want 4 + 4 = 8 moles, but you have 5. **The constraint binds:** you will use all 5 moles, and neither pathway gets its favourite amount.

**Step 3: the 9th-grade route.** Write c = c_A, so c_B = 5 − c:

T(c) = 16c − 2c² + 24(5 − c) − 3(5 − c)²
  = 16c − 2c² + 120 − 24c − 3(25 − 10c + c²)
  = 16c − 2c² + 120 − 24c − 75 + 30c − 3c²
  = −5c² + 22c + 45.

A parabola ac² + bc + k with a < 0 peaks at c = −b/(2a) = −22/(−10) = **2.2**. So c_A = 2.2 and c_B = 2.8, both between 0 and 5. ✓

T(2.2) = −5(4.84) + 48.4 + 45 = −24.2 + 48.4 + 45 = **69.2**.

Check by pathway: d_A = 35.2 − 9.68 = 25.52 and d_B = 67.2 − 23.52 = 43.68, which add to 69.2. ✓ So ⌊69.2⌋ = **69**.

**Step 4: the route that generalises (equal marginal gains).** The **marginal gain** is the extra D from one more small amount of catalyst, which is the slope of the yield curve. For d_A it is 16 − 4c_A. At c_A = 1, for example, it is 12, so going from 1 to 1.01 moles adds about 0.12 moles of D.

Suppose A's marginal gain were bigger than B's. Then moving a little catalyst from B to A would raise the total. So at the best split the two are equal:

16 − 4c_A = 24 − 6c_B, with c_B = 5 − c_A,
16 − 4c_A = −6 + 6c_A, so c_A = 2.2. Same answer.

Both marginal gains are 7.2 there, which is positive, so using *all* 5 moles is right. If they had come out negative, you would leave some catalyst unused.

**Step 5: check the edges.** All the catalyst to B (c_A = 0) gives 45. All of it to A gives 30. Both are worse than 69.2.

**What to remember:** *M7 Equal marginal gains (check if the constraint binds).* First see what each part wants on its own. If the wants add up to more than the budget, split it so the last unit is equally useful everywhere. (Practice: [set 05, problem 5.2](../../practice/05-math-optimization.md).)

**Common trap:** splitting 2.5/2.5 "to be fair". That gives 27.5 + 41.25 = 68.75, so ⌊⌋ = 68, which is one off. Another trap is giving each pathway its unconstrained best of 4 moles, which needs 8 moles you don't have.

</details>

---

### A2.5 The Pit-Stop Paradox

<details><summary>Hint 1: understand the question</summary>

You observed one thing: Hamilton won. The hidden situation is one of 2 × 4 = 8 scenarios (rain or not, times 4 strategies). How likely is each scenario to produce a Hamilton win?

</details>

<details><summary>Hint 2: the key idea</summary>

Imagine 4000 races. Split them by weather (2000 each), then by strategy, then count how many end in a Hamilton win. After you learn the result, only the races Hamilton won matter.

</details>

<details><summary>Hint 3: set it up</summary>

"At least one pitted" is everything except "neither pitted". It's easier to count the Hamilton wins where neither pitted and subtract.

</details>

<details><summary>Answer</summary>

**86**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: terms.** The **prior** is your probability *before* seeing the evidence: here, 50% rain. P(A | B), read "A given B", means: among the cases where B happened, the fraction where A also happened.

**Step 1: natural frequencies.** Imagine 4000 races. We chose 4000 so every count below is a whole number. 2000 are dry and 2000 rainy.

| Weather | Strategy | Races | P(H wins) | H wins |
|---|---|---|---|---|
| Dry | Neither | 0.45 × 2000 = 900 | 0.25 | 225 |
| Dry | Only V | 600 | 0.80 | 480 |
| Dry | Only H | 200 | 0.10 | 20 |
| Dry | Both | 300 | 0.55 | 165 |
| Rain | Neither | 0.05 × 2000 = 100 | 0.50 | 50 |
| Rain | Only V | 200 | 0.05 | 10 |
| Rain | Only H | 200 | 0.95 | 190 |
| Rain | Both | 1500 | 0.60 | 900 |

**Step 2: keep only what matches the evidence.** Hamilton won 890 + 1150 = **2040** races. In 225 + 50 = **275** of them neither driver pitted. So at least one pitted in 2040 − 275 = **1765**.

P(at least one pitted | H won) = 1765/2040 = 0.8652, so ⌊86.52⌋ = **86**.

**Step 3: the same thing as a formula** (Bayes' rule, P(A | B) = P(A and B)/P(B)):
- P(H wins) = 0.5(0.445) + 0.5(0.575) = 0.51
- P(neither pitted and H wins) = 0.5(0.1125) + 0.5(0.025) = 0.06875
- Answer: (0.51 − 0.06875)/0.51 = 0.8652.

**Why it's called a paradox:** before the race, P(at least one pits) = 0.5(0.55) + 0.5(0.95) = 0.75. Learning that Hamilton won pushes it *up* to 0.865, because his wins come mostly from scenarios where someone pitted.

(The text says each driver chooses independently, but the table's numbers aren't products of separate probabilities. Use the table: it *is* the data.)

**What to remember:** *M2 Natural frequencies.* Imagine a round number of cases (chosen so the counts are whole), split them along the tree, then keep only the cases consistent with what you observed. Also *M18 Confounders*: rain changes both the strategy and the win chances, so multiply *within* each weather before adding. (Practice: [set 02, problems 2.2 and 2.5](../../practice/02-probability.md).)

**Common trap:** averaging the dry and rain columns first and then multiplying. That ignores the fact that rain drives both the strategy and the outcome, and it gives 80. Another trap is answering 75, the probability before you knew who won.

</details>

---

### B1 Code Triage: shared setup

Q1, Q2 and Q7 all live inside one 3 × 3 table of **counts** for the 1000 test patients. Try to build it yourself first, with rows = actual class and columns = predicted class. The block below builds it step by step. Open it when a hint sends you here.

<details><summary>Shared setup: build the full count table (M3 Fill the whole table)</summary>

**Step 0: pick a layout and say it out loud.** The paper's background matrix puts the **predicted** class in rows and the **actual** class in columns: F_{Ci,Cj}, a class-j patient classified as class i, sits in row i, column j. The Q7 benefit matrix uses **actual** rows. We use **rows = actual, columns = predicted** throughout, to match Q7.

- **Sensitivity** of class i (also called TPR, the true positive rate) = (actual i, predicted i) ÷ (all actual i). In our layout that is diagonal ÷ row total. Example: 100 actual ICU patients, 80 predicted ICU → sensitivity 0.80.
- **Specificity** of class i = (actual not-i, predicted not-i) ÷ (all actual not-i): among patients who are *not* class i, the fraction the system also says are not class i.

**Step 1: row totals.** 60%, 30% and 10% of 1000 give 600, 300 and 100.

**Step 2: the diagonal from the sensitivities.** 0.85 × 600 = 510, 0.70 × 300 = 210, 0.80 × 100 = 80.

**Step 3: the two "egregious error" cells.** 3.33% (that is, 1/30) of 600 = 20 actual-1 patients predicted 3. 10% of 100 = 10 actual-3 patients predicted 1.

**Step 4: finish rows 1 and 3 by subtraction.** Row 1: 600 − 510 − 20 = 70 predicted 2. Row 3: 100 − 80 − 10 = 10 predicted 2.

**Step 5: split row 2 using a specificity.** Row 2 has 300 − 210 = 90 errors. Call the number predicted 1 "a", so 90 − a are predicted 3.
- Specificity of class 3 is 0.91. There are 900 non-class-3 patients. Those wrongly predicted 3 are 20 (from row 1) + (90 − a). So 900 − 20 − (90 − a) = 0.91 × 900 = 819, which gives **a = 29** and **61** predicted 3.
- Check with specificity 1: the 400 non-class-1 patients include 29 + 10 = 39 predicted 1, and (400 − 39)/400 = 0.9025, which rounds to 0.90. ✓ Specificity 2: 70 + 10 = 80 of 700 predicted 2, and 620/700 = 0.886, which rounds to 0.89. ✓

> **Heads-up.** If you start from specificity 1 instead (0.90 × 400 = 360), you get a = 30 and 60. Then specificity 3 = 820/900 = 0.911, which *also* rounds to 0.91. The given rates are rounded to two decimals, so this one split is pinned down only to within one patient. Both versions give the same answer to every question (Q7: 95.05 vs 95.00, both → 95).

**The table (rows = actual, columns = predicted):**

| Actual \ Predicted | 1 | 2 | 3 | Total |
|---|---|---|---|---|
| **1** | 510 | 70 | 20 | 600 |
| **2** | 29 | 210 | 61 | 300 |
| **3** | 10 | 10 | 80 | 100 |
| **Total** | 549 | 290 | 161 | 1000 |

Check: the columns add to 549 + 290 + 161 = 1000. ✓

</details>

---

### B1 Q1: Missed ICU Patients

<details><summary>Hint 1: understand the question</summary>

What is the denominator: all 1000 patients, or only the patients who actually need the ICU?

</details>

<details><summary>Hint 2: the key idea</summary>

The class 3 sensitivity already tells you what fraction of actual ICU patients were classified as ICU. What fraction is left over?

</details>

<details><summary>Answer</summary>

**20**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the group.** The question is about the 100 patients who *actually* need the ICU.

**Step 2: subtract.** Sensitivity for class 3 is 0.80, so 80 of the 100 were classified as ICU. The other 100 − 80 = 20 were classified as Class 1 (10, given) or Class 2 (the remaining 10). x = 20/100 = 0.20, and ⌊100x⌋ = **20**.

You don't need the "10% misclassified as Class 1" figure. It tells you how the 20 split up; it is not extra on top.

**What to remember:** *M1 Read the definition, not your memory.* Sensitivity is computed inside the actual-positive group, so "missed" = 1 − sensitivity (the false negative rate).

**Common trap:** adding the 10% to the 20% to get 30. The 10% is *part of* the 20%.

</details>

---

### B1 Q2: Outpatient Triaging

<details><summary>Hint 1: understand the question</summary>

The group is "patients who actually need only outpatient care", the 600 Class 1 patients. The Class 1 row has two numbers, sensitivity 0.85 and specificity 0.90. Which one is computed *among those 600*?

</details>

<details><summary>Hint 2: the key idea</summary>

Specificity for class 1 is about patients who are *not* Class 1. For a Class 1 patient, "correctly identified" means predicted Class 1.

</details>

<details><summary>Answer</summary>

**85**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the group.** Actual Class 1: 600 patients.

**Step 2: the event.** "Correctly classified as Class 1 rather than Class 2 or 3" means predicted 1. Among actual Class 1, the fraction predicted 1 is exactly the **sensitivity of Class 1**: 510/600 = 0.85, so ⌊100x⌋ = **85**.

**Why not 0.90?** Specificity₁ = 361/400 is computed over the 400 patients who *do* need hospital care: of them, how many did the system correctly keep out of the outpatient class? It's a different group. The phrase "not requiring hospitalization" sounds negative and pulls you towards specificity. But the group here is actual Class 1, and for them "correct" means predicted Class 1, which is Class 1's true positive rate.

**What to remember:** *M1 Read the definition, not your memory.* For every rate, ask "computed among which *actual* group?". Sensitivity_i is computed among actual i, and specificity_i among actual not-i.

**Common trap:** answering 90 (the specificity), triggered by the words "not requiring hospitalization".

</details>

---

### B1 Q3: Operating Point for ICU Detection

<details><summary>Hint 1: understand the question</summary>

The 25-bed limit is on how many patients are *flagged* per day. Who gets flagged? Real ICU patients the system catches, **and** non-ICU patients it flags by mistake.

</details>

<details><summary>Hint 2: the key idea</summary>

Turn rates into counts. Of the 200 patients a day, how many are ICU patients and how many aren't? Use the 10% from the test population.

</details>

<details><summary>Hint 3: set it up</summary>

Flagged per day = 20 × TPR + 180 × FPR. Compute it for each of the six points.

</details>

<details><summary>Answer</summary>

**Option 3** (Point C)

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: the ROC curve.** Each threshold t₂ gives one pair (FPR, TPR):
- TPR (true positive rate) = sensitivity = the fraction of ICU patients flagged.
- FPR (false positive rate) = 1 − specificity = the fraction of non-ICU patients flagged.

Plotting the pairs for every threshold gives the ROC curve. Lowering the threshold flags more people, so TPR goes up, but FPR goes up too.

**Step 1: counts per day.** 10% of 200 = 20 ICU patients and 180 non-ICU patients.

**Step 2: flags per day at each point.**

| Point | ICU caught = 20 × TPR | Non-ICU flagged = 180 × FPR | Total flagged |
|---|---|---|---|
| A | 12.0 | 3.6 | 15.6 |
| B | 14.4 | 7.2 | 21.6 |
| C | 15.6 | 9.0 | **24.6** |
| D | 16.8 | 14.4 | 31.2 |
| E | 17.6 | 21.6 | 39.2 |
| F | 18.4 | 36.0 | 54.4 |

**Step 3: apply the limit.** A, B and C fit under 25. Of those, C has the highest sensitivity (0.78), so the answer is **option 3**.

Notice that the non-ICU group is 9 times bigger, so FPR drives the flag count. D's FPR is only 3 percentage points above C's, yet it adds 5.4 extra non-ICU flags a day.

**What to remember:** *M5 Rates → counts.* A capacity limit is a limit on counts, and count = rate × size of the group the rate applies to. (Same move: [practice set 01, problem 1.3](../../practice/01-metrics.md).)

**Common trap:** comparing FPR with 25/200 = 12.5% and choosing E. That forgets that the ICU patients the system catches also take beds, and it applies FPR to all 200 patients instead of the 180 non-ICU ones.

</details>

---

### B1 Q4: ROC Curve: Effect of Score Transformation

<details><summary>Hint 1: understand the question</summary>

An ROC curve comes from sweeping a threshold and recording (FPR, TPR) each time. What decides which patients are above a threshold: the actual score values, or only their order?

</details>

<details><summary>Hint 2: the key idea</summary>

If a > b, is a^1.5 > b^1.5? Then, for any old threshold t, which *new* threshold flags exactly the same patients?

</details>

<details><summary>Answer</summary>

**Option 3** (the curve remains unchanged)

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: monotone increasing.** A function f is *monotone increasing* if a > b always gives f(a) > f(b), so it never swaps the order of two numbers. s^1.5 on s ≥ 0 is one: 4 > 1 gives 8 > 1.

**Step 1: same patients flagged.** Take any old threshold t. The patients with s_old ≥ t are flagged. Under the new score, use the threshold t^1.5. Because s ↦ s^1.5 keeps the order, s_new ≥ t^1.5 happens for **exactly the same patients**. The same patients flagged means the same TPR and the same FPR.

**Step 2: same curve.** Every point on the old curve is also on the new curve, and the other way round, so the curve is unchanged: **option 3**.

A tiny example: four patients scored 0.2 (non-ICU), 0.5 (ICU), 0.6 (non-ICU), 0.9 (ICU) get new scores 0.09, 0.35, 0.46, 0.85. The order is the same, so the ROC curve is the same.

**A flaw in the question.** It says s_old ∈ ℝ (any real number), but s^1.5 = s·√s has no real value when s is negative. The intended reading is non-negative scores, or the sign-keeping version sign(s)·|s|^1.5. Either way the transformation is monotone increasing, so the answer stands.

Option 4 (the "gap between class means") is a distractor. The means do change, but the ROC curve never looks at means.

**What to remember:** *M4 ROC invariances.* ROC curves (and AUC) depend only on the **order** of the scores, so any strictly increasing transform leaves them unchanged. (Same move: [practice set 01, problem 1.2](../../practice/01-metrics.md).)

**Common trap:** thinking that "spreading out the high scores" helps separate the classes. It changes the distances between scores but not their order, and ROC only sees order.

</details>

---

### B1 Q5: ROC Curve: Effect of Distribution Shift

<details><summary>Hint 1: understand the question</summary>

TPR is a fraction *of which group*? FPR is a fraction of which group? If the ICU share rises from 10% to 25%, does the fraction of ICU patients scoring above a given threshold change?

</details>

<details><summary>Hint 2: the key idea</summary>

Picture only the ICU group growing: 100 ICU patients become 250, with the same spread of scores. What happens to "ICU patients flagged ÷ all ICU patients"?

</details>

<details><summary>Answer</summary>

**Option 3** (the curve remains unchanged)

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: prevalence.** Prevalence is the fraction of the population that belongs to the positive class. Here it rises from 10% to 25%.

**Step 1: TPR stays.** TPR = (ICU patients flagged) ÷ (ICU patients). Both the top and the bottom are counts *inside the ICU group*. With 2.5 times as many ICU patients and the same score distribution, both grow 2.5 times, so the ratio is unchanged. At point C, 100 ICU patients give 78 flagged (0.78), and 250 give 195 flagged (0.78).

**Step 2: FPR stays.** FPR is computed entirely inside the non-ICU group, so the same argument applies.

**Step 3: the curve stays.** At every threshold (FPR, TPR) is unchanged, so the curve is unchanged: **option 3**.

**What *does* change** is precision, and the number of patients flagged per day (Q3's capacity sum). At 25% ICU, point C flags 50 × 0.78 + 150 × 0.05 = 46.5 patients a day. The hospital would pick a different operating point even though the curve itself hasn't moved.

**What to remember:** *M4 ROC invariances.* TPR and FPR are each computed within one true class, so prevalence doesn't move the ROC curve. Anything that divides by a *predicted* count (precision), or counts flags (capacity), does change. (Same move: [practice set 01, problem 1.1](../../practice/01-metrics.md).)

**Common trap:** option 1, "more positives, so the curve improves". The number of positives never enters TPR or FPR.

</details>

---

### B1 Q6: Designing an Ordinal Classifier System

<details><summary>Hint 1: understand the question</summary>

There are five claims and six options. Before you judge the subtle claims, find one you are *sure* is false and cross out every option that contains it. Which claim gets a basic fact about loss functions wrong?

</details>

<details><summary>Hint 2: the key idea</summary>

X uses **one** weight vector with two thresholds. What does that force about the two boundaries (1 | 2 and 2 | 3)? The question says the two decisions rely on *different* medical criteria.

</details>

<details><summary>Hint 3: set it up</summary>

Tabulate the three losses at a few margins y·f(x) = −5, 0, 1, 3. Which grows fastest for a badly wrong point (an outlier)? Which one also punishes a point that is confidently *correct*?

</details>

<details><summary>Answer</summary>

**Option 4** (Claims 1, 2, 4). This is the most defensible reading; see the note at the end of the solution.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: terms.**
- **Linear classifier:** score f(x) = w·x + b, a weighted sum of the features plus a constant. All points with the same score lie on a flat boundary (a line in 2-D, a plane in 3-D).
- **Ordinal classes:** categories with an order, here severity 1 < 2 < 3. Calling a 1 a 3 is worse than calling it a 2.
- **Margin** m = y·f(x), with y = +1 or −1. It is positive when the point is on the correct side, and large when it is confidently correct.
- The three losses, written in terms of m (because y² = 1, (y − f)² = (1 − m)²):

| m = y·f(x) | −5 (badly wrong: an outlier) | 0 | 1 | 3 (confidently right) |
|---|---|---|---|---|
| squared, (1 − m)² | 36 | 1 | 0 | **4** |
| hinge, max(0, 1 − m) | 6 | 1 | 0 | 0 |
| logistic, ln(1 + e^−m) | 5.01 | 0.69 | 0.31 | 0.05 |

**Step 1: Claim 5 is false, so cross out options 2 and 3.** Squared loss grows like the *square* of the error. One outlier (m = −5) costs 36 and dominates training, pulling the boundary towards itself. Logistic loss grows only about linearly (5.01), and its slope never gets bigger than 1 in size. "Smooth gradients" is true of both losses, but smooth doesn't mean robust. Squared loss even punishes confidently *correct* points (m = 3 costs 4). That leaves options 1 {1,2,3,4}, 4 {1,2,4}, 5 {2,3,4} and 6 {1,3,4}.

**Step 2: Claim 4 is in all four survivors. Check that it makes sense.** For X (one score, two thresholds), fitting the score to ordered targets such as 1, 2, 3 with squared loss pulls class 2 scores *between* class 1 and class 3. It respects both the order and the spacing. Hinge loss is built for two classes (±1) and only asks "right side, by a margin of 1?". It has no built-in idea that class 2 sits between 1 and 3. But, as Step 1 showed, squared loss lets outliers drag the thresholds. So Claim 4 is **true**.

**Step 3: Claim 1 is true, so cross out option 5.** Y's two classifiers are trained separately, with different weights. For one patient, "1 vs {2,3}" can say *class 1* while "{1,2} vs 3" says *class 3*: low severity and ICU at once, which needs a rule to settle it. Z's three pairwise votes can go round in a circle (1 beats 2, 2 beats 3, 3 beats 1), a three-way tie. Both need post-processing. Options 1, 4 and 6 are left, and they differ only on Claims 2 and 3.

**Step 4: Claim 2 (Y beats X) is true.** X has one weight vector, so its two boundaries {score = t₁} and {score = t₂} are **parallel**: the same weighted combination of features, cut at two levels. The question says the two decisions use *different* criteria (pain/infection markers vs vital instability), so the best 1 | 23 boundary and the best 12 | 3 boundary point in different directions. Y has two separate weight vectors and can learn both. That gives it a high chance of doing better, though not a guarantee.

**Step 5: Claim 3 (Z beats Y) is false.** Z's classifiers are 1 vs 2, 2 vs 3 and 3 vs 1. Each is trained only on its own two classes, so each sees *less* of the already limited data. The 1 vs 3 classifier ignores class 2 entirely and adds no boundary that matters for ordered classes, since Y's two boundaries already settle every case. Z costs data and creates the vote conflicts from Claim 1, with no expected gain in accuracy.

**Step 6: conclusion.** Claims 1, 2 and 4 are true, so the answer is **option 4**.

| Option | Claims | What's wrong with it |
|---|---|---|
| 1 | 1, 2, 3, 4 | includes Claim 3 (false) |
| 2 | 1, 2, 4, 5 | includes Claim 5 (false) |
| 3 | 1, 2, 3, 5 | includes Claims 3 and 5 (both false) |
| **4** | **1, 2, 4** | nothing |
| 5 | 2, 3, 4 | leaves out Claim 1 (true), includes Claim 3 (false) |
| 6 | 1, 3, 4 | leaves out Claim 2 (true), includes Claim 3 (false) |

> **Ambiguity.** Claims 2–4 are judgement calls ("high chance", "better suited"), not theorems. Option 4 is the most defensible reading: Claim 5 is definitely false, Claim 1 is definitely true, and the details the question gives (different criteria, limited data) settle 2 against 3.

**What to remember:** *M10 Kill options with counterexamples.* Find the claim you're surest about (here Claim 5), cross out every option containing it, and let the option list tell you which claims are still worth arguing about.

**Common trap:** believing Claim 5 because "smooth gradients" sounds good. Smooth is not robust: under squared loss, one outlier can dominate the fit.

</details>

---

### B1 Q7: Triage Benefits

<details><summary>Hint 1: understand the question</summary>

"Expected benefit per patient" = total benefit over all 1000 patients ÷ 1000. To get the total, you need to know how many patients land in each (actual, predicted) cell.

</details>

<details><summary>Hint 2: the key idea</summary>

You need all 9 counts. Build the full 3 × 3 table from the sensitivities, the two "egregious error" figures and one specificity. (The shared setup above walks through it.)

</details>

<details><summary>Hint 3: set it up</summary>

Check that your table and the benefit matrix use the same orientation (rows = actual). Then multiply each count by its benefit and add.

</details>

<details><summary>Answer</summary>

**95**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the count table** (from the shared setup; rows = actual, columns = predicted):

| | Pred 1 | Pred 2 | Pred 3 |
|---|---|---|---|
| Actual 1 | 510 | 70 | 20 |
| Actual 2 | 29 | 210 | 61 |
| Actual 3 | 10 | 10 | 80 |

**Step 2: multiply cell by cell.** The benefit matrix also has actual classes in rows, so the cells line up directly.

| | Pred 1 | Pred 2 | Pred 3 | Row total |
|---|---|---|---|---|
| Actual 1 | 510 × 100 = 51,000 | 70 × 50 = 3,500 | 20 × 0 = 0 | 54,500 |
| Actual 2 | 29 × 0 = 0 | 210 × 100 = 21,000 | 61 × 50 = 3,050 | 24,050 |
| Actual 3 | 10 × 0 = 0 | 10 × 50 = 500 | 80 × 200 = 16,000 | 16,500 |

The total is 95,050, so the benefit per patient is 95.05 and ⌊x⌋ = **95**.

**Step 3: robustness.** With the other possible split from the shared setup (30 and 60), row 2 gives 21,000 + 3,000 = 24,000, the total is 95,000, and the answer is 95.00 → 95. Same answer.

**What to remember:** *M3 Fill the whole table.* When an answer needs every cell, rebuild the full count table from the row totals, the diagonal, the given off-diagonal numbers and a specificity, and check the row and column sums. Before multiplying two tables, check that they use the same orientation. (Same move: [practice set 01, problem 1.5](../../practice/01-metrics.md).)

**Common trap:** using the paper's background layout (rows = predicted) for the counts while the benefit matrix has rows = actual. Multiplying mismatched cells gives 93.

</details>

---

### B2 Q1: Recall@k Calculation

<details><summary>Hint 1: understand the question</summary>

Recall@5 looks only at the first 5 chocolates in Charlie's order. Its denominator R is the number of relevant chocolates in the *whole city*, not in his basket.

</details>

<details><summary>Hint 2: the key idea</summary>

List the relevant chocolates (Relevance > 0). How many are there, and how many of them are among the first five he bought?

</details>

<details><summary>Answer</summary>

**25**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: definitions** (from the background box):
- Recall@k = (relevant chocolates in the top k) ÷ R, where R is the number of relevant chocolates anywhere.
- Precision@k = (relevant in the top k) ÷ k.

**Step 1: the relevant set.** D1 (10), D5 (3), D8 (5) and D9 (3), so R = 4.

**Step 2: cut the list at k = 5.** [D2, D3, D5, D6, D7, D8] → D2, D3, D5, D6, D7. D8 is 6th, so it doesn't count. Of these five, only D5 is relevant.

Recall@5 = 1/4 = 0.25, so the answer is **25**.

**What to remember:** *M12 Ranking-metric mechanics.* Cut the list at k first, then count. Recall divides by *all* relevant items, while precision divides by k. (Practice: [set 04, problem 4.4](../../practice/04-ranking-retrieval.md).)

**Common trap:** counting D8 (position 6), or dividing by the number of chocolates bought instead of R.

</details>

---

### B2 Q2: Comparison of Ranking Strategies

<details><summary>Hint 1: understand the question</summary>

Compute both scores for all 9 chocolates. Which chocolates does each strategy put at the top, and what is different between the two?

</details>

<details><summary>Hint 2: the key idea</summary>

No k is given, so you must decide what "retrieved" means. A natural reading: a strategy retrieves the chocolates it gives a **positive** score, because score 0 means "not interested". Compute precision and recall for each retrieved set.

</details>

<details><summary>Hint 3: set it up</summary>

A retrieves the chocolates with *both* cocoa and hazelnut. B retrieves those with *at least one* of them. Which extra chocolates does B pull in, and are any of them relevant?

</details>

<details><summary>Answer</summary>

**Option 1** (B improves recall but reduces precision), under the reading "retrieved = positive score". See the ambiguity note in the solution.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the scores.**

| Choc | Cocoa | Hazelnut | Score_A | Score_B | Relevant? |
|---|---|---|---|---|---|
| D1 | 1 | 1 | 2 | 2 | yes (10) |
| D2 | 1 | 1 | 2 | 2 | no |
| D3 | 1 | 0 | 0 | 1 | no |
| D4 | 0 | 1 | 0 | 1 | no |
| D5 | 1 | 1 | 2 | 2 | yes (3) |
| D6 | 0 | 0 | 0 | 0 | no |
| D7 | 1 | 0 | 0 | 1 | no |
| D8 | 1 | 1 | 2 | 2 | yes (5) |
| D9 | 0 | 1 | 0 | 1 | yes (3) |

**Step 2: retrieved = score > 0.**
- A retrieves {D1, D2, D5, D8}. 3 are relevant, so precision = 3/4 = 0.75 and recall = 3/4 = 0.75.
- B retrieves {D1, D2, D3, D4, D5, D7, D8, D9}. All 4 relevant are in it, so precision = 4/8 = 0.5 and recall = 4/4 = 1.

B catches D9 (hazelnut but no cocoa), so recall goes **up**. It also pulls in D3, D4 and D7, which have no ticket, so precision goes **down**. That is **option 1**.

Under this reading the tie-breaking rule never matters, because a chocolate is either retrieved or not. That fits the question's own wording, which first says "ties broken arbitrarily".

**Step 3: the ambiguity (a teaching point).** Suppose "retrieved" meant "the top k of the ranking" instead. With ties broken by ID:
- A ranks D1, D2, D5, D8, D3, D4, **D6**, D7, D9.
- B ranks D1, D2, D5, D8, D3, D4, **D7**, D9, D6.

The first six are identical, and position 7 just swaps one empty chocolate for another. So for **every k ≤ 7**, precision and recall are identical (option 5 would be true). At **k = 8**, B is better on both (option 4). At **k = 9** they are identical again. The answer depends entirely on what "retrieved" means. The positive-score reading is the only one that doesn't need a k the question never gave.

**What to remember:** *M12 Ranking-metric mechanics* plus *M1 Read the definition.* Loosening a filter ("either ingredient" instead of "both") can only *add* items, so recall can't go down. Precision drops if the added items are mostly irrelevant. When a metric needs k and none is given, pin down what "retrieved" means before you compute, and write down your reading.

**Common trap:** choosing option 5 because the tops of the two lists match. That's true for small k, but the two strategies differ in *what they retrieve at all*.

</details>

---

### B2 Q3: Discounted Cumulative Gain

<details><summary>Hint 1: understand the question</summary>

Compute DCG for both lists. Which is bigger? Then look at the most relevant chocolate, D1 (relevance 10). Where is it in A, and where in B?

</details>

<details><summary>Hint 2: the key idea</summary>

The position weights 1/log₂(i + 1) are 1, 0.631, 0.5, 0.431. Write DCG_B − DCG_A position by position as (change in relevance) × (weight). Which position produces B's advantage? Then test each option: would that property make B win?

</details>

<details><summary>Answer</summary>

**Option 6** (none of the above). See the note in the solution about option 2.

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: log₂ and the weights.** log₂ n is the power you raise 2 to in order to get n: log₂ 2 = 1, log₂ 4 = 2, log₂ 3 ≈ 1.585. Position i gets weight 1/log₂(i + 1):

| Position i | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Weight | 1/1 = 1 | 1/1.585 = 0.631 | 1/2 = 0.5 | 1/2.32 = 0.431 |

DCG@4 = Σ relevance × weight. The weight falls steeply from rank 1 to rank 2 and only gently after that.

**Step 1: compute both.**
- A = [D5, D1, D8, D2], relevances [3, 10, 5, 0]: 3(1) + 10(0.631) + 5(0.5) + 0 = 3 + 6.31 + 2.5 = **11.81**.
- B = [D8, D5, D1, D2], relevances [5, 3, 10, 0]: 5(1) + 3(0.631) + 10(0.5) + 0 = 5 + 1.89 + 5 = **11.89**.

B wins, but only narrowly.

**Step 2: where does B's advantage come from?** Position by position, B − A:
- position 1: (5 − 3) × 1 = **+2.00**
- position 2: (3 − 10) × 0.631 = **−4.42**
- position 3: (10 − 5) × 0.5 = **+2.50**
- net: **+0.08**

B puts a 5 instead of a 3 in the top slot, which has the biggest weight, and that gain just outweighs the cost of moving D1 (relevance 10) from rank 2 *down* to rank 3. The cost is small because the weights at ranks 2 and 3 (0.631 and 0.5) are close.

**Step 3: test each option.**
1. "Depends only on how many relevant appear": false. A and B contain the same chocolates, yet their DCGs differ.
2. "Strong weight to placing the highest-relevance document as early as possible": this property would favour **A**, because A has D1 at rank 2 and B has it at rank 3. It cannot explain preferring B.
3. "Treats all non-zero relevances as equal": false, since DCG uses the actual values 10, 5, 3. And if it were true, A and B would tie, because both have relevant chocolates at ranks 1–3.
4. "Ignores all ranks after the first": that *would* prefer B (5 > 3), but it isn't a property of DCG, which counts all four ranks.
5. "Penalises irrelevant more than it rewards relevant": DCG never penalises (an irrelevant item adds 0), and both lists have D2 at rank 4 anyway.

None fits, so the answer is **option 6**.

> **Note.** Option 2 is the tempting answer and may be what the setters had in mind, since it describes what DCG is *for* in general. But read the lists: in B the most relevant chocolate is placed *later*. We go with option 6. If an official key appears and says option 2, that is the reason.

**What to remember:** *M12 Ranking-metric mechanics.* Compute the metric, then explain the difference position by position. DCG's discount is steep between ranks 1 and 2 and gentle after that, so the top slot matters most. (Practice: [set 04, problem 4.3](../../practice/04-ranking-retrieval.md).)

**Common trap:** picking option 2 from a slogan ("DCG rewards putting the best document first") without checking where the best document actually is.

</details>

---

### B2 Q4: Optimal Scoring Function

<details><summary>Hint 1: understand the question</summary>

You only need the top 2 chocolates under each scoring function. Compute all four scores for all nine chocolates in one table, and apply the tie-break exactly: smaller ID first.

</details>

<details><summary>Hint 2: the key idea</summary>

Simplify before computing. Every weight is ≥ 1, so min(1, w_i) = 1, and every d_i is 0 or 1. What does Score_B become? Write n = Σd_i (the number of ingredients). Then Score_C = Score_A − n and Score_D = Score_A/(1 + n).

</details>

<details><summary>Answer</summary>

**Option 4** (Score_D only)

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: simplify.** Score_A = 3C + 3H + K + M. Score_B = Σ min(1, d_i) · 1 = n, the number of ingredients. Score_C = Score_A − n. Score_D = Score_A/(1 + n).

**Step 2: the table.**

| Choc | C H K M | n | A | B | C | D | Relevance |
|---|---|---|---|---|---|---|---|
| D1 | 1 1 0 0 | 2 | 6 | 2 | 4 | 2.00 | 10 |
| D2 | 1 1 1 0 | 3 | 7 | 3 | 4 | 1.75 | 0 |
| D3 | 1 0 1 0 | 2 | 4 | 2 | 2 | 1.33 | 0 |
| D4 | 0 1 0 0 | 1 | 3 | 1 | 2 | 1.50 | 0 |
| D5 | 1 1 0 1 | 3 | 7 | 3 | 4 | 1.75 | 3 |
| D6 | 0 0 1 1 | 2 | 2 | 2 | 0 | 0.67 | 0 |
| D7 | 1 0 0 0 | 1 | 3 | 1 | 2 | 1.50 | 0 |
| D8 | 1 1 0 0 | 2 | 6 | 2 | 4 | 2.00 | 5 |
| D9 | 0 1 1 0 | 2 | 4 | 2 | 2 | 1.33 | 3 |

**Step 3: top 2 for each, using the ID tie-break.**
- A: the top score is 7 (D2, D5), giving 1 relevant, so P@2 = 0.5.
- B: the top score is 3 (D2, D5), the same pair, so 0.5.
- C: the top score is 4, a four-way tie (D1, D2, D5, D8). By ID the top 2 are D1, D2, so 0.5.
- D: the top score is 2.00 (D1, D8). Both are relevant, so **1.0**.

Only D reaches the highest P@2, so the answer is **option 4**.

**Why D works.** Dividing by (1 + n) rewards chocolates made *mostly* of the heavy-weight ingredients (cocoa, hazelnut) and penalises extras. D2 and D5 get a high raw Score_A only because they contain a third ingredient, which has nothing to do with tickets. Score_C also penalises extras, but subtracting 1 per ingredient exactly cancels caramel's and mint's weight of 1. So D1, D2, D5 and D8 tie, and the ID tie-break gives the second slot to D2.

**What to remember:** *M12 Ranking-metric mechanics* plus *M1 Read the definition.* For P@k you only need the top k, but ties decide who gets in, so apply the tie-break rule exactly. Dividing by size (normalising) changes a ranking in a way that subtracting doesn't.

**Common trap:** ignoring the tie-break for Score_C and assuming D1 and D8 come out on top. That makes C look as good as D and leads to option 6 ("multiple").

</details>

---

### B2 Q5: Position-based Inspection Effects

<details><summary>Hint 1: understand the question</summary>

First get Score_A's full ranking (you have the scores from Q4). Which chocolates are in positions 1–5, with ties broken by ID?

</details>

<details><summary>Hint 2: the key idea</summary>

PI-Recall@5 is like Recall@5, except that a relevant chocolate at position i counts p_i instead of 1. Then divide by R, as before.

</details>

<details><summary>Answer</summary>

**27**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: the indicator.** 𝟙(Rel > 0) is 1 for a relevant chocolate and 0 otherwise. It just switches each term on or off.

**Step 1: the ranking.** Score_A: D2 7, D5 7, D1 6, D8 6, D3 4, D9 4, D4 3, D7 3, D6 2. Ties by ID: D2 before D5, D1 before D8, D3 before D9. The top 5 are **D2, D5, D1, D8, D3**.

**Step 2: weight the hits.**

| Position i | Chocolate | p_i | Relevant? | p_i × 𝟙 |
|---|---|---|---|---|
| 1 | D2 | 0.5 | no | 0 |
| 2 | D5 | 0.5 | yes | 0.5 |
| 3 | D1 | 0.3 | yes | 0.3 |
| 4 | D8 | 0.3 | yes | 0.3 |
| 5 | D3 | 0.2 | no | 0 |

The sum is 1.1. Dividing by R = 4 gives 0.275, so ⌊27.5⌋ = **27**.

**Step 3: what it means.** Plain Recall@5 would be 3/4 = 0.75. The inspection model says that, on average, Charlie actually finds only 1.1 of the 4 tickets. The ranking wastes the most-inspected slot on an empty chocolate (D2) and puts the VIP ticket (D1) third.

**What to remember:** *M12 Ranking-metric mechanics.* PI-Recall is *expected* recall: weight each hit by the chance that its position gets looked at. Get the ranking (including tie-breaks) right first; the rest is a weighted count.

**Common trap:** dividing by the cut-off 5 instead of R = 4, which gives 22. Another is breaking the D3/D9 tie the wrong way, which puts the relevant D9 at position 5 and gives 32.

</details>

---

### B3 Q1: Convolution with Custom Kernel

<details><summary>Hint 1: understand the question</summary>

Follow the paper's recipe in order: pad, then reverse the kernel, then slide with stride 2. What is the padded series, and how many outputs fit?

</details>

<details><summary>Hint 2: the key idea</summary>

The padded x is [3, 2, 1, 3, 4, 3] and the reversed kernel is [2, 1]. With stride 2, the window starts at positions 1, 3 and 5.

</details>

<details><summary>Answer</summary>

**A** [8, 5, 11]

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: convolution vs correlation.** The paper's convolution **reverses the kernel** before sliding it: y_i = Σ_j h_j · x_{i+k−j}. Sliding the kernel *without* reversing is called **(cross-)correlation**, and it's what most ML libraries call "convolution". Always check which one a paper uses. The paper's own example: x = [2, 4, 6, 8] and h = [1, −1] reversed to [−1, 1] give y = [2, 2, 2]. Without reversing you would get [−2, −2, −2].

**Step 1: pad.** Add one 3 at each end: [3, 2, 1, 3, 4, 3] (length 6).

**Step 2: reverse.** [1, 2] becomes [2, 1]. Each output is 2 × (left value) + 1 × (right value) of the window. In symbols, y_i = h₁x_{i+1} + h₂x_i = x_{i+1} + 2x_i.

**Step 3: slide with stride 2** (move the window two places each time):
- window at 1, [3, 2]: 2·3 + 1·2 = **8**
- window at 3, [1, 3]: 2·1 + 1·3 = **5**
- window at 5, [4, 3]: 2·4 + 1·3 = **11**
- a window at 7 would need positions 7 and 8, which don't exist.

y = [8, 5, 11], option **A**.

What the slips would give: without reversing you get [7, 7, 10], which isn't an option. With stride 1 you get [8, 5, 5, 10, 11]. Without padding you get [5, 10].

**What to remember:** *M1 Read the definition, not your memory.* This paper's convolution flips the kernel. The order is: pad → flip → slide by the stride → multiply and add. (Practice: [set 04, problems 4.5 and 4.6](../../practice/04-ranking-retrieval.md).)

**Common trap:** sliding the kernel unreversed, which is what NumPy's and PyTorch's "convolution" layers do.

</details>

---

### B3 Q2: Signal Smoothness vs Fluctuations

<details><summary>Hint 1: understand the question</summary>

Start with the easiest requirement: which kernels give S = 0 for a constant signal such as [5, 5, 5, 5, 5]? That removes some options immediately.

</details>

<details><summary>Hint 2: the key idea</summary>

For the survivors, don't compute every y_i. Write y_i in terms of the steps d_i = x_{i+1} − x_i and add them up: most of the terms cancel. (This is called *telescoping*.)

</details>

<details><summary>Hint 3: set it up</summary>

For h = [1, −2, 1], y_i = x_{i+2} − 2x_{i+1} + x_i. Rewrite that as (x_{i+2} − x_{i+1}) − (x_{i+1} − x_i), then add up all the y_i.

</details>

<details><summary>Answer</summary>

**C** [1, −2, 1]

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the formula for a length-3 kernel.** Because the kernel is reversed, h₁ multiplies the *rightmost* value in the window: y_i = h₁x_{i+2} + h₂x_{i+1} + h₃x_i, for i = 1, …, n − 2.

**Step 2: the constant test.** If every x_i = c, then each y_i = c(h₁ + h₂ + h₃). For S = 0 you need **h₁ + h₂ + h₃ = 0**. That rules out A [1, 1, 1] (sum 3) and E [0, 1, 0] (sum 1). The survivors are B, C, D and F.

**Step 3: telescoping.** A sum *telescopes* when each term is "something minus the previous something", so all the middle pieces cancel: (b − a) + (c − b) + (d − c) = d − a. For example, (4 − 2) + (6 − 4) + (8 − 6) = 8 − 2.

- **C [1, −2, 1]:** y_i = (x_{i+2} − x_{i+1}) − (x_{i+1} − x_i) = d_{i+1} − d_i. Adding them, S = (d₂ − d₁) + (d₃ − d₂) + … = d_{n−1} − d₁, the **last step minus the first step**.
  - x = [2, 4, 6, 8, 10]: S = (10 − 8) − (4 − 2) = **0**.
  - z = [2, 6, 3, 10, 4]: S = (4 − 10) − (6 − 2) = **−10**, so |S| = 10.

  Smooth gives 0 and fluctuating gives 10. ✓
- **B [−1, 0, 1]:** y_i = x_i − x_{i+2}, so S = (x₁ + x₂) − (x_{n−1} + x_n). x gives −12 and z gives −6, so the smooth signal scores *higher*. ✗
- **F [1, 0, −1]:** y_i = x_{i+2} − x_i. x gives 12 and z gives 6: this measures the overall rise. ✗
- **D [−1, 1, 0]:** y_i = x_{i+1} − x_{i+2}, so S = −(x_n − x₂). x gives −6 and z gives 2. ✗

The answer is **C**.

**Step 4: the limits of this detector.** S for [1, −2, 1] compares only the last step with the first. It is exactly 0 for any straight-line signal, which is why it passes the "smooth → small" test. But a very jumpy signal like [2, 10, 2, 10, 2, 10] *also* gives S = (10 − 2) − (10 − 2) = 0. So C is the best of these options, not a perfect volatility detector. Q4 shows the fix: add up absolute values instead.

**What to remember:** *M11 Kernels telescope.* When a kernel's entries add to 0, write y_i as a difference of differences and add up. Most terms cancel, and S depends only on the ends of the signal. (Practice: [set 04, problem 4.5](../../practice/04-ranking-retrieval.md).)

**Common trap:** grinding through all six kernels on both signals, which is slow and error-prone. Another is forgetting to reverse: for the symmetric C it makes no difference, but for B, D and F it flips the sign.

</details>

---

### B3 Q3: Signal Acceleration

<details><summary>Hint 1: understand the question</summary>

"Constant velocity → S = 0" means S must be 0 for any straight-line signal, such as [1, 3, 5, 7, 9]. Which kernels pass that test?

</details>

<details><summary>Hint 2: the key idea</summary>

You already know from Q2 what S is for [1, −2, 1]: last step minus first step. What sign does that have for an accelerating signal, and for a decelerating one?

</details>

<details><summary>Answer</summary>

**C** [1, −2, 1]

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: velocity and acceleration for a list of numbers.** *Velocity* is the step between neighbours, d_i = x_{i+1} − x_i. *Acceleration* is how the step changes, d_{i+1} − d_i (the "second difference").

**Step 1: the constant-velocity test.** Try the straight line [1, 3, 5, 7, 9], whose step is always 2. Using y_i = h₁x_{i+2} + h₂x_{i+1} + h₃x_i:
- A [1, 1, 1]: every y_i ≥ 9, so S ≠ 0. ✗
- B [−1, 0, 1]: y_i = x_i − x_{i+2} = −4 each, so S = −12. ✗
- **C [1, −2, 1]:** y_i = d_{i+1} − d_i = 2 − 2 = 0, so S = 0. ✓
- D [−1, 1, 0]: y_i = −d_{i+1} = −2 each, so S = −6. ✗
- E [1, 0, −1]: y_i = x_{i+2} − x_i = 4 each, so S = 12. ✗
- F [0, 1, −1]: y_i = x_{i+1} − x_i = 2 each, so S = 6. ✗

Only C passes.

**Step 2: check the signs.** From Q2, S = (last step) − (first step).
- x = [1, 2, 4, 7, 11]: S = 4 − 1 = **3 > 0**. ✓
- w = [1, 5, 8, 10, 11]: S = 1 − 4 = **−3 < 0**. ✓

The answer is **C**.

It's the same kernel as Q2. Here you see what it naturally measures: [1, −2, 1] is the list version of acceleration (a "second derivative").

**What to remember:** *M11 Kernels telescope.* [1, −2, 1] is a difference of differences, which is acceleration. Summed, it telescopes to (last step − first step).

**Common trap:** choosing a first-difference kernel such as F [0, 1, −1]. That measures *velocity*: it is positive for any rising signal, whether it is speeding up or not.

</details>

---

### B3 Q4: Spikes in Signals

<details><summary>Hint 1: understand the question</summary>

Start with the cheap tests. Which kernels give S^abs = 0 for a constant signal? Of those, which give S^abs = 0 (or small) for the smooth z = [2, 3, 4, 5, 6, 7]?

</details>

<details><summary>Hint 2: the key idea</summary>

At a spike the signal goes up and then down, so the *step changes a lot*. Which kernel measures change in steps? And why does this question add up |y_i| rather than y_i? Think about what telescoping did in Q2.

</details>

<details><summary>Answer</summary>

**B** [−1, 2, −1]

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the constant test.** A constant signal c gives every y_i = c(h₁ + h₂ + h₃), so you need a sum of 0. That rules out A [1, 1, 1], D [0, 1, 0] and E [1, −1, 1] (sum 1). B, C and F survive.

**Step 2: the smooth test.** z = [2, 3, 4, 5, 6, 7] is a straight line with step 1.
- **B [−1, 2, −1]:** y_i = −x_i + 2x_{i+1} − x_{i+2} = −(second difference), which is 0 on a straight line, so S^abs = **0**. ✓
- C [−1, 0, 1]: y_i = x_i − x_{i+2} = −2 each, so S^abs = 8. ✗ (not small)
- F [0, 1, −1]: y_i = x_{i+1} − x_i = 1 each, so S^abs = 4. ✗

**Step 3: the spike.** x = [2, 3, 8, 3, 2, 3] with B (B is symmetric, so reversing changes nothing):
- y₁ = −2 + 2·3 − 8 = −4
- y₂ = −3 + 2·8 − 3 = **10** (the spike)
- y₃ = −8 + 2·3 − 2 = −4
- y₄ = −3 + 2·2 − 3 = −2

S^abs = 4 + 10 + 4 + 2 = **20**, which is large. ✓ The answer is **B**.

**Step 4: why the absolute value matters.** Without it, S = −4 + 10 − 4 − 2 = **0**. The big positive value at the spike is cancelled by the negative "shoulders" beside it. It's the telescoping from Q2 again: S = −[(last step) − (first step)] = −[(3 − 2) − (3 − 2)] = 0. A plain S would never see the spike, and the absolute value stops the cancelling.

([−1, 2, −1] is Q2 and Q3's [1, −2, 1] with the sign flipped. The absolute value makes the sign irrelevant.)

**What to remember:** *M11 Kernels telescope.* For a zero-sum kernel the plain sum collapses to the ends of the signal, so *local* events like spikes cancel out. To catch local events, add up absolute values.

**Common trap:** picking E [1, −1, 1] because it also scores 20 on the spike. It fails the constant test: a constant signal c gives c at every position.

</details>

---

### B3 Q5: Signal Symmetry

<details><summary>Hint 1: understand the question</summary>

A length-4 signal, a length-4 kernel and no padding: how many outputs are there? Write that one output y as a formula in x₁, x₂, x₃, x₄ (remember the kernel is reversed).

</details>

<details><summary>Hint 2: the key idea</summary>

A symmetric length-4 signal has x₄ = x₁ and x₃ = x₂. Substitute these into your formula. What must be true of h for y to be 0 *whatever* x₁ and x₂ are?

</details>

<details><summary>Answer</summary>

**D** [1, −1, 1, −1]

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: one output.** m = n − k + 1 = 4 − 4 + 1 = 1. With the reversed kernel:

y = h₁x₄ + h₂x₃ + h₃x₂ + h₄x₁.

**Step 2: impose symmetry.** Put x₄ = x₁ and x₃ = x₂:

y = (h₁ + h₄)x₁ + (h₂ + h₃)x₂.

For this to be 0 for *every* x₁ and x₂, both brackets must be 0. (Try x = [1, 0, 0, 1], which gives y = h₁ + h₄, and x = [0, 1, 1, 0], which gives y = h₂ + h₃.) So **h₁ = −h₄ and h₂ = −h₃**: the kernel must be *antisymmetric*, meaning that read backwards it is its own negative.

**Step 3: check the options against that rule** (no signals needed):

| Option | h | h₁ + h₄ | h₂ + h₃ | Pass? |
|---|---|---|---|---|
| A | [−1, 2, −1, 0] | −1 | 1 | no |
| B | [1, −1, −1, 1] | 2 | −2 | no |
| C | [1, −2, 1, 0] | 1 | −1 | no |
| **D** | **[1, −1, 1, −1]** | **0** | **0** | **yes** |
| E | [1, −2, 0, −1] | 0 | −2 | no |
| F | [1, 0, −1, 0] | 1 | −1 | no |

Only D passes. Check it on the paper's signals:
- x = [2, 5, 5, 2]: y = 1·2 − 1·5 + 1·5 − 1·2 = **0** ✓
- z = [1, 2, 3, −1]: y = 1·(−1) − 1·3 + 1·2 − 1·1 = **−3 ≠ 0** ✓

**Step 4: the limits.** D gives y = (x₄ − x₁) − (x₃ − x₂). The asymmetric signal [0, 0, 1, 1] gives y = 1 − 1 = 0, so D misses some asymmetric signals. One output number can't catch every kind of asymmetry. D is the only option that *never* raises a false alarm on a symmetric signal, which is what the question asks for.

**What to remember:** *M10 Kill options with counterexamples* plus *M11.* Write the output as a formula in the x's, impose the condition (here x₄ = x₁, x₃ = x₂), and read off what the kernel's numbers must satisfy. Then check every option against that rule instead of trying random signals.

**Common trap:** choosing B [1, −1, −1, 1] because the kernel itself *looks* symmetric. A symmetric kernel gives a symmetric signal a big non-zero output (−6 for [2, 5, 5, 2]). To cancel a symmetric signal you need an *antisymmetric* kernel.

</details>

---

### B4 Q1: Reverse Engineering the Weights

<details><summary>Hint 1: understand the question</summary>

Look at X. Rows 1–4 each contain a single 1. What does that tell you about s₁, s₂, s₃, s₄ in terms of the weights?

</details>

<details><summary>Hint 2: the key idea</summary>

Row 1 gives w₁ directly, row 3 gives w₃, and so on. For s^A, the known values give w₁, w₃ and w₄ directly, and row 5 (features 1 and 2) then gives w₂. Do the same for s^B. Then fill in the "?"s and compare the predictions with y.

</details>

<details><summary>Answer</summary>

**5**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: terms.**
- **Score** z_i = w·x_i = Σ_j w_j x_ij, a *dot product*: multiply matching entries and add them. Example: w = (2, −1) and x = (3, 4) give 6 − 4 = 2.
- **Prediction:** 1 if z > 0, otherwise 0. A score of exactly 0 predicts 0.
- **ℓ1 norm:** ‖w‖₁ = the sum of the absolute values of the entries. ‖(3, −4)‖₁ = 3 + 4 = 7.

**Step 1: what each row says.** s₁ = w₁, s₂ = w₂, s₃ = w₃, s₄ = w₄, s₅ = w₁ + w₂, s₆ = w₁ + w₃ + w₄.

**Step 2: option A**, s^A = [2, ?, 1, −1, 1, ?].
- From rows 1, 3, 4: w₁ = 2, w₃ = 1, w₄ = −1.
- From row 5: w₁ + w₂ = 1, so w₂ = −1.
- w^A = (2, −1, 1, −1). Filling the gaps: s₂ = −1 and s₆ = 2 + 1 − 1 = 2.
- s^A = [2, −1, 1, −1, 1, 2], so ŷ = [1, 0, 1, 0, 1, 1], which equals y: **6/6 correct**.

**Step 3: option B**, s^B = [3, −5, ?, −1, ?, 1].
- From rows 1, 2, 4: w₁ = 3, w₂ = −5, w₄ = −1.
- From row 6: 3 + w₃ − 1 = 1, so w₃ = −1.
- w^B = (3, −5, −1, −1). Filling the gaps: s₃ = −1 predicts 0, but y₃ = 1 ✗. s₅ = 3 − 5 = −2 predicts 0, but y₅ = 1 ✗.
- **4/6 correct.**

**Step 4: the answer.** w\* = w^A, and ‖w\*‖₁ = |2| + |−1| + |1| + |−1| = **5**.

**What to remember:** *M15 Linear-classifier mechanics.* A score is the dot product of a row with w. Rows with a single 1 read off one weight directly, and the mixed rows then pin down the rest. Predictions use a strict "> 0".

**Common trap:** reporting ‖w^B‖₁ = 10 (the bigger vector rather than the more accurate one), or adding the weights without absolute values (2 − 1 + 1 − 1 = 1).

</details>

---

### B4 Q2: Finding the Optimal Pruning Strategy

<details><summary>Hint 1: understand the question</summary>

Before pruning anything, compute all 7 scores and the accuracy. Then ask what each feature contributes to each row.

</details>

<details><summary>Hint 2: the key idea</summary>

Make a "contribution table" whose entries are x_ij · w_j. Pruning feature j deletes column j from every row's sum. Which feature can you prune for free? When you prune another one, which rows flip?

</details>

<details><summary>Hint 3: set it up</summary>

w₇ = 0, so column 7 contributes nothing, however big its entries look. You must still prune one more feature. For each candidate, check which rows cross the threshold of 0.

</details>

<details><summary>Answer</summary>

**42**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: contributions x_ij · w_j.**
- Features j = 1…5 have w_j = −1. Column j holds −1 in row j and +1 in row 7, so feature j adds **+1 to row j** and **−1 to row 7**.
- Feature 6 has w₆ = 1. It adds **+1 to row 6** and **+5 to row 7**.
- Feature 7 has w₇ = 0, so it adds **0 everywhere**. Its big entries (3, −2, 6, 7, −6, −9) are all multiplied by 0. They are a distraction.

Unpruned scores: rows 1–6 score 1 and predict 1 ✓. Row 7 scores −5 + 5 + 0 = 0, which predicts 0 because 0 is not > 0 ✓. **Accuracy 7/7.**

**Step 2: what's the best possible?** You must prune exactly two features, and only one weight is 0. So at least one nonzero feature j has to go, and that drops row j's score from 1 to 0, which is wrong. The best possible is therefore **6/7**.

**Step 3: pair feature 7 (free) with each other feature.**
- j ∈ {1, …, 5}: row j drops to 0 (wrong). Row 7 becomes 0 − (−1) = +1, which predicts 1 (wrong). **5/7.**
- j = 6: row 6 drops to 0 (wrong). Row 7 becomes 0 − 5 = −5, which predicts 0 ✓. **6/7.**

Any pair without feature 7 removes two nonzero features, so at least two rows go wrong: at most 5/7.

The best pair is uniquely **{6, 7}**, and j\* · k\* = **42**.

**What to remember:** *M15 Linear-classifier mechanics.* Pruning feature j subtracts column j's contribution x_ij · w_j from every score. Build the contribution table; a zero weight is free to prune. Then track exactly which rows cross 0.

**Common trap:** being distracted by column 7's large numbers, which are multiplied by w₇ = 0. Another is forgetting that a score of exactly 0 predicts class 0.

</details>

---

### B4 Q3: Bias Correction for Improved Performance

<details><summary>Hint 1: understand the question</summary>

Write down the pruned score vector from Q2. Adding b shifts every score by the same amount. For each row, which values of b make its prediction correct?

</details>

<details><summary>Hint 2: the key idea</summary>

Each row gives one inequality on b. Find the values of b that satisfy all of them, then apply the tie-break rule.

</details>

<details><summary>Answer</summary>

**43**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: bias.** The bias b is a constant added to every score. It slides the decision threshold. For example, scores [1, 0, −5] with b = 1 become [2, 1, −4].

**Step 1: pruned scores** (w₆ = w₇ = 0): rows 1–5 score 1, row 6 scores 0, row 7 scores −5.

**Step 2: one condition per row.**
- Rows 1–5 (y = 1): 1 + b > 0, so b > −1, i.e. b ≥ 0 for whole numbers.
- Row 6 (y = 1): 0 + b > 0, so b ≥ 1.
- Row 7 (y = 0): −5 + b ≤ 0, so b ≤ 5.

All 7 rows are correct exactly when 1 ≤ b ≤ 5. From the allowed set {−3, …, 3}, that is **b ∈ {1, 2, 3}**.

| b | −3 | −2 | −1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|
| Accuracy | 1/7 | 1/7 | 1/7 | 6/7 | 7/7 | 7/7 | 7/7 |

**Step 3: tie-break.** Choose the smallest |b|, so b\* = 1. The answer is ⌊42 + 1⌋ = **43**.

**Connection to the background box.** The paper's correction b' = b + μ_S would add the average removed contribution. The removed contributions are (0, 0, 0, 0, 0, 1, 5), so μ_S = 6/7 ≈ 0.86, which gives 7/7 as well. b = 1 is the whole-number version of that shift.

**What to remember:** *M15 Linear-classifier mechanics.* A bias shifts every score by the same amount. Each example gives one inequality on b; intersect them, then apply the tie-break rule.

**Common trap:** forgetting that the threshold is strict. With b = 0, row 6 sits at exactly 0 and predicts class 0, which is wrong. Another trap is picking b = 3 (the largest) instead of following the "smallest |b|" rule.

</details>
