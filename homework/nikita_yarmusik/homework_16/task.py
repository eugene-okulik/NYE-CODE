import csv
import os

from dotenv import load_dotenv

import mysql.connector as mysql


load_dotenv(verbose=True)


def db_connection():
    db = mysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DATABASE"),
    )
    cursor = db.cursor(dictionary=False)
    return db, cursor


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(
    homework_path, "eugene_okulik", "Lesson_16", "hw_data/data.csv"
)


def read_csv(path):
    with open(path, newline="") as csvfile:
        file_data = csv.reader(csvfile)
        next(file_data)
        for row in file_data:
            yield row


def get_data(compare_data):
    db, cursor = db_connection()
    cursor.execute(
        """
        SELECT EXISTS(
            SELECT 1
            FROM students st
            JOIN `groups` g
                ON g.id = st.group_id
            LEFT JOIN books b
                ON b.taken_by_student_id = st.id
            LEFT JOIN marks m
                ON st.id = m.student_id
            LEFT JOIN lessons l
                ON m.lesson_id = l.id
            LEFT JOIN subjects s
                ON l.subject_id = s.id
            WHERE
                st.name = %s
                AND st.second_name = %s
                AND g.title = %s
                AND b.title = %s
                AND s.title = %s
                AND l.title = %s
                AND m.value = %s
        ) AS exists_flag;
    """,
        tuple(compare_data),
    )

    exists_flag = cursor.fetchone()[0]
    db.close()
    return exists_flag


csv_data = read_csv(file_path)


def check_in_db(data):
    for line in data:
        request = get_data(line)
        if not request:
            print("Нет в базе:", line)


check_in_db(csv_data)
