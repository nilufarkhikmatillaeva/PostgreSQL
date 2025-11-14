# # 29
# a=int(input("a="))
# b=int(input("b="))
# n=int(input("n="))
# l=abs(a-b)/n
# for i in range(n):
#     a+=l
#     print(a)
# # 30
# a=int(input("a="))
# b=int(input("b="))
# n=int(input("n="))
# l=abs(b-a)/n
# s=0
# import math
# for i in range(n+1):
#     x=a+i*l
#     F=1-math.sin(x)
#     print(x)
#     print(F)
# # 31
# n=int(input("n="))
# a0=2
# for i in range(n+1):
#     a1=2+1/a0
#     a0=a1
#     print(a1)
# # 32
# n=int(input("n="))
# a0=1
# for i in range(n+1):
#     a1=(a0+1)/i
#     a0=a1
#     print(a1)
# # 33
# f1=1
# f2=1
# n=int(input("n="))
# for i in range(n):
#     f3=f1+f2
#     f1=f2
#     f2=f3
#     print(f3)
# # 34
# a1=1
# a2=2
# n=int(input("n="))
# for i in range(n):
#     a3=(a1+2*a2)/3
#     a1=a2
#     a2=a3
#     print(a3)
# # 35
# a1=1
# a2=2
# a3=3
# n=int(input("n="))
# for i in range(n):
#     a4=a3+a2-2*a1
#     a1=a2
#     a2=a3
#     a3=a4
#     print(a4)
# # 36
# n=int(input("n="))
# k=int(input("k="))
# s=0
# s1=1
# for i in range(1,n+1):
#     s+=i**k
#     print(s)
# # 37
# n=int(input("n="))
# s=0
# s1=1
# for i in range(1,n+1):
#     s+=i**i
# print(s)
# # 38
# n=int(input("n="))
# S = 0
# for i in range(1, n + 1):
#     S += i ** (n - i + 1)
#
# print(f"Yig'indi = {S}")
# 39
a=int(input("a="))
b=int(input("b="))
s=0
for i in range(a,b+1):
    s+=i
    for j in range(s):
        print(j,end=" ")
    print()

