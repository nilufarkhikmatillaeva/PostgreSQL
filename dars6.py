# a=50
# b=10
# while a>b:
#     a-=1
#     if a%3==0:
#      print(a)
# 1
a=int(input("a="))
b=int(input("b="))
while a>=b:
    a-=b
print(a)
# 2
a=int(input("a="))
b=int(input("b="))
s=0
while a>=b:
    a-=b
    s+=1
print(s)
# 3
n=int(input("n="))
k=int(input("k="))
s=0
while n>k:
    n-=k
    s+=1
print(f"qoldiq- {n}, butun qismi-{s}")
# 4
n=int(input("n="))
i=0
while n>3**i:
    i+=1
print(i)
if n==3**i:
    print(f"ha {i}")
else: print("yo'q")
# 5
n=int(input("n="))
k=0
while n>=2**k:
    k+=1
print(k-1)
# 6
n=int(input("n="))
s=1
k=n
while k>1:
    s*=k
    k-=2

print(s)
# 7
n=int(input("n="))
k=1
while n>=k**2:
    k+=1
print(k)
# 8
n=int(input("n="))
k=1
while k**2<=n:
    k+=1
print(k-1)
# 9
n=int(input("n="))
k=1
while k**3<n:
    k+=1
print(k)
# 10
n=int(input("n="))
k=1
while k**3<n:
    k+=1
print(k)
# 11
n=int(input("n="))
k=0
s=0
while n>=s:
    k+=1
    s+=k
print(k-1)
# 12
n=int(input("n="))
s=0
k=0
while s<=n:
    k+=1
    s+=k
print(k-1)
# 13
a=int(input("a="))
k=1
s=0
while s<=a:
    k+=1
    s+=1/k
    print(s)
print(k-1)
# 14
a=int(input("a="))
s=0
k=0
while s<=a:
    k+=1
    s+=1/k
    print(k)
# 15
s=float(input("s="))
p=float(input("p="))
k=0
start=s
while s<=2*start:
    k+=1
    s=s+s*p/100
print("Oylar soni",k)
print("Summa",s)

# 16
p=int(input("p="))
a1=10
s=0
while s<200:
    a1+=(a1*p)/100
    s+=a1
    print(f"umumiy masofa {s}")
    print(a1)
# 17
n=int(input("n="))
m=int(input("m="))
while n>m:
    n-=m
print(n)
# 18
n=int(input("n="))
while n>0:
    k=n%10
    n=n//10
    print(k, end="")
# 19
n=int(input("n="))
summa=0
count=0
while n>0:
    k=n%10
    summa+=k
    count+=1
    n=n//10
print("Summa",summa)
print("count",count)
# 20
n=int(input("n="))
bor=False
while n>0:
    k=n%10
    if k==2:
        bor = True
    n=n//10
if bor:
    print("bor")
else:
    print("yo'q")
# 21
n=int(input("n="))
bor=False
while n>0:
    k=n%10
    if k%2==1:
        bor=True
    n=n//10
if bor:
    print("bor")
else:
    print("yo'q")
# 22
n=int(input("n="))

# 23
a=int(input("a="))
b=int(input("b="))
# 30
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=0
d=0
while a>0:
    a-=c
    d+=1
print(a)
while b>0:
    b-=c
    s+=1
print(b)
print(d,s)