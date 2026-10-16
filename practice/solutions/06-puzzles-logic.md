# Set 06 solutions: Puzzles and logic

> Make a real attempt first (10–15 min per problem). Then open **one** hint, try again, and only then open the next. If a word or symbol in a problem is new to you, open Hint 1 straight away: notation is not something to struggle with. You can check a final answer without spoilers in `notebooks/06_puzzles_logic.ipynb`.
>
> Moves used in this set: **M8** Parity / colouring · **M10** Kill options with counterexamples · **M14** LLM reality check · **M17** Align and decode · **M1** Read the definition, not your memory.

---

### 6.1 Robot vacuum parity

<details><summary>Hint 1: understand the question</summary>

The dock (0, 1) is right next to the start, so it looks as if the robot could tour the whole room and come back. Can it really visit all 25 cells? A 5 × 5 grid has too many paths to try them all, so shrink the problem. Draw a **2 × 2** grid and a **3 × 3** grid, keep the same start (0, 0) and end (0, 1), and find the longest path on each by hand.
</details>

<details><summary>Hint 2: the key idea</summary>

On your small grids, colour the cells like a chessboard: call cell (r, c) **dark** if r + c is even and **light** if r + c is odd. Write down the colour of each cell along your best path, in order. What pattern do you see? Can you explain why it *must* happen on every path?
</details>

<details><summary>Hint 3: set it up</summary>

Every move changes r or c by exactly 1, so r + c changes by exactly 1, and the colour flips on every move. The start (0, 0) is dark and the end (0, 1) is light. Count the dark cells and the light cells on the 5 × 5 board. If a path goes dark, light, dark, light, … and ends on light, how many of each colour can it contain?
</details>

<details><summary>Answer</summary>

**24**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: try small cases first.** The 5 × 5 board is too big to search by hand, so look at smaller boards for a pattern.
- **2 × 2:** the path (0,0) → (1,0) → (1,1) → (0,1) visits all **4** cells.
- **3 × 3:** try to visit all 9. You will keep missing one. The best you can find is **8**, for example (0,0) → (1,0) → (2,0) → (2,1) → (2,2) → (1,2) → (0,2) → (0,1), which skips the centre (1,1).

Failing to find a 9-cell path is not a proof that none exists. You need a *reason*.

**Step 2: colour the board (M8).** The **parity** of a whole number is whether it is even or odd. Colour cell (r, c) by the parity of r + c: dark (D) if r + c is even and light (L) if it is odd. The 3 × 3 board looks like this, with row 0 at the top:

```
D L D
L D L
D L D
```

Now read off the colours along the 8-cell path from Step 1: D, L, D, L, D, L, D, L. They alternate.

**Step 3: why the colours always alternate.** A move up or down changes r by 1 and leaves c alone. A move left or right changes c by 1 and leaves r alone. Either way, r + c goes up or down by exactly 1, so it switches between even and odd. So **every move switches colour**, on every path, not just the one we drew.

**Step 4: what alternation forces.** Number the cells of a path 1, 2, 3, … The first cell (0, 0) is dark, so the odd-numbered cells are dark and the even-numbered cells are light. The last cell (0, 1) has 0 + 1 = 1, which is odd, so it is light. That means the path has an even number of cells, half dark and half light.

Check this on the small boards:
- 2 × 2 has 2 dark and 2 light cells, so the bound is 2 + 2 = 4. That matches: every cell can be visited.
- 3 × 3 has 5 dark and 4 light cells. A path can use at most 4 light cells, so at most 4 dark cells as well: 4 + 4 = 8. One dark cell must always be left out. That explains why 9 was impossible.

**Step 5: count the 5 × 5 board.** Rows 0, 2 and 4 have dark cells in columns 0, 2 and 4: 3 × 3 = 9. Rows 1 and 3 have dark cells in columns 1 and 3: 2 × 2 = 4. That gives 13 dark cells and 25 − 13 = 12 light cells. A path from dark to light has equal numbers of each, so it has at most 12 light + 12 dark = **24** cells.

**Step 6: show that 24 is actually reachable.** Step 5 gives an **upper bound**: a number the answer can't exceed. An upper bound is only half an answer. You also need a path that reaches it. Here is one, with each cell numbered by the step at which the robot visits it (row 0 at the top, and `.` is the skipped cell):

```
 1 24 23 22 21
 2 15 16 19 20
 3 14 17 18  .
 4 13 12 11 10
 5  6  7  8  9
```

