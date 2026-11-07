# Lab 1 - Introduction to AI & Paradigms

**Student:** Rasikh Ali (42365) | **Course:** CAI601400 - Artificial Intelligence | **Lab:** 1 (CLO1)

Compares a transparent rule-based scholarship pre-screening checker with a simple
probability-threshold rule. "Review" = flag for a **human** reviewer, not an award
decision. All scores, probabilities and thresholds are **synthetic lab assumptions**;
no model is trained and no accuracy is claimed.

## Setup
Requires Python 3.8+ (tested on 3.12). No third-party packages, no virtual
environment needed.

```bash
python --version
```

## Run
```bash
python lab1_compare.py     # symbolic vs. threshold, 4 cases + disagreement column
python lab1_boundary.py    # Section 1.6: isolate score=69 and probability=0.69
python lab1_rules.py       # Task 2: 4 rules, 4 core tests (exit code 0 = all pass)
```

## Files
| File | Purpose |
|---|---|
| `lab1_compare.py` | Section 1.5 experiment (symbolic vs. threshold) |
| `lab1_boundary.py` | Section 1.6 boundary isolation |
| `lab1_rules.py` | Task 2: extended rules (+ attendance, + signed form) and tests |
| `outputs/*.txt` | Captured outputs of the three scripts |
| `Lab1_Report.docx` | Full report: timeline, tests, disagreement table, analysis, reflection |

## Reproducing the outputs
```bash
python lab1_compare.py  > outputs/compare_output.txt
python lab1_boundary.py > outputs/boundary_output.txt
python lab1_rules.py    > outputs/rules_output.txt
```

## Sources
`lab1_compare.py` is taken from the Lab 1 manual (Section 1.5). `lab1_boundary.py` and
`lab1_rules.py` are my own extensions following Sections 1.6 and Task 2. Historical
sources for the timeline are listed in the References section of `Lab1_Report.docx`.
No credentials, private data or virtual environments are included.
