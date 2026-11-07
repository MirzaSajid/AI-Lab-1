"""Lab 1 - Task 2: transparent rule-based scholarship pre-screening.

"Review" means: flag the application for a HUMAN reviewer. It is NOT an award
decision. All thresholds below are SYNTHETIC LAB ASSUMPTIONS, not real policy.

Rules (all must hold for "Review"):
  1. score_ok              : score >= 70                     (from the manual)
  2. documents_complete    : all required documents present  (from the manual)
  3. attendance_ok         : attendance_pct >= 75            (added, synthetic)
  4. financial_form_signed : declaration form is signed      (added, synthetic)

Run: python lab1_rules.py
Exit code is 0 if every test passes, 1 otherwise.
"""
import sys

MIN_SCORE = 70
MIN_ATTENDANCE = 75  # percent


def evaluate(score, documents_complete, attendance_pct, financial_form_signed):
    """Return (decision, reason). Every failed rule is named in the reason."""
    failed = []
    if not score >= MIN_SCORE:
        failed.append(f"score_ok failed ({score} < {MIN_SCORE})")
    if not documents_complete:
        failed.append("documents_complete failed (missing document)")
    if not attendance_pct >= MIN_ATTENDANCE:
        failed.append(f"attendance_ok failed ({attendance_pct} < {MIN_ATTENDANCE})")
    if not financial_form_signed:
        failed.append("financial_form_signed failed (form unsigned)")

    if failed:
        return "Hold", "; ".join(failed)
    return "Review", "all four conditions satisfied"


# Exactly four core test cases: a pass, a failure of EACH new condition
# (one at a time, so the failure is attributable), and a threshold boundary.
TESTS = [
    # name, (score, docs, attendance, signed), expected
    ("pass_all",           (82, True, 88, True),  "Review"),
    ("fail_attendance",    (85, True, 60, True),  "Hold"),
    ("fail_unsigned_form", (85, True, 90, False), "Hold"),
    ("boundary_inclusive", (70, True, 75, True),  "Review"),
]


def main():
    print("Thresholds are synthetic lab assumptions: "
          f"score >= {MIN_SCORE}, attendance >= {MIN_ATTENDANCE}%.\n")
    failures = 0
    for i, (name, args, expected) in enumerate(TESTS, start=1):
        actual, reason = evaluate(*args)
        ok = actual == expected
        failures += not ok
        score, docs, att, signed = args
        print(f"Case {i}: {name}")
        print(f"  Input   : score={score}, documents_complete={docs}, "
              f"attendance_pct={att}, financial_form_signed={signed}")
        print(f"  Expected: {expected}")
        print(f"  Actual  : {actual}")
        print(f"  Reason  : {reason}")
        print(f"  Result  : {'PASS' if ok else 'FAIL'}\n")
    print(f"{len(TESTS) - failures}/{len(TESTS)} tests passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
