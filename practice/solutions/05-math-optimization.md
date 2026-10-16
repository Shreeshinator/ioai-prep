# Set 05 solutions: Math engine

> Make a real attempt first (10–15 min per problem). Then open **one** hint, try again, and only then open the next. If a word or symbol in a problem is new to you, open Hint 1 straight away: notation is not something to struggle with. You can check a final answer without spoilers in `notebooks/05_math_optimization.ipynb`.

---

### 5.1 Where to put the charger?

<details><summary>Hint 1: understand the question</summary>

Each part asks for the *position* x that makes a quantity as small as possible, not for the smallest value itself. Before using any theory, try some numbers: compute the total distance Σ|x − xᵢ| at x = 2, x = 3 and x = 12. Which is smallest?
</details>

<details><summary>Hint 2: the key idea</summary>

- (a): nudge x a tiny step to the right. For each robot, does its distance go up or down? Count them.
- (b): expand the sum into a quadratic in x and find its lowest point.
- (c): only two of the robots can ever be the farthest one. Which two?
</details>

<details><summary>Hint 3: set it up</summary>

- (a): if x moves right by a tiny δ, every robot to the left of x adds δ to the total and every robot to the right subtracts δ. Where does the count of left robots overtake the count of right robots?
- (b): Σ(x − xᵢ)² = 5x² − 2(0 + 1 + 2 + 10 + 50)x + (0² + 1² + 2² + 10² + 50²).
- (c): for x between 0 and 50, the worst distance is the bigger of x and 50 − x.
</details>

<details><summary>Answer</summary>

(a) **2** (median) (b) **12.6** (mean) (c) **25** (midrange); the median barely moves when the robot at 50 goes to 500.
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the words.** For the sorted list [0, 1, 2, 10, 50]:
- **median**: the middle value once the list is sorted, here 2. (Tiny example: [1, 4, 10] has median 4.)
- **mean**: the sum divided by the count, here 63/5 = 12.6. ([1, 4, 10] has mean 5.)
- **midrange**: halfway between the smallest and the largest, here (0 + 50)/2 = 25. ([1, 4, 10] has midrange 5.5.)
- **argmin**: the input that makes a quantity smallest. Tiny example: f(x) = (x − 3)² + 1 has smallest *value* 1, reached at x = 3, so its argmin is 3.

Every part of this problem asks for an argmin. This is move **M6: what does the argmin pick?** Each loss picks a different "centre" of the data, and the point of the problem is to see which.

**Step 2: (a) the nudge argument.** Put the charger at some x that isn't on a robot, and nudge it right by a tiny amount δ.
- Every robot to the **left** of x is now δ farther away: +δ each.
- Every robot to the **right** of x is now δ closer: −δ each.

So the total changes by δ × (number of robots on the left − number on the right).

| x is between | Robots on left | Robots on right | Nudging right changes the total by |
|---|---|---|---|
| 0 and 1 | 1 | 4 | −3δ (keep moving right) |
| 1 and 2 | 2 | 3 | −δ (keep moving right) |
| 2 and 10 | 3 | 2 | +δ (moving right now hurts) |
| 10 and 50 | 4 | 1 | +3δ |

The total keeps falling while more robots are on the right, and starts rising once more are on the left. It switches at x = **2**, the median, which has 2 robots on each side. Check: the total at x = 2 is 2 + 1 + 0 + 8 + 48 = 59; at x = 1 or x = 3 it is 60; at x = 12 it is 73.

Stop and notice: the *sizes* of the distances never entered the argument, only how many robots are on each side. That is why moving the robot at 50 changes nothing here.

**Step 3: (b) squares give a quadratic.** Expand each term: (x − xᵢ)² = x² − 2xᵢx + xᵢ². Add up all five:

f(x) = 5x² − 2(0 + 1 + 2 + 10 + 50)x + (0 + 1 + 4 + 100 + 2500) = 5x² − 126x + 2605.

