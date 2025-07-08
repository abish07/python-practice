# Polymorphism
class vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
    def showDetails(self):
        print(f"Name : {self.name}")
        print(f"Color : {self.color}")
        print(f"Price : {self.price}")
    def maxSpeed(self):
        print("The max speed is 180 km/hr")
    def gears(self):
        print("5")

class car(vehicle):
    def maxSpeed(self):
        print(f"The max speed is 200 km/hr")
    def gears(self):
        print("6")

class Truck(vehicle):
    def maxSpeed(self):
        print(f"The max speed is 100 km/hr")
    def gears(self):
        print("7")

truckObj = Truck("Toyota","red","100000$")
truckObj.maxSpeed()
truckObj.gears()

carObj = car("Toyota","red","100000$")
carObj.maxSpeed()
carObj.gears()