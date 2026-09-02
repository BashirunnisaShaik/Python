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