**Quadratic vertex:** a quadratic ax² + bx + c with a > 0 is lowest at x = −b/(2a). Why: completing the square gives ax² + bx + c = a(x + b/(2a))² + (c − b²/(4a)). The squared part is never negative and is 0 only at x = −b/(2a). Tiny example: x² − 6x + 10 = (x − 3)² + 1, lowest at x = 3. (If a < 0, the same x gives the *highest* point.)

Here x = 126/10 = **12.6**, which is exactly the mean, 63/5. That is no coincidence: for n points the quadratic is nx² − 2(sum of the xᵢ)x + …, so the vertex is always (sum)/n, the mean.

**Step 4: (c) the worst case.** The farthest robot is always one of the two ends, 0 or 50. For x between them, the worst distance is the bigger of x and 50 − x. As x grows, the first goes up and the second goes down, so the bigger of the two is smallest where they are equal: x = 50 − x gives x = **25**, the midrange, with worst distance 25.

**Step 5: move the robot at 50 to 500.**
- Median: still **2**. The counts on each side haven't changed.
- Mean: (0 + 1 + 2 + 10 + 500)/5 = 513/5 = 102.6.
- Midrange: (0 + 500)/2 = 250.

The median is *robust* to outliers: one far-away robot can't drag it. (The Jan 18 Godown problem is built on this: L1 distance gives the coordinate-wise median, KL gives the mean.)

**What to remember:** absolute loss is minimised by the median, squared loss by the mean, and worst-case loss by the midrange. The median only counts how many points lie on each side, so an outlier can't drag it.

**Common trap:** assuming the best "centre" is always the mean. First ask what the loss rewards.
</details>

---

### 5.2 Does the budget bind?

<details><summary>Hint 1: understand the question</summary>

Forget the budget for a moment. How many hours would each model want if hours were free? Do those wishes fit inside B = 10? Inside B = 5?
</details>

<details><summary>Hint 2: the key idea</summary>

If both wishes fit, the budget doesn't change anything. If they don't fit, you must spend the whole budget, and split it so that one more hour would be worth the same to either model.
</details>

<details><summary>Hint 3: set it up</summary>

- Each gain is a downward parabola. Rewrite g₁ = 6h₁ − h₁² in the form (peak value) − (h₁ − peak position)².
- For (b), substitute h₂ = 5 − h₁ into g₁ + g₂. You get a quadratic in h₁ alone.
</details>

<details><summary>Answer</summary>

(a) **25** at (3, 4); budget not binding (b) **23** at (2, 3) (c) 20.5 at (4.5, 5.5): forcing all 10 hours to be spent pushed both models past their peaks.
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: each model on its own.** Complete the square: g₁ = 6h₁ − h₁² = 9 − (h₁ − 3)². (Check: 9 − (h₁² − 6h₁ + 9) = 6h₁ − h₁².) The subtracted square is never negative, so g₁ peaks at h₁ = 3 with g₁ = 9. More hours past the peak make it *worse*: at h₁ = 5, g₁ = 5.

In the same way, g₂ = 8h₂ − h₂² = 16 − (h₂ − 4)², which peaks at h₂ = 4 with g₂ = 16.

**Step 2: (a) does the budget bind?** This is move **M7: equal marginal gains (check if the constraint binds)**, and the check comes first. Both peaks together need 3 + 4 = 7 hours, and 7 ≤ 10. So you can give each model its favourite amount, and no split can beat having each model at its own peak. The maximum total gain is 9 + 16 = **25**, at (3, 4), with 3 hours left unused.

The budget is *not binding*: removing it wouldn't change the answer. This is why you check first. The "equal marginal gains" rule below assumes you must spend the whole budget, and here spending more would hurt.

**Step 3: marginal gain.** The *marginal gain* of a model is the extra gain per hour from adding one more small slice of hours. For g₁ = 6h − h², going from h to h + δ adds

