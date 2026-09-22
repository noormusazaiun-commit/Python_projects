from abc import ABC,abstractmethod

class Person(ABC):
    @abstractmethod
    def __init__(self,name,email):
        self.name=name
        self.email=email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,value):
        if "@gmail.com" not in value:
            raise ValueError ("invalied email")
        else:
            self.__email=value

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def __str__(self):
        return f"Name : {self.name} \nEmail : {self.email}"

class Student(Person):
    def __init__(self, student_ID, name, email):
        super().__init__(name, email)
        self.student_ID=student_ID
        self.courses=[]

    def add_course(self,course):
        self.courses.append(course)

    def info(self):
        return f"ID : {self.student_ID} \nCourse : {self.courses}"
    
    def __str__(self):
        return f"I am a Student \n{super().__str__()} \n{self.info()}"

    def __repr__(self):
        return f"Student {self.student_ID}:{self.name}"

class Teacher(Person):
    def __init__(self, name, email,teacher_ID, subject):
        super().__init__(name, email)
        self.teacher_ID=teacher_ID
        self.subject=subject

    def info(self):
        return f"Id : {self.teacher_ID} \nSubject : {self.subject}"

    def __str__(self):
        return f"I am a Teacher \n{super().__str__()}\n{self.info()}"

class Course:
    def __init__(self,course_name):
        self.course_name =course_name
        self.students=[]

    def add_student(self,student):
        self.students.append(student)
        student.add_course(self.course_name)

    def __str__(self):
      
        return f"Course Name : {self.course_name}"
        


class School:
    def __init__(self,name, teachers):
        self.name=name
        self.teachers=teachers

    def show_teachers(self):
        i=1
        for teacher in self.teachers:
            print(i,":",teacher)
            i +=1

    def __str__(self):
        return f"School : {self.name}"

Student1=Student("001","ali","ali@gmail.com")
Student2=Student("002","ahmad","ahmad@gmail.com")
Student3=Student("003","sahil","sahil@gmail.com")
Student4=Student("004","hamid","hamid@gmail.com")

Teacher1=Teacher("osman","os@gmail.com","111","python")
Teacher2=Teacher("shaker","shah@gmail.com","211","database")

python_course=Course("Python")
python_course.add_student(Student1)
python_course.add_student(Student2)
database_course=Course("Database")
database_course.add_student(Student3)
database_course.add_student(Student4)


school=School("afg new School",["osman","shaker"])
print("=============================== School ================================")
print(school)
print("Teachers")
school.show_teachers()

print("\n=============================== Students ==============================")
print(Student1)
print()

print(Student2)
print()

print(Student3)
print()

print(Student4)
print()

print("\n=============================== Teachers ==============================")
print(Teacher1)
print()
print(Teacher2)
print()

print("\n============================== Courses ================================")
print(python_course)
print(python_course.students)
print(database_course)
print(database_course.students)
