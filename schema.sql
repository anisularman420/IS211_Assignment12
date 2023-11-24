-- schema.sql

-- Create Students table
CREATE TABLE Students (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

-- Create Quizzes table
CREATE TABLE Quizzes (
    id INTEGER PRIMARY KEY,
    subject TEXT NOT NULL,
    questions INTEGER NOT NULL,
    date TEXT NOT NULL
);

-- Create Results table
CREATE TABLE Results (
    student_id INTEGER,
    quiz_id INTEGER,
    score INTEGER,
    PRIMARY KEY (student_id, quiz_id),
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (quiz_id) REFERENCES Quizzes(id)
);

-- Insert sample data
INSERT INTO Students (first_name, last_name) VALUES ('John', 'Smith');
INSERT INTO Quizzes (subject, questions, date) VALUES ('Python Basics', 5, 'February 5, 2015');
INSERT INTO Results (student_id, quiz_id, score) VALUES (1, 1, 85);
