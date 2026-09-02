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