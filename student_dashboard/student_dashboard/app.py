"""Streamlit UI. Run with: streamlit run app.py"""
import pandas as pd
import streamlit as st

import config
import database
import services


def show_add_student_form() -> None:
    st.subheader("Add Student")
    student_name = st.text_input("Student Name")
    student_score = st.number_input(
        "Score", min_value=config.MIN_SCORE, max_value=config.MAX_SCORE, step=1
    )
    if not st.button("Add Student"):
        return

    error_message = services.validate_student(student_name, student_score)
    if error_message:
        st.error(error_message)
        return
    database.add_student(student_name.strip(), int(student_score))
    st.success(f"{student_name.strip()} added.")


def show_statistics(students: list[dict]) -> None:
    st.subheader("Statistics")
    stats = services.calculate_statistics(students)
    columns = st.columns(4)
    columns[0].metric("Total Students", stats["total"])
    columns[1].metric("Average Score", stats["average"])
    columns[2].metric("Highest Score", stats["highest"])
    columns[3].metric("Lowest Score", stats["lowest"])


def show_students_table(students: list[dict]) -> None:
    table = pd.DataFrame(services.add_grades(students))
    if table.empty:
        st.info("No students found.")
        return
    table.columns = ["Name", "Score", "Grade"]
    st.dataframe(table, hide_index=True, use_container_width=True)


def main() -> None:
    st.title("Student Performance Dashboard")
    show_add_student_form()

    search_text = st.text_input("Search Student")
    students = database.get_student(search_text) if search_text else database.get_students()

    show_statistics(students)
    st.subheader("Students")
    show_students_table(students)


if __name__ == "__main__":
    main()
