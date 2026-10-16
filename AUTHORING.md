# How we write material in this repo

This applies to everything here: problems, solutions, notebooks and visualisations. The goal is to build Shreesh's **thought process**, not to hand over answers.

## Unit design: five questions

Insight plus practice is not enough by itself. Every unit (a week, a notebook or a problem set) must answer all five of these questions before we write it:

| | Question | What it looks like here |
|---|---|---|
| **Hook** | Why should he care? | A situation from his own robotics/VLA work where the idea solves a real problem. For example: "your gripper detector is 95% accurate, so why does it keep grabbing air?" The insight needs somewhere to land. |
| **Aha** | What is the one insight? | Name it explicitly, e.g. "AUC only sees the order of the scores." It is written down in the unit plan but **not shown to him** until he has had a chance to reach it. |
| **Struggle** | Where will he get stuck, and is that useful? | Plan the confusion on purpose, such as the rows-vs-columns convention or a budget that doesn't bind. Let it happen, then resolve it. Don't pre-empt it. |
| **Practice** | What makes the move automatic? | Problems that use the same idea in new clothes, timed once he understands it. |
| **Synthesis** | What does it connect to? | A question linking back to earlier units, for example: "Why are ROC invariance and Bayes' rule the same idea?" See `toolkit/CONNECTIONS.md`. |

**Taste and judgement** can't be broken down into insights. They come from exposure and mentorship:
- **Weekly teach-back.** He explains one solved problem out loud and Varun keeps asking "why?".
- **Read others' solutions.** He reads other people's solutions after solving, such as the official 2025 key.
- **Estimate before computing.** Get a feel for whether an answer "looks right" before working it out.

## Principles

1. **Show how someone *without* the trick gets there.** Describe what they would notice, what they would try first, and why it works or fails. A good explanation could be followed by someone who has never seen the problem type.
2. **No jumps.** Each step follows from the one before, and its reason is written down. If a step relies on a fact, either prove the fact in a line or two, or link to where it is built up (a notebook section).
3. **No assumed knowledge.** Define every term the first time it appears in a file, with a tiny example. Assume a 9th-grade baseline: algebra, coordinate geometry and basic probability. Anything beyond that gets a one-line definition. Examples:
   - *monotone increasing*: if a > b then f(a) > f(b)
   - *convex*: the chord lies above the curve
   - *eigenvector*: a direction the matrix only stretches
   - log₂
   - the step function
4. **Productive struggle, where it makes sense.**
   - Problems live in a different file from solutions. Solutions use a **hint ladder** in collapsed blocks, so he opens one rung at a time.
   - Notebooks ask him to **predict** before running the cell that reveals the answer.
   - Rough timing: struggle **10–15 min** before Hint 1, and about **5 min** between hints.
   - If two hints don't unlock it, the gap is in his *knowledge*, not his *effort*. Send him to the fundamentals section of the matching notebook instead of letting him grind.
   - **Don't make him struggle with:** notation, conventions, definitions he hasn't met, or arithmetic. Just tell him those.
5. **Verify every answer numerically** (a script or notebook cell) before committing. Never commit an unverified answer.
6. **End with the transferable idea.** Every solution finishes with **What to remember**: one or two sentences he can copy into his own words in `log/ERROR_LOG.md`.

## Solution format

Copy this skeleton. GitHub renders `<details>` as click-to-open. Keep the blank lines after `<summary>…</summary>` and before `</details>`, or the markdown inside won't render.

```markdown
### 1.1 Title of the problem

<details><summary>Hint 1: understand the question</summary>

Ask a question back that reframes the problem. Add no new facts.
</details>

<details><summary>Hint 2: the key idea</summary>

The one idea that unlocks it, phrased as something to try.
</details>

<details><summary>Hint 3: set it up</summary>

The first concrete step. Stop before the computation.
</details>

<details><summary>Answer</summary>

**26** and **81**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: …** why we do this → what we get.
**Step 2: …**

**What to remember:** …
**Common trap:** …
</details>
```

Use 2–4 hints. Each hint should give the *minimum* needed for the next step.

## Notebook format (`notebooks/`)

Each notebook is a guided derivation, not an answer key. The sections run in this order:

0. **Hook**: a short scenario from robotics or his own projects that creates the need for the idea. No formulas yet.
1. **Before you start**: what you'll be able to do afterwards, and what you need to know already (with links).
2. **Fundamentals**, built concept by concept. For each concept:
   - **Idea:** plain words, no formulas yet.
   - **Smallest example:** code that *prints every intermediate step* (tables, not just results).
   - **PREDICT:** a markdown cell asking for a guess, followed by the code cell that reveals it.
   - **BUILD:** a function stub with `raise NotImplementedError` and tests that run through `prep.test(...)`. He writes the algorithm; the tests confirm it.
3. **Exam task walkthrough** (Jan 18 paper): the task broken into steps. At each step, ask the question, leave an empty cell for his attempt, and offer `prep.hint(id, n)`.
4. **Your turn**: the practice-set problems, solved on paper first, checked with `prep.check(id, answer)`. The checker compares against hashed answers, so it never prints the answer itself.
5. **Explore**: experiments of the form "change one number, predict, run", plus plots.
6. **Connect**: 2–3 synthesis questions linking this notebook to earlier ones, answered in his own words in a markdown cell.

Every notebook must **run top to bottom without errors while the BUILD stubs are still unfilled**. Tests print `TODO` instead of crashing. Commit notebooks **with outputs cleared**.

## Visualisations and animations (`viz/`)

Build these when an explanation needs one, not ahead of time.
- Start each one from a question ("Why does AUC ignore monotone transforms?"), and make the animation answer it.
- Use manim for derivations that unfold over time, and matplotlib for plots he should poke at.
- Keep each scene short (under 60 s) and about one idea.
- List every visual in `viz/README.md` with the problem(s) it supports.
