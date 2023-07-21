class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  
        print(name , age, grade)

    def get_grade(self):
        return self.grade

class Course:
    
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student (self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
        
    def get_average_grade(self):
        value = 0
        for i in self.students:
            value += i.grade
        average = value / len(self.students)
        return average
#------------------------------------------------------------------------------------------------------------------------

s1 = Student("Muneeb", 16, 95)
s2 = Student("Fatima", 14, 60)
s3 = Student("Eshaal", 12, 80)

Maths = Course("Mathematics", 3)
Maths.add_student(s1)
Maths.add_student(s2)
Maths.add_student(s3) 

print(Maths.get_average_grade())