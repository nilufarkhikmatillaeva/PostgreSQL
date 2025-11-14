# for i in range (4):
#     print("salom") salom sozini 4 marta yozib beradi
# for i in range (2,7):
#     print(i) 2 va 6 orasidagi sonlarni yozib beradi
# for i in range (10,50,6):
#     print(i) 10 va 50 orasidagi sonlarni 6 qoshib yozib chiqadi. Mn 16,22,28...

# for i in range (10,50):
#     if i%3==0:
#         print(i)
# for i in range (200,150,-1): - bolsa kamayib boradi
#     if i%5==0 and i%2==0:
#         print(i)
# s=0 qiymat qoshlishi un
# for i in range (20,50):
#     if i%6==0:
#         s+=i*i ga oshib boradi
#         print(i)
# print(s)
# for i in range (20,50):
#  break- toxtatadi
# continue
# pass
# 1
# k=int(input("k="))
# n=int(input("n="))
# for i in range(n):
#     print(k)
# # 2
# a=int(input("a="))
# b=int(input("b="))
# s = 0
# for i in range(a,b+1):
#     print(i)
#     s+=1
# print(s)
# # 3
# a=int(input("a="))
# b=int(input("b="))
# s = 0
# for i in range(a-1,b,-1):
#     s+=1
#     print(i)
# print(s)
# # 4
# n=int(input("n="))
# for i in range(1,11):
#     print(n*i)
# # 5
# n=(int(input("n=")))
# for i in range(1,10):
#     print((i/10)*n)
# # 6
# k=int(input("k="))
# for i in range(12,21,2):
#      print(i/10*k)
# # 7
# a=int(input("a="))
# b=int(input("b="))
# s=0
# for i in range(a,b+1 ):
#     s+=i
# print(s)
# # 8
# a=int(input("a="))
# b=int(input("b="))
# s=1
# for i in range(a,b+1):
#     s*=i
# print(s)
# # 9
# a=int(input("a= ") )
# b=int(input("b="))
# s=0
# for i in range(a,b+1):
#     print(i)
#     s+=i*i
# print(s)
# # 10
# n=int(input("n="))
# s = 0
# for i in range(1,n+1):
#     s+=1/i
#     print(i)
# print(s)
# # 11
# n=int(input("n="))
# s=0
# for i in range(n,2*n+1):
#     s+= i**2
# print(s)
# # 12
# n=int(input("n="))
# s=1
# for i in range(1,n+1):
#     print(i)
#     s*=1+i/10
# print(s)
# # 13
# n=int(input("n="))
# s=0
# for i in range(1,n+1):
#     s+=(-1)**(i+1)*(1+i/10)
# print(s)
# 14
# n=int(input("n="))
# s=0
# for i in range(1,2*n,2):
#     s+=i
#     print(s)
# 15
a=int(input("a="))
n=int(input("n="))
s=0
for i in range(1,n+1):
    s=a**i
    print("a^",i,"=",s)
# 16
a=int(input("a="))
n=int(input("n="))
s=0
for i in range(1,n+1):
    s=a**i
    print("a^",i,"=",s)
# 17
a=int(input("a="))
n=int(input("n="))
s=0
yigindi=0
for i in range(1,n+1):
    s=a**i
    yigindi+=s
    print("a^",i,"=",s)
print("yigindi",yigindi)
# 18
a=int(input("a="))
n=int(input("n="))
s=0
yigindi=0
for i in range(1,n+1):
    s=a**i
    yigindi+=(-1)**(i+1)*s
    print(s)
print("yigindi",1-yigindi)
