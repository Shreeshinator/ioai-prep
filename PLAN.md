# 8-week plan: Sat 17 Oct → Sun 13 Dec 2026 (INAIO Stage 1)

## Ground rules

- **School comes first.** The plan budgets about **5 hours a week**, with no two heavy days in a row.
- **Paper before code.** Every problem is solved on paper first. Notebooks come *after*, to check, explore and build intuition. The exam has no computer.
- **Struggle first.** Spend 10–15 min on a problem before opening Hint 1, and about 5 min between hints. If two hints don't unlock it, you're missing knowledge, not effort. Go back to the fundamentals section of the notebook.
- **Every session ends with a log line** in `log/WEEKLY.md`. Every miss goes into `log/ERROR_LOG.md`.
- **Commit after every session:** `git add -A && git commit -m "w2 tue: set 02 #1-3" && git push`.

## Weekly rhythm (~5 h)

| Day | Time | What |
|---|---|---|
| Mon | 40 min | Notebook: fundamentals for the week's topic |
| Tue | 40 min | Practice-set problems on paper |
| Wed | — | Off (school). Optional 10 min: re-read your error log |
| Thu | 40 min | More problems on paper, check them in the notebook, log your misses |
| Fri | — | Off |
| Sat | 75 min | Remaining problems, explore cells, the notebook's exam walkthrough |
| Sun | 75–120 min | Mock or timed set, review, then a **15-min teach-back with Varun** |

**The 40-minute session:**
1. 5 min recall: write down, from memory, the last session's key idea.
2. 30 min work.
3. 5 min log.

**School test week? Switch to maintenance mode:** only the Sunday session (60 min), plus 10 min a day of error-log review. Weeks 7–8 have slack to absorb this.

## Each week answers five questions