The robot goes down column 0, along the bottom row, snakes back through the middle, and finishes along the top row into the dock. The skipped cell is (2, 4), and 2 + 4 = 6 is even, so it is dark, exactly as Step 5 predicts. (A computer search over every possible path also finds 24 as the maximum.)

**Connect:** the Jan 18 Pikachu question has a knight moving on a 5 × 5 board. Does a knight's move (2 one way, 1 the other) always flip the colour? What does colouring tell you about a knight path from (0, 0) to (4, 4)?

**What to remember:** if every move changes some quantity by exactly 1 (here r + c), colour by parity. The colours must alternate, so counting each colour gives a bound that no amount of clever path-finding can beat. Then build an example that reaches the bound.

**Common trap:** answering 25 because "the dock is right next to the start, so just tour the room". The other trap is stopping at the bound of 24 without showing a path that reaches it. The answer needs both the bound and an example.
</details>

---

### 6.2 Trace the loop

<details><summary>Hint 1: understand the question</summary>

Before tracing anything, write down exactly which values `range(1, 6)` produces. Then: which values does `range(i, 6)` produce when i = 1? When i = 4? When i = 5?
</details>

<details><summary>Hint 2: the key idea</summary>

Don't juggle it in your head. Make a table with one row for every time the innermost line runs, and the columns i, j, i + j, action, x. Fill it in row by row, updating x as you go.
</details>

<details><summary>Hint 3: set it up</summary>

i runs 1 to 5, and for each i, j runs from i up to 5. So there are 5 + 4 + 3 + 2 + 1 = 15 rows. The first two:

| i | j | i + j | action | x |
|---|---|---|---|---|
| 1 | 1 | 2 | not a multiple of 3: −1 | −1 |
| 1 | 2 | 3 | multiple of 3: + 1 × 2 | 1 |

Carry on from here.
</details>

<details><summary>Answer</summary>

**34**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: read the code exactly (M1).**
- `range(a, b)` starts at a and stops **before** b. So `range(1, 6)` gives 1, 2, 3, 4, 5. It never gives 6.
- `range(i, 6)` therefore gives i, i+1, …, 5. For i = 4 that is 4, 5. For i = 5 it is just 5.
- `%` is the remainder: 7 % 3 = 1 and 9 % 3 = 0. So `(i + j) % 3 == 0` means "i + j is a multiple of 3".
- `x += i * j` means x = x + i × j, and `x -= 1` means x = x − 1.

**Step 2: count the rows.** The inner loop runs 5 times for i = 1, then 4, 3, 2 and 1 times: 15 rows in total.

**Step 3: the trace table.**

| i | j | i + j | action | x |
|---|---|---|---|---|
| 1 | 1 | 2 | −1 | −1 |
| 1 | 2 | 3 | +2 | 1 |
| 1 | 3 | 4 | −1 | 0 |
| 1 | 4 | 5 | −1 | −1 |
| 1 | 5 | 6 | +5 | 4 |
| 2 | 2 | 4 | −1 | 3 |
| 2 | 3 | 5 | −1 | 2 |
| 2 | 4 | 6 | +8 | 10 |
| 2 | 5 | 7 | −1 | 9 |
| 3 | 3 | 6 | +9 | 18 |
| 3 | 4 | 7 | −1 | 17 |
| 3 | 5 | 8 | −1 | 16 |
| 4 | 4 | 8 | −1 | 15 |
| 4 | 5 | 9 | +20 | 35 |
| 5 | 5 | 10 | −1 | **34** |

**Step 4: check it a second way.** Split the rows into the two kinds of action.
- The rows where i + j is a multiple of 3 are (1,2), (1,5), (2,4), (3,3) and (4,5). They add 2 + 5 + 8 + 9 + 20 = 44.
- The other 15 − 5 = 10 rows each subtract 1, which is −10 in total.

So x = 44 − 10 = **34**, agreeing with the table. A second method that agrees with the first is your best defence against an arithmetic slip.

**What to remember:** trace loops with a table, one row per run of the innermost line, and write down every intermediate value. `range(a, b)` stops before b. When you can, check the total a second way.

**Common trap:** each misreading gives a different wrong answer, so if you got one of these, you know where the slip was:
- treating `range(1, 6)` as including 6 (and `range(i, 6)` too) gives 84;
- starting the inner loop at 1 instead of at i gives 63;
- forgetting the `else` branch gives 44.
</details>

