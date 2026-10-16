# IOAI prep: INAIO 2027, Stage 1

Shreesh's preparation for the **Indian National AI Olympiad (INAIO) Stage 1**, the first step on the road to IOAI 2027. Varun mentors.

## The exam

| | |
|---|---|
| **Stage 1** | **Sun 13 Dec 2026, 10:00–12:00.** In person, objective questions, **no AI assistants** |
| Format details | INAIO publishes them about 2 weeks before (around 29 Nov). Update this table and `toolkit/EXAM_STRATEGY.md` then |
| Stage 2 | 24 Jan 2027. Online; AI assistants allowed in some sections; Python/ML |
| Later stages | Stage 3 (Mar/Apr, online) → Stage 4 (May, camp at IIIT Hyderabad) → IOAI 2027, Singapore, 4–10 July |
| Source | [inaio.in](https://www.inaio.in/), checked 16 Oct 2026 |

## What Stage 1 actually tests

Four past papers are analysed in `papers/README.md`. The test is **not** about how much ML you already know: every algorithm is defined inside the question. It tests three things:

1. **Reading a new definition and executing it exactly.** The B-sections each open with a Background box.
2. **Classic math reasoning in AI clothing:** Bayes, median vs mean, constrained optimisation, recurrences, colouring arguments.
3. **Careful bookkeeping under time pressure:** tie-break rules, strict vs non-strict inequalities, ⌊100x⌋.

Your deep-learning background gives you context, but it can mislead you. For example:
- the paper's "convolution" **flips** the kernel, and PyTorch's doesn't;
- its confusion matrix put **predictions on the rows**.

Trust the paper's definitions over your memory.

## How we work

Every week, notebook and problem answers five questions (details in `AUTHORING.md`):

- **Hook:** why should you care? We start from your robots and VLA work.
- **Aha:** the one insight to *reach*, not to be told.
- **Struggle:** where you'll get stuck, on purpose.
- **Practice:** reps until the move is automatic.
- **Connect:** how it links to everything before.

The loop for every problem:

> guess → solve **on paper** → check in the notebook (spoiler-free) → stuck? climb the **hint ladder**, one rung at a time → log the miss → make a variant → explain it to Varun on Sunday

## Start here (Shreesh)

1. Read [`PLAN.md`](PLAN.md). It takes 10 minutes and maps all 8 weeks.
2. Set up Python:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   jupyter lab notebooks/
   ```
3. **Sun 18 Oct: diagnostic.** Take `papers/2026-stage1-jan18/paper.pdf` in 2 hours, on paper, with no help.

## Repo map

| Path | What's there |
|---|---|
| [`PLAN.md`](PLAN.md) | The 8-week schedule (about 5 h/week, built around school) and the mock dates |
| [`practice/`](practice/) | Six original problem sets (problems + hint-ladder solutions) |
| [`notebooks/`](notebooks/) | Guided notebooks: build each idea from scratch, check answers without spoilers, explore |
| [`papers/`](papers/) | Official past papers + our worked solutions |
| [`toolkit/`](toolkit/) | `MOVES.md` (names for ideas you'll discover), `CONNECTIONS.md` (same idea, different clothes), `EXAM_STRATEGY.md` (timing, habits, constants, exam-day checklist) |
| [`log/`](log/) | Your error log, session log and mock scores. Fill these in every session |
| [`RESOURCES.md`](RESOURCES.md) | Curated external resources by topic |
| [`viz/`](viz/) | Visualisations and animations, built when an idea needs one |
| [`syllabus/`](syllabus/) | The official INAIO syllabus (Stage 1: pages 1–2) |
| [`AUTHORING.md`](AUTHORING.md) | How we write material here: pedagogy, solution format, notebook format |

## Collaboration

- **Shreesh:** commit and push after every session, e.g. `git commit -m "w2 tue: set 02 #1-3"`.
- **Questions:** open a GitHub issue titled with the problem id (e.g. "3.5: why is the eigenvector the direction?").
- **Varun:** reviews the logs on Sunday, runs the teach-back, picks the mixed sets, and builds visuals in `viz/`.
- **Don't open a paper before its mock date.** The Feb 28 retest only measures your growth if it's unseen.
