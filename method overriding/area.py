class Shape:
    def area(self):
        print("Calculating Area")
class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle =",length*breadth)
class Circle(Shape):
    def area(self):
        print("Area of Circle =",3.14*radius*radius)
class Triangle(Shape):
    def area(self):
        print("Area of Triangle =",0.5*base*height)
r=Rectangle(10,20)
c=Circle(7)
t=Triangle(8,6)
r.area()
c.area()
t.area()