class Display:
    def show(self,a):
        print(a)
    def show(self,a,b):
        print(a,b)
    def show(self,a,b,c):
        print(a,b,c)
d=Display()
d.show(10,0,0)
d.show(10,20,0)
d.show(10,20,30)



class student:
    def show(self,name):         
        print(name)
    def show(Age):
       print(Age)
    def show(self,C):
       print(C)
s=student()
s.show("bashir")
s.show(17)
s.show("cse")

class salary:
    def show(self,ws,b=0):
        print("before bonus:",ws)
        print("after bonus:",ws+b)
       
s=salary()
s.show(9000,1000)


class message:
    def msg(self,o):
     print(o)
    def msg(self,p,ma):
     print(p,ma)
M=message()

M.msg("hi","welcome msg")

class bank:
    def deposit(self,a,b):
     print(a)

    def deposit(self,b,n):
     print(b+n)
b=bank()
b.deposit(100,90)
b.deposit(200,90)

class mathop:
    def mul(self,a,b):
     print(a*b)

c=mathop()
c.mul(2,4)

class shoppingcart:
    def pro(self,a,b,c):
        print(a+b+c)
s=shoppingcart()
s.pro(20,5,80)