# class Student:
#     def __init__(self,name,age,grade):
#         self.name =name
#         self.set_age(age)
#         self.set_grade(grade)

#     def get_age(self):
#         return self.__age

#     def set_age(self,age):
#         if age>5 and age<100:
#             self.__age=age
#         else :
#             raise ValueError("the age must be in (5,100)")
        
#     def get_grade(self):
#         return self.__grade

#     def set_grade(self,grade):
#         if grade>0 and grade<100:
#             self.__grade=grade
#         else :
#             raise ValueError("the grade must be in (0,100)")

# student=Student("ali",28,88)
# print(student.get_age())
# student.set_grade(99)
# print(student.get_grade())






# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"Hello my name is {self.name}\nI am {self.age} Years")

# class Student(Person):
#     def __init__(self, name, age,sub):
#         super().__init__(name, age)
#         self.sub=sub
#     def info(self):
#         return super().info() , print(f"i like {self.sub}")
        

    
# student=Student("ali",19,"math")
# student.info()







# class Animal:
#     def speak(self):
#         pass

# class Cat(Animal):
#     def speak(self):
#         print("Meow")

# class Dog(Animal):
#     def speak(self):
#         print("woof")

# animals=[Dog(),Cat()]
# for animal in animals:
#     animal.speak()






# class Employee:
#     def work(self):
#         pass


# class Manager(Employee):
#     def work(self):
#         print("Manager is working")

# class Developer(Employee):
#     def work(self):
#         print("Developer is working")

# class Designer(Employee):
#     def work(self):
#         print("Designer is working")


# employes=[Manager(),Developer(),Designer()]

# for employee in employes:
#     employee.work()





# class CPU:
#     def process(self):
#         print("CPU is processing")

# class Computer:
#     def __init__(self):
#         self.cpu=CPU()

#     def run(self):
#         self.cpu.process()
#         print("Computer is runing")

# computer = Computer()
# computer.run()
# computer.cpu.process()





# class Deportment:
#     def __init__(self,teacher):
#         self.teacher = teacher

# class Teacher:
#     def __init__(self,name):
#         self.name = name

# teacher=Teacher("ali")
# deportment=Deportment(teacher)
# print(deportment.teacher.name)






# class Players:
#     def __init__(self,players):
#         self.players=players

#         """
#     we can also do this

#     def __str__(self):
#             return str(self.players)
#         """
    

#     def __str__(self):
#         name=""

#         for player in self.players:
#             name += player + "\n"

#         return name.strip()

#     def __len__(self):
#         return len(self.players)

# players=Players(["ali","ahmad","sahil"])

# print(len(players))
# print(players)






# class Car:
#     def __init__(self,company,model):
#         self.company=company
#         self.model=model

#     @property
#     def model(self):
#         return self.__model

#     @model.setter
#     def model(self,value):
#         if value > 2000:
#             self.__model =value
#         else :
#              raise ValueError ("the model is expaired")

#     def __str__(self):
#         return f"company {self.company}  model {self.model}"


# car1=Car("Corrola",2002)
# print(car1)
# car2=Car("Benz",2005)
# print(car2)



