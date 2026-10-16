# Set 02 solutions: Probability & Bayes

> Make a real attempt first (10–15 min per problem). Then open **one** hint, try again, and only then open the next. If a symbol or word in a problem is new to you, open Hint 1 straight away: it explains the notation, and notation is not something to struggle with. You can check a final answer without spoilers in `notebooks/02_probability.ipynb`.

---

### 2.1 The AI-essay detector

<details><summary>Hint 1: understand the question</summary>

Notation first. **P(A | B)** is read "the probability of A *given* B". It means: look only at the cases where B is true, and ask what fraction of them also have A. This is called a **conditional probability**.

Tiny example: a class has 12 girls (3 wear glasses) and 18 boys (5 wear glasses). P(glasses | girl) = 3/12 = 0.25: look only at girls. P(girl | glasses) = 3/8 = 0.375: look only at the 8 glasses-wearers. Same two words, opposite order, different numbers.

Now translate the problem:
- "flags 95% of AI-written essays" is P(flagged | AI) = 0.95.
- "wrongly flags 4% of human essays" is P(flagged | human) = 0.04.
- Part (a) asks for P(AI | flagged).

The detector tells you "flagged, given AI". You want "AI, given flagged". Which essays are inside the group "flagged"? Do they all come from the AI pile?
</details>

<details><summary>Hint 2: the key idea</summary>

Move **M2 (Natural frequencies)**: stop working with percentages. Pretend there are exactly **1,000 essays** and count how many land in each box: AI and flagged, AI and not flagged, human and flagged, human and not flagged. The answer is then one count divided by another.

For (b): of the essays the first detector flagged, which ones will the second detector flag too?
</details>

<details><summary>Hint 3: set it up</summary>

Of 1,000 essays, 10% = 100 are AI-written and 900 are human-written. Fill in the table.

| | Flagged | Not flagged |
|---|---|---|
| AI (100) | ? | ? |
| Human (900) | ? | ? |

P(AI | flagged) = (AI and flagged) ÷ (all flagged).

For (b), take only the flagged essays from your table and run the second detector on them.
</details>

<details><summary>Answer</summary>

(a) **72** (b) **98**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: estimate first.** The detector catches 95% of AI essays, so it is tempting to say a flagged essay is 95% likely to be AI. But only 1 essay in 10 is AI. Human essays outnumber AI essays 9 to 1, so even a small 4% false-alarm rate on humans will produce a fair number of flags. Expect an answer well below 95.

**Step 2: turn rates into counts (1,000 essays).**
- AI = 10% of 1,000 = 100. The detector flags 95% of them: 0.95 × 100 = **95**.
- Human = 900. The detector wrongly flags 4% of them: 0.04 × 900 = **36**.

| | Flagged | Not flagged | Total |
|---|---|---|---|
| AI | 95 | 5 | 100 |
| Human | 36 | 864 | 900 |
| Total | 131 | 869 | 1,000 |

**Step 3: read off the answer.** "Given flagged" means: look only at the Flagged column. It holds 131 essays, and 95 of them are AI. P(AI | flagged) = 95/131 = 0.725, so ⌊100 × 0.725⌋ = **72**.

Stop and notice: 36 of the 131 flags, about 1 in 4, land on a student who wrote their own essay.

**Step 4: where Bayes' rule comes from.** You just used Bayes' rule without needing a formula. Write each count from Step 2 in symbols:
- 95 = 1,000 × P(AI) × P(flagged | AI) = 1,000 × 0.1 × 0.95
- 36 = 1,000 × P(human) × P(flagged | human) = 1,000 × 0.9 × 0.04
- 131 = 95 + 36 = 1,000 × P(flagged)

Divide the first line by the last. The 1,000 cancels, and you get

P(AI | flagged) = P(AI) × P(flagged | AI) ÷ P(flagged).

That is **Bayes' rule**. It flips a conditional probability around ("flagged given AI" into "AI given flagged"). The 10% you started with, P(AI), is called the **prior**: what you believed before any evidence. The 72% is the **posterior**: what you believe after seeing the flag. If you ever forget the formula, rebuild the 1,000-essay table and it comes back.

**Step 5: (b) what "independent" means here.** Two events are **independent** if knowing that one happened doesn't change the probability of the other. Tiny example: two coin flips. The first landing heads doesn't change the 1/2 chance on the second.