(6(h + δ) − (h + δ)²) − (6h − h²) = 6δ − 2hδ − δ²,

which is about (6 − 2h)δ when δ is tiny. So model 1's marginal gain is 6 − 2h₁. Tiny example: g₁(1) = 5 and g₁(1.1) = 5.39, an extra 0.39, close to (6 − 2)(0.1) = 0.4. In the same way, model 2's marginal gain is 8 − 2h₂.

**Step 4: (b) B = 5, where the budget binds.** Now 7 > 5, so both models can't have their peaks. Below its peak, each model's marginal gain is positive, so every hour helps and you should spend all 5: h₁ + h₂ = 5.

Why the marginal gains must be equal at the best split: suppose model 1's marginal gain were bigger. Move a sliver δ of hours from model 2 to model 1. The total changes by about (MG₁ − MG₂)δ, which is positive, so the split you started with wasn't the best. The same argument works the other way round. So at the best split, MG₁ = MG₂:

6 − 2h₁ = 8 − 2h₂, so h₂ = h₁ + 1. With h₁ + h₂ = 5: 2h₁ + 1 = 5, so h₁ = 2 and h₂ = 3.

Gain = (12 − 4) + (24 − 9) = 8 + 15 = **23**. Both marginal gains are 6 − 4 = 8 − 6 = 2, which is positive: each model would still like more hours, which confirms that the budget binds.

Without the trick: substitute h₂ = 5 − h₁:

total = 6h₁ − h₁² + 8(5 − h₁) − (5 − h₁)² = −2h₁² + 8h₁ + 15.

This is a downward parabola (a = −2), so its vertex is the highest point: h₁ = −8/(2 × (−2)) = 2, giving −8 + 16 + 15 = 23. Same answer.

**Step 5: (c) what the classmate did.** Forcing h₁ + h₂ = 10 with equal marginal gains: h₂ = h₁ + 1 and 2h₁ + 1 = 10, so h₁ = 4.5 and h₂ = 5.5.
- g₁ = 6(4.5) − 4.5² = 27 − 20.25 = 6.75
- g₂ = 8(5.5) − 5.5² = 44 − 30.25 = 13.75
- Total = **20.5**, worse than the 25 from (a).

What went wrong: at (4.5, 5.5) the marginal gains are 6 − 9 = −3 and 8 − 11 = −3. They are equal, but *negative*: each extra hour makes each model worse, because both have been pushed past their peaks. "Equal marginal gains" finds the best way to spend *all* of the budget. It can't tell you whether you should spend all of it.

**What to remember:** first solve without the constraint and check whether the answer fits. Only if it doesn't (the constraint binds) do you spend the whole budget, split so that the marginal gains are equal.

**Common trap:** assuming "use the whole budget". Equal marginal gains that are *negative* are the red flag.
</details>

---

### 5.3 AM-GM and Jensen

<details><summary>Hint 1: understand the question</summary>

(a): call the side parallel to the wall x and each of the other two sides y. Which expression in x and y is fixed by the 40 m of fence, and which expression do you want to make as big as possible?

(b): just compute both numbers. Which is smaller?
</details>

<details><summary>Hint 2: the key idea</summary>

(a): AM-GM says that when two non-negative numbers have a fixed sum, their product is biggest when they are equal. You need a pair whose *sum* is fixed. Is x + y fixed? Which pair is?

(b): for a curve that bends upward, like squaring, the value at the average is never more than the average of the values. This is Jensen's inequality.
</details>

<details><summary>Hint 3: set it up</summary>

(a): use the pair x and 2y, whose sum is 40.

(b): the errors (prediction − truth) are −3, 0 and 6. Write each error as (average error) + (its deviation from the average), and square.
</details>

<details><summary>Answer</summary>

(a) **200 m²** (20 × 10) (b) average squared error **15**, error of the average **1**. The squared error of the average is smaller, and that is guaranteed (Jensen).
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: AM-GM, and why it is true.** For any two numbers a, b ≥ 0:

