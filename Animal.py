from abc import ABC ,abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def eating(self):
        print("animal is eating")


class cat(Animal):
    def make_sound(self):
        print("meow")

    def eating(self):
        print(f"the {self.name} is eating")

class dog(Animal):
    def make_sound(self):
        print("wow")

    def eating(self):
        print(f"the {self.name} is eating")



Cat=cat("Tom")
Cat.make_sound()
Cat.eating()

Dog =dog("Alex")
Dog.eating()
Dog.make_sound()
