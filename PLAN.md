# 8-week plan: Sat 17 Oct → Sun 13 Dec 2026 (INAIO Stage 1)

## Ground rules

- **School, tuition and Allen come first.** The plan budgets **5 hours a week**: three 60-min sessions on tuition days (Mon, Wed, Fri) and 2 hours on Sunday morning. Tue, Thu and Sat are Allen days and stay free of INAIO work. So does time for outings and sport.
- **Paper before code.** Every problem is solved on paper first. Notebooks come *after*, to check, explore and build intuition. The exam has no computer.
- **Struggle first.** Spend 10–15 min on a problem before opening Hint 1, and about 5 min between hints. If two hints don't unlock it, you're missing knowledge, not effort. Go back to the fundamentals section of the notebook.
- **Every session ends with a log line** in `log/WEEKLY.md`. Every miss goes into `log/ERROR_LOG.md`.
- **Commit after every session:** `git add -A && git commit -m "w2 wed: set 02 #1-3" && git push`.

## Weekly rhythm (~5 h)

Built around Shreesh's timetable ([issue #2](https://github.com/Shreeshinator/ioai-prep/issues/2)): school until 2:30 PM on weekdays, tuition Mon/Wed/Fri 4–5 PM, Allen Tue/Thu/Sat 5–8:30 PM.

| Day | When | What |
|---|---|---|
| **Mon** | 60 min after tuition | Notebook: the week's fundamentals |
| Tue | — | Off (Allen) |
| **Wed** | 60 min after tuition | Practice-set problems on paper, then check them in the notebook |
| Thu | — | Off (Allen) |
| **Fri** | 60 min after tuition | The rest of the notebook, more problems, log your misses |
| Sat | — | Off (Allen). A catch-up slot only if you're behind *and* feel like it |
| **Sun** | **10:00–12:00** | Mock, or the week's exam walkthroughs + Connect. Ends with a **15-min teach-back with Varun** |

- **Pick one fixed slot for Mon/Wed/Fri** (for example 6:00–7:00 PM) and keep it. A fixed slot becomes a habit; a floating one gets skipped.
- **Why Sunday 10:00–12:00?** It's the exam's slot. After eight Sundays of hard thinking at 10 AM, exam day feels like any other Sunday.
- **Videos don't count toward the 5 hours.** The StatQuest and 3Blue1Brown videos in `RESOURCES.md` are optional extras for any spare 15 minutes. Watch each one *after* its notebook section.

**The 60-minute session:**
1. 5 min recall: write down, from memory, the last session's key idea.
2. 45 min work.
3. 10 min check, log and commit.

**School test week? Switch to maintenance mode:** only the Sunday session, plus 10 min of error-log review on Mon/Wed/Fri.

**Behind? Drop things in this order:**
1. EXPLORE cells. Keep the BUILDs and the problems.
2. Walkthroughs of Jan 18 questions you already got right in the diagnostic.
3. Optional videos and puzzles.

Never drop the problems on paper, the mocks or the error log.

## Each week answers five questions