(a + b)/2 ≥ √(ab).

The left side is the *arithmetic mean* (AM) and the right side is the *geometric mean* (GM). Tiny example: a = 2, b = 8 gives AM = 5 and GM = √16 = 4, and 5 ≥ 4.

Proof: a square is never negative, so (√a − √b)² ≥ 0. Expanding gives a − 2√a√b + b ≥ 0, i.e. a + b ≥ 2√(ab). Divide by 2. Equality holds only when √a − √b = 0, i.e. a = b.

Squaring both sides gives the form you'll use: **ab ≤ ((a + b)/2)²**. So if the sum a + b is fixed, the product ab can be at most (sum/2)², and it reaches that exactly when a = b.

**Step 2: (a) set it up.** Let x be the side parallel to the wall and y each of the two sides touching it. The fence covers x + 2y = 40, and the area is xy.

Why not use AM-GM on x and y directly? Because x + y isn't fixed: it changes as you trade length for width. But x + 2y is fixed, so use the pair a = x and b = 2y.

**Step 3: apply it.** x · 2y ≤ ((x + 2y)/2)² = 20² = 400. So 2xy ≤ 400 and xy ≤ **200**. Equality needs x = 2y, and with x + 2y = 40 that means x = 20 and y = 10. The arena is **20 × 10, with area 200 m²**.

Check without AM-GM: area = (40 − 2y) · y = −2y² + 40y, a downward parabola with its vertex at y = 40/4 = 10, giving 200. Same answer.

**Step 4: (b) the two numbers.** Errors (prediction − truth): 7 − 10 = −3, then 0, then 6.
- Average squared error: (9 + 0 + 36)/3 = **15**.
- Average prediction: (7 + 10 + 16)/3 = 11. Its error is 1, so its squared error is **1**.

The averaged prediction (an *ensemble*) does far better: 1 against 15.

**Step 5: is it guaranteed? Convexity and Jensen.** A function is **convex** if the chord joining any two points of its graph lies on or above the graph, i.e. the curve bends upward. Example, f(x) = x²: the chord from (−1, 1) to (3, 9) has midpoint (1, 5), and the curve at x = 1 is only 1, below the chord.

**Jensen's inequality** says that for a convex f, f(average of some numbers) ≤ average of f(those numbers). With f = squaring and the numbers being the errors: (average error)² ≤ average of the squared errors. So 1 ≤ 15 is guaranteed, whatever the predictions are.

Here is a proof for squares, with no jumps. Let ē be the average error (here 1), and write each error as eᵢ = ē + dᵢ, where dᵢ is its deviation from the average (here −4, −1, 5). Deviations from an average always add up to 0. Square:

eᵢ² = ē² + 2ē·dᵢ + dᵢ².

Now average over i. The middle term averages to 2ē × (average of the dᵢ) = 0. So

average of eᵢ² = ē² + average of dᵢ².

Here: 15 = 1 + (16 + 1 + 25)/3 = 1 + 14. The last term is never negative, so the average of the squares can never be less than the square of the average. The two are equal only when all the models agree.

**What to remember:** AM-GM: with a fixed sum, a product peaks when the parts are equal, so choose parts whose sum is fixed. Jensen for squares: average squared error = squared error of the average + spread. That is why averaging models never does worse on squared error than the members do on average.

**Common trap:** in (a), applying AM-GM to x and y. That gives x = y = 40/3 and area ≈ 178, which is not the maximum, because x + y wasn't fixed. In (b), reading Jensen as "the ensemble beats every member". It only beats the *average* member: here the model that predicted 10 has error 0, better than the ensemble's 1.
</details>

---

### 5.4 Growing user base

<details><summary>Hint 1: understand the question</summary>

(a) is just the rule applied three times. For (b) you could keep applying it, but how many steps might that take? Is there some quantity that simply gets multiplied by the same number each day?
</details>

<details><summary>Hint 2: the key idea</summary>

