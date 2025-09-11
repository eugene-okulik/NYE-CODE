INSERT INTO students (name, second_name, group_id)
VALUES
    ('Mikita', 'Tester', 1);

INSERT INTO books (title, taken_by_student_id)
VALUES
    ('Very interesting book 1', (SELECT ID FROM students
                                           WHERE name = 'Mikita' and second_name = 'Tester')),
    ('Very interesting book 2', (SELECT ID FROM students
                                           WHERE name = 'Mikita' and second_name = 'Tester'));

INSERT INTO `groups` (title, start_date, end_date)
VALUES
    ('Super Group', '11.09.2025', '10.09.2027');

UPDATE students SET group_id = (SELECT id FROM `groups` WHERE title = 'Super Group' )
                WHERE name = 'Mikita' and second_name = 'Tester';

INSERT INTO subjects (title) VALUES ('Super Subject 1'), ('Super Subject 2');

INSERT INTO lessons (title, subject_id)
VALUES
    ('Super Lesson 1 for Super Subject 1', (SELECT id FROM subjects WHERE title = 'Super Subject 1')),
    ('Super Lesson 2 for Super Subject 1', (SELECT id FROM subjects WHERE title = 'Super Subject 1')),
    ('Super Lesson 1 for Super Subject 2', (SELECT id FROM subjects WHERE title = 'Super Subject 2')),
    ('Super Lesson 2 for Super Subject 2', (SELECT id FROM subjects WHERE title = 'Super Subject 2'));

INSERT INTO marks (value, lesson_id, student_id)
VALUES
    ('5',
     (SELECT id FROM lessons WHERE title = 'Super Lesson 1 for Super Subject 1'),
     (SELECT id FROM students WHERE name = 'Mikita' and second_name = 'Tester')
    ),
     ('4',
     (SELECT id FROM lessons WHERE title = 'Super Lesson 2 for Super Subject 1'),
     (SELECT id FROM students WHERE name = 'Mikita' and second_name = 'Tester')
    ),
    ('3',
     (SELECT id FROM lessons WHERE title = 'Super Lesson 1 for Super Subject 2'),
     (SELECT id FROM students WHERE name = 'Mikita' and second_name = 'Tester')
    ),
     ('5',
     (SELECT id FROM lessons WHERE title = 'Super Lesson 2 for Super Subject 2'),
     (SELECT id FROM students WHERE name = 'Mikita' and second_name = 'Tester')
    );

SELECT value FROM  marks
             WHERE student_id = (SELECT id FROM students WHERE name = 'Mikita' and second_name = 'Tester');

SELECT title FROM books
             WHERE taken_by_student_id = (SELECT id FROM students WHERE name = 'Mikita' and second_name = 'Tester');

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
JOIN "groups" g
    ON g.id = st.group_id
LEFT JOIN books b
    ON b.taken_by_student_id = st.id
LEFT JOIN marks m
    ON st.id = m.student_id
LEFT JOIN lessons l
    ON m.lesson_id = l.id
LEFT JOIN subjects s
    ON l.subject_id = s.id
WHERE st.name = 'Mikita';