From `AUTHORING.md`: **Hook** (why care), **Aha** (the insight to reach), **Struggle** (where you'll get stuck, on purpose), **Practice**, **Connect** (links to earlier weeks). The Aha line is for Varun. Shreesh, try not to read it until the week is done.

## Mock schedule (all timed, no calculator, no internet, no AI)

| When | Paper | Why |
|---|---|---|
| **Sun 18 Oct**, 10:00–12:00 | 2026 Stage 1, Jan 18: `papers/2026-stage1-jan18/` | **Diagnostic.** Shows where you stand today |
| **Sun 29 Nov**, 10:00–12:00 | 2026 Stage 1 *alternate*, Feb 28: `papers/2026-stage1-feb28-alt/` | **Retest.** Same 14 topics as the diagnostic with new numbers, so the score difference measures your growth |
| Fri 4 Dec (60 min) | 2025 Stage 1 sample test | A short, fresh paper; solutions on its last page |
| **Sun 6 Dec**, 10:00–12:00 | 2025 Stage 1 actual test | **Final rehearsal**, graded with the official key |

With only one long slot a week, a mid-November mock would cost a whole topic's walkthroughs, so there isn't one. Instead, every Sunday walkthrough starts with a **timed, cold re-attempt** of that week's Jan 18 questions, which makes each Sunday a small mock.

---

## Kick-off weekend: Sat 17 – Sun 18 Oct

- **Sat (30 min, before Allen):**
  - Clone the repo. Read `README.md` and this plan.
  - Skim the syllabus PDF once.
  - Set up Python (`pip install -r requirements.txt`) and open `notebooks/01_metrics.ipynb` to check it runs.
- **Sun 10:00–12:00: diagnostic.** Then 15 more minutes:
  - Take the Jan 18 paper in **2 hours**, timed, with no notes.
  - Grade it using only the answer table in its `SOLUTIONS.md`.
  - Log every miss with a category: *misread / convention / arithmetic / concept / time*.
  - **Don't read any full solutions yet.** You'll re-attempt the misses during the weeks that cover them.

## Week 1 (19–25 Oct): Evaluation metrics (short week: SOF IMO on Fri 23 Oct)
`notebooks/01_metrics.ipynb` · `practice/01-metrics.md`

- **SOF IMO on Fri 23 Oct.** Mon–Thu go to IMO prep; its algebra and counting overlap with Stage 1 anyway. Week 1 shrinks to Sunday, plus Monday of Week 2. You already know most of this topic, so problems come first, and you only build a notebook section if its problem went wrong.
- **Hook:** your gripper detector is "95% accurate", so why does it keep grabbing air?
- **Aha:** every rate is a *count ÷ a group*. Rates measured within a true class (recall, FPR) ignore prevalence; precision doesn't. AUC only sees the *order* of the scores.
- **Struggle:** problem 1.5's rows-are-predicted convention; turning rates into counts under a capacity limit (1.3).
- **Practice:** Set 01, then re-attempt Jan 18 **B1** (notebook §9).
- **Connect:** precision is "P(sick | flagged)". You'll see next week that this is Bayes.

| Mon–Thu | Fri 23 | Sun 25, 10:00–12:00 |
|---|---|---|
| SOF IMO prep. No INAIO work | **SOF IMO** | Set 01 (1.1–1.5) on paper, 55 min → check your answers → for each miss, work through the notebook section behind it (1.1 → §2–3, 1.2 → §4–5, 1.3 → §6, 1.4 → §7, 1.5 → §8) → log + teach-back |

The B1 walkthrough (§9) and Connect move to Mon 26 Oct.

## Week 2 (26 Oct – 1 Nov): Probability & Bayes
`notebooks/02_probability.ipynb` · `practice/02-probability.md`

- **Hook:** your robot's cheap IR sensor shouts "obstacle!" Should it believe it?
- **Aha:** Bayes isn't a formula to memorise. Imagine 1,000 cases, keep only the rows consistent with the evidence, and divide. Today's posterior is tomorrow's prior.
- **Struggle:** the absent-word factor in Naive Bayes (2.3); Simpson's paradox (2.5).
- **Practice:** Set 02, then re-attempt Jan 18 **Pit-Stop** and **Blind Board**.
- **Connect:** sensitivity = P(flag | sick) and precision = P(sick | flag). Same table, read two ways.

| Mon | Wed | Fri | Sun |
|---|---|---|---|
| Finish Week 1: B1 walkthrough (notebook 01 §9) + Connect | Notebook 02 §1–6 (counting → Naive Bayes) | 2.1–2.3 on paper → check; §7–8 (Elo, series) | §9–10 (Simpson, Markov); 2.4–2.6 on paper → check; Pit-Stop + Blind Board walkthroughs (§11–12); teach-back |

## Week 3 (2–8 Nov): Algorithms by hand (Diwali, Sun 8 Nov: no Sunday session)
`notebooks/03_algorithms.ipynb` · `practice/03-algorithms-by-hand.md`

- **Hook:** a 20-sample gesture classifier on your Arduino. How does each algorithm actually decide?
- **Aha:** the exam *gives* you the algorithm. Each one is a short loop you can run by hand. Your job is to run it **exactly**, ties included.
- **Struggle:** k-means landing in different answers from different starts (3.2); PCA's eigenvector (3.5).
- **Practice:** Set 03, then re-attempt Jan 18 **B4**.
- **Connect:** a k-means centroid is a *mean*. Why the mean? (Week 1, problem 1.4.)

| Mon | Wed | Fri | Sun 8 |
|---|---|---|---|
| Notebook 03 §1–5 (distances, k-NN, k-means, Gini, splits) | 3.1–3.3 on paper → check; §6 (linkage) | §7 PCA (read it slowly: it's the "why eigenvectors" section); 3.4–3.5 on paper | Diwali: rest |

§8–11 (the linear classifier and the B4 walkthrough) move to Mon 9 Nov.

## Week 4 (9–15 Nov): Ranking, retrieval & convolution
`notebooks/04_ranking_signals.ipynb` · `practice/04-ranking-retrieval.md`

- **Hook:** your VLA must fetch the right skill from a library of 1,000; your IMU signal is noisy, so how do you spot a jolt?
- **Aha:** ranking metrics only score *which positions hold hits*. Difference kernels are derivatives, and their sums **telescope**.
- **Struggle:** the exam's convolution **flips** the kernel and PyTorch's doesn't (4.6); what does "retrieved" mean when *k* isn't given?
- **Practice:** Set 04, then re-attempt Jan 18 **B2** and **B3**.
- **Connect:** PageRank's steady state is the same idea as the Markov chain in 2.6.

| Mon | Wed | Fri | Sun |
|---|---|---|---|
| Finish Week 3: notebook 03 §8–11 (linear classifier, B4 walkthrough) + Connect | Notebook 04 §1–5 (tf-idf, PageRank, ranking metrics, DCG); 4.1–4.2 on paper | 4.3–4.4 on paper → check; B2 walkthrough (§6) | §7–11 (convolution, kernels); 4.5–4.6 on paper; B3 walkthrough (§12); teach-back |

## Week 5 (16–22 Nov): The math engine
`notebooks/05_math_optimization.ipynb` · `practice/05-math-optimization.md`

- **Hook:** where should the charging dock go for your robot fleet? How do you split a battery budget between perception and planning?
- **Aha:** the loss decides which "centre" wins (median, mean or midrange). At a constrained optimum the marginal gains are equal, but only if the constraint actually binds.
- **Struggle:** a budget that doesn't bind (5.2); fractional vs whole-number optimum (5.5); graph "peaks" that aren't where the sine peaks (5.7).
- **Practice:** Set 05, then re-attempt Jan 18 **Godown, Catalyst, Crude Curve, V-67**. Optional: AoPS Alcumus drills (quadratics, series, AM-GM) in spare time.
- **Connect:** median ↔ MAE (1.4) ↔ Godown. Fixed point ↔ Markov chain (2.6) ↔ PageRank (4.2).

| Mon | Wed | Fri | Sun |
|---|---|---|---|
| Notebook 05 §1–5 (argmin; median, mean, midrange; L1 in 2-D) | 5.1–5.3 on paper → check; §6–8 (marginal gain, AM-GM, Jensen) | §9–12 (recurrences, LP, base-b, graphs); 5.4–5.6 on paper | 5.7; the four walkthroughs (§13); teach-back |

## Week 6 (23–29 Nov): Puzzles, logic & LLM sense
`notebooks/06_puzzles_logic.ipynb` · `practice/06-puzzles-logic.md`

- **Hook:** your robot should clean every floor tile without crossing its own path; the LLM in your VLA stack miscounts letters with total confidence.
- **Aha:** an **invariant** (such as colouring) gives you a ceiling before you search. With "which option satisfies the rules" questions, **kill options with counterexamples** instead of proving the right one.
- **Struggle:** Wason cards (6.4); decoding an unknown language (6.5).
- **Practice:** Set 06. Jan 18 **Section A1** comes in Week 7. Optional, in spare time: a UKLO or PLO puzzle and a few Bebras tasks.
- **Connect:** the rule in 6.6 is the [1, −1] kernel from Week 4 in disguise.
- **About 29 Nov:** INAIO publishes the official Stage 1 format. Update the table in `README.md` and `toolkit/EXAM_STRATEGY.md`.

| Mon | Wed | Fri | Sun |
|---|---|---|---|
| Notebook 06 §1–4 (invariants, search, tracing code, if-then) | 6.1–6.4 on paper → check; §5–7 (hidden rules, formula design, string similarity) | §8–9 (decoding, LLM sense); 6.5–6.7 on paper | **Retest: Feb 28 alternate, 10:00–12:00** |

## Week 7 (30 Nov – 6 Dec): Consolidate

- **Mon:** grade the retest with its `SOLUTIONS.md`. Compare it with the diagnostic section by section, write the comparison in `log/MOCKS.md`, and talk it through with Varun.
- **Wed:**
  - A1 walkthroughs (notebook 06 §10) for any A1 question you still get wrong.
  - Then redo every miss in `ERROR_LOG.md` **cold**, with no notes. Anything that still fails becomes a new practice variant.
- **Fri:** the 2025 sample test, timed: 50 min, then 10 min grading with the solutions on its last page.
- **Sun, 10:00–12:00:** final rehearsal with the 2025 actual test.

## Week 8 (7–12 Dec): Taper → exam Sun 13 Dec

| Mon | Tue | Wed | Thu | Fri | Sat | **Sun 13 Dec** |
|---|---|---|---|---|---|---|
| Grade the rehearsal with the official key (20 min), then re-read your "Moves I own" and error log (30 min) | Off (Allen) | 40 min: one B-section, timed (Varun picks one you've missed before) | Off (Allen) | 20 min: constants sheet and exam-day checklist (`toolkit/EXAM_STRATEGY.md`) | Morning: pack your kit, confirm the centre and timing. Early night after Allen | **Stage 1, 10:00–12:00** |

## After 13 Dec

Stage 2 is on **24 Jan 2027**: online, Python (NumPy, pandas, scikit-learn), with AI assistants allowed in some sections. Your coding background is an advantage here, and the notebooks are already a head start. We'll write a separate plan on 14 Dec.

## Who does what

- **Shreesh:** runs the sessions, solves on paper, uses the notebooks, logs every session, commits and pushes.
- **Varun:** does the Sunday teach-back (keeps asking "why?"), writes practice variants for stubborn misses, picks the Week 8 B-section, answers questions raised as GitHub issues, and builds visualisations or animations in `viz/` whenever an idea needs one.