Find the value $U^*$ that the rule leaves unchanged, i.e. solve $U^* = 1.1U^* + 100$. Then track how far $U_t$ is from $U^*$ each day.
</details>

<details><summary>Hint 3: set it up</summary>

Let $V_t = U_t + 1000$. Show that $V_{t+1} = 1.1\,V_t$. Then turn "$U_t > 5000$" into a condition on $1.1^t$.
</details>

<details><summary>Answer</summary>

(a) **1662** (b) **t = 12**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: where 1.1 comes from.** Of each 1 active user, 0.2 leave and 0.3 new users arrive: 1 − 0.2 + 0.3 = 1.1. Then 100 more sign up on their own.

**Step 2: (a) tabulate.** This is move **M9: tabulate recurrences**: just apply the rule, one row at a time. A handy shortcut: 1.1 × U = U + U/10.
- U₁ = 1.1 × 1000 + 100 = 1200
- U₂ = 1.1 × 1200 + 100 = 1420
- U₃ = 1.1 × 1420 + 100 = 1562 + 100 = **1662**

**Step 3: (b) the fixed point.** A **fixed point** of a recurrence is a value that stays put once you reach it. Tiny example: $x_{t+1} = 0.5x_t + 3$ has fixed point 6, because 0.5 × 6 + 3 = 6. Here: $U^* = 1.1U^* + 100$, so $-0.1U^* = 100$ and $U^* = -1000$. (Negative users make no sense; this is purely an algebra tool.)

**Step 4: the distance from the fixed point grows by the same factor each day.** Subtract the fixed-point equation from the rule:

$$U_{t+1} - U^* = (1.1U_t + 100) - (1.1U^* + 100) = 1.1\,(U_t - U^*).$$

The +100s cancel. With $U^* = -1000$, define $V_t = U_t + 1000$. Then $V_{t+1} = 1.1\,V_t$, and $V_0 = 1000 + 1000 = 2000$. So $V_t = 2000 \times 1.1^t$. This is called a geometric sequence: each term is the previous one times the same number.

Check: V₃ = 2000 × 1.331 = 2662, so U₃ = 2662 − 1000 = 1662, matching (a).

**Step 5: solve the inequality.** $U_t > 5000 \iff V_t > 6000 \iff 2000 \times 1.1^t > 6000 \iff 1.1^t > 3$.

Tabulate powers of 1.1 (each one is the previous one plus a tenth of it):

| t | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $1.1^t$ | 1.1 | 1.21 | 1.331 | 1.464 | 1.611 | 1.772 | 1.949 | 2.144 | 2.358 | 2.594 | 2.853 | 3.138 |

Estimate first: the table shows $1.1^t$ roughly doubles in 7 days (1.949), so tripling should take a bit longer than 11. The power first passes 3 at t = 12, so the answer is **t = 12**.

Check: U₁₁ ≈ 2000 × 2.853 − 1000 ≈ 4706 (not yet over 5000), and U₁₂ ≈ 2000 × 3.138 − 1000 ≈ 5277 (over).

**What to remember:** for $U_{t+1} = r\,U_t + c$, find the fixed point $U^*$ (solve $U^* = r\,U^* + c$). The gap $U_t - U^*$ gets multiplied by r every step, which turns the recurrence into a geometric sequence.

**Common trap:** writing $U_t = 1000 \times 1.1^t + 100t$. That treats the organic sign-ups as never growing, but they also bring in new users after they join. It undercounts (1631 instead of 1662 at t = 3) and gives a wrong answer for (b).
</details>

---

### 5.5 Kits from parts

<details><summary>Hint 1: understand the question</summary>

Let a be the number of Kit A and b the number of Kit B. Write one inequality for motors and one for sensors. What expression are you trying to make as big as possible?
</details>

<details><summary>Hint 2: the key idea</summary>

Sketch all the points (a, b) that satisfy every inequality. The best point is always at a corner of that region, so list the corners and compare them.
</details>

