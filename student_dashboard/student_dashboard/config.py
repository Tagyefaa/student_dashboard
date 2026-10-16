"""Application configuration. Values can be overridden with environment variables."""
import os

DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
DB_SERVER = os.getenv("DB_SERVER", "localhost")
DB_NAME = os.getenv("DB_NAME", "UniversityDB")

# Leave DB_USER empty to use Windows Authentication (Trusted Connection).
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

MIN_SCORE = 0
MAX_SCORE = 100
