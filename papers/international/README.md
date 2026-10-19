# Papers from other countries

Collected on 19 Oct 2026 from other countries' national AI olympiads (most are their selection rounds for IOAI) and from the International AI Olympiad (IAIO). **Every paper below is high-school level**: set for grades 9–12, or a band that overlaps it. Papers for younger students or university students were left out.

## What they're good for

None of them is a copy of INAIO Stage 1. They fall into two groups:

1. **English papers that test whether you know a concept.** USAAIO (USA), Canada, the Philippines, IAIO. They ask about regularisation, bias–variance, SVM margins and Hessians *without* defining them. That's the opposite of INAIO, but it's exactly the breadth from [issue #1](https://github.com/Shreeshinator/ioai-prep/issues/1). Use them on the free-week Thursday and in bonus week A, alongside the StatQuest familiarity list.
2. **Papers in INAIO's style, but not in English.** Iran, Russia, Hungary, Brazil, Colombia, Indonesia. They're pen-and-paper and define ideas inside the question, and most have answer keys. They need translating before Shreesh can use them.

**Licences:** only the Philippines papers (MIT licence) are copied into this repo. Everything else is linked, because it says "all rights reserved" or states no licence, and this repo is public. Varun has local copies of the rest in `_local/`, which git ignores.

## Keep these unopened: Sun 22 Nov mock

- **Planned mock:** an English translation of **Iran's 2026 Stage 1 paper**. It's the closest match to INAIO conditions: 20 multiple-choice questions, pen and paper, no calculator, in person, with an answer key. The translation will be shared privately, because the original is "all rights reserved".
- **Backup:** **IAIO 2024 Scientific Round**, questions 1, 3, 4 and 6.

Don't open either before 22 Nov.

## English papers: for breadth

| Paper | Level | Format | Answer key | Fit for Stage 1 | Where |
|---|---|---|---|---|---|
| **Philippines** IOAI PH 2026, National Finals theory | K–12, born on or after 1 Jul 2007 | 30 multiple choice, 1 h | No | Medium-high: short conceptual ML questions, a few with quick calculations | [`philippines-2026/`](philippines-2026/), copied from [ioaiph/2026](https://github.com/ioaiph/2026) (MIT, © IOAI Philippines) |
| Philippines IOAI PH 2026, Semi-Finals theory | Same | 20 multiple choice, online, open book | No | Medium | [`philippines-2026/`](philippines-2026/) |
| **USAAIO** 2026 Round 1 (USA and Canada) | Middle or high school, under 20 | Problems 1–3 and part 4.1 are pen-and-paper multiple choice (ML concepts, a PCA projection, matrix maths); the rest is coding | No official key | High for Problems 1–3 | [usaaio.org/past-problems](https://usaaio.org/past-problems) |
| USAAIO 2025 Round 1 | Same | Notebook exam: 19 of 41 parts need no code (linear algebra, recurrences) | **Yes**, official solutions | Medium | [USAAIO forum](https://forum.beaver-edge.ai/c/ai-olympiads/usa-north-america-ai-olympiad/8) |
| **Canada** CAIO national qualifier, practice sets A, B, C (2026–27) | Grades 9–12 | 35 questions, 90 min | No | Medium: the fill-ins are INAIO-like; the rest is recall and Python tracing | [A](https://www.iaiocanada.com/assets/pdfs/2026-27-caio-national-qualifier-practical-competition-a.pdf) · [B](https://www.iaiocanada.com/assets/pdfs/2026-27-caio-national-qualifier-practical-competition-b.pdf) · [C](https://www.iaiocanada.com/assets/pdfs/2026-27-caio-national-qualifier-practical-competition-c.pdf) |
| Canada CJAIO (junior), Part 1 practice sets 1 and 2 | Grade 10 and below | Multiple choice + short answer, 60 min | No | Medium; Section D (k-means and logistic regression by hand) is very close | [Set 1](https://www.iaiocanada.com/CJAIO_Part1_Practice_Set_1_Questions.pdf) · [Set 2](https://www.iaiocanada.com/CJAIO_Part1_Practice_Set_2_Questions.pdf) |
| **IAIO** 2024 Scientific Round | Secondary school, 20 or under | 6 written questions | Model answers | High for Q1 (metrics), Q3 (k-means by hand), Q4 (counting transformer parameters), Q6 (a small decision process). Q2 is ethics; Q5 is too hard. **Backup mock: keep it unopened** | [PDF](https://www.iaio-official.org/wp-content/uploads/2025/11/IAIO2024_scientific_round_test.pdf) |
| **Kazakhstan** FAIO 2025 qualifier, tasks 1–3 | School students (exact grades not stated) | Short-answer theory (a Bayes test, probability) | No | Medium, easy | [GitHub](https://github.com/BeksultanSagyndyk/faio-tasks) (Apache-2.0) |

Also worth knowing: **[Training for the International AI Olympiad](https://iaio-official.org/wp-content/uploads/2026/02/IAIO-Training-Eljakim-Schrijvers.pdf)** (Eljakim Schrijvers, 2026, 381 pages, CC BY-NC 4.0). It's a free textbook with practice problems and answers (Appendix H). Shreesh likes learning by reading, so this suits him: dip into the chapters that match the StatQuest familiarity list.

## INAIO-style papers in other languages: need translating

| Paper | Level | Format | Answer key | Language | Where |
|---|---|---|---|---|---|
| **Iran** AI Olympiad, Stage 1, 2025 and 2026 | Grades 10–11 | 20 multiple choice, 150 min, in person, no calculator, +3/−1 marking | Yes | Persian | Young Scholars Club (YSC); official copies need a login. Local copies in `_local/iran/`. **2026 is the planned mock** |
| Iran AI Olympiad, Stage 2, 2025 and 2026 | Grades 10–11 | 15 multiple choice (120 min) + written paper | Multiple choice only | Persian | `_local/iran/` |
| **Russia** All-Russian olympiad (ВсОШ) in AI, regional stage Tour 1, Jan 2026 | Grades 9–11 | 8 theory problems, exact numeric answers | Yes | Russian | [vos.olimpiada.ru](https://vos.olimpiada.ru/upload/files/Arhive_tasks/2025-26/reg/ai/tasks-ai-9-11-tur1-reg-25-26.pdf) ([archive](https://vos.olimpiada.ru/subject/ai)) |
| Russia ВсОШ AI, Moscow school stage 2025/26 | Grades 9–11 | 8 tasks (2 need code): confusion-matrix metric, loss minimisation, probability, ensemble vote | Yes | Russian | [PDF](https://vos.olimpiada.ru/upload/files/Arhive_tasks/2025-26/school/ai/tasks-ai-9-11-sch-msk-25-26.pdf) |
| Russia ВсОШ AI, Moscow invitational stage 2026/27 | Grades 8–10 | Short answer: ROC AUC by counting pairs, probability, optimisation | Yes | Russian | [PDF](https://vos.olimpiada.ru/upload/files/Arhive_tasks/2026-27/prigl/iikt/tasks-ai-8-10-prigl-msk-26-27.pdf) |
| Russia ВсОШ AI, final Tour 1, Mar 2026 | Grades 9–11 | 6 written problems, some proofs. Harder | Yes | Russian | [PDF](https://vos.olimpiada.ru/upload/files/Arhive_tasks/2025-26/final/ai/tasks-ai-9-11-tur1-final-25-26.pdf) |
| **Hungary** HAIO national round 1 theory, 2025 and 2026 | Grades 9–12 (2026: up to grade 13) | Pen and paper, no aids, 60 min, multi-select multiple choice | Yes | Hungarian | GitHub, CC BY-NC-SA 4.0: [2026](https://github.com/Hungarian-AI-Olympiad/HAIO-Hungarian-AI-Olympiad/tree/main/2026/nyari-orszagos/elmeleti) · [2025](https://github.com/Hungarian-AI-Olympiad/HAIO-Hungarian-AI-Olympiad/tree/main/2025/nyari-orszagos/elmeleti) |
| **Colombia** OCIA round 2, 2025 | Grades 8–11 | 16 multiple choice; each idea is taught, then applied (Gini, k-means++, 2-D convolution by hand) | No | Spanish | [PDF](https://emersonjleon.github.io/emersonjleon/uan/OCdeIA/2025/selectiva.pdf) |
| **Brazil** ONIA phase 4, 2025 (two stages) | Finalists (school students; category not stated) | 20 multiple choice; stage 1 is 3 h with no calculators | Yes | Portuguese | [oniabrasil.com.br](https://oniabrasil.com.br/page1.html) |
| **Indonesia** OSN 2025 AI exhibition essay, and the official sample paper | Grades 10–12 | Written problems (a logic puzzle, hinge-loss gradient descent by hand, bigram probability) | No | Indonesian | [Essay](https://ioai.toki.id/assets/soal2025/Ekshibisi_Essay_Final_AI.pdf) · [Sample](https://ioai.toki.id/assets/contohsoal/Contoh_Soal_Eksebisi.pdf) |

## Not useful for Stage 1

- **Coding contests: Stage 2 material, after 13 Dec.** Poland, Romania, Bangladesh (BdAIO), Japan, Singapore's team selection, IOAI's own tasks, and the Russian NTO and DANO olympiads (DANO is statistics more than ML).
- **No public theory papers found:** Singapore, China, South Korea, Taiwan, the UK, Australia, Bulgaria, Spain, Ukraine, Vietnam and South Africa.
