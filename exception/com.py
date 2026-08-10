try:
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    print(x/y)
except ValueError:
    print("invalid integer value")
except ZeroDivisionError:
    print("division by zero is error")
else:
    print("division:",x/y)
finally:
    print("Execution completed")