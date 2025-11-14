 # len(a)-list ichidagi element sonini chiqazadi


from random import randint
# 1
# a=[]
# n=randint(8,10)
# while n>len(a):
#      k=randint(1,90)
#      if k%2==1:
#        a.append(k)
# print(a)
a=[]
n=randint(8,10)
print("n=",n)
for i in range(1,2*n,2):
    a.append(i)
print(a)

a=[]
n=randint(8,10)
print("n=",n)
for i in range(1,n+1):
    a.append(2**i)
print(a)
# 3
a=[]
n=randint(8,10)
print("n=",n)
a1=2
d=3
a.append(a1)
for i in range(n):
    a1+=d
    a.append(a1)
print(a)
# 4
a=[]
n=randint(8,10)
print("n=",n)
a1=1
d=3
a.append(a1)
for i in range(n):
    a2=a1*d
    a1=a2
    a.append(a1)
print(a)
 # 5
a=[]
n=randint(8,10)
print("n=",n)
f0=1
f1=1
for i in range(n):
    f2=f1+f0
    f0=f1
    f1=f2
    a.append(f2)
print(a)
# 6
n=randint(8,10)
print("n=",n)
A=randint(1,5)
B=randint(1,5)

a=[A,B]

for i in range(2,n+1):
    s=sum(a)
    a.append(s)
print(a)

# 7
n=randint(8,10)
print("n=",n)
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    print(i,end=" ")
# 8
a=[1,2,3,4,5,6,7,8,9]
n=randint(8,10)
print("n=",n)
for i in a:
    if i%2==1:
        print(i,end=" ")

for i in range(len(a)):
   print(a[len(a)-1-i])
# 9
a=[1,2,3,4,5,6,7,8,9]
for i in range(len(a)):
    if a[len(a)-1-i]%2==0:
        print(a[len(a)-1-i],end=" ")
# 10
a=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)):
    if a[len(a)-1-i]%2==0:
        print(a[len(a)-1-i],end=" ")
for i in range(len(a)):
    if a[i]%2==1:
        print(a[i],end=" ")
# 11
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
k=3
for i in range(0,len(a),k):
    print(a[i],end=" ")
# 12
n=randint(8,10)
print("n=",n)
a=[]
for i in range(1,n+1):
    a.append(i)
print(a)
print("a[0]=",a[0],"a[2]=",a[2],"a[4]=",a[4])
# 13
n=randint(8,10)
print("n=",n)
a = [i for i in range(1, n + 1)]
print("a=",a)
a.reverse()
print("a=",a)
# 14
n=randint(8,10)
print("n=",n)
a=[]
for i in range(n):
    k= randint(1,50)
    a.append(k)
print(a)
for i in range(0,n,2):
    print(a[i],end=" ")
for i in range(1,n,2):
    print(a[i],end=" ")

# 18
a=[18,23,34,4,5,6,7,8,9,10]
for i in a:
    if a[-1]>i:
        print(i)
        break
# 19
a=[102,135,64,38,92,124]
for i in range(1,len(a)):
    if a[-1]<i and a[0]>i:
        print(i)
        break
# 20
n = randint(8, 10)
print("n =", n)

a = []
for i in range(n):
    k = randint(1, 20)
    a.append(k)

print("a=", a)
K = int(input("K = "))
L = int(input("L = "))

s = 0
for i in range(K, L + 1):
    s+=a[i]
    print("K va L orasidagi elementlar yig'indisi =", s)
# 20 again

# 21
from random import randint

n = randint(8, 10)
print("n =", n)

a = []
for i in range(n):
    k = randint(1, 20)
    a.append(k)

print("a=", a)

K = int(input("K = "))
L = int(input("L = "))

s = 0
for i in range(K, L + 1):
    s = s + a[i]

count = L - K + 1
avg = s / count

print("K va L orasidagi elementlar o'rta arifmetigi =", avg)

# 24
