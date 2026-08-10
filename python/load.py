class calculator:
   def add(self,a,b,c=0):
      print(a+b+c)
obj=calculator()
obj.add(2,3) #using 2 numbers 
obj.add(2,3,10) # using 3 numbers

class Area:
    def square(self,s):
     print(s*s)
    def rectangle(self,l,b): 
      print(l*b)
    def circle(self,r):
       print(3.14*r*r)
a=Area()
a.square(4)
a.rectangle(2,3)
a.circle(10)