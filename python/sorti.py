li=[2,1,3,4,0]
li.sort()
print(li)
li.sort(reverse=True)
print(li)

print("secondd largest:",li[-2])
lar=0
small=0
for x in li:
 if x>lar:
    small=lar
    lar=x
 elif x>small:
    small=x
print(small)

t=(1,2,3,5,6)
even=0
odd=0
for x in t:
    if x%2==0:
        even+=1
    else:
        odd+=1
print("even",even)
print("odd",odd)   

t2=("C","ds","python","java")
for x in t2:
 print(x)

t3=(30,20,50,25,90)
for x in t3:
    if x>50:
       print("greater than 50:" ,x)

for x in t3:
    if x%2==0:
        print("even:" ,x)

for x in t3:
    if x%2!=0:
        print("odd:" , x)

t4=(("name:","bashir"),("branch:","cse"),("marks:",952))
for x in t4:
    print(x[0],x[1])
