"""Task 2: example of refactoring bad code into Clean Code."""

# ---------- BEFORE (bad) ----------
def f(x, y):
    if y >= 90:
        r = "A"
    elif y >= 80:
        r = "B"
    elif y >= 70:
        r = "C"
    elif y >= 60:
        r = "D"
    else:
        r = "F"
    print(x, y, r)
    t = 0
    for i in [85, 72, 48, 91, 63]:
        t = t + i
    print(t / 5)


# ---------- AFTER (clean) ----------
GRADE_THRESHOLDS = ((90, "A"), (80, "B"), (70, "C"), (60, "D"))
FAILING_GRADE = "F"


def calculate_grade(score: float) -> str:
    for minimum_score, grade in GRADE_THRESHOLDS:
        if score >= minimum_score:
            return grade
    return FAILING_GRADE


def calculate_average(scores: list[float]) -> float:
    return sum(scores) / len(scores) if scores else 0.0


def print_student_result(student_name: str, student_score: float) -> None:
    print(student_name, student_score, calculate_grade(student_score))


if __name__ == "__main__":
    student_scores = [85, 72, 48, 91, 63]
    print_student_result("Ali", 85)
    print(calculate_average(student_scores))