<details><summary>Hint 3: set it up</summary>

- The interesting corner is where both resources run out at once: solve 2a + b = 14 and a + 3b = 15 together.
- For (b), go through a = 0, 1, …, 7 and find the largest whole b you can afford for each.
</details>

<details><summary>Answer</summary>

(a) (5.4, 3.2) → **₹290** (b) **₹270** at (5, 3)
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: set it up.**
- Motors: 2a + b ≤ 14
- Sensors: a + 3b ≤ 15
- No negative kits: a ≥ 0, b ≥ 0
- Profit = 30a + 40b

The **feasible region** is the set of all points (a, b) that satisfy every constraint. Tiny check: (3, 3) uses 9 motors and 12 sensors, so it is feasible; (7, 3) needs 17 motors, so it isn't.

**Step 2: find the corners.** Each constraint keeps the points on one side of a straight line, so the region is a polygon. Its **corner points** are where two boundary lines meet *and* every other constraint still holds.
- a = 0 and b = 0: (0, 0).
- b = 0 and the motor line: 2a = 14, giving (7, 0). Sensors: 7 ≤ 15, fine.
- a = 0 and the sensor line: 3b = 15, giving (0, 5). Motors: 5 ≤ 14, fine.
- The motor line and the sensor line: from 2a + b = 14, b = 14 − 2a. Substitute into the sensor line: a + 3(14 − 2a) = 15, so a + 42 − 6a = 15, so 5a = 27. That gives a = 5.4 and b = 14 − 10.8 = 3.2.
- Not corners: the motor line meets a = 0 at (0, 14), but that needs 42 sensors. The sensor line meets b = 0 at (15, 0), but that needs 30 motors.

**Step 3: why the best point is a corner.** All points with the same profit P lie on the straight line 30a + 40b = P. Raising P slides this line outward, parallel to itself. Keep sliding while it still touches the region: the last point it touches is a corner (or a whole edge, whose ends are corners). Another way to see it: walk along any edge of the region. Profit changes at a steady rate along a straight edge, so it is biggest at one of the edge's two ends, which are corners. So you only need to check the corners.

| Corner | Profit 30a + 40b |
|---|---|
| (0, 0) | 0 |
| (7, 0) | 210 |
| (0, 5) | 200 |
| (5.4, 3.2) | 162 + 128 = **290** |

So (a) is the corner **(5.4, 3.2)**, with profit **₹290**.

**Step 4: (b) whole kits.** You can't build 5.4 kits. Rounding down to (5, 3) is only a guess, so check every case. For a fixed a, a bigger b only adds profit, so take the largest whole b that satisfies both b ≤ 14 − 2a (motors) and b ≤ (15 − a)/3 (sensors).

| a | Motor limit on b | Sensor limit on b | Best whole b | Profit |
|---|---|---|---|---|
| 0 | 14 | 5 | 5 | 200 |
| 1 | 12 | 4.67 | 4 | 190 |
| 2 | 10 | 4.33 | 4 | 220 |
| 3 | 8 | 4 | 4 | 250 |
| 4 | 6 | 3.67 | 3 | 240 |
| 5 | 4 | 3.33 | 3 | **270** |
| 6 | 2 | 3 | 2 | 260 |
| 7 | 0 | 2.67 | 0 | 210 |

The best is **₹270** at **(5, 3)**. Notice that the nearby point (5, 4) is not feasible (5 + 12 = 17 sensors > 15), and neither is (6, 3) (12 + 3 = 15 motors > 14). The best whole-kit profit is ₹20 below the fractional best.

**What to remember:** when both the objective and the constraints are linear, the best point is a corner of the feasible region: list the corners, evaluate each, pick the best. For whole numbers, don't just round the fractional corner. Fix one variable, push the other as far as it can go, and check every case.

**Common trap:** rounding (5.4, 3.2) to (5, 3) and stopping. It happens to be right here, but rounding isn't guaranteed to find the best whole point. Rounding *up* to (5, 4) or (6, 3) breaks a constraint.
</details>

