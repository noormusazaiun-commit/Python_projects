from abc import ABC ,abstractmethod

class person(ABC):

    def __init__(self,name,email):
        self.name=name
        self.email=email
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,value):
        if "@" not in value:
            raise ValueError("invalid Email Address")
        self._email=value

    @abstractmethod
    def info():
        pass

    def __str__(self):
        return f"Name : {self.name} \n Email : {self.email}"

class Student(person):
    def __init__(self, name, email,student_id):
        super().__init__(name, email)
        self.student_id=student_id

    def info(self):
        return f"Student | ID : {self.student_id}"

    def __str__(self):
        return f"{super().__str__() },{self.info()}"

class Lecturer(person):
    def __init__(self, name, email,subject):
        super().__init__(name, email)
        self.subject=subject

    def info(self):
        return f"Lecturer | Subject : {self.subject}"
        

    def __str__(self):
        return f" {super().__str__()} , {self.info()}"


class Course:
    def __init__(self,course_name,lecturer):
        self.course_name=course_name
        self.lecturer=lecturer
        self.student = []

    def add_student(self,student):
        self.student.append(student)
    def __str__(self):
        return f"Course : {self.course_name} , lecturer : {self.lecturer.name}"



student1 =Student("Noor","noor123@gmail.com","001")
student2 =Student("sahil","sahilafg@gmail.com","002")

lecturer=Lecturer("EN Ahmad","EN_ahamd@gamil.com","Programming")

course=Course("Python OOP",lecturer)

course.add_student(student1)
course.add_student(student2)

people=[student1,student2,lecturer]

for person in people:
    print(person.info())

print("\n==========================Course Information ===================")
print(course)

print("\n==========================Student Information===================")
for student in course.student:
    print(student)