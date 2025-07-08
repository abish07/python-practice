from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Start the car")
    def stop(self):
        print("Stop the car")
carObj = Car()
carObj.start()
carObj.stop()