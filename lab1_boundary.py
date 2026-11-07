"""Lab 1 - Section 1.6: isolate the effect of the boundary score and probability.

Each input is changed SEPARATELY so a disagreement can be traced to one cause.
All values are synthetic lab assumptions.
Run: python lab1_boundary.py
"""


def symbolic(score, complete):
    return "Review" if complete and score >= 70 else "Hold"


def threshold(probability):
    return "Review" if probability >= 0.70 else "Hold"


# (label, score, complete, probability)
runs = [
    ("baseline (70, 0.70)",         70, True, 0.70),
    ("score only changed to 69",    69, True, 0.70),
    ("probability only changed 0.69", 70, True, 0.69),
    ("both changed (69, 0.69)",     69, True, 0.69),
]

print("run | symbolic | threshold | disagreement")
for label, score, complete, probability in runs:
    a, b = symbolic(score, complete), threshold(probability)
    print(label, a, b, a != b, sep=" | ")
