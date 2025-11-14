from random import randint
# a[start:end:step]



a= {12, 5, 24, 8, 11, 7, 24}
b= {12, 5, 11, 8, 15, 7, 24}
a.intersection_update(b)
print("a=",a)
# 90
a=[12, 5, 24, 8, 11, 7, 24]
k=3
# a.pop(k)
# print(a)
b=[]
for i in range(len(a)):
    if i != k:
        b.append(a[i])
print("b=",b)
# 91
a=[12, 5, 24, 8, 11, 7, 24, 13, 16, 20]
s=a[1::2]
print("s=",s)
for i in range(1,len(a),2):
    b.append(a[i])
print("b=",b)
# 92
a=[12, 5, 24, 8, 11, 5, 24, 13, 11, 20]
b=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        b.append(a[i])
print("b=",b)
print("Array93")
a=[12, 5, 24, 8, 18, 5, 23, 13, 11, 20]
b=[]
for i in range(0,len(a),2):
    b.append(a[i])
print("b=",b)
print("Array94")
a=[12, 5, 24, 8, 11, 22, 24, 13, 11, 20]
b=[]
for i in range(1,len(a),2):
    b.append(a[i])
print("b=",b)
# 2nd way
b=a[1::2]
print("b=",b)
print("Array95")
a = [12, 12, 5, 5, 5, 24, 24, 13, 11, 11,11,11]
b=[a[0]]
for i in range(1,len(a)):
    if a[i] != a[i-1]:
        b.append(a[i])
print("b=",b)
print(len(b))
print("Array96")
a=[12, 5, 24, 8, 11, 22, 24, 13, 11, 20]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print("b=",b)
print("Array97")
a=[12, 5, 24, 13, 11, 8, 22,22, 24, 13, 11, 20]
for i in reversed(a):
    if i not in b:
        b.append(i)
print("b=",b)
print("Array98")
a=[12,13,12,12,12,5,5,6,13,6,6,9,9,10,9]
b=[]
for x in a:
    a.count(x)
    if a.count(x)>=3:
        b.append(x)
print("b=",b)
# 99
a=[7,12,13,12,5,20,5,6,17,13,6,6,10,9,8]
b=[]
for x in a:
    a.count(x)
    if a.count(x) < 2:
        b.append(x)
print("b=",b)
print(len(b))
# 100
a=[7,12,13,12,5,20,5,6,17,13,6,6,10,9,8]
b=[]
for x in a:
    a.count(x)
    if a.count(x) != 2:
        b.append(x)
print("b=",b)
print(len(b))
# 101
a=[7,12,13,12,5,20,5]
k=4
a.insert(k-1,0)
print("a=",a)
print(len(a))
# 102
a=[7,12,13,12,5,20,5]
k=4
a.insert(k+1,0)
print("a=",a)
print(len(a))
# 103
a=[7,12,8,16,1,9,13,12,5,20,5]
max_index=a.index(max(a))
min_index=a.index(min(a))
a.insert(max_index+1,0)
a.insert(min_index,0)
print("a=",a)
print(len(a))
print("Array104")
a=[7,12,8,16,1,9,13,12,5,20,5]
k=3
m=2
for _ in range(m):
    a.insert(k,0)
print("a=",a)
# 105