---

### 6.3 Design a path-quality score

<details><summary>Hint 1: understand the question</summary>

Each rule is a test, and a formula must pass all four tests for **every** allowed d and n. How many bad inputs (d, n) do you need to throw a formula out?
</details>

<details><summary>Hint 2: the key idea</summary>

One **counterexample** (a single input where the formula breaks a rule) is enough to reject a formula. Find it with the simplest or most extreme inputs: d = 0 and n = 0; d = 0 with lots of turns; a huge d. For R4, compare Q(0, 1) with Q(2, 0).
</details>

<details><summary>Hint 3: set it up</summary>

Draw a grid with the rules R1–R4 across the top and the options A–F down the side. Put a counterexample in a cell when you find one. For the formulas that survive, you still need a reason why they pass for *every* input. For that, ask what R4 says if you apply it several times in a row: Q(d, n) = Q(d + 2, n − 1) = …
</details>

<details><summary>Answer</summary>

**A, D, F**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: what it takes to pass or fail (M10).** Each rule says "always" or "for all d and n". So a single input where a formula breaks a rule, called a **counterexample**, is enough to reject it. Accepting a formula is harder: a few passed tests prove nothing, and you need a reason that covers every input.

**Step 2: choose test inputs that stress each rule.**
- R1: Q(0, 0) must be 1, and anything else, such as Q(0, 5) or Q(5, 0), must be below 1.
- R2: try a huge input such as d = 20, where Q might drop to 0 or below.
- R3: add turns with d = 0, and add metres with n = 0. Q must go down each time.
- R4: compare Q(0, 1) with Q(2, 0), and also Q(1, 1) with Q(3, 0).

**Step 3: fill in the grid.** A ✓ here only means "no counterexample found yet".

| | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| A | ✓ | ✓ | ✓ | ✓ |
| B | ✓ | ✓ | ✓ | ✗ Q(0,1) = e^(−0.5) ≈ 0.61, but Q(2,0) = e^(−2) ≈ 0.14 |
| C | ✓ | ✗ Q(20,0) = 1 − 2 = −1 | ✓ | ✓ |
| D | ✓ | ✓ | ✓ | ✓ |
| E | ✗ Q(0,5) = 1/(1+0) = 1 | ✓ | ✗ Q(0,n) = 1 for every n | ✗ Q(1,1) = 1/3, but Q(3,0) = 1 |
| F | ✓ | ✓ | ✓ | ✓ |

Notice E: it **passes** the first R4 test, because Q(0,1) = Q(2,0) = 1. It only fails on the second test. One passed test doesn't make a rule true.

Notice C: it behaves perfectly for small inputs (Q(0,1) = Q(2,0) = 0.8). It only fails when you push d up to 10 or beyond. That is why you test extreme inputs.

**Step 4: why the survivors pass for every input.** Use R4 with n − 1 in place of n: Q(d, n) = Q(d + 2, n − 1). Apply it again and again, each time swapping one turn for 2 metres:

Q(d, n) = Q(d + 2, n − 1) = Q(d + 4, n − 2) = … = Q(d + 2n, 0).

So a formula obeying R4 can only depend on the single number **s = d + 2n**, the "effective length" in which each turn counts as 2 metres. Write Q = g(s). The other rules now become rules about g:
- R1: g(0) = 1, and g(s) < 1 when s > 0. (Here s = 0 exactly when d = 0 and n = 0, because both are ≥ 0.)
- R2: 0 < g(s) ≤ 1.
- R3: g gets strictly smaller as s gets bigger. Increasing d or n always increases s.

Now check the survivors:
- **A:** g(s) = 1/(1 + s). g(0) = 1. For s > 0 the denominator is bigger than 1, so 0 < g < 1. A bigger s gives a bigger denominator, so a smaller g. ✓
- **D:** use the exponent law aᵐ · aᵏ = aᵐ⁺ᵏ: e^(−d) · e^(−2n) = e^(−(d + 2n)) = e^(−s). g(0) = e⁰ = 1. e^(−s) = 1/eˢ is always positive, and it shrinks as eˢ grows. ✓ D only *looks* different from A and F. Rewrite before you judge.
- **F:** g(s) = 2/(1 + eˢ). g(0) = 2/(1 + 1) = 1. For s > 0, eˢ > 1, so the denominator is bigger than 2 and g < 1. It is always positive. A bigger s gives a bigger eˢ, so a smaller g. ✓

