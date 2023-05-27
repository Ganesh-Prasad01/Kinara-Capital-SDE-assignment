CREATE DATABASE student_database;
USE student_database;
CREATE TABLE students (
    id INT NOT NULL AUTO_INCREMENT,
    sname VARCHAR(255) NOT NULL,
    id_number VARCHAR(255) NOT NULL,
    total_marks INT NOT NULL,
    PRIMARY KEY (id)
);
-- Filter Table --
CREATE TABLE filtering (
    filter_name VARCHAR(255) NOT NULL,
    filter_value VARCHAR(255) NOT NULL,
    PRIMARY KEY (filter_name, filter_value)
);