class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def start(self):
        print("Car")
class Bike(Vehicle):
    def start(self):
        print("Bike")
class Bus(Vehicle):
    def start(self):
        print("Bus")
car=Car()
bike=Bike()
bus=Bus()
car.start()
bike.start()
bus.start()


