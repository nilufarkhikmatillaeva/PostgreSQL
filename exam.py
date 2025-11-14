# 1
a=int(input("a="))
b=int(input("b="))
s=(a*b)**(1/2)
print("o'rta geometrigi=",s)
# 2
x1=int(input("x1="))
x2=int(input("x2="))
y1=int(input("y1="))
y2=int(input("y2="))
l=((x2-x1)**2+(y2-y1)**2)**(1/2)
print("l=",l)
# 3
a=int(input("a="))
x1=a%10
x2=a//10%10
x3=a//100%10
s=x1+x2+x3
print("raqamlar yig'indisi=",s)
# 4
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a>0 and b<0 and c<0 or a<0 and b>0 and c<0 or a<0 and b<0 and c>0
print(s)
# 5
x1=int(input("x1="))
y1=int(input("y1="))
if x1>0 and y1>0:
    print("nuqta 1-chorakda")
elif x1<0 and y1>0:
    print("nuqta 2-chorakda")
elif x1<0 and y1<0:
    print("nuqta 3-chorakda")
else:
    print("nuqta 4-chorakda")
# 6
k=int(input("k="))
s=0
for i in range(2,11,2):
    s=k*(1+i/10)
    print((1+i/10)," kg konfet narxi=",s)
# 7
n=int(input("n="))
s=0
count=0
while n>0:
    k=n%10
    s+=k
    count+=1
    n=n//10
print("raqamlar yig'indisi",s)
print("raqamlar soni",count)
