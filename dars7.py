# if max < a: = bolsa oxirgi, bolmasa birinchi
# 30
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s=0
# d=0
# while a>0:
#     a-=c
#     d+=1
# # print(a)
# while b>0:
#     b-=c
#     s+=1
# # print(b)
# print(d*s)
# 1
from random import randint
n=randint(10,15)
print("n=",n)
a=randint(-20,20)
print("1.",a)
min=a
max=a
for i in range(2,n+1):
    a=randint(-20,20)
    print(f"{i}.",a)
    if a<min:
        min=a
    if a>max:
        max=a
print("min=",min)
print("max=",max)
# 2
n=randint(10,15)
print("n=",n)
a=randint(-10,10)
b=randint(-10,10)
print("1.",a,b)
min=a*b
for i in range(2,n+1):
    a=randint(-20,20)
    b=randint(-20,20)
    print(f"{i}",a,b)

    if min>a*b:
        min=a*b
print("min=",min)
# 3
n=randint(10,15)
print("n=",n)
a=randint(5,15)
b=randint(5,15)
print("1.",a,b)
max=a+b
for i in range(2,n+1):
    a=randint(5,15)
    b=randint(5,15)
    print(f"{i}.",a,b)
    if max< a+b:
        max= a+b
print("max=",max)
# 4
n=randint(8,14)
print("n=",n)
a=randint(5,15)
print("1.",a)
min=a
index=1
for i in range(2,n+1):
    a=randint(5,15)
    print(f"{i}.",a)
    if min>a:
        min=a
        index=i
print("min=",min,"index=",index)
# 5
n=randint(10,15)
print("n=",n)
m=randint(-10,10)
v=randint(-10,10)
print("1.",m,v)
max=m/v
for i in range(2,n+1):
    m=randint(-10,10)
    v=randint(-10,10)
    print(f"{i}",m, v)
    if m/v>max:
        max=m/v
print("max=",max)
# 6
n=randint(10,15)
print("n=",n)
a=randint(-10,10)
min=a
max=a
index1=1
index2=1
for i in range(2,n+1):
    a=randint(-10,10)
    print(f"{i}.",a)
    if a>=max:
        max=a
        index1=i
    if a<min:
        min=a
        index2=i
print(f"max={max}, index={index1} ")
print(f"min={min}, index={index2}")

# 7
n=randint(8,14)
print("n=",n)
a=randint(5,15)
print("1.",a)
max=a
min=a
index1=1
index2=1
for i in range(2,n+1):
    a=randint(5,15)
    print(f"{i}.",a)
    if max<a:
        max=a
        index1=i
    if min>a:
        min=a
        index2=i
print("max=",max, "index=",index1)
print("min=",min, "index=",index2)
# 8
n=randint(10,15)
print("n=",n)
a=randint(-10,10)
print("1.",a)
min=a
index1=1
index2=2
for i in range(2,n+1):
    a=randint(-10,10)
    print(f"{i}.",a)
    if min>a:
        min=a
        index1=i
    if min>=a:
        min=a
        index2=i
print("min=",min)
print("index1=",index1)
print("index2=",index2)
# 9
n=randint(5,15)
print("n=",n)
a=randint(5,15)
print("1.",a)
max=a
index1=1
index2=1
for i in range(2,n+1):
    a=randint(5,15)
    print(f"{i}.",a)
    if a > max:
        max=a
        index1=i
    if a>=max:
        index2=i
print("max=",max,"index1=",index1,"index2=",index2)
# 10
n=randint(10,15)
print("n=",n)
a=randint(-10,10)
print("1.",a)
max=a
min=a
index1=1
index2=1
for i in range(2,n+1):
    a=randint(-10,10)
    print(f"{i}.",a)
    if max<a:
        max=a
        index1=i
    if min>a:
        min=a
        index2=i
if index1>index2:
    print(max,min)
else:
    print(min,max)
# 11
n=randint(5,15)
print("n=",n )
a=randint(5,15)
print("1.",a)
max=a
min=a
index1=1
index2=1
for i in range(2,n+1):
    a=randint(5,15)
    print(f"{i}.",a)
    if a>max:
        max=a
        index1=i
    if a<min:
        min=a
        index2=i
if index1>index2:
    print(max,min)
else:
    print(min,max)
# 12
n=randint(10,15)
print("n=",n)
a=randint(-10,10)
print("1.",a)
min=a
for i in range(2,n+1):
    a=randint(-10,10)
    print(f"{i}.",a)
    if min>a and a>0:
        min=a
    elif a<0:
        a=0
print(a)
print("musbat min=",min)
# 13
n=randint(5,15)
print("n=",n)
a=randint(5,15)
bool=True
max=0
for i in range(1,n+1):
    a=randint(5,15)
    print(f"{a}.",a)
    if a%2==1 and bool:
        max=a
        bool=False
    if a%2==1 and max<a:
        max=a

print(max)
# 14
n=randint(10,15)
print("n=",n)
b=int(input("b="))
a=randint(0,10)
print("1.",a)
min=a
index=1
for i in range(2,n+1):
    a=randint(0,10)
    print(f"{i}.",a)
    if a>min:
       if b>min:
          min=a
          index=i

print("min=",min)
print("index=",index)
# 15
n=randint(10,15)
print("n=",n)
b=int(input("b="))
c=int(input("c="))
a=randint(0,10)
print("1.",a)
max=a
index=1
for i in range(2,n+1):
    a=randint(0,10)
    print(f"{i}.",a)
    if b<a<c:
        if max<a:
            max=a
            index=i
print("max=",max)
# 16
n=randint(10,15)
print("n=",n)
a=randint(0,10)
print("1.",a)
min=a
count=1
for i in range(2,n+1):
    a=randint(1,10)
    print(f"{i}.",a)
    if min>a:
        min=a
        count=i
print(f"min={min}")
print(f"count={count-1}")
# 17
n=randint(10,15)
print("n=",n)
a=randint(1,10)
print("1.",a)
max=a
for i in range(2,n+1):
    a=randint(1,10)
    print(f"{i}.",a)
    if max<=a:
        max=a
print(f"max={max}")













