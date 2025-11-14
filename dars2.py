# 1-m
a=int(input("a="))
s=a>0
print(s)
# 2-m
a=int(input("a="))
s=a%2==1
print(s)
# 3-m
a=int(input("a="))
s=a%2==0
print(s)
# 4-m
a=int(input("a="))
b=int(input("b="))
s=a>2 and b<=3
print(s)
# 5-m
a=int(input("a= "))
b=int(input("b="))
s=a>=0 and b<-2
print(s)
# 6-m
a=int(input("a= "))
b=int(input("b="))
c=int(input("c="))
s=a<=b<=c
print(s)
# 7-m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a<b<c or c<b<a
print(s)
# 8-m
a=int(input("a="))
b=int(input("b="))
s=a%2==1 and b%2==1
print(s)
# 9-m
a=int(input("a="))
b=int(input("b="))
s=a%2==1 or b%2==1
print(s)
# 10-m
a=int(input("a="))
b=int(input("b="))
s=a%2==1 and b%2==0 or a%2==0 and b%2==1
print(s)
a=int(input("a="))
b=int(input("b="))
s=a%2 != b%2
print(s)
# 11-m
a=int(input("a="))
b=int(input("b="))
s=a%2==1 and b%2==1 or a%2==0 and b%2==0
d=a%2 == b%2
print(d)
# 12-m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a>0 and b>0 and c>0
print(s)
# 13-m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a>0 and b<0 and c<0 or a<0 and b>0 and c<0 or a<0 and b<0 and c>0
print(s)
# 14-m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a>0 and b>0 and c<0 or a>0 and b<0 and c>0 or a<0 and b>0 and c>0
print(s)
# 15-m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s= a > 0 > c and b > 0 or a < 0 < b and c > 0 or a > 0 > b and c > 0
print(s)
# 16
a=int(input("a="))
s=a%2==0 and 9<a<100
print(s)
# 17
a=int(input("a="))
s=a%2==1 and 99<a<1000
print(s)
# 18
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a==b or a==c or b==c
print(s)
# 19
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a==-c or a==-b or b==-c
print(s)
# 20
a=int(input("a="))
x1=a%10
x2=a//10%10
x3=a//100%10
s=x1 != x2 and x2 != x3 and x1 != x3
print(s)
# 21-m
a=int(input("a="))
x1=a%10
x2=a//10%10
x3=a//100%10
s=x3==x2-1 and x2==x1-1
print(s)
# 22-m
a=int(input("a="))
x1=a%10
x2=a//10%10
x3=a//100%10
s=x3==x2-1 and x2==x1-1 or x3==x2+1 and x2==x1+1
print(s)
# 23-m
a=int(input("a="))
x1=a%10
x2=a//10%10
x3=a//100%10
s=x1==x3
print(s)
# 24-m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=b**2-4*a*c>=0
print(d)
# 25-m
x=int(input("x="))
y=int(input("y="))
s= x < 0 < y
print(s)
# 26-m
x=int(input("x="))
y=int(input("y="))
s=x > 0 > y
print(s)
# 27-m
x=int(input("x="))
y=int(input("y="))
s=x<0<y or x<0 and y<0
print(s)
# 28-m
x=int(input("x="))
y=int(input("y="))
s=x>0 and y>0 or x<0 and y<0
print(s)
# 29-m
x=int(input("x="))
y=int(input("y="))
x1=int(input("x1="))
x2=int(input("x2="))
y1=int(input("y1="))
y2=int(input("y2="))
s=x1<=x<=x2 and y1<=y<=y2
print(s)
# 30-m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a==b==c
print(s)
# 31-m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a=b and c<a+b or a==c and b<a+c or b==c and a<b+c
print(s)
# 32-m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a**2+b**2==c**2
print(s)
# 33-m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=a+b>c and a+c>b and b+c>a
print(s)