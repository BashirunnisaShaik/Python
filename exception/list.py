c = ["Python", "Java", "Data Science","C"]
try:
    ind= int(input("Enter course index: "))
    print("Selected course:", c[ind])
except ValueError:
    print("Enter an integer index")
except IndexError:
    print("The selected course index is not available")