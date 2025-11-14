# 1
a=8
if a>0:
    print(a+1)
else:
    print(a)
# 2
a=-9
if a>0:
    a+=1
print(a-2)
# 3
a=int(input("a="))
if a>0:
    a+=1
elif a<0:
    a-=2
else:
    a=10
print(a)
# 4
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
x=0
if a>0:
    x+=1
if b>0:
    x+=1
if c>0:
    x+=1
print(x)
# 5
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
musbat=0
manfiy=0
if a>0:
    musbat += 1
elif a<0:
    manfiy += 1
if b>0:
    musbat += 1
elif b<0:
    manfiy += 1
if c>0:
    musbat+= 1
elif c<0:
    manfiy +=1
print("Musbat sonlar soni:",musbat,"Manfiy sonlar soni:",manfiy)
# 6
a=int(input("a="))
b=int(input("b="))
katta_son=0
if a>b:
    katta_son = a
else:
    katta_son = b
print(katta_son)

# 7
a=int(input("a="))
b=int(input("b="))
if a<b:
    print("birinchi son:",a)
else:
    print("ikkinchi son:",b)
# 8
a=int(input("a="))
b=int(input("b="))
if a>b:
    print("birinchi son:",b,"ikkinchi son:",a)
else:
    print("birinchi son:",a,"ikkinchi son:",b)

# 9
a=int(input("a="))
b=int(input("b="))
if b<a:
    a,b=b,a
else:
    a,b=a,b
print("a=",a,"b=",b)

# 10
a=int(input("a="))
b=int(input("b="))
if a != b:
    yigindi=a+b
    a=yigindi
    b=yigindi
else:
    a=0
    b=0
print(a,b)
# 11
a=int(input("a="))
b=int(input("b="))
if a != b:
    if a>b:
     kattasi=a
     a=kattasi
     b=kattasi
    else:
      kattasi = b
      a=kattasi
      b=kattasi
else:
    a=0
    b=0
print("a=",a,"b=",b)
# 12
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a>c and b>c:
    kichik=c
elif a>b and c>b:
    kichik=b
elif c>a and b>a:
    kichik=a
print("kichik son=",kichik)
# 13
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a > b > c or c > b > a:
    ortasi=b
elif b>a>c or c>a>b:
    ortasi=a
elif a>c>b or b>c>a:
    ortasi=c
print(ortasi)
# 14
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
max=max(a,b,c)
min=min(a,b,c)
print("max=",max)
print("min=",min)
# 15
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
ab=a+b
ac=a+c
bc=b+c
if ab>bc and ab>ac:
    print(a,b)
elif ac>bc and ac>ab:
    print(a,c)
elif bc>ab and bc>ab:
    print(b,c)
# 17
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a>b>c or a<b<c:
    a *=2
    b *=2
    c *=2
else:
    a = -a
    b = -b
    c = -c
print("a =",a)
print("b =",b)
print("c =",c)
# 19
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))
if a==b and b==c:
    print("4-raqam")
elif a==b and b==d:
    print("3-raqam")
elif a==c and c==d:
    print("2-raqam")
elif b==c and c==d:
    print("1-raqam")
# 21
x=int(input("x="))
y=int(input("y="))
if x==0 and y==0:
    print(0)
elif x!=0 and y==0:
    print(1)
elif x==0 and y!=0:
    print(2)
elif x!=0 and y!=0:
    print(3)

x=int(input("x="))
y=int(input("y="))


from math import *
x=(int)(input("x="))
if x>0:
    print(2*sin(x))
elif x<=0:
    print(x-6)
# 28
x=int(input("x="))
if x%4==0:
    if x%400==0:
        print("366")
    elif x%100==0:
        print("365")
    else:
        print("366")
else:
    print("366")
















