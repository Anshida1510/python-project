class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)   # call Person __init__
        self.grade = grade

    def details(self):
        # Person details first
        super().details()
        # then Student part
        print(f"Grade: {self.grade}")


class CollegeStudent(Student):
    def __init__(self, name, age, grade, department):
        super().__init__(name, age, grade)   # call Student __init__
        self.department = department

    def details(self):
        # Student + Person details
        super().details()
        # then CollegeStudent part
        print(f"Department: {self.department}")


# ---- object creation and method calls ----

print("Person object:")
p1 = Person("Aliya", 40)
p1.details()
print()

print("Student object:")
s1 = Student("Rahul", 16, "10th")
s1.details()
print()

print("CollegeStudent object:")
c1 = CollegeStudent("Meera", 19, "1st year", "Computer Science")
c1.details()