Here it means: once you know what *kind* of essay it is, the second detector's chance of flagging it doesn't depend on what the first detector did. An AI essay gets flagged by detector 2 with probability 0.95, whatever detector 1 said. (Careful: the two flags are *not* independent if you don't know the kind of essay. If detector 1 flags, the essay is probably AI, so detector 2 will probably flag it too. The independence holds within each kind of essay.)

**Step 6: (b) count.** Start from the 131 flagged essays in the table and run detector 2 on them:
- The 95 AI essays: 95% get flagged again, 0.95 × 95 = 90.25.
- The 36 human essays: 4% get flagged again, 0.04 × 36 = 1.44.

Fractions of an essay are fine: they are averages. (With 100,000 essays instead of 1,000 you get whole numbers, 9,025 and 144, and the same ratio.)

P(AI | both flagged) = 90.25 ÷ (90.25 + 1.44) = 90.25/91.69 = 0.984, so **98**.

**Step 7: a second way to see (b).** Step 6 started from the flagged essays of part (a). In other words, the posterior from (a) became the prior for (b). Check it with Bayes' rule, using 72.5% as the prior: 0.725 × 0.95 ÷ (0.725 × 0.95 + 0.275 × 0.04) = 0.6888/0.6998 = 0.984. Same answer. Today's posterior is tomorrow's prior.

**What to remember:** P(A | B) and P(B | A) are different numbers. To flip one into the other, imagine 1,000 cases, fill in the table, and keep only the column you actually observed. That *is* Bayes' rule. When evidence arrives in pieces, the posterior after one piece becomes the prior for the next.

**Common trap:** answering 95 for (a), which confuses P(flagged | AI) with P(AI | flagged). The 900 human essays are what drag the answer down.
</details>

---

### 2.2 The late robot

<details><summary>Hint 1: understand the question</summary>

The bar means "given", as in 2.1. For example, P(late | S, lift working) = 0.3 means: among trips where the lift was working but the robot took the stairs anyway, 30% are late.

You never see *why* the robot was late. Before you learn whether it was late, which different *situations* could a trip be in? Notice that "took the stairs" can happen in two different situations, with two different lateness rates. How many situations are there in total?
</details>

<details><summary>Hint 2: the key idea</summary>

Move **M2 (Natural frequencies)** again: imagine 1,000 trips. For each situation, count how many trips land in it, then how many of *those* are late. "Given late" means you throw away every on-time trip and look only at what's left.
</details>

<details><summary>Hint 3: set it up</summary>

Of 1,000 trips, the lift works on 700 and is broken on 300. Split the 700: 90% take the lift, 10% take the stairs. Fill in the last column.

| Situation | Trips | Late rate | Late trips |
|---|---|---|---|
| Lift works, takes L | 630 | 0.1 | ? |
| Lift works, takes S | 70 | 0.3 | ? |
| Lift broken, takes S | 300 | 0.5 | ? |
</details>

<details><summary>Answer</summary>

**64**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: estimate first.** Before any evidence, the lift is broken on 30% of trips. A broken lift makes lateness more likely (0.5, against 0.1 or 0.3 otherwise). So learning "late" should push the 30% *up*. Expect something well above 30.

**Step 2: list every hidden situation.** A trip depends on two things you don't see: whether the lift works, and which way the robot went. A broken lift always means stairs, so there are three situations:
1. lift works, robot takes L
2. lift works, robot takes S
3. lift broken, robot takes S

Don't treat "stairs" as one situation. Stairs with a working lift (late 30% of the time) and stairs with a broken lift (late 50%, crowded) behave differently, so they need separate rows.

**Step 3: count trips in each situation (1,000 trips).**
- Lift works: 0.7 × 1,000 = 700. Of these, 0.9 × 700 = 630 take L and 70 take S.
- Lift broken: 0.3 × 1,000 = 300, and all of them take S.

Check: 630 + 70 + 300 = 1,000.

**Step 4: count late trips in each.** Late trips = trips × late rate for that situation.

| Situation | Trips | Late rate | Late trips |
|---|---|---|---|
| Lift works, L | 630 | 0.1 | 63 |
| Lift works, S | 70 | 0.3 | 21 |
| Lift broken, S | 300 | 0.5 | 150 |
| **Total** | 1,000 | | **234** |

**Step 5: keep only the late trips.** You observed "late", so throw away every on-time trip. 234 late trips remain, and 150 of them had a broken lift. P(broken | late) = 150/234 = 0.641, so ⌊100 × 0.641⌋ = **64**.

Your estimate said "well above 30". The evidence moved the belief from 30% to 64%.

**Step 6: the general recipe.** Each "late trips" entry is 1,000 × P(situation) × P(late | situation). Why multiply? P(late | situation) is the *fraction* of that situation's trips that are late, so (trips in the situation) × (that fraction) = trips that are both in the situation *and* late. Dividing one row by the total is Bayes' rule from 2.1. The recipe:
1. List every hidden situation.
2. Multiply along each branch to get "situation and evidence".
3. Keep only the rows consistent with what you observed, and divide.

This is the same shape as the Jan 18 Pit-Stop problem.

**What to remember:** when an observation could have several hidden causes, list *every* situation (including ones that look the same from outside), count "situation and evidence" for each, then divide by the total evidence.

**Common trap:** answering 50. That is P(late | broken), the question asked backwards. A second trap is merging both stairs situations into one row with a single late rate.
</details>

---

### 2.3 Naive Bayes by hand

<details><summary>Hint 1: understand the question</summary>

Decode the formula before using it.
- $\prod_w$ means "multiply together one factor for each word $w$". Here the words are free, meeting and win.
- $x_w$ is 1 if the word is in the email and 0 if it isn't.
- Anything to the power 1 is itself. Anything to the power 0 is 1.
- P(c) is the fraction of training emails in class c.
- The symbol ∝ means "proportional to": the left side equals the right side times some number, and that number is the *same for every class*.

So what does the factor $P(w\mid c)^{x_w}\,(1-P(w\mid c))^{1-x_w}$ turn into for a word that is present ($x_w = 1$)? For a word that is absent ($x_w = 0$)?
</details>

<details><summary>Hint 2: the key idea</summary>

Move **M1 (Read the definition, not your memory)**. The formula on the page says an *absent* word still counts: it contributes a factor 1 − P(w | c). "meeting" is absent, so it contributes (1 − P(meeting | c)) to each class.

Compute a score for each class: score(c) = P(c) × (factor for free) × (factor for meeting) × (factor for win). Then P(spam | email) = score(spam) ÷ (score(spam) + score(ham)).

For (b), smoothing changes only the P(w | c) numbers. Turn each fraction in the table back into a count first: 3/4 for "free" in spam means 3 of the 4 spam emails contain "free".
</details>

<details><summary>Hint 3: set it up</summary>

Priors: P(spam) = 4/10, P(ham) = 6/10. For spam, the email's three factors are: free (present) 3/4, meeting (absent) 1 − 1/4 = 3/4, win (present) 2/4.

score(spam) = 0.4 × 3/4 × 3/4 × 2/4. Now build score(ham) the same way.

For (b), the counts are: spam (N = 4): free 3, meeting 1, win 2. Ham (N = 6): free 1, meeting 4, win 1.
</details>

<details><summary>Answer</summary>

(a) **95** (b) **86**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: what the formula says, in words.** Bayes' rule (2.1) says P(class | email) is proportional to P(class) × P(email | class). The hard part is P(email | class): how likely is this exact combination of words in, say, a spam email? Naive Bayes makes a simplifying assumption: within a class, each word appears **independently** of the others (independent as defined in 2.1). That assumption is the "naive" part. It lets you multiply one factor per word, exactly as you multiplied the two detectors in 2.1(b):
- word present ($x_w = 1$): the factor is $P(w\mid c)^1 (1-P(w\mid c))^0 = P(w \mid c)$
- word absent ($x_w = 0$): the factor is $P(w\mid c)^0 (1-P(w\mid c))^1 = 1 - P(w \mid c)$

So the exponents are just compact notation for "use p if the word is there, and 1 − p if it isn't".

Why the absent factor makes sense: if 1/4 of spam emails contain "meeting", then 3/4 of spam emails *don't*. That 3/4 is the chance a spam email matches this one *on the word "meeting"*.

**Step 2: (a) score each class.** The email has free = 1, meeting = 0, win = 1. Of the 10 training emails, 4 are spam, so P(spam) = 0.4 and P(ham) = 0.6.

| | Prior | free (present) | meeting (absent) | win (present) | Score |
|---|---|---|---|---|---|
| Spam | 0.4 | 3/4 | 1 − 1/4 = 3/4 | 2/4 | 0.1125 |
| Ham | 0.6 | 1/6 | 1 − 4/6 = 2/6 | 1/6 | 0.00556 |

- Spam: 0.4 × 3/4 × 3/4 × 2/4 = 0.4 × 9/32 = 0.1125.
- Ham: 0.6 × 1/6 × 2/6 × 1/6 = 0.6 × 2/216 = 0.00556.

**Step 3: turn scores into probabilities.** "∝" means the true probabilities are these scores times one common number. The two probabilities must add to 1, so divide each score by the total:

P(spam | email) = 0.1125 ÷ (0.1125 + 0.00556) = 0.1125/0.11806 = 0.953, so **95**. (As an exact fraction it is 81/85.)

This is the 1,000-essay table from 2.1 in disguise. The scores play the role of the counts "spam and looks like this email" and "ham and looks like this email", and you divide one by their total.

**Step 4: what Laplace smoothing is, and why.** Look at a weakness of the raw fractions. Suppose some word appeared in 0 of the 4 spam emails. Then P(word | spam) = 0, and every future email containing that word gets a spam score of exactly 0, however spammy the rest of it is. One small training set would rule out spam forever. The same happens the other way: a word seen in all 4 spam emails gives 1 − P = 0 whenever it's absent.

**Laplace smoothing** fixes this by pretending you saw one extra email *with* the word and one extra email *without* it:

$P(w\mid c) = \dfrac{\text{count}+1}{N_c+2}$

Here count is the number of class-c emails containing w, and $N_c$ is the number of class-c emails. The +2 underneath is the two imaginary emails. Tiny example: 0 of 4 becomes (0 + 1)/(4 + 2) = 1/6 instead of 0, and 4 of 4 becomes 5/6 instead of 1. Every estimate gets pulled a little toward 1/2, and none can be exactly 0 or 1.

**Step 5: (b) recompute with smoothing.** First recover the counts from the fractions (3/4 means 3 of 4 spam emails, 4/6 means 4 of 6 ham emails, and so on).

| Word | Spam count (N = 4) | Smoothed | Ham count (N = 6) | Smoothed |
|---|---|---|---|---|
| free | 3 | 4/6 | 1 | 2/8 |
| meeting | 1 | 2/6 | 4 | 5/8 |
| win | 2 | 3/6 | 1 | 2/8 |

"meeting" is still absent, so its factor is 1 − (smoothed value): spam 1 − 2/6 = 4/6, ham 1 − 5/8 = 3/8. The priors stay 0.4 and 0.6, because the problem only smooths P(w | c).

- Spam: 0.4 × 4/6 × 4/6 × 3/6 = 0.0889
- Ham: 0.6 × 2/8 × 3/8 × 2/8 = 0.01406

P(spam | email) = 0.0889 ÷ (0.0889 + 0.01406) = 0.0889/0.1030 = 0.863, so **86**.

Stop and notice: the posterior dropped from 95 to 86. Smoothing pulls every word probability toward 1/2, so each word is weaker evidence than before. For example, "free" was 3/4 vs 1/6 (spam vs ham, a ratio of 4.5); after smoothing it is 4/6 vs 2/8 (a ratio of about 2.7). Weaker evidence means a less extreme posterior.

**What to remember:** Naive Bayes score = prior × one factor per word, and an absent word contributes 1 − p, not nothing. Divide each score by the sum of scores at the end. Laplace smoothing adds one imaginary "has the word" and one imaginary "doesn't", so no probability is ever exactly 0 or 1.

**Common trap:** dropping the factor for the absent word "meeting". You'd get 0.15/(0.15 + 0.0167) = 0.90, so **90** instead of 95. That's using a formula from memory (some versions of Naive Bayes do ignore absent words) instead of the one on the page.
</details>

---

### 2.4 Best of three

<details><summary>Hint 1: understand the question</summary>

This formula is the **Elo** rating system, used in chess. Each player has a rating number, and the formula turns the *gap* between two ratings into a win probability. Get a feel for it with two quick cases before part (a):
- Equal ratings, S = R. What does the formula give?
- R is 400 points higher, so (S − R)/400 = −1. What does it give now?

For (b), "best-of-3, first to 2 wins" means the match stops as soon as someone has 2 wins. Write W for a game the 1800 player wins and L for a game they lose. Which sequences of W and L win the series for the 1800 player?
</details>

<details><summary>Hint 2: the key idea</summary>

Move **M16 (Elo & series)**. Part (a) is plug-in: the exponent is (1600 − 1800)/400 = −0.5, and $10^{-0.5} = 1/\sqrt{10}$.

For (b): because the games are independent, the probability of a whole sequence is the product of its game probabilities. List the series-winning sequences, multiply along each one, then add them up.
</details>

<details><summary>Hint 3: set it up</summary>

Let p = P(the 1800 player wins one game), from (a). The series-winning sequences are WW, WLW and LWW. (Why isn't WWL on the list?)

P(WLW) = p × (1 − p) × p. Write the other two the same way and add.
</details>

<details><summary>Answer</summary>

(a) **0.760** (b) **85**
(c) Each extra game is another independent try, so luck averages out: the favourite's share of games won settles near its true 76%, and the majority (which decides the series) goes to the favourite more and more reliably.
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: get a feel for the Elo formula.** It only depends on the rating *gap* S − R.
- Equal ratings: $10^0 = 1$, so P = 1/(1 + 1) = 1/2. A fair game, as it should be.
- R is 400 points higher: $10^{-1} = 0.1$, so P = 1/1.1 = 0.909. A 400-point gap means roughly 10-to-1 odds.

A 200-point gap should land somewhere between 0.5 and 0.909.

**Step 2: (a).** R = 1800 and S = 1600, so (S − R)/400 = −200/400 = −0.5.

$10^{-0.5} = 1/10^{0.5} = 1/\sqrt{10}$. By hand: 3.16² = 9.99, so √10 ≈ 3.162 and 1/√10 ≈ 0.3162.

P = 1/(1 + 0.3162) = 1/1.3162 = 0.7597, which is **0.760** to 3 decimal places. It lands between 0.5 and 0.909, as Step 1 predicted.

**Step 3: (b) list every way to win the series.** The series stops as soon as one player has 2 wins. The 1800 player wins the series with:
- **WW**: wins games 1 and 2. Over after 2 games.
- **WLW**: wins game 1, loses game 2, wins game 3.
- **LWW**: loses game 1, wins games 2 and 3.

There is no "WWL": after WW the series is already over, so a third game never happens. Every other sequence gives the 1600 player 2 wins first.

**Step 4: the probability of each sequence.** The games are independent, so the probability of a sequence is the product of its games. With p = 0.7597 and 1 − p = 0.2403:
- P(WW) = p × p = p²
- P(WLW) = p × (1 − p) × p = p²(1 − p)
- P(LWW) = (1 − p) × p × p = p²(1 − p)

The three sequences are different histories, so they can't both happen. That means you add them:

P(series) = p² + 2p²(1 − p) = p²(1 + 2 − 2p) = **p²(3 − 2p)**.

**Step 5: plug in.** p² = 0.5772 and 3 − 2p = 1.4806, so P = 0.5772 × 1.4806 = 0.8546, giving **85**.

Does rounding p matter? With p = 0.76: 0.5776 × 1.48 = 0.8548. Still 85.

**Step 6: check the formula two ways.**
- Fair game, p = 1/2: (1/4)(3 − 1) = 1/2. A fair game gives a fair series. Good.
- Pretend they always play all 3 games, even when the series is already decided. The extra game can't change who got to 2 wins first, so the 1800 player wins the series exactly when they win at least 2 of the 3 games. "Exactly 2 wins" happens in 3 orders (WWL, WLW, LWW), each with probability p²(1 − p). "All 3 wins" is p³. Total: 3p²(1 − p) + p³ = 3p² − 2p³ = p²(3 − 2p). The same formula.

**Step 7: (c) why longer series help the favourite.** Here is the same p = 0.760 in longer series:

| Series | Best of 1 | Best of 3 | Best of 5 | Best of 7 |
|---|---|---|---|---|
| P(favourite wins) | 76% | 85% | 91% | 94% |

In a single game, the underdog wins 24% of the time just by luck. To win a long series, the underdog has to win *more than half* of many independent games, even though each game favours the opponent. As the number of games grows, the favourite's fraction of wins settles close to 76%, and a majority for the underdog becomes rarer and rarer. This is the same reason averaging many noisy measurements beats trusting one.

**What to remember:** for "first to k wins", list the winning sequences and remember that the series stops early. Independent games multiply; different sequences add. Best-of-3 gives p²(3 − 2p).

**Common trap:** using just p² (forgetting the series can go to a third game), which gives 57. Another is adding WWL as an extra way to win alongside WW, which counts the same outcome twice.
</details>

---

### 2.5 Does the AI tutor help?

<details><summary>Hint 1: understand the question</summary>

Each option is a claim about **pass rates**: passed ÷ students in a group. Read the table carefully. The first "Passed" column counts passes among tutor users. The second "Passed" column counts passes among non-users.

Some options talk about what happens *within each school*, and one talks about what happens *overall*. Which pass rates would you need to check each option?
</details>

<details><summary>Hint 2: the key idea</summary>

Move **M10 (Kill options with counterexamples)**: compute the pass rates first, then for each option look for a number that contradicts it.

Then move **M18 (Confounders)**: if the overall comparison points one way and the within-school comparisons point the other way, ask what is different about *who* uses the tutor.
</details>

<details><summary>Hint 3: set it up</summary>

School X: users 85/100, non-users 18/20. Do the same for School Y.

For "overall", add the counts across both schools *before* dividing. For example, overall tutor users passed (85 + 5) out of (100 + 20).
</details>

<details><summary>Answer</summary>

**B** (Simpson's paradox: the school is a confounder)
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: pass rates within each school.**

| Group | Passed / students | Pass rate |
|---|---|---|
| X, used tutor | 85/100 | 85% |
| X, didn't use | 18/20 | 90% |
| Y, used tutor | 5/20 | 25% |
| Y, didn't use | 32/60 | 53% |

In *both* schools, non-users pass more often.

**Step 2: overall pass rates.** Combine the schools by adding counts, not by averaging the percentages:
- Tutor users: (85 + 5)/(100 + 20) = 90/120 = **75%**
- Non-users: (18 + 32)/(20 + 60) = 50/80 = **62.5%**

Overall, tutor users pass *more* often. The direction has flipped.

**Step 3: kill the wrong options (M10).**
- **A** ("the tutor raises pass rates in both schools"): Step 1 contradicts it. In X, 85% < 90%. In Y, 25% < 53%. Killed.
- **C** ("overall, non-users pass more often"): Step 2 contradicts it. 62.5% < 75%. Killed.
- **D** ("independent"): tutor use and passing are **independent** if knowing whether a student used the tutor doesn't change their chance of passing (the definition from 2.1). Then users and non-users would pass at the same rate. Overall, 75% ≠ 62.5%. Killed.
- **E** ("the data proves the tutor lowers pass rates"): this data only *observes* who chose to use the tutor. Nobody was assigned at random. Students who chose the tutor might differ in other ways (for example, struggling students might be more likely to sign up), so the data can't *prove* what the tutor causes. Killed by the word "proves".
- **B** ("overall, users pass more often, but within each school non-users pass more often"): matches Step 1 and Step 2 exactly. **B** survives.

**Step 4: why the flip happens (M18).** Look at *where* each group studies:
- 100 of the 120 tutor users are in School X, where almost everyone passes (85–90%).
- 60 of the 80 non-users are in School Y, where pass rates are low (25–53%).

So the overall 75% for users is mostly School X's number, and the overall 62.5% for non-users is mostly School Y's number. You can see it in the weighted averages:
- users overall = (100 × 85% + 20 × 25%)/120 = 75%
- non-users overall = (20 × 90% + 60 × 53.3%)/80 = 62.5%

The "overall" comparison is really comparing *schools*, not tutor use.

The school is a **confounder**: a third factor linked to both the "treatment" (which school you're in affects whether you use the tutor) and the outcome (which school you're in affects whether you pass). Tiny example: ice-cream sales and drownings rise and fall together, but neither causes the other. Hot weather drives both. When a trend reverses after you split the data by a third factor, it is called **Simpson's paradox**.

**What to remember:** before trusting an overall comparison, ask whether the groups differ in some third factor that also affects the outcome. Split by that factor and compare within each piece. Observational data shows association; it can't prove cause.

**Common trap:** stopping at the overall numbers and concluding "the tutor helps", or swinging to E. The within-school comparisons are better evidence than the overall one, but "proves" still needs a randomised experiment.
</details>

---

### 2.6 Charging or working

<details><summary>Hint 1: understand the question</summary>

This setup is called a **Markov chain**: a system that hops between states (here W and C) where the chance of the next state depends *only* on the current state, not on how it got there. Tiny example: weather where "sunny today" means a 70% chance of sunny tomorrow, whatever happened last week.

For (a): to be working two hours from now, where could the robot be one hour from now?

For (b): "long-run fraction" asks what fraction of hours it would be working if you watched for a very long time. Do you think it matters whether it starts working or charging?
</details>

<details><summary>Hint 2: the key idea</summary>

(a) List every two-hour path that starts at W and ends at W. Multiply the probabilities along each path, then add the paths.

(b) Move **M2 (Natural frequencies)**: imagine 1,000 robots all following this rule at once, and track how many are working each hour. Eventually the number stops changing. At that point, how many robots *leave* W each hour, and how many *enter* W?
</details>

<details><summary>Hint 3: set it up</summary>

(a) The paths are W → W → W and W → C → W.

(b) Call the long-run fractions π_W and π_C. (π, "pi", is just a name here, not 3.14.) Each hour, 0.2 of the working robots leave W, and 0.6 of the charging robots enter W. Write "out of W = into W" as an equation, and use π_W + π_C = 1.
</details>

<details><summary>Answer</summary>

(a) **76** (b) **75**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: (a) list the paths.** The robot is at W now. In one hour it is at W or C. In two hours it must be at W. So there are exactly two paths:
- W → W → W: keeps working, then keeps working again. 0.8 × 0.8 = 0.64.
- W → C → W: goes to charge, then comes back. 0.2 × 0.6 = 0.12.

Why multiply along a path? The second hour's move depends only on where the robot is after the first hour (that's the Markov property). So P(first move, then second move) = P(first move) × P(second move | first move). Why add the paths? They are different histories, and both can't happen.

P(working in 2 hours) = 0.64 + 0.12 = 0.76, so **76**.

The same thing with counts: 100 robots working now. After 1 hour: 80 working, 20 charging. After 2 hours: 80 × 0.8 = 64 still working, plus 20 × 0.6 = 12 back from charging, so 76 working.

**Step 2: (b) watch it settle.** Keep going with 100 robots, once starting all working and once starting all charging:

| Hour | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Working, if all start at W | 100 | 80 | 76 | 75.2 | 75.04 | 75.01 |
| Working, if all start at C | 0 | 60 | 72 | 74.4 | 74.88 | 74.98 |

Each row uses the same rule: next hour's working = 0.8 × (working now) + 0.6 × (charging now). Both rows settle at 75, so where you start doesn't matter in the long run. A split between states that no longer changes from one hour to the next is called the **steady state**. Your estimate is now 75%. Next, see *why* it is 75.

**Step 3: balance the flows.** In the steady state, the number of working robots stays the same each hour. But robots are still moving in both directions every hour. The only way the count can stay the same is: **flow out of W = flow into W**.
- Flow out of W each hour: 20% of the working robots go to charge, 0.2 × π_W.
- Flow into W each hour: 60% of the charging robots return, 0.6 × π_C.

Set them equal: 0.2 π_W = 0.6 π_C, so π_W = 3 π_C.

Every robot is somewhere, so π_W + π_C = 1. Substitute: 3π_C + π_C = 1, so π_C = 0.25 and π_W = **0.75**, giving **75**.

Check with 1,000 robots: 750 working, 250 charging. Leaving W: 0.2 × 750 = 150. Entering W: 0.6 × 250 = 150. Balanced, so the counts stay put.

**Step 4: from a crowd of robots to one robot's hours.** The question is about one robot over many hours. The table in Step 2 shows that after a few hours, the chance that a robot is working is 0.75 no matter how it started. So over a long time, about 75% of its hours are working hours. (This holds for chains like this one, where each state can be reached from the other.)

Sense check: the robot leaves work rarely (0.2 per hour) and leaves the charger quickly (0.6 per hour), so it should spend most of its time working. 75% fits.

This fixed-point idea, "find the split that the update rule leaves unchanged", comes back in PageRank (Set 04).

**What to remember:** for a multi-step probability, list the paths, multiply along each path and add across paths. For the long run, find the steady state by setting flow out of a state equal to flow into it, then use "the fractions add to 1".

**Common trap:** in (a), answering 0.8 × 0.8 = 64 and forgetting the W → C → W path. In (b), flipping the ratio and getting 25. Ask yourself which state the robot leaves more slowly: that's where it spends more time.
</details>
