date=int(input("enter date:"))
if date==1 and date<=15:
    print("starting date of the month")
elif date>=15 and date<=25:
    print("Middle date of the month")
elif date>=25 and date<=32:
    print("end of the month")
else:
    print("invalid")