try:
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    print(x/y)
    print("completed")
except ZeroDivisionError:
    print("division by zero is error")
except ValueError:
    print("invalid integer value")
