# Student Performance Dashboard

1. SQL Server-də `sql/setup.sql` faylını icra edin (UniversityDB, Students cədvəli, GetStudentResult).
2. `pip install -r requirements.txt` (ODBC Driver 17/18 for SQL Server quraşdırılmalıdır).
3. Lazım olsa `config.py`-da və ya mühit dəyişənlərində (DB_SERVER, DB_USER, DB_PASSWORD) bağlantını dəyişin.
4. `streamlit run app.py`

Quruluş: SQL Server -> database.py -> services.py -> app.py
