import mysql.connector as mysql


def db_connection():
    db = mysql.connect(
        host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
        user="st-onl",
        passwd="AVNS_tegPDkI5BlB2lW5eASC",
        port=25060,
        database="st-onl",
    )
    cursor = db.cursor(dictionary=True)
    return db, cursor


def create_student(name, second_name):
    db, cursor = db_connection()
    cursor.execute("""
        INSERT INTO students (name, second_name)
        VALUES (%s, %s);
    """, (name, second_name))
    db.commit()
    student_id = cursor.lastrowid
    db.close()
    return student_id


def create_books(data):
    db, cursor = db_connection()
    cursor.executemany("""
        INSERT INTO books (title, taken_by_student_id)
        VALUES (%s, %s);
    """, data)
    db.commit()
    db.close()


def create_group(title, start_date, end_date):
    db, cursor = db_connection()
    cursor.execute("""
        INSERT INTO `groups` (title, start_date, end_date)
        VALUES (%s, %s, %s);
    """, (title, start_date, end_date))
    db.commit()
    group_id = cursor.lastrowid
    db.close()
    return group_id


def update_student_group(group_id, student_id):
    db, cursor = db_connection()
    cursor.execute("""
        UPDATE students
        SET group_id = %s
        WHERE id = %s
    """, (group_id, student_id))
    db.commit()
    db.close()


def create_subjects(data):
    db, cursor = db_connection()
    ids = []
    for elem in data:
        cursor.execute("""
            INSERT INTO subjects (title)
            VALUES (%s);
        """, elem)
        ids.append(cursor.lastrowid)
    db.commit()
    db.close()
    return ids


def create_lessons(lessons_data, subjects_ids):
    db, cursor = db_connection()
    ids = []
    for (title,) in lessons_data:
        for subject_id in subjects_ids:
            cursor.execute("""
                INSERT INTO lessons (title, subject_id)
                VALUES (%s, %s);
            """, (title, subject_id))
            ids.append(cursor.lastrowid)
    db.commit()
    db.close()
    return ids


def add_marks(lessons_ids, student_id):
    db, cursor = db_connection()
    data = [(5, lesson_id, student_id) for lesson_id in lessons_ids]
    cursor.executemany("""
        INSERT INTO marks (value, lesson_id, student_id)
        VALUES (%s, %s, %s);
    """, data)
    db.commit()
    db.close()


def get_marks(student_id):
    db, cursor = db_connection()
    cursor.execute("""
        SELECT value FROM marks
        WHERE student_id = %s;
    """, (student_id,))
    result = cursor.fetchall()
    db.close()
    return result


def get_books(student_id):
    db, cursor = db_connection()
    cursor.execute("""
        SELECT title FROM books
        WHERE taken_by_student_id = %s;
    """, (student_id,))
    result = cursor.fetchall()
    db.close()
    return result


def get_all_data(student_id):
    db, cursor = db_connection()
    cursor.execute("""
        SELECT
            st.id AS student_id,
            st.name AS student_name,
            st.second_name AS student_second_name,
            g.title AS group_title,
            b.title AS book_title,
            m.value AS mark_value,
            l.title AS lesson_title,
            s.title AS subject_title
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
        WHERE st.id = %s;
    """, (student_id,))
    result = cursor.fetchall()
    db.close()
    return result


student_id = create_student("Ivan", "Ivanov")

books_data = [("My Book 1", student_id), ("My Book 2", student_id)]
create_books(books_data)

group_id = create_group("Group 1", "2017-09-01", "2021-05-30")

update_student_group(group_id, student_id)

subjects_data = [("Subject One",), ("Subject Two",)]
subjects_ids = create_subjects(subjects_data)

lessons_data = [("Lesson One",), ("Lesson Two",)]
lessons_ids = create_lessons(lessons_data, subjects_ids)

add_marks(lessons_ids, student_id)

print(get_marks(student_id))
print(get_books(student_id))
print(get_all_data(student_id))
