t1=(10,20,30,40,50,60,70,80,)
print(len(t1))
print(t1[0])
print(t1[7])
print(t1[2])
print(t1[:4])
print(t1[2:6])
print(t1[-3:])
print(t1[1:])
print(t1[:-1])
print(t1[::-1])
print(t1[::2])
print(t1[1::2])
print(t1[6])
print(30 in t1)

l2=(5,3)
print(5*2)

t2=("C","ds","python","java")
print(t2.index("python"))

t3=(10,3,20)
print(t3.count(10))
print("java" in t2)
print(t1+t3)
print(t1*3)

li=[10,2,3,9]
print(type(li))
t4=tuple(li)
print(type(t4))

l2=list(t4)
print(type(l2))
l2.append(50)
print(l2)
t5=tuple(l2)
print(type(t5))

t6=list(l2)
print(type(t6))
l2.remove(50)
print(l2)
t7=tuple(l2)
print(type(t7))

t8=list(l2)
print(type(t8))
li[3]=80
print(li)

n =int(input("enter tuple values:"))
l3=[]
l3.append(n)
t9=tuple(l3)
print(type(t9))
print(t9)

li[2]=213
print(li)


t11=tuple(input("tuple:"))
print(t11)

print(max(t1))
print(min(t1))

sum=0
for x in li:
    sum+=x
print(sum)

t12=sum
t15=len(li)
avg=t12/t15
print(avg)






