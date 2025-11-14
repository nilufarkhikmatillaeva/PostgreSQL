from random import randint
# # 25
# a=[1,2,4,8,16,32,64,128]
# n=randint(8,12)
# q=abs(a[1]/a[0])
# for i in range(1,len(a)):
#     if q!=abs(a[i]/a[i-1]):
#         print("yo'q")
#         break
#     else:
#         if i ==len(a)-1:
#             print(q)
# # 26
# a=[12,23,36,45,37,23,42,35,64,13,19]
# for i in range(1,len(a)):
#     if int(a[i]%2==0) == int(a[i-1]%2 == 0):
#         print(i)
#         break
# else:
#         print(0)
#
#
# # 27
# a=[3,-8,25,-6,12,-18,7,32,17,-23]
# for i in range(1,len(a)):
#   if (a[i] > 0 and a[i-1] > 0) or (a[i] < 0 and a[i-1] < 0):
#        print(i)
#        break
#   else:
#        print(0)
# # 28
# a=[12,34,23,56,223,2,7,32,54,19]
# min=a[0]
# for i in range(1,len(a)):
#    if i%2==0:
#        if a[i]<min:
#            min=a[i]
#            print(min)
#
# # 29
# a=[12,23,4,8,52,73,12,54,81,10]
# max=a[1]
# for i in range(1,len(a)):
#     if max<a[i] and i%2==1:
#         max=a[i]
# print(max)
#
# # 30
# a=[12,34,23,56,223,2,7,32,54,19,32,53,21,77,95]
# count=0
# b=[]
# for i in range(len(a)-1):
#     if a[i]<a[i+1]:
#         count+=1
#         b.append(i)
# print(count)
# print(b)
#
# # 31
# a=[12,23,43,25,64,63,25,38,42,51,59,43,75,82]
# count=0
# b=[]
# for i in range(1,len(a)):
#     if a[i]>a[i-1]:
#         count+=1
#         b.append(i)
# print(count)
# b.reverse()
# print(b)
#
# # 32
# a=[12,23,4,8,52,73,12,54,81,10]
# for i in range(1,len(a)-1):
#     if a[i-1]>a[i] and a[i]<a[i+1]:
#         print(i)
#
# # 33
# a=[12, 23, 4, 8, 52, 73, 12, 54, 81, 10]
# last_max_index = -1
#
# for i in range(1, len(a)-1):
#     if a[i] > a[i-1] and a[i] > a[i+1]:
#         last_max_index = i
# print(last_max_index)
# # 34
# a=[12, 3, 24, 8, 52, 73, 12, 54, 81, 10]
# max=a[1]
# for i in range(1,len(a)-1):
#     if a[i] < a[i-1] and a[i] < a[i+1]:
#         if a[i] > max:
#             max=a[i]
# print(max)
# # 35
# a=[12, 36, 24, 8, 52, 73, 12, 54, 81, 10]
# min=a[1]
# for i in range(1,len(a)-1):
#     if a[i]>a[i-1] and a[i]>a[i+1]:
#         if a[i] < min:
#             min=a[i]
# print(min)
#
#
# # 36
# a=[12,23,4,8,52,73,12,54,81,10]
# b=[]
# for i in range(1,len(a)-1):
#     if a[i-1]>a[i]  and a[i]<a[i+1] or a[i-1]<a[i]  and a[i]>a[i+1] :
#         pass
#     else:
#         b.append(a[i])
# print(b)
# # 37
# a=[12,23,41,84,52,35,21,12,24,54,81,10]
# count=0
# b = True
# for i in range(1,len(a)):
#     if a[i] > a[i-1]:
#         if b:
#             count += 1
#             b = False
#     else:
#         b = True
# print(count)
# # 38
# a=[12,23,41,84,52,35,21,12,24,54,81,10]
# count=0
# b=True
# for i in range(1,len(a)):
#     if a[i-1]>a[i]:
#         if b:
#             count+=1
#             b=False
#     else:
#         b=True
# print(count)
# # 39
# a =[12,23,41,84,52,35,21,12,24,54,81,10]
# count = 0
# i = 0
#
# while i < len(a) - 1:
#     if a[i] < a[i + 1]:
#         count += 1
#         while i < len(a) - 1 and a[i] < a[i + 1]:
#             i += 1  # Move to the end of this segment
#     elif a[i] > a[i + 1]:
#         # Decreasing segment
#         count += 1
#         while i < len(a) - 1 and a[i] > a[i + 1]:
#             i += 1  # Move to the end of this segment
#     else:
#         # Equal elements, skip
#         i += 1
#
# print(count)
# # 40
# a=[12,23,41,84,52,35,21,12,24,54,81,10]
# r=25
# closest=a[0]
# min_diff=abs(a[0]-r)
# for i in a:
#     diff=abs(i-r)
#     if diff < min_diff:
#         min_diff=diff
#         closest=i
# print(closest)
# # 41
# n = randint(8, 12)
# print("n =", n)
# a = [randint(1, 50) for _ in range(n)]
# print("a =", a)
# max_sum = a[0] + a[1]
# for i in range(1, n-1):
#     if a[i] + a[i + 1] > max_sum:
#         max_sum = a[i] + a[i + 1]
#         print(i, i + 1)
# print("max_sum =", max_sum)
# # 42
# a=[12,23,41,84,52,35,21,12,24,54,81,10]
# r=48
# closest=(a[0],a[1])
# min_diff=abs(a[0]+a[1]-r)
# for i in range(len(a)-1):
#     current_sum=a[i]+a[i+1]
#     diff=abs(current_sum-r)
#     if diff < min_diff:
#         min_diff=diff
#         closest=a[i],a[i+1]
# print(closest)
# # 43
# a = [1, 2, 2, 3, 4, 4, 4, 5]  # Example sorted array
# distinct_count = 1  # First element is always distinct
#
# for i in range(1, len(a)):
#     if a[i] != a[i - 1]:  # New distinct element
#         distinct_count += 1
#
# print(distinct_count)
# # 44
# a=[12, 36, 24, 8, 52, 73, 12, 54, 81, 10]

# # 45
# a = [12, 23, 41, 84, 52, 35, 21]  # Example
# min_diff = abs(a[1] - a[0])
# closest_pair = (0, 1)
#
# for i in range(len(a) - 1):
#     diff = abs(a[i+1] - a[i])
#     if diff < min_diff:
#         min_diff = diff
#         closest_pair = (i, i+1)
#
# print(closest_pair)
#
#
# # 47
# a=[12,24,18,36,27,12,44,35,48,14,29,24,15,53]
# b=[]
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)
# 49

# # 50
# a=[12,24,18,36,27,12,44,35,48,14,29,24,15,53]
# count=0
# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         count+=1
# print(count)













