INSERT INTO students (name, second_name)
VALUES
    ('Mikita', 'Tester');

SET @student_id = LAST_INSERT_ID();

INSERT INTO books (title, taken_by_student_id)
VALUES
    ('Very very interesting book 1', @student_id),
    ('Very very interesting book 2', @student_id);

INSERT INTO `groups` (title, start_date, end_date)
VALUES
    ('Super puper Group', '11.09.2025', '10.09.2027');

UPDATE students SET group_id = (SELECT id FROM `groups` WHERE title = 'Super puper Group')
                WHERE id = @student_id;

INSERT INTO subjects (title) VALUES ('Super puper Subject 1'), ('Super puper Subject 2');

INSERT INTO lessons (title, subject_id)
VALUES
    ('Super puper Lesson 1 for Super puper Subject 1', (SELECT id FROM subjects WHERE title = 'Super puper Subject 1')),
    ('Super puper Lesson 2 for Super puper Subject 1', (SELECT id FROM subjects WHERE title = 'Super puper Subject 1')),
    ('Super puper Lesson 1 for Super puper Subject 2', (SELECT id FROM subjects WHERE title = 'Super puper Subject 2')),
    ('Super puper Lesson 2 for Super puper Subject 2', (SELECT id FROM subjects WHERE title = 'Super puper Subject 2'));

INSERT INTO marks (value, lesson_id, student_id)
VALUES
    ('5',
     (SELECT id FROM lessons WHERE title = 'Super puper Lesson 1 for Super puper Subject 1'),
     @student_id
    ),
     ('4',
     (SELECT id FROM lessons WHERE title = 'Super puper Lesson 2 for Super puper Subject 1'),
     @student_id
    ),
    ('3',
     (SELECT id FROM lessons WHERE title = 'Super puper Lesson 1 for Super puper Subject 2'),
     @student_id
    ),
     ('5',
     (SELECT id FROM lessons WHERE title = 'Super puper Lesson 2 for Super puper Subject 2'),
     @student_id
    );

SELECT value FROM  marks
             WHERE student_id = @student_id;

SELECT title FROM books
             WHERE taken_by_student_id = @student_id;

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
WHERE st.id = @student_id;
