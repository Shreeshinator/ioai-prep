# Notebooks: build the idea, then check it

Each notebook is a **guided derivation**, not an answer key. It goes:

**Hook** (why care) → **fundamentals** (smallest example, every step printed) → **PREDICT** (guess before running) → **BUILD** (you write the algorithm; tests confirm it) → **exam walkthrough** (a Jan 18 task, step by step) → **your turn** (practice set, spoiler-free checks) → **explore** (change a number, predict, run) → **connect** (link to earlier weeks).

| Notebook | Week | Jan 18 tasks inside |
|---|---|---|
| `01_metrics.ipynb` | 1 | B1 Code Triage |
| `02_probability.ipynb` | 2 | Pit-Stop Paradox, Blind Board Gambit |
| `03_algorithms.ipynb` | 3 | B4 Model Compression |
| `04_ranking_signals.ipynb` | 4 | B2 WonkaRank, B3 Convolution |
| `05_math_optimization.ipynb` | 5 | Godown, Catalyst, Crude Curve, V-67 |
| `06_puzzles_logic.ipynb` | 6 | Glyphs, Faulty Oracle, Smart Search, Pikachu |

> The exam walkthroughs reveal how each Jan 18 task works. Take the **diagnostic first** (Sun 18 Oct).

## Setup

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab            # or open the folder in VS Code
```

Open the notebooks **from this folder**, so that `import prep` works.

## Rules

- **Paper first.** Solve each practice problem on paper *before* touching its notebook cell.
- **BUILD stubs** contain `raise NotImplementedError`. Replace that line with your code, then re-run the test cell.
- `prep.check(id, answer)` compares against hashed answers, so it never prints the answer. (Yes, you could brute-force the hashes. Don't. You'd only be cheating your future self.)
- Clear outputs before committing: *Kernel → Restart & Clear Outputs*, or `jupyter nbconvert --clear-output --inplace *.ipynb`.