---

### 5.6 Bases

<details><summary>Hint 1: understand the question</summary>

In base 10, 2026 means 2·1000 + 0·100 + 2·10 + 6. What is each place worth in base 7?
</details>

<details><summary>Hint 2: the key idea</summary>

- (a): find the largest power of 7 that fits into 2026, and how many times it fits. Then repeat with what's left.
- (b): write "121" in base b as an expression in b. Does that expression factor?
</details>

<details><summary>Answer</summary>

(a) **5623₇** (b) **b = 11**. "121" in base b equals b² + 2b + 1 = (b + 1)², a perfect square in every base.
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: place value.** In base b, the digits run from 0 to b − 1, and each place is worth b times the place to its right: 1, b, b², b³, and so on. Example: "23" in base 7 = 2·7 + 3 = 17. In base 10, "121" = 1·100 + 2·10 + 1.

**Step 2: (a) largest power first.** This is how anyone would start. The powers of 7 are 1, 7, 49, 343, 2401. Since 2401 > 2026, the number has 4 digits, starting with the 343s place.
- 2026 ÷ 343 = 5, remainder 2026 − 1715 = 311.
- 311 ÷ 49 = 6, remainder 311 − 294 = 17.
- 17 ÷ 7 = 2, remainder 3.
- 3 ones are left.

The digits are 5, 6, 2, 3: **5623₇**.

**Step 3: the same answer by repeated division.** This is faster and doesn't need the powers listed. Why it works: 2026 = 7 × (something) + (last digit), because every place except the last is a multiple of 7. So the last digit is the remainder when you divide by 7. Dividing the quotient by 7 again gives the next digit, and so on.
- 2026 = 7·289 + **3**
- 289 = 7·41 + **2**
- 41 = 7·5 + **6**
- 5 = 7·0 + **5**

Read the remainders from the bottom up: 5623. Check: 5·343 + 6·49 + 2·7 + 3 = 1715 + 294 + 14 + 3 = 2026.

**Step 4: (b)** "121" in base b = 1·b² + 2·b + 1 = b² + 2b + 1 = **(b + 1)²**. Set it equal to 144 = 12². Since b + 1 is positive, b + 1 = 12, so **b = 11**. The digits 1 and 2 are both less than 11, so "121" is a valid base-11 numeral.

**Step 5: why it's a perfect square in every base.** (b + 1)² is a whole number squared, whatever b is. In fact "121" in base b is "11" in base b, squared, exactly as 121 = 11² in base 10. ("Every base" means every base where the digit 2 is allowed, so b ≥ 3.)

**What to remember:** a base-b numeral is a polynomial in b with the digits as coefficients. To convert into base b, divide by b repeatedly and read the remainders from the bottom up.

**Common trap:** reading the remainders from the top down, which gives 3265 instead of 5623.
</details>

---

### 5.7 Read the model off the graph

<details><summary>Hint 1: understand the question</summary>

Each piece of the formula draws a different feature of the curve. Which piece makes it wiggle, which makes it drift upward, and which makes the sudden jump at t = 12? Which feature of the graph would tell you T?
</details>

<details><summary>Hint 2: the key idea</summary>

Read T first, from the spacing between repeating features (peak to peak, or dip to dip). Once you know T, work out sin(2πt/T) at each marked t: they all turn out to be simple numbers. Then each marked point gives you a simple equation.
</details>

<details><summary>Hint 3: set it up</summary>

T = 8. At t = 2, 6, 10, 14 the sine equals +1, −1, +1, −1. Before t = 12 the step term is 0. Write P(2) = 13, P(6) = 11 and P(10) = 17 as equations in A, B and E, then subtract pairs that share the same sine value.
</details>

<details><summary>Answer</summary>

