"""Helpers shared by the prep notebooks.

    check(qid, answer)   spoiler-free answer checker (compares hashes, never prints the answer)
    test(fn, cases)      runs a function you wrote on small cases and reports what passed
    ready(fn, *args)     True once fn is implemented (explore cells wait for your BUILD steps)
    table(rows, header)  prints a small table so you can see every intermediate step

Authors can add answers from the command line (plain text never gets committed):

    python prep.py add 1.1P 26          # several accepted forms: python prep.py add J18-virus C 281
"""

import hashlib
import json
import math
import sys
from pathlib import Path

_ANSWERS_FILE = Path(__file__).with_name("answers.json")
_SALT = "inaio-prep"


def _load():
    try:
        return json.loads(_ANSWERS_FILE.read_text())
    except FileNotFoundError:
        return {}


def _norm(x):
    """Turn an answer into a canonical string: 0.750 -> '0.75', ' a, d ' -> 'a,d', [2, 13] -> '2,13'."""
    if isinstance(x, bool):
        return str(x).lower()
    if isinstance(x, (int, float)):
        v = round(float(x), 4)
        if v == int(v):
            return str(int(v))
        return f"{v:.4f}".rstrip("0").rstrip(".")
    if isinstance(x, (list, tuple)):
        return ",".join(_norm(i) for i in x)
    if isinstance(x, set):
        return ",".join(sorted(_norm(i) for i in x))
    s = str(x).strip().lower().replace(" ", "")
    try:
        return _norm(float(s))
    except ValueError:
        pass
    parts = s.split(",")
    if len(parts) > 1 and all(len(p) == 1 and p.isalpha() for p in parts):
        s = ",".join(sorted(parts))  # select-all answers: order doesn't matter
    return s


def _hash(qid, answer):
    return hashlib.sha256(f"{_SALT}|{qid}|{_norm(answer)}".encode()).hexdigest()[:16]


def check(qid, answer):
    """Check your answer to question `qid`. Prints 'correct' or 'not yet' and never the answer."""
    answers = _load()
    if qid not in answers:
        print(f"Unknown question id {qid!r}.")
        return None
    if answer is ... or answer is None:
        print(f"{qid}: write your answer first (replace the ...).")
        return None
    ok = _hash(qid, answer) in answers[qid]
    if ok:
        print(f"{qid}: correct.")
    else:
        print(f"{qid}: not yet. Re-check your working, then use the hint ladder in practice/solutions/.")
    return ok


def _close(got, expected):
    if isinstance(expected, float) or isinstance(got, float):
        try:
            return math.isclose(got, expected, rel_tol=1e-6, abs_tol=1e-9)
        except TypeError:
            return False
    if isinstance(expected, (list, tuple)) and isinstance(got, (list, tuple)):
        return len(got) == len(expected) and all(_close(g, e) for g, e in zip(got, expected))
    if isinstance(expected, dict) and isinstance(got, dict):
        return expected.keys() <= got.keys() and all(_close(got[k], v) for k, v in expected.items())
    return got == expected


def test(fn, cases):
    """Run fn(*args) for each (args, expected) pair and report. Unfinished stubs print TODO."""
    name = getattr(fn, "__name__", "function")
    passed = 0
    for args, expected in cases:
        if not isinstance(args, tuple):
            args = (args,)
        try:
            got = fn(*args)
        except NotImplementedError:
            print(f"TODO: {name} isn't written yet. Fill it in, then run this cell again.")
            return False
        except Exception as e:  # show the error but keep the notebook running
            print(f"{name}{args}: raised {type(e).__name__}: {e}")
            continue
        if _close(got, expected):
            passed += 1
        else:
            print(f"{name}{args}: got {got!r}, expected {expected!r}")
    print(f"{name}: {passed}/{len(cases)} tests passed.")
    return passed == len(cases)


def ready(fn, *sample_args):
    """True once fn is implemented (used by explore cells that need your BUILD functions)."""
    try:
        fn(*sample_args)
        return True
    except NotImplementedError:
        print(f"This cell needs {getattr(fn, '__name__', 'your function')}. Finish that BUILD step first.")
        return False


def table(rows, header=None):
    """Print rows (a list of lists) as an aligned text table."""
    rows = [[_fmt(c) for c in r] for r in rows]
    if header:
        rows = [list(map(str, header))] + rows
    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    for k, r in enumerate(rows):
        print("  ".join(c.rjust(w) for c, w in zip(r, widths)))
        if header and k == 0:
            print("  ".join("-" * w for w in widths))


def _fmt(c):
    if isinstance(c, float):
        return f"{c:.4g}"
    return str(c)


def add(qid, *accepted):
    """Author tool: store hashed accepted answers for qid in answers.json."""
    answers = _load()
    answers[qid] = sorted({_hash(qid, a) for a in accepted})
    _ANSWERS_FILE.write_text(json.dumps(answers, indent=1, sort_keys=True) + "\n")
    print(f"stored {qid} ({len(answers[qid])} accepted form(s))")


if __name__ == "__main__":
    if len(sys.argv) >= 4 and sys.argv[1] == "add":
        add(sys.argv[2], *sys.argv[3:])
    else:
        print(__doc__)
