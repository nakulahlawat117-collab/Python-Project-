
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)

    def calculate_result(self):
        if all(mark >= 40 for mark in self.marks):
            return "PASS"
        else:
            return "FAIL"

    def display(self):
        print("\n----- Student Details -----")
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Percentage:", self.calculate_percentage(), "%")
        print("Result:", self.calculate_result())


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        marks = []
        for i in range(3):
            mark = float(input(f"Enter marks of Subject {i+1}: "))
            marks.append(mark)

        student = Student(roll, name, marks)
        self.students.append(student)

        print("Student added successfully!")

    def display_all(self):
        if not self.students:
            print("No student records found.")
        else:
            for student in self.students:
                student.display()

    def search_student(self):
        roll = input("Enter Roll Number to search: ")

        for student in self.students:
            if student.roll_no == roll:
                student.display()
                return

        print("Student not found.")


# Main Program
system = StudentManagementSystem()

while True:
    print("\n===== STUDENT MARKS MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.display_all()

    elif choice == "3":
        system.search_student()

    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Try again.")
