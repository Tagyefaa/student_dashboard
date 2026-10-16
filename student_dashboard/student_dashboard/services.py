"""Business logic: grades, statistics and input validation. No DB or UI code here."""
import config

GRADE_A_MIN_SCORE = 90
GRADE_B_MIN_SCORE = 80
GRADE_C_MIN_SCORE = 70
GRADE_D_MIN_SCORE = 60

GRADE_THRESHOLDS = (
    (GRADE_A_MIN_SCORE, "A"),
    (GRADE_B_MIN_SCORE, "B"),
    (GRADE_C_MIN_SCORE, "C"),
    (GRADE_D_MIN_SCORE, "D"),
)
FAILING_GRADE = "F"


def calculate_grade(score: float) -> str:
    for minimum_score, grade in GRADE_THRESHOLDS:
        if score >= minimum_score:
            return grade
    return FAILING_GRADE


def add_grades(students: list[dict]) -> list[dict]:
    return [{**student, "grade": calculate_grade(student["score"])} for student in students]


def calculate_statistics(students: list[dict]) -> dict:
    scores = [student["score"] for student in students]
    if not scores:
        return {"total": 0, "average": 0.0, "highest": 0, "lowest": 0}
    return {
        "total": len(scores),
        "average": round(sum(scores) / len(scores), 1),
        "highest": max(scores),
        "lowest": min(scores),
    }


def validate_student(student_name: str, student_score: float) -> str | None:
    """Return an error message, or None if the input is valid."""
    if not student_name.strip():
        return "Student name cannot be empty."
    if not config.MIN_SCORE <= student_score <= config.MAX_SCORE:
        return f"Score must be between {config.MIN_SCORE} and {config.MAX_SCORE}."
    return None
