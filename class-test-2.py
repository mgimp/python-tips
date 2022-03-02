class Student:
    def __init__(self, arg_name, arg_age, arg_grade):
        self.name = arg_name
        self.age = arg_age
        self.grade = arg_grade  # [0, 100]

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, arg_name, arg_max_students):
        self.name = arg_name
        self.max_students = arg_max_students
        self.students = []

    def add_students(self, arg_student):
        if len(self.students) < self.max_students:
            self.students.append(arg_student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Geology", 2)
course.add_students(s1)
course.add_students(s2)
# print(course.students[0].name)  # OUT: Tim
print(course.get_average_grade())   # OUT: 80.0
print(course.add_students(s3))  # OUT: False