A = 10, B = 0.5, E = 2, T = 8, D = −6; ⌊P(25)⌋ = **17**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: what each piece does.**
- **A** is the starting level: the value at t = 0 (where the wave and the step are both 0).
- **Bt** is the **trend**, a straight-line drift. B is the change per week.
- **E sin(2πt/T)** is a wave. Its **amplitude** E is how far the wave swings above and below its middle line. Its **period** T is how many weeks it takes to repeat: when t grows by T, the angle 2πt/T grows by 2π, one full turn. Example with T = 4: sin(2πt/4) at t = 0, 1, 2, 3, 4 is 0, 1, 0, −1, 0.
- **D·h(t − 12)** uses the **step function** h(s) = 1 if s ≥ 0, else 0. Examples: h(−0.5) = 0, h(0) = 1, h(3) = 1. So D·h(t − 12) is 0 before week 12 and D from week 12 on: a sudden, permanent jump of size D.

This is move **M13: read parameters off a graph**. Separate the features, then read each parameter from the feature it controls.

**Step 2: the period T.** The wave repeats. Its dips are near t ≈ 5.6, 13.6 and 21.6, and its peaks near t ≈ 2.4, 10.4 and 18.4: each is 8 weeks after the last. So **T = 8**. The trend tilts every peak sideways by the same amount, so the spacing between peaks is still exactly one period, even though the peaks aren't exactly where the sine equals 1.

**Step 3: the sine at each marked point.** With T = 8, the angle is 2πt/8 = πt/4. Adding whole turns of 2π doesn't change a sine.

| t | Angle πt/4 | sin |
|---|---|---|
| 2 | π/2 | 1 |
| 6 | 3π/2 | −1 |
| 10 | 5π/2 = 2π + π/2 | 1 |
| 12 | 3π = 2π + π | 0 |
| 14 | 7π/2 = 2π + 3π/2 | −1 |

**Step 4: equations before week 12** (the step term is still 0).
- P(2) = A + 2B + E = 13
- P(6) = A + 6B − E = 11
- P(10) = A + 10B + E = 17

Subtract P(2) from P(10). The sine values match, so A and E both cancel: 8B = 4, so **B = 0.5**.

Put B = 0.5 into the other two. P(2): A + 1 + E = 13, so A + E = 12. P(6): A + 3 − E = 11, so A − E = 8. Adding these gives 2A = 20, so **A = 10**, and then **E = 2**.

**Step 5: the step D.** At t = 12 the sine is 0, so the smooth part of the curve is 10 + 0.5 × 12 + 0 = 16. That is the open circle (12⁻, 16), the value just before the step. Just after the step the curve is at (12⁺, 10). The jump is 10 − 16, so **D = −6**.

**Step 6: check with points you haven't used.** P(14) = 10 + 0.5 × 14 + 2 × (−1) − 6 = 10 + 7 − 2 − 6 = 9, which matches (14, 9). Also P(0) = A = 10, which matches where the curve starts.

**Step 7: P(25).** 25 ≥ 12, so the step is switched on.
- The angle is 25π/4 = 6π + π/4. Dropping the three whole turns, sin(25π/4) = sin(π/4) = √2/2 ≈ 0.707.
- P(25) = 10 + 0.5 × 25 + 2 × 0.707 − 6 = 10 + 12.5 + 1.414 − 6 = 17.914.
- ⌊17.914⌋ = **17**.

**What to remember:** pull a graph apart into features (level, trend, wave, jump) and read each parameter from the feature it controls. Then use points where the wave is simple (sine = 0 or ±1), and subtract equations that share the same sine value to cancel unknowns.

**Common trap:** treating the marked points as the curve's exact peaks and troughs. The trend tilts the peaks, so use the formula at the given t-values, not "the peak is where the sine is 1". For the same reason, half the gap between (6, 11) and (10, 17) is 3, not E. The trend adds 4 × 0.5 = 2 between those weeks, so the wave accounts for only 6 − 2 = 4 of the gap, and E = 2.
</details>