The same view explains each failure. B depends on d + n/2, so a turn costs half a metre instead of 2. C does depend only on s, but 1 − s/10 reaches 0 at s = 10 and goes negative after that. E depends on the product dn, so a path with no turns at all scores 1 however long it is.

**Connect:** the Jan 18 "Smart Student Search" question asks for a similarity function that obeys a list of design rules. It is the same task, so use the same rules × options grid.

**What to remember:** to reject an option, one counterexample is enough. Find it with simple or extreme inputs (zeros, one huge value). To accept an option, you need a reason that works for every input. A rule like R4 often hides a structure (here: "Q only sees d + 2n") that makes the checking quick.

**Common trap:** accepting E because Q(0,1) = Q(2,0), or accepting C because it works for small numbers. Both pass some tests and still fail. The opposite trap is rejecting D because it looks different from the others.
</details>

---

### 6.4 Which cards to flip?

<details><summary>Hint 1: understand the question</summary>

The rule makes a promise about deployed models. Describe the one kind of model that would **break** the promise: what is on its "deployment" side, and what is on its "test" side?
</details>

<details><summary>Hint 2: the key idea</summary>

A card needs flipping only if its hidden side could turn it into that rule-breaking model. For each card, ask: "Is there any hidden side that would make this a violation?" You are looking for possible violations, not for examples that agree with the rule.
</details>

<details><summary>Hint 3: set it up</summary>

Go through the cards one at a time. Card A shows "Deployed", so its hidden side is either "Passed" or "Failed". Does either one break the rule? Now do the same for B, C and D.
</details>

<details><summary>Answer</summary>

**A and D**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: read the rule as written (M1).** Call "the model is deployed" P and "it passed the safety test" Q. The rule has the form "if P then Q". List all four kinds of model and ask which ones break it:

| Deployed? | Passed? | Breaks the rule? |
|---|---|---|
| yes | yes | no: the promise is kept |
| yes | no | **yes: deployed but failed** |
| no | yes | no |
| no | no | no |

Only "deployed **and** failed" breaks the rule. The rule makes no promise at all about models that were not deployed, so they can never break it, whatever their test result.

An everyday check: "If it rains, I take an umbrella." You carry an umbrella on a sunny day. Have you broken your promise? No. The promise was only about rainy days.

**Step 2: card by card.**
- **A (Deployed):** the hidden side could be "Failed", which would be a violation. **Flip it.**
- **B (Not deployed):** the rule says nothing about undeployed models. It can never be a violation. Leave it.
- **C (Passed):** the hidden side is "Deployed" (deployed and passed: fine) or "Not deployed" (fine). It can never be a violation. Leave it.
- **D (Failed):** the hidden side could be "Deployed", which would be a violation. **Flip it.**

**Step 3: why C tempts you.** Flipping C feels like checking the rule, because finding "Deployed" behind "Passed" seems to *confirm* it. But C can only ever show agreement, never a violation, and agreeing examples can't prove a rule. Picking C also quietly reads the rule backwards, as "if it passed, then it is deployed". That reversed statement is called the **converse**, and it is a different claim. The lab never promised to deploy every model that passes.

**Step 4: why people miss D.** The violating case contains "Failed", so any card showing "Failed" might be hiding "Deployed". Another way to see it: "if deployed, then passed" says exactly the same thing as "if failed, then not deployed". This flipped-and-negated version is called the **contrapositive**, and it is always equivalent to the original. Card D tests the contrapositive.

This is the **Wason selection task**, a famous psychology experiment from 1966. Most adults get it wrong, and most of them choose A and C.

**What to remember:** "if P then Q" is broken only by P-and-not-Q. To test it, check every case that shows P and every case that shows not-Q. Look for cases that could break the rule, not cases that could confirm it. This is the same hunt for one counterexample as in 6.3.

**Common trap:** choosing A and C. That means looking for confirmation, or reading "if" as "if and only if".
</details>

---

### 6.5 Decode the robot language

<details><summary>Hint 1: understand the question</summary>

Don't try to translate whole sentences yet. Pick one English word that appears in several sentences, such as "robot". Which robot-language words appear in those same sentences? What changes about the word from one sentence to the next?
</details>

<details><summary>Hint 2: the key idea</summary>

