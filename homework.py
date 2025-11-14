# 1-20
# 2-23 integer
# 3-15 boolean
# 4-28 if
# 5-31 for
# 6-15 while
# 7-10 min,max
# 20
# x1=int(input("x1="))
# x2=int(input("x2="))
# y1=int(input("y1="))
# y2=int(input("y2="))
# l=((x2-x1)**2 + (y2-y1)**2)**0.5
# print(l)
# # 23
# n=int(input("n="))
# s=n//3600
# min=(n%3600)//60
# print(s)
# print(min)
# # 15
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s=a>0 and b>0 and c<0 or a>0 and b<0 and c>0 or a<0 and b>0 and c>0
# print(s)
# # 28
# y=int(input("y="))
# if y%400==0 or y%4==0 and y%100!=0:
#     print(366)
# else:
#     print(365)
# # 28
# if y%4==0:
#     if y%400==0:
#         print(366)
#     elif y%100==0:
#         print(365)
#     else:
#         print(366)
# else: print(365)
#
# # 31
# k=int(input("k="))
# a0=2
# for i in range(1,k+1):
#     a1=2+1/a0
#     a0=a1
#     print(f"{i}.",a1)
# # 15
# s=int(input("s="))
# p=int(input("p="))
# k=0
# begin=s
# while 2*begin>s:
#     s+=s*p/100
#     k+=1
# print(k)
# print(s)
# # 10
# from random import randint
# n=randint(10,15)
# print("n=",n)
# a=randint(-10,10)
# print("1.",a)
# max=a
# min=a
# index1=1
# index2=1
# for i in range(2,n+1):
#     a=randint(-10,10)
#     print(f"{i}.",a)
#     if a<=min:
#         min=a
#         index1=i
#     if a>=max:
#         max=a
#         index2=i
# if index1<index2:
#     print("min",min,"max",max)
# else:
#     print("max",max,"min",min)


# 19
x1=int(input("x1="))
x2=int(input("x2="))
y1=int(input("y1="))
y2=int(input("y2="))
a=abs(x1-x2)
b=abs(y1-y2)
P=2*(a+b)
S=a*b
print("Perimrtr=",P)
print("Yuza=",S)
# 20
x1=int(input("x1="))
x2=int(input("x2="))
y1=int(input("y1="))
y2=int(input("y2="))
l=((x2-x1)**2+(y2-y1)**2)**0.5
print(l)
# 15
a=int(input("a="))
x1=a%10
x2=a//10%10
x3=a//100%10
b=x2*100+x3*10+x1
print(b)
# 22
n=int(input("n="))
h=n//3600
min=(n%3600)//60
s=n%60
print("Minut=",min)
print("Sekund=",s)
# 13
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a>0 or b>0 or c>0
print(s)
# 20
a=int(input("a="))
x1=a%10
x2=a//10%10
x3=a//100%10
s= x1 != x2 and x2 != x3 and x1 != x3
print(s)
# 29
a=int(input("a="))
if a>0 and a%2==1:
    print("a musbat toq son")
elif a<0 and a%2==0:
    print("a manfiy juft son")
elif a==0:
    print("a nolga teng")
# 30
a=int(input("a="))
if a%2==0:
    if 10<=a<100:
        print("a 2 xonali juft son")
    elif 100<=a<1000:
        print("a 3 xonali juft son")
if a%2==1:
    if 10<=a<100:
      print("a 2 xonali toq son")
    elif 100<=a<1000:
      print("a 3 xonali toq son")
# 13
n=int(input("n="))
s=0
for i in range(1,n+1):
    s+=(-1)**(i+1)*(1+i/10)
print(s)
# 35
n=int(input("n="))
a1=1
a2=2
a3=3
for i in range(n):
    a4=a3+a2-2*a1
    a1=a2
    a2=a3
    a3=a4
    print(a4,end=" ")
    print()
# 12
n=int(input("n="))
s=0
k=0
while s<=n:
    k+=1
    s+=k
print(s)
print(k-1)
# 14
n=int(input("n="))
s=0
k=0
while s<=n:
    k+=1
    s+=1/k
print(s)
print(k-1)


