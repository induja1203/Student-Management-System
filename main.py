import sqlite3

# -------------------- STUDENT CLASS --------------------
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


# -------------------- DATABASE MANAGER CLASS --------------------
class DatabaseManager:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT
        )
        """)
        self.conn.commit()

    def add_student(self, student):
        self.cursor.execute(
            "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
            (student.name, student.age, student.course)
        )
        self.conn.commit()

    def view_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def update_student(self, student_id, student):
        self.cursor.execute(
            "UPDATE students SET name=?, age=?, course=? WHERE id=?",
            (student.name, student.age, student.course, student_id)
        )
        self.conn.commit()

    def delete_student(self, student_id):
        self.cursor.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )
        self.conn.commit()

    def close(self):
        self.conn.close()


# -------------------- MAIN SYSTEM CLASS --------------------
class StudentManagementSystem:
    def __init__(self):
        self.db = DatabaseManager()

    def add_student(self):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        course = input("Enter course: ")

        student = Student(name, age, course)
        self.db.add_student(student)
        print("Student added successfully!\n")

    def view_students(self):
        students = self.db.view_students()
        if not students:
            print(" No records found.\n")
            return

        print("\nID | Name | Age | Course")
        print("-" * 30)
        for s in students:
            print(s)
        print()

    def update_student(self):
        student_id = int(input("Enter student ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        course = input("Enter new course: ")

        student = Student(name, age, course)
        self.db.update_student(student_id, student)
        print("Student updated successfully!\n")

    def delete_student(self):
        student_id = int(input("Enter student ID to delete: "))
        self.db.delete_student(student_id)
        print("Student deleted successfully!\n")

    def run(self):
        while True:
            print("    STUDENT MANAGEMENT SYSTEM   ")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")

            choice = input("Enter choice (1-5): ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                self.db.close()
                print("Exiting program")
                break
            else:
                print("Invalid choice. Try again.\n")


# -------------------- PROGRAM START --------------------
if __name__ == "__main__":
    app = StudentManagementSystem()
    app.run()