Line up sentences that share a word and look at **what is different** about the word when its job in the sentence is different. Compare "robo" in (1) with "robon" in (2): what is the robot doing in each sentence? Then compare "robo" with "karobo", and "mor" with "mori".
</details>

<details><summary>Hint 3: set it up</summary>

Make a table with one row per sentence. Columns: word 1, word 2, word 3, then in English: who does the action, who or what it is done to, the action, and when it happens (now or in the past). Then try to explain every extra piece you can see: the ending -n, the ending -i and the beginning ka-. Test each explanation against **all five** sentences.
</details>

<details><summary>Answer</summary>

(a) **A** (karobo veln mori) (b) **kamina kaveln taki**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 0: a few words we need.** In "The girl saw the robot":
- the **subject** is the one doing the action (the girl);
- the **object** is the one the action is done to (the robot).

**Plural** means more than one (robots). **Tense** is when the action happens: present ("sees") or past ("saw"). A **prefix** is added to the front of a word, and a **suffix** to the end.

**Step 1: align the sentences (M17).** "Robot" appears in English in (1), (2), (3) and (5). The robot-language words in those sentences that look alike are robo (1, 5), robon (2) and karobo (3), all built on **robo**. "Girl" appears in (2), (3), (4) and (5), matching mina (2, 4) and minan (3, 5), built on **mina**.

**Step 2: what does the suffix -n do?** Write down the job of each form:

| Form | Sentences | Job |
|---|---|---|
| robo | (1), (5) | subject |
| robon | (2) | object |
| mina | (2), (4) | subject |
| minan | (3), (5) | object |

-n appears exactly when the word is the object, for both nouns. **Hypothesis: -n marks the object.** Now test it on a word we haven't used: the car words veln (1) and kaveln (4) are objects in both sentences, and both end in -n ✓. So "car" on its own is *vel*, and *veln* is "car" as the object.

