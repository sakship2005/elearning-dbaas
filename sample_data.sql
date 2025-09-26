INSERT INTO students (name, email) VALUES
("Alice Johnson", "alice@example.com"),
("Bob Smith", "bob@example.com"),
("Charlie Brown", "charlie@example.com");

INSERT INTO courses (title, description) VALUES
("Database Systems", "Learn SQL and relational models"),
("Web Development", "Build modern web applications"),
("Data Science", "Introduction to machine learning");

INSERT INTO enrollments (student_id, course_id) VALUES
(1, 1), -- Alice -> Database
(2, 2), -- Bob -> Web Development
(3, 3), -- Charlie -> Data Science
(1, 3); -- Alice -> Data Science