From `AUTHORING.md`: **Hook** (why care), **Aha** (the insight to reach), **Struggle** (where you'll get stuck, on purpose), **Practice**, **Connect** (links to earlier weeks). The Aha line is for Varun. Shreesh, try not to read it until the week is done.

## Mock schedule (all timed, no calculator, no internet, no AI)

| When | Paper | Why |
|---|---|---|
| **Sun 18 Oct** (kick-off) | 2026 Stage 1, Jan 18: `papers/2026-stage1-jan18/` | **Diagnostic.** Shows where you stand today |
| Sun 1 Nov | 2025 Stage 1 sample test (60 min) | Gentle warm-up; solutions on its last page |
| Sun 15 Nov | 2025 Stage 1 actual test (2 h) | Mid-plan check against the official key |
| **Sun 29 Nov, 10:00–12:00** | 2026 Stage 1 *alternate*, Feb 28: `papers/2026-stage1-feb28-alt/` | **Retest.** Same 14 topics as the diagnostic with new numbers, so the score difference measures your growth. Taken at the real exam time |
| Sun 6 Dec | Fresh paper that Varun assembles from unseen sources | Final rehearsal |

---

## Kick-off weekend: Sat 17 – Sun 18 Oct

- **Sat (45 min):**
  - Clone the repo. Read `README.md` and this plan.
  - Skim the syllabus PDF once.
  - Set up Python (`pip install -r requirements.txt`) and open `notebooks/01_metrics.ipynb` to check it runs.
- **Sun (2 h 30 min): diagnostic.**
  - Take the Jan 18 paper in **2 hours**, timed, with no notes.
  - Grade it using only the answer table in its `SOLUTIONS.md`.
  - Log every miss with a category: *misread / convention / arithmetic / concept / time*.
  - **Don't read any full solutions yet.** You'll re-attempt the misses during the weeks that cover them.

## Week 1 (19–25 Oct): Evaluation metrics (short week: SOF IMO on Fri 23 Oct)
`notebooks/01_metrics.ipynb` · `practice/01-metrics.md`

- **SOF IMO on Fri 23 Oct.** Mon–Thu go to IMO prep; its algebra and counting overlap with Stage 1 anyway. Week 1 shrinks to the weekend. You already know most of this topic, so problems come first, and you only read a notebook section closely if its problem went wrong.
- **Hook:** your gripper detector is "95% accurate", so why does it keep grabbing air?
- **Aha:** every rate is a *count ÷ a group*. Rates measured within a true class (recall, FPR) ignore prevalence; precision doesn't. AUC only sees the *order* of the scores.
- **Struggle:** problem 1.5's rows-are-predicted convention; turning rates into counts under a capacity limit (1.3).
- **Practice:** Set 01, then re-attempt Jan 18 **B1** (notebook §9).
- **Connect:** precision is "P(sick | flagged)". You'll see next week that this is Bayes.

| Mon–Thu | Fri 23 | Sat 24 (90 min) | Sun 25 (2 h) |
|---|---|---|---|
| SOF IMO prep. No INAIO work | **SOF IMO** | 1.1–1.3 on paper, then BUILDs 1–4 (§1–5) and check your answers. Read §3 or §6 closely only if 1.1 or 1.3 went wrong | 1.4, 1.5 on paper; §7–8 (BUILD 5); B1 walkthrough (§9) + Connect + teach-back |

## Week 2 (26 Oct – 1 Nov): Probability & Bayes
`notebooks/02_probability.ipynb` · `practice/02-probability.md`

- **Hook:** your robot's cheap IR sensor shouts "obstacle!" Should it believe it?
- **Aha:** Bayes isn't a formula to memorise. Imagine 1,000 cases, keep only the rows consistent with the evidence, and divide. Today's posterior is tomorrow's prior.
- **Struggle:** the absent-word factor in Naive Bayes (2.3); Simpson's paradox (2.5).
- **Practice:** Set 02, then re-attempt Jan 18 **Pit-Stop** and **Blind Board**.
- **Connect:** sensitivity = P(flag | sick) and precision = P(sick | flag). Same table, read two ways.

| Mon | Tue | Thu | Sat | Sun |
|---|---|---|---|---|
| Notebook fundamentals | 2.1–2.3 on paper | 2.4–2.6 → check | Pit-Stop + Blind Board walkthroughs | 2025 sample test (60 min) + review + teach-back |

## Week 3 (2–8 Nov): Algorithms by hand (Diwali, Sun 8 Nov: light weekend)
`notebooks/03_algorithms.ipynb` · `practice/03-algorithms-by-hand.md`

- **Hook:** a 20-sample gesture classifier on your Arduino. How does each algorithm actually decide?
- **Aha:** the exam *gives* you the algorithm. Each one is a short loop you can run by hand. Your job is to run it **exactly**, ties included.
- **Struggle:** k-means landing in different answers from different starts (3.2); PCA's eigenvector (3.5).
- **Practice:** Set 03, then re-attempt Jan 18 **B4**.
- **Connect:** a k-means centroid is a *mean*. Why the mean? (Week 1, problem 1.4.)

| Mon | Tue | Thu | Sat | Sun |
|---|---|---|---|---|
| k-NN, k-means | 3.1–3.3 on paper | linkage, PCA; 3.4–3.5 | B4 walkthrough (45 min) | Diwali: rest |

## Week 4 (9–15 Nov): Ranking, retrieval & convolution
`notebooks/04_ranking_signals.ipynb` · `practice/04-ranking-retrieval.md`

- **Hook:** your VLA must fetch the right skill from a library of 1,000; your IMU signal is noisy, so how do you spot a jolt?
- **Aha:** ranking metrics only score *which positions hold hits*. Difference kernels are derivatives, and their sums **telescope**.
- **Struggle:** the exam's convolution **flips** the kernel and PyTorch's doesn't (4.6); what does "retrieved" mean when *k* isn't given?
- **Practice:** Set 04, then re-attempt Jan 18 **B2** and **B3**.
- **Connect:** PageRank's steady state is the same idea as the Markov chain in 2.6.

| Mon | Tue | Thu | Sat | Sun |
|---|---|---|---|---|
| tf-idf, PageRank | 4.1–4.4 on paper | convolution; 4.5–4.6 | B2 + B3 walkthroughs | **Mock: 2025 actual (2 h)** + grade + log |

## Week 5 (16–22 Nov): The math engine
`notebooks/05_math_optimization.ipynb` · `practice/05-math-optimization.md`

- **Hook:** where should the charging dock go for your robot fleet? How do you split a battery budget between perception and planning?
- **Aha:** the loss decides which "centre" wins (median, mean or midrange). At a constrained optimum the marginal gains are equal, but only if the constraint actually binds.
- **Struggle:** a budget that doesn't bind (5.2); fractional vs whole-number optimum (5.5); graph "peaks" that aren't where the sine peaks (5.7).
- **Practice:** Set 05, then re-attempt Jan 18 **Godown, Catalyst, Crude Curve, V-67**. Plus two 15-min AoPS Alcumus drills (quadratics, series, AM-GM).
- **Connect:** median ↔ MAE (1.4) ↔ Godown. Fixed point ↔ Markov chain (2.6) ↔ PageRank (4.2).

| Mon | Tue | Thu | Sat | Sun |
|---|---|---|---|---|
| argmin, budgets | 5.1–5.3 on paper | recurrences, LP; 5.4–5.6 | 5.7 + the four walkthroughs | Mixed timed set (45 min) + teach-back |

## Week 6 (23–29 Nov): Puzzles, logic & LLM sense
`notebooks/06_puzzles_logic.ipynb` · `practice/06-puzzles-logic.md`

- **Hook:** your robot should clean every floor tile without crossing its own path; the LLM in your VLA stack miscounts letters with total confidence.
- **Aha:** an **invariant** (such as colouring) gives you a ceiling before you search. With "which option satisfies the rules" questions, **kill options with counterexamples** instead of proving the right one.
- **Struggle:** Wason cards (6.4); decoding an unknown language (6.5).
- **Practice:** Set 06; re-attempt Jan 18 **Section A1**; one UKLO or PLO puzzle; 5 Bebras tasks.
- **Connect:** the rule in 6.6 is the [1, −1] kernel from Week 4 in disguise.
- **About 29 Nov:** INAIO publishes the official Stage 1 format. Update the table in `README.md` and `toolkit/EXAM_STRATEGY.md`.

| Mon | Tue | Thu | Sat | Sun |
|---|---|---|---|---|
| invariants, search | 6.1–6.4 on paper | 6.5–6.7; A1 walkthroughs | UKLO/PLO + Bebras | **Retest: Feb 28 alternate, 10:00–12:00** |

## Week 7 (30 Nov – 6 Dec): Consolidate

- **Mon:** grade the retest with its `SOLUTIONS.md`. Compare section by section with the diagnostic and write the comparison in `log/MOCKS.md`.
- **Tue / Thu:** redo every miss in `ERROR_LOG.md` **cold**, with no notes. Anything that still fails becomes a new practice variant.
- **Sat:** two 30-min mixed timed sets that Varun picks from Sets 01–06, with the numbers changed.
- **Sun, 10:00:** final rehearsal mock, then review.

## Week 8 (7–12 Dec): Taper → exam Sun 13 Dec

| Mon | Tue | Wed | Thu–Fri | Sat | **Sun 13 Dec** |
|---|---|---|---|---|---|
| 30 min: re-read your own "Moves I own" and error log | 40 min: one B-section, timed | 20 min: constants sheet and exam-day checklist (`toolkit/EXAM_STRATEGY.md`) | Rest. Sleep. | Pack your kit, confirm the centre and timing. 20 min light reading | **Stage 1, 10:00–12:00** |

## After 13 Dec

Stage 2 is on **24 Jan 2027**: online, Python (NumPy, pandas, scikit-learn), with AI assistants allowed in some sections. Your coding background is an advantage here, and the notebooks are already a head start. We'll write a separate plan on 14 Dec.

## Who does what

- **Shreesh:** runs the sessions, solves on paper, uses the notebooks, logs every session, commits and pushes.
- **Varun:** does the Sunday teach-back (keeps asking "why?"), picks the mixed sets, answers questions raised as GitHub issues, and builds visualisations or animations in `viz/` whenever an idea needs one.
