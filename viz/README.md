# Visualisations & animations

Built **on demand**, when an explanation needs a picture. Each visual starts from a question and answers it. Keep scenes under 60 s and about one idea. Use manim for derivations that unfold over time, and matplotlib for plots he should poke at.

## Conventions

- One folder per visual: `viz/<short-name>/`, containing the source (`scene.py` or `plot.py`), the rendered output (`.mp4` or `.gif`, kept under 10 MB), and a 3-line `README.md` (the question it answers, which problems it supports, how to render it).
- manim: `pip install manim`, then `manim -pqm scene.py SceneName` (`-qm` = medium quality).
- Link each visual from the matching solution's hint ladder or notebook section once it exists.

## Shortlist: where a visual would help most

Ranked by how often students get stuck on the idea:

| # | Question the visual answers | Supports | Suggested form |
|---|---|---|---|
| 1 | Why does Bayes "zoom in"? 1,000 dots, filter by evidence, count | 1.1, 2.1–2.3, Pit-Stop | manim: dot grid → highlight → ratio |
| 2 | Where does the ROC staircase come from? Sweep the threshold down the sorted scores | 1.2, B1 Q3–Q5 | manim: number line of scores + ROC drawn step by step |
| 3 | Why is AUC a pair count? Each right-step's area = positives above that negative | 1.2 | manim, following on from #2 |
| 4 | Why does the exam's convolution flip the kernel? Slide-and-multiply, flipped vs not | 4.5, 4.6, B3 | manim: kernel sliding over the signal, both versions side by side |
| 5 | Why does the median minimise total distance? Nudge the point and watch the left/right counts | 1.4, 5.1, Godown | matplotlib slider or manim |
| 6 | Why does a knight path alternate colours? Colour the board, animate the moves | 6.1, Pikachu | manim |
| 7 | How does k-means move? Assign → average → repeat, from two different starts | 3.2 | matplotlib animation |
| 8 | What is PageRank's random surfer? Dots hopping along links, with the histogram converging | 4.2 | manim or matplotlib animation |
| 9 | Why do marginal gains equalise? Two parabolas and a budget line | 5.2, Catalyst | matplotlib with a slider |

## Built so far

*(none yet)*