(Every sentence here has its object in second position. So "-n marks the second word" would fit too. For the questions asked it gives the same answers, so we don't need to decide.)

**Step 3: what does the prefix ka- do?** robo/karobo is robot/robots, and veln/kaveln is car/cars. The only thing these two pairs have in common is "one" vs "more than one". Is there another explanation? karobo appears in a present-tense sentence and kaveln in a past one, so ka- isn't about tense. karobo is a subject and kaveln is an object, so it isn't about the word's job either. **ka- marks the plural.**

**Step 4: the word order.** Now label every sentence by job: (1) robo [subject] veln [object] mor [verb], and the same pattern holds in all five. The order is always **subject, object, verb** (often shortened to SOV). The verb comes last.

**Step 5: what does the suffix -i do?** The leftover words are the verbs: mor (1, "builds"), mori (4, "built"), tak (3, "see") and taki (2 and 5, "saw"). The forms with -i are exactly the past-tense ones. **Hypothesis: -i marks the past tense.**

Now try hard to break your own hypothesis. Is there another feature that matches -i just as well?
- Look at (2) and (4) only. In both, the **subject is the girl**. If you speak Hindi, this looks very natural: in *ladka gaya* / *ladki gayi* ("the boy went" / "the girl went"), the -i ending marks a feminine subject. With only sentences (1)–(4), "-i means the girl is the subject" fits the data as well as "-i means past", and it would make the answer to (a) **C**.
- Sentence (5) separates the two. *robo minan taki* has a **robot** as its subject and still has -i. So -i is not about the girl.
- Is -i about plurals? (2) and (5) have no plurals at all, yet they have -i. No.
- Is it about which verb it is? Both "build" and "see" appear with and without -i. No.

Only tense matches all five sentences. This is why a rule must be tested against every sentence. When two features always appear together in your data, you need a sentence where they come apart.

**Step 6: the rules, all together.**

| Piece | Meaning |
|---|---|
| robo, mina, vel | robot, girl, car |
| mor, tak | build(s), see(s) |
| ka- (prefix on a noun) | plural |
| -n (suffix on a noun) | object |
| -i (suffix on a verb) | past tense |
| word order | subject, object, verb |

Check that these rules rebuild all five given sentences. (They do.)

**Step 7: (a) "The robots built the car."**
- "the robots" is a plural subject: ka + robo = **karobo**, with no -n.
- "the car" is a singular object: vel + n = **veln**.
- "built" is past: mor + i = **mori**.
- The order is subject, object, verb: **karobo veln mori**, option **A**.

Each wrong option breaks exactly one or two rules (M10):
- **B.** robo kaveln mori means "The robot built the cars" (both numbers are wrong).
- **C.** karobo veln mor is present tense: "The robots build the car."
- **D.** karobon vel mori puts the object marker on the robots and leaves it off the car.
- **E.** veln karobo mor has the object first, and is in the present tense.
- **F.** karobo kaveln mori means "The robots built the cars."

**Step 8: (b) "The girls saw the cars."** "The girls" is a plural subject: ka + mina = **kamina**. "The cars" is a plural object: ka + vel + n = **kaveln**. "Saw" is past: tak + i = **taki**. The answer is **kamina kaveln taki**.

**Going further:** this kind of problem is the core of linguistics olympiads. For real practice, use the past papers of **UKLO** (the UK Linguistics Olympiad) and the **Panini Linguistics Olympiad** (India). Both publish problems with full solutions.

**What to remember:** align sentences that share a word and change one thing at a time. Form a hypothesis, test it against **every** sentence, and actively look for a second rule that would also fit. If two features always occur together, you can't tell them apart until a sentence separates them.

**Common trap:** choosing C. Both "karobo" and "veln" are right, so your eye stops checking before it reaches the verb. The deeper trap is accepting the first rule that fits two sentences without trying to break it.
</details>

---

### 6.6 Find the rule

<details><summary>Hint 1: understand the question</summary>

Five examples, one hidden rule. Write down the simplest rule you can think of (for example, "count the 1s") and test it on **all five** examples, not just the first one. Where does it break?
</details>

<details><summary>Hint 2: the key idea</summary>

Compare the two extremes. 1111 gives 0 and 1010 gives 3, and both have four bits. What happens at every step of 1010 that never happens in 1111? Look at **neighbouring pairs** of bits, not single bits.
</details>

<details><summary>Hint 3: set it up</summary>

Write the gaps between neighbours: 1 | 0 | 1 | 0 has 3 gaps. Mark each gap where the two bits on either side are different. Do the same for all five examples and compare with f.
</details>

<details><summary>Answer</summary>

**5**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: candidate 1, the number of 1s (M10).** 0110 has two 1s, which gives 2 ✓. 1111 has four 1s, which gives 4, but f(1111) = 0 ✗. It is dead after two examples. (It fails on 1010 too: 2, not 3.)

**Step 2: candidate 2, the number of 0s.** 0110 has two 0s, giving 2 ✓. 1111 has none, giving 0 ✓. 1010 has two 0s, giving 2, but f(1010) = 3 ✗. This rule survived two tests and is *still* wrong. That's why you test against every example.

**Step 3: learn from the failures.** Both candidates looked at single bits and failed. Now look at what makes the extremes different. 1111 never changes from one bit to the next, and it gets 0. 1010 changes at every step, and it gets 3, the most a 4-bit string can have. **New candidate: count the places where a bit differs from the bit next to it.**

**Step 4: test it on all five.**

| Input | Neighbouring pairs | Pairs that differ | f | Match? |
|---|---|---|---|---|
| 0110 | 01, 11, 10 | 2 | 2 | ✓ |
| 1111 | 11, 11, 11 | 0 | 0 | ✓ |
| 1010 | 10, 01, 10 | 3 | 3 | ✓ |
| 0001 | 00, 00, 01 | 1 | 1 | ✓ |
| 1001 | 10, 00, 01 | 2 | 2 | ✓ |

All five fit.

**Step 5: apply it.** 0101101 has the pairs 01, 10, 01, 11, 10, 01. Every pair except 11 differs, so f(0101101) = **5**.

The same rule can also be described as "the number of blocks of equal bits, minus 1". For example, 0110 splits into 0 | 11 | 0, which is 3 blocks, giving 2.

**Step 6: connect it to convolution.** In Set 04 problem 4.5(a), convolving with the kernel h = [1, −1] gave the first difference, yᵢ = xᵢ₊₁ − xᵢ. Do that to the bits 0, 1, 0, 1, 1, 0, 1:

y = [1, −1, 1, 0, −1, 1].

Each entry is +1 (a jump up from 0 to 1), −1 (a jump down) or 0 (no change). Take absolute values and add them: 1 + 1 + 1 + 0 + 1 + 1 = 5. So f is "convolve with [1, −1], then add up the absolute values". That counts the **edges** in a signal, and the same filter finds edges in images. The Jan 18 question "Spikes in Signals" uses exactly this score: the sum of the absolute values of a convolution.

**What to remember:** in "find the rule" puzzles, propose a rule, test it on **every** example, and when it dies, ask what the failing example has that the others don't. Look at relationships between neighbours, not only at individual symbols.

**Common trap:** stopping as soon as the first one or two examples fit. "Count the 0s" fits both 0110 and 1111 and is still wrong.
</details>

---

### 6.7 LLM reality check

<details><summary>Hint 1: understand the question</summary>

For each task, ask two questions. (1) Is everything the model needs already in the prompt, or extremely common in ordinary text? (2) Does the task need the model to see individual letters, or to know something it could not have read during training?
</details>

<details><summary>Hint 2: the key idea</summary>

An LLM doesn't read letters. Its input is chopped into **tokens**, chunks of text that are often whole words or pieces of words, and each token is turned into a number. Also, everything it knows comes from text collected up to a fixed date. Which tasks run into one of these two walls?
</details>

<details><summary>Hint 3: set it up</summary>

Make a table with the columns: task, where the needed information comes from, which wall it hits (if any), likely result. Fill it in for A–F.
</details>

<details><summary>Answer</summary>

**A and D**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: how an LLM sees text (M14).** An LLM (large language model) produces text one token at a time, each time predicting what comes next. Before it sees your prompt, a **tokenizer** splits the text into tokens and replaces each token with an ID number. A tokenizer might split "strawberry" into "straw" + "berry", for example. (Exact splits differ between models.)

So the model never receives s, t, r, a, w, b, e, r, r, y as ten separate symbols. It receives two numbers. To count the r's, it has to *remember* how each of those tokens is spelled, which it only learned indirectly from patterns in its training text. Imagine being handed two sealed boxes labelled "straw" and "berry" and asked how many r's are inside, without opening them. "Strawberry" has 3 r's (st**r**awbe**rr**y), and chatbots have famously answered 2.

(One trick that often helps: ask the model to spell the word out first, one letter per line. Then each letter becomes its own token, and the letters are finally visible to it.)

**Step 2: how an LLM knows facts.** Everything it knows comes from text collected up to a date called its **training cutoff**. After that the model is frozen. Yesterday's cricket match happened after the cutoff of any model you can run today, and with no internet or tools, there is no way for it to look the score up. Worse, it was trained to produce likely-looking text, and a score-shaped answer looks likely. So instead of saying "I don't know", it will often produce a confident, believable, made-up score. This is called a **hallucination**.

**Step 3: go through all six.**

| Task | Where the needed information comes from | Wall? | Likely result |
|---|---|---|---|
| A. count the r's | the letters inside tokens | tokens hide letters | **often wrong** |
| B. review sentiment | the prompt | none: a classic, easy pattern task | right |
| C. "good morning" in Hindi | an extremely common phrase in training text | none | right |
| D. yesterday's score | an event after the cutoff | knowledge wall, plus a confident guess | **wrong** |
| E. summarise a paragraph | the prompt | none | right |
| F. quotation in a headline | the prompt: quote marks, words like "said" | none | right |

**Step 4: A versus F.** Both look like "inspect the characters" tasks. F asks whether a *pattern* is present: quote marks and words like "said" usually get tokens of their own, so the model can see them, and the answer is just yes or no. A needs an **exact count of letters hidden inside tokens**. Exact counting at the character level is where the token view breaks down.

**Step 5: why not C?** A small model can struggle with long or rare passages in Hindi. But "good morning" is one of the most common phrases there is, and it appears in training text in every major language. "Translation sounds hard" is a feeling about humans, not about LLMs.

**Connect:** the Jan 18 question "Filtering Fakes with Faulty Oracle" asks which features a small offline model would produce unreliably. It includes a character-count feature (F1) and a quote-presence feature (F8), just like tasks A and F here. Go back to it and run every feature, F1 to F8, past the two walls from this problem.

**What to remember:** an LLM sees **tokens, not letters**, and knows **nothing after its training cutoff**. Before trusting an output, ask: is the information in the prompt or very common? Does the task need character-level detail or exact counting? Does it need facts the model could not have seen? If either of the last two is yes, expect a confident error.

**Common trap:** assuming that a task that is easy for you (counting letters) is easy for the model. You see letters and it sees tokens. The opposite trap is picking C because translation feels hard: common phrases are among the easiest things an LLM does.
</details>
