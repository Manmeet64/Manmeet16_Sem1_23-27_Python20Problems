'''
Create three classes, “Person,” “Employee,” and “Student.” Use multiple
inheritance to create a class “PersonInfo” that inherits from both “Employee” and
“Student.” Add attributes and methods specific to each class.
'''
# Define a class to represent basic Person information
class Person:

    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display person information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Define a class to represent Employee information
class Employee:

    # Constructor to initialize employee ID and department
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    # Method to display employee information
    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")

    # Method to simulate employee working
    def work(self):
        print("Employee is working.")

# Define a class to represent Student information
class Student:

    # Constructor to initialize student ID and major
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    # Method to display student information
    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Major: {self.major}")

    # Method to simulate student studying
    def study(self):
        print("Student is studying.")

# Define a class to combine Person, Employee, and Student information
class PersonInfo(Employee, Student):  # Inherit from Employee and Student

    # Constructor to initialize all attributes
    def __init__(self, name, age, employee_id, department, student_id, major):
        Employee.__init__(self, employee_id, department)  # Call Employee constructor first
        Student.__init__(self, student_id, major)         # Call Student constructor next
        Person.__init__(self, name, age)                  # Call Person constructor last

    # Method to display combined person, employee, and student information
    def display_person_info(self):
        # self.display_info()  # Uncomment this line if you also want to display Person info
        self.display_employee_info()
        self.display_student_info()


def main():
    person_info = PersonInfo("John Doe", 25, "E123", "IT", "S456", "Computer Science")

    person_info.display_person_info()

    # Accessing methods from the Employee and Student classes
    person_info.work()
    person_info.study()

if __name__=="__main__":
    main()