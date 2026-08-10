try:
    age=int(input("enter age:"))
    if age<18:
       raise ValueError("enter above age 18 or 18")
    print("you are eligible")
except:
    print("you are not eligible")