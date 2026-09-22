class Car:
    def __init__(self,name , model,color):
        self.name =name
        self.model=model
        self.color=color


    def off (self):
            print("the car is turned off")

    
    def On (self):
            print("the car is turned on")

    def info(self):
        print(f"name {self.name}\nmodel {self.model}\ncolor {self.color}")

car=Car("benz","C300","bLack")

car.On()

car.info()