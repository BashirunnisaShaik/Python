class salary:
    def show(self,ws,b=0):
        print("before bonus:",ws)
        print("after bonus:",ws+b)
       
s=salary()
s.show(9000,1000)