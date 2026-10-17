# Resources

Problems beat videos. Watch a video only to unlock a concept you're stuck on (1.5× speed is fine), then go straight back to problems. All links were checked on 16–17 Oct 2026.

**Agreed in [issue #1](https://github.com/Shreeshinator/ioai-prep/issues/1) (17 Oct):** the core resources are StatQuest (a short list, [below](#statquest-ml-playlist-what-to-watch)), 3Blue1Brown, Bebras, IOQM past papers and Wikipedia for Elo. Google's ML Crash Course, Khan Academy and the IR book are dropped. The notebooks cover what they did.

## How to use videos and AI

- **Problem first, video second.** The exam hands you a definition you may never have seen and expects you to run it exactly. Learning from the definition on the page *is* the skill being tested. So try the notebook section or practice problem first, then watch to fill in the "why".
- **Learning by reading with an AI is fine, but the exam has no AI and no calculator.** After any AI explanation, close it and solve one problem by hand. Ask it for hints and new problems, not solutions. Check its arithmetic in the notebook: LLMs slip on exactly the kind of counting the exam asks for.

## Official INAIO / IOAI

| Resource | Use it for |
|---|---|
| [inaio.in](https://www.inaio.in/) | Dates, registration, announcements. Check it around **29 Nov** for the Stage 1 format |
| [inaio.in/resources](https://www.inaio.in/resources) | Official past papers (all copied into `papers/`), the Stage 2 papers and notebooks, INAIO's curated resource list, and the "Using AI tools for preparation" guide |
| [IOAI resources](https://ioai-official.org/resources/) | Past IOAI tasks and other countries' national olympiads. Mostly coding, so they're **Stage 2+ material**; save them for after 13 Dec |
| [Bangladesh AI Olympiad 2025 preliminary (PDF)](https://github.com/mdajijulhakimquanta/BdAIO/blob/main/bdaio-2025-preliminary.pdf) | A first-round paper from another country; a spare unseen paper if you want one more mock |
| [Polish AI Olympiad](https://github.com/OlimpiadaAI/I-OlimpiadaAI) · [Hungarian AI Olympiad](https://github.com/Hungarian-AI-Olympiad/HAIO-Hungarian-AI-Olympiad) | More national papers (mostly Stage 2 style) |

## By topic (syllabus order)

| Topic | Resource | Notes |
|---|---|---|
| Classification metrics, ROC/AUC | StatQuest #3, #4, #23 ([list below](#statquest-ml-playlist-what-to-watch)) | You know these already: earn the skip with Set 01 first. Week 1 |
| Probability & Bayes | [3Blue1Brown: Bayes theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM) | Watch before notebook 02. It's the "1,000 people" picture |
| | [3Blue1Brown: The medical test paradox](https://www.youtube.com/watch?v=lG4VkPoG3ko) | Why the same test has a different precision in a different population (problem 1.1, Pit-Stop). Week 2 |
| | [Seeing Theory](https://seeing-theory.brown.edu/) (Brown University) | Optional. Visual and interactive; chapters 1–3 and 5 |
| k-NN, k-means, trees, PCA, Naive Bayes, hierarchical clustering | StatQuest ([list below](#statquest-ml-playlist-what-to-watch)) | One video per algorithm, *after* the notebook section. Weeks 2–3 |
| PCA: why eigenvectors? | Notebook 03 §7 | Built step by step for exactly this question. See [the PCA note below](#pca-why-eigenvectors-why-the-covariance-matrix) |
| TF-IDF, ranking metrics, PageRank | Notebook 04 | Covers all three from scratch. StatQuest has no videos on them |
| | [The $25,000,000,000 Eigenvector (PDF)](https://www.rose-hulman.edu/~bryan/googleFinalVersionFixed.pdf) | A short read on PageRank, and a second look at eigenvectors that helps with PCA. Week 4 |
| | [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/) (free) | Reference only. If you want tf-idf in three pages: §6.2 |
| Convolution | [3Blue1Brown: But what is a convolution?](https://www.youtube.com/watch?v=KuXjwB4LzSA) | Week 4. Note how the kernel **flips**. Leave StatQuest's CNN video (#86) until after Stage 1: like PyTorch, it slides the filter without flipping it |
| Linear algebra | [3Blue1Brown: Essence of linear algebra](https://www.3blue1brown.com/) | Done. Re-watch chapters 14–15 (eigenvectors; the quick trick for eigenvalues) before notebook 03 §7 |
| Algebra, inequalities, series, counting | [IOQM past papers (HBCSE)](https://olympiads.hbcse.tifr.res.in/) | Algebra and combinatorics only; skip geometry. Doubles as SOF IMO practice |
| | [AoPS Alcumus](https://artofproblemsolving.com/alcumus) (free, adaptive) | 15-min drills on free days: quadratics, AM-GM, series, counting & probability |
| Logic & computational thinking | [Bebras](https://www.bebras.org/) · [Bebras India](https://www.bebras.in/) | The main logic resource: 5 tasks a week from Week 6, more if you like |
| Linguistics puzzles (the glyph-type question) | [UKLO past papers](https://www.uklo.org/past-exam-papers/) · [Panini Linguistics Olympiad](https://plo-in.org/) | Bebras doesn't cover "decode an unknown language". Start with UKLO *Foundation/Breakthrough* level. One puzzle a week from Week 6 |
| LLM behaviour (tokens, hallucination) | [Karpathy: Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) | Done: the first 15 min explain why LLMs can't count letters |
| Elo rating | [Wikipedia: Elo rating system](https://en.wikipedia.org/wiki/Elo_rating_system) | "Theory" section only |

## StatQuest ML playlist: what to watch

The [Machine Learning playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) had 100 videos on 17 Oct 2026; **#** is the position in the playlist. Stage 1 needs **6 new videos, about 75 min** (50 min at 1.5×). Every other video is either something you already know, Stage 2 material, or on no INAIO syllabus.

**Watch** (new to you, on the Stage 1 syllabus):

| # | Video | Length | Week | Watch out for |
|---|---|---|---|---|
| 44 | Naive Bayes, Clearly Explained | 15:12 | 2 | StatQuest multiplies only the words that are *present*. Problem 2.3 (Bernoulli Naive Bayes) also multiplies (1 − p) for every *absent* word. The exam defines its own version, so always use the paper's formula |
| 41 | K-means clustering | 8:30 | 3 | |
| 40 | Hierarchical Clustering | 11:19 | 3 | Linkage (single vs complete) is what questions vary: problem 3.4 |
| 30 | PCA, Step-by-Step | 21:58 | 3 | After notebook 03 §7 |
| 9 | The Main Ideas of Fitting a Line to Data | 9:22 | 3 | Least squares, for B4. Skip #10 (27 min, mostly R² and p-values) |
| 71 | Cosine Similarity, Clearly Explained | 10:14 | 4 | For retrieval and similarity questions (2025's Similarity Sleuth) |

**Earn the skip** (you know these): solve the problems in the last column without help, and you can skip the video. Miss one? Watch it, then log the miss.

| # | Video | Length | Test yourself with |
|---|---|---|---|
| 3 | The Confusion Matrix | 7:13 | 1.5 |
| 4 | Sensitivity and Specificity | 11:47 | 1.1, 1.3 |
| 23 | ROC and AUC, Clearly Explained | 16:17 | 1.2; Jan 18 B1 Q3–Q5 |
| 2, 6 | Cross Validation; Bias and Variance | 6:05, 6:36 | Nothing needed: Stage 1 only asks what train/test splits are for |
| 43 | K-nearest neighbors | 5:30 | 3.1 |
| 46 | Decision and Classification Trees | 18:08 | 3.3 (Gini, as in the video) |

**Optional:** 31 (PCA main ideas in 5 minutes), 7 (Entropy, in case a tree question uses information gain instead of Gini), 16 (Logistic Regression, one kind of linear classifier), 11 (Multiple Regression, 5 min), 5 (the 42-second sing-along, which really does help with precision vs recall).

**After 13 Dec** (Stage 2: overfitting, tuning, embeddings, retrieval, scikit-learn): 25–28, 32, 47, 50, 52–53, 55–57, 76–86, 89, 91–94, plus the Python walkthroughs 34, 51 and 75.

**Skip:**
- R-only: 21, 24, 29, 33, 38, 54
- Statistical inference (p-values, deviance, ANOVA, odds ratios): 10, 12–15, 17–20, 22
- Methods on no INAIO syllabus: 8, 35, 37, 39, 42, 45, 48–49, 58–62, 64–70, 72–74, 87–88, 90
- Already covered, or just for fun: 1, 36, 63
- Beyond Stage 2 (PyTorch, transformer matrix maths): 95–100

## PCA: why eigenvectors, why the covariance matrix?

Most explanations show *how* to do PCA and skip *why*. Notebook 03 §7 builds the why in three steps, and it's mostly reading:

- **7a. Spread along a direction:** the sum of the squared shadows of the points on a line through the centre.
- **7b. Why the covariance matrix:** expand one squared shadow, and you find that the spread in *every* direction depends on just three sums: Σx², Σxy and Σy². The scatter matrix is those three sums arranged in a grid, so that spread = u · (S u). Think of it as a machine: feed it a direction, and it tells you the spread along it. (The covariance matrix is the same grid divided by n. Dividing doesn't change which direction wins.)
- **7c. Why eigenvectors:** at the peak of the spread curve, S doesn't turn u, so S u = λ u. The spread there equals λ.

7c proves "the peak is an eigenvector" with a derivative. There's also a proof with no calculus, and you know enough linear algebra to find it. Try it after 7c:

> The two eigenvectors of S are perpendicular (in §7c they're at 18.43° and 108.43°). Write any direction in that eigenvector grid: u = cos φ · e₁ + sin φ · e₂. What does u · (S u) become? Why does that make it obvious that the best φ is 0?

An animation for this is first in the queue in `viz/README.md`.

## Alternative routes to Stage 2 (from inaio.in)

Some students qualify for Stage 2 directly:
- INOI medalists
- PLO training-camp participants
- INMO qualifiers
- top scorers in **Bebras India** (Mahavira and Ramanujam categories)

Check [inaio.in](https://www.inaio.in/) for the exact rules. These aren't a substitute for Stage 1 prep, but worth knowing about. Bebras is your main logic resource anyway, so ask your school whether it's registered for this year's Bebras India challenge.
