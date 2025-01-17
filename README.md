-- To create a table STUDENTS
CREATE TABLE Students (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    MatriculationNumber VARCHAR(20),
    Gender VARCHAR(6)
);

-- To insert values into table STUDENTS
INSERT INTO Students (ID, Name, MatriculationNumber, Gender) VALUES
(1, 'Alice Johnson', '25CJ029200', 'Female'),
(2, 'Bob Smith', '25CJ029201', 'Male'),
(3, 'Charlie Brown', '25CJ029202', 'Male'),
(4, 'Diana Prince', '25CJ029203', 'Female'),
(5, 'Ethan Hunt', '25CJ029204', 'Male'),
(6, 'Fiona Apple', '25CJ029205', 'Female'),
(7, 'George Orwell', '25CJ029206', 'Male'),
(8, 'Hannah Montana', '25CJ029207', 'Female'),
(9, 'Ian Fleming', '25CJ029208', 'Male'),
(10, 'Julia Roberts', '25CJ029209', 'Female');

-- To display table STUDENTS
SELECT * FROM Students;

-- To update any value in table STUDENTS
UPDATE Students
SET Name = 'Ezinwa-Obi, Chidimma'
WHERE ID = 1;
