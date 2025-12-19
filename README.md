# Student Management System (Python, OOPS, SQLite)

## Overview
This is a **Student Management System** developed using **Python**, **Object-Oriented Programming (OOPS)**, and **SQLite**.  
The application allows users to perform **CRUD operations** (Create, Read, Update, Delete) on student records through a menu-driven interface.  

## Features
- Add new students
- View all students
- Update student information
- Delete students
- Stores data persistently using SQLite
- Uses Object-Oriented Programming principles for clean, modular code

## Technologies Used
- Python 3
- SQLite (sqlite3)
- Object-Oriented Programming (Classes, Objects, Encapsulation, Abstraction)

## Project Structure
Student-Management-System/
├── main.py # Main program
├── README.md # Project documentation
└── students.db # SQLite database (auto-created)

## How to Run
1. Clone or download the repository.
2. Make sure Python 3 is installed on your system.
3. Open terminal/command prompt in the project folder.
4. Run the program: python main.py

Follow the menu to add, view, update, or delete students.

##Demo

Here is an example of the program in action:

===== Student Management System =====
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
Enter choice (1-5): 1
Enter student name: indu
Enter student age: 10
Enter course: python
✅ Student added successfully!

===== Student Management System =====
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
Enter choice (1-5): 5
👋 Exiting program...

OOPS Concepts Used :

Class & Object: Student, DatabaseManager, StudentManagementSystem
Encapsulation: Database operations hidden in DatabaseManager
Abstraction: Users interact only with menu, not SQL logic
Reusability: Methods reused across classes

SQL Operations Used :

CREATE TABLE
INSERT (Add student)
SELECT (View students)
UPDATE (Update student)
DELETE (Delete student)
SQLite ensures persistent storage

Why This Project?

Demonstrates Python basics and OOPS concepts
Shows practical SQL knowledge

Author

Your Name – P.Induja

GitHub: [will paste link once i have created]
