"""Database layer: the only module that talks to SQL Server."""
from contextlib import closing

import pyodbc

import config


def _build_connection_string() -> str:
    parts = [
        f"DRIVER={{{config.DB_DRIVER}}}",
        f"SERVER={config.DB_SERVER}",
        f"DATABASE={config.DB_NAME}",
    ]
    if config.DB_USER:
        parts += [f"UID={config.DB_USER}", f"PWD={config.DB_PASSWORD}"]
    else:
        parts.append("Trusted_Connection=yes")
    parts.append("TrustServerCertificate=yes")
    return ";".join(parts)


def create_connection() -> pyodbc.Connection:
    return pyodbc.connect(_build_connection_string())


def _rows_to_students(rows) -> list[dict]:
    return [{"name": row.Name, "score": row.Score} for row in rows]


def add_student(student_name: str, student_score: int) -> None:
    query = "INSERT INTO dbo.Students (Name, Score) VALUES (?, ?)"
    with closing(create_connection()) as connection:
        connection.execute(query, student_name, student_score)
        connection.commit()


def get_students() -> list[dict]:
    query = "SELECT Name, Score FROM dbo.Students ORDER BY StudentId"
    with closing(create_connection()) as connection:
        return _rows_to_students(connection.execute(query).fetchall())


def get_student(student_name: str) -> list[dict]:
    """Return all students whose name contains `student_name` (case-insensitive)."""
    query = "SELECT Name, Score FROM dbo.Students WHERE Name LIKE ? ORDER BY StudentId"
    with closing(create_connection()) as connection:
        rows = connection.execute(query, f"%{student_name}%").fetchall()
        return _rows_to_students(rows)
