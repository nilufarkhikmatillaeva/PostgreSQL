
from random import randint
# print("Array51")
# a=[12,32,13,14,15,21,7,9,11,5]
# b=["x","y","z","w","a","b","c"]
# a,b=b,a
# print("a=",a)
# print("b=",b)
# print("Array52")
# a=[2,5,12,1,20,3,6,22]
# b=[]
# for i in range(len(a)):
#     b.append(a[i])
#     if a[i]<5:
#         b[i]=2*a[i]
#     else:
#         b[i]=a[i]/2
# print(b)
# print("Array53")
# a=[12,32,13,14,15,21,7,9,11,5]
# b=[2,5,12,1,20,3,6,22,28,15,9]
# c=[]
# c.append(max(a))
# c.append(max(b))
# print("c=",c)
# print("Array54")
# a=[12,34,23,4,13,7,15,22,18,11]
# b=[]
# for i in range(len(a)):
#     if a[i]%2==0:
#         b.append(a[i])
# print("b=",b)
# print(len(b))
# print("Array55")
# a=[12,34,23,4,13,7,15,22,18,11]
# b=[]
# for i in range(len(a)):
#     if i%2==1:
#         b.append(a[i])
# print("b=",b)
# print(len(b))
# print("Array56")
# a=[3,12,4,7,11,8,6,9,10,5,14]
# b=[]
# for i in range(0,len(a),3):
#     b.append(a[i])
# print("b massiv=",b)
# print("elementlar soni",len(b))
# print("Array57")
# a=[12,34,23,4,13,7,15,22,18,11]
# b=[]
# for i in range(0,len(a),2):
#     b.append(a[i])
# for j in range(1,len(a),2):
#     b.append(a[j])
# print("b=",b)
# print(len(b))
# print("Array58")
# a=[12,34,23,4,13,7,15,22,18,11]
# b=[]
# sum=0
# for i in range(len(a)):
#     sum+=a[i]
#     b.append(sum)
# print("b=",b)
#
# print("Array59")
# a=[3,12,4,7,11,8,6,9,10,5,14]
# b=[]
# sum=0
# for i in range(len(a)):
#     sum+=a[i]
#     b.append(sum/(i+1))
# print("b massiv=",b)
# print("Array60")
# a=[12,34,23,4,13,7,15,22,18,11]
# b=[]
# sum=0
# for i in range(1,len(a)):
#     sum+=a[len(a)-i]
#     b.append(sum)
# print("b=",b)
# print("Array61")
# a=[12,34,23,4,13,7,15,22,18,11]
# b=[]
# sum=0
# for i in range(len(a)):
#     sum+=a[i]
#     b.append(sum/(i+1))
# print("b=",b)
# print("Array62")
# a=[12,34,-23,4,-13,7,-15,22,-18,11]
# b=[]
# c=[]
# for i in range(len(a)):
#     if a[i]>0:
#         b.append(a[i])
#
# print("b=",b)
# print(len(b))
# for i in range(len(a)):
#     if a[i]<0:
#         c.append(a[i])
# print("c=",c)
# print(len(c))
# print("Array63")
# a=[10,12,14,16,18]
# b=[11,13,15,17,19]
# c=[]
# for i in range(len(a)):
#     c.append(a[i])
# for i in range(len(b)):
#     c.append(b[i])
# c.sort()
# print("c=",c)
# print("Array64")
# a=[10,13,16,19,22]
# b=[11,14,17,20,23]
# c=[12,15,18,21,24]
# d=[]
# for i in range(len(a)):
#     d.append(a[i])
# for i in range(len(b)):
#     d.append(b[i])
# for i in range(len(c)):
#     d.append(c[i])
# d.sort()
# print("d=",d)
# print("Array65")
# a=[12,34,23,4,13,7,15,22,18,11]
# k=int(input("k="))
# for i in range(len(a)):
#     a[i]+=k
# print("a=",a)
#
#
# print("Array66")
# a=[10,3,2,4,7,11,8,6,9,10,5,14]
# x=0
# for i in range(len(a)):
#     if a[i]%2==0:
#         x=a[i]
#         break
# for j in range(len(a)):
#     if a[j]%2==0:
#         a[j]+=x
# print("a massiv=",a)
# print("Array67")
# a=[10,3,2,4,7,11,8,6,9,10,5,14]
# x=0
# for i in range(len(a)):
#     if a[i]%2==1:
#         x=a[i]
#         break
# for j in range(len(a)):
#     if a[j]%2==1:
#         a[j]+=x
# print("a massiv=",a)
# print("Array68")
# a = [10,3,2,4,7,11,8,6,9,10,5,14]
#
# max_index = 0
# min_index = 0
#
# for i in range(1, len(a)):
#     if a[i] > a[max_index]:
#         max_index = i
#     elif a[i] < a[min_index]:
#         min_index = i
# a[max_index], a[min_index] = a[min_index], a[max_index]
#
# print("a =", a)
# print("Array69")
# a=[10,3,2,4,7,11,8,6,9,10,5,14]
# for i in range(0,len(a),2):
#     a[i],a[i+1] = a[i+1],a[i]
# print("a =", a)
# print("Array70")
# a=[10,5,12,4,8,13,7,9,11,2]
# for i in range(len(a)//2):
#      if len(a)%2==0:
#          a[i],a[len(a)//2+i]=a[len(a)//2],a[i]
#          pass
# else:
#         a[i], a[len(a) // 2 + i] = a[len(a) // 2 + i], a[i]
# print(a)
# print("Array71")
# a = [10, 5, 12, 4, 8, 13, 7, 9, 11, 2]
#
# for i in range(len(a)//2):
#     a[i], a[len(a)-1-i] = a[len(a)-1-i], a[i]
#
# print("a =", a)
# print("Array74")
# a=[10,5,12,4,8,13,7,9,11,2]
# max_index = a.index(max(a))
# min_index = a.index(min(a))
#
# for i in range(0,len(a)):
#     if max_index < i < min_index or min_index<i<max_index:
#         a[i]=0
# print("a =", a)
# print("Array75")
# a=[10,5,12,4,8,13,7,9,11,2]
# max_index = a.index(max(a))
# min_index = a.index(min(a))
# for i in range(0,len(a)):
#     if min_index > max_index:
#         min_index, max_index = max_index, min_index
# while min_index < max_index:
#     a[min_index], a[max_index] = a[max_index], a[min_index]
#     min_index += 1
#     max_index -= 1
# print("a =", a)
# print("Array76")
# a=[10,5,12,4,8,13,7,9,11,2]
# for i in range(1,len(a)-1):
#     if a[i]>a[i-1] and a[i]>a[i+1]:
#         a[i]=0
# print("a =", a)
#
# print("Array77")
# a=[10,5,12,4,19,13,7,22,11,2]
# b=[10]
# for i in range(1,len(a)-1):
#     if a[i-1]>a[i] and a[i]<a[i+1]:
#         b.append(a[i]**2)
#     else:
#         b.append(a[i])
# b.append(a[-1])
# print(b)
# print("Array78")
# a=[10,5,12,4,19,13,7,22,11,2]
# sum=0
# b=[]
# for i in range(len(a)-1):
#     sum=a[i]+a[i+1]
#     b.append(sum/2)
# print("b =", b)
# print("Array79")
# a=[10,5,12,4,19,13,7,22,11,2]
# for i in range(len(a)-1):
#     a[i],a[i+1] = a[i+1],a[i]
#     a[0]=0
# a.remove(a[-1])
# print("a =", a)
# print("Array80")
# a=[10,5,12,4,19,13,7,22,11,2]
# a.remove(a[0])
# a.append(0)
# print(a)
# print("Array81")
a=[10,5,12,4,19,13,7,22,11,2]
k=randint(1,len(a))
print("k=",k)
for i in range(len(a)-1,k-1,-1):
    a[i]=a[i-k]
for i in range(k):
    a[i]=0
print("a=",a)
# 84
a=[10,5,12,4,19,13,7,22,11,2]
for i in range(1,len(a)):
    a[i],a[i-1]=a[i-1],a[i]
print("a=",a)
print(85)
a=[10,5,12,4,19,13,7,22,11,2]
for j in range(5):
    for i in range(1,len(a)):
        a[i],a[i-1]=a[i-1],a[i]
print("a=",a)
