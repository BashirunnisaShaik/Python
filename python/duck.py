class Duck:
    def talk(self):
        print("Duck is animal")
class Person:
    def talk(self):
        print("Persontalk")
def speak(obj):
    obj.talk()
d = Duck()
p = Person()
speak(d)
speak(p)

class Dog:
    def bark(self):
        print("Dog says: Bow Bow!")
class RobotDog:
    def bark(self):
        print("Robot Dog says: Beep Beep!")
def sound(obj):
    obj.bark()
d = Dog()
r = RobotDog()
sound(d)
sound(r)