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

class Animal:
    def sound(self):
        print("Animals sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
class Cow(Animal):
    def sound(self):
        print("Cow moos")
ani=Animal()
ani.sound()
cat=Cat()
dog=Dog()
cow = Cow()
cat.sound()
dog.sound()
cow.sound()

class Employee:
    def calculate_salary(self):
        print("Employee salary")
class Manager(Employee):
    def calculate_salary(self):
        print("Manager Salary=80000")
class Developer(Employee):
    def calculate_salary(self):
        print("Developer Salary=50000")
manager = Manager()
developer = Developer()
manager.calculate_salary()
developer.calculate_salary()