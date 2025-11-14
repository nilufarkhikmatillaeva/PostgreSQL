# # with as, list comprehension, map, zip, lambda, filter, reduce
# from files import count
#
# #
# # # 38
# # f=open("text.txt","r")
# # s=f.read().split()
# # a=list(map(int,s))
# # print(a)
# # f.close()
# # f=open("text.txt","w")
# # for i in range(len(a)):
# #     if i%2==1:
# #         a[i]=2*a[i]
# #         f.write(str(a[i])+' ')
# # f.close()
# # #
# # a=list(range(20))
# # print(a)
# # b=[i for i in a if i%5==0 and i%2==1]
# # print(b)
#
# # a=list(range(5))
# # b=[5*i for i in a]
# # print(b)
# #
# # a='''ajnja sj snknd nkzna nms xznxz dsd hjkkx sjsjds cnnnnxx hjsjkkS xbxz zxbz  xhjcj
# # ssssssmx sjnjs sss'''
# #
# # b=' '.join([i for i in a.split() if len(i)>4])
# # print(b)
#
#
# # n=lambda a,b,c,d:a+b+c+d
# # print(n(10,12,7,8))
# #
# # print((lambda a,b:a*b)(4,6))
# #
# # # a=list(range(10))
# # # s=list(map(lambda x:x*x,a))
# # # print(s)
# # # # toqlarini ikkilantirish
# # # a=list(range(10))
# # # print("")
# # # s=list(map(lambda x:x*2,list(filter(lambda x:x%2==1,a))))
# # # print(s)
#
#
# # Homework
# # 5
# s="Even small steps count when you’re walking toward something that matters."
# f=open("text.txt","a",encoding="utf-8")
# f.write("\n"+s)
# f.close()
# # 6
# f=open("text.txt","r")
# s=f.read()
# f1=open("copy.txt","r")
# s1=f1.read()
# f=open("text.txt","a")
# f.write("\n"+s1)
# f.close()
# f1.close()
# # 7
# t="Moments feel eternal"
# f=open("text.txt","r")
# s=f.read()
# with open("text.txt","w") as f1:
#     f1.write(t+"\n"+s)
# # 8
# with open("text.txt","r") as f:
#     s=f.read()
# with open("copy.txt","r") as f1:
#     s1=f1.read()
# with open("copy.txt","w") as f2:
#     f2.write(s+"\n"+s1)
# # 9
# k=int(input("k="))
#
# with open("text.txt","r") as f:
#     s=f.readlines()
# with open("copy.txt","w") as f1:
#     for i in range(len(s)):
#         if i==k-1:
#             f1.write("\n")
#         f1.write(s[i])
# # 10
# k=int(input("k="))
# with open("text.txt","r") as f:
#     s=f.readlines()
# with open("copy.txt","w") as f1:
#     for i in range(len(s)):
#         f1.write(s[i])
#         if i==k-1:
#             f1.write("\n")
# # 11
#
# with open("text.txt","r") as file:
#     s=file.readlines()
#
# with open("text.txt","w") as f:
#     for i in s:
#         if i.strip()=="":
#            f.write("\n\n")
#         else:
#             f.write(i)
#
# # 12
# S="Hello World"
# print(S)
# with open("text.txt","r") as file:
#     s=file.readlines()
# with open("text.txt","w") as f:
#     for i in s:
#         if i.strip()=="":
#             f.write(S+"\n")
#         else:
#             f.write(i)
# # 13
# with open("text.txt","r") as file:
#     s=file.readlines()
# with open("text.txt","w") as f:
#     for i in s[1:]:
#         f.write(i)
# # 14
# with open("text.txt","r") as file:
#     s=file.readlines()
# with open("text.txt","w") as f:
#     for i in s[:-1]:
#         f.write(i)
#
# # 15
# k=5
#
# with open("text.txt","r") as file:
#     s=file.readlines()
# if 0<=k<len(s):
#     s.pop(k)
#     with open("text.txt","w") as f:
#         f.writelines(s)
#
# # 16
# with open("text.txt","r") as file:
#     s=file.readlines()
# b=[line for line in s if line.strip()!=""]
# with open("text.txt","w") as f:
#     f.writelines(b)
#
# # 17
# with open("text.txt","r") as file1:
#     line1=file1.readlines()
# with open("copy.txt","r") as file2:
#     line2=file2.readlines()
# b=[]
# for i in range(len(line1)):
#    b.append(line1[i])
#    if i<len(line2):
#        b.append(line2[i])
# with open("text.txt","w") as f:
#     f.writelines(b)
#
# # 18
# k=int(input("k="))
#
# with open("text.txt","r") as f:
#     s=f.readlines()
# new_s=[]
# for line in s:
#     new_s.append(line[k:])
# with open("text.txt","w") as f1:
#     f1.writelines(new_s)
#
# # 19
# with open("text.txt","r") as f:
#     text=f.read()
# text=text.swapcase()
# with open("text.txt","w") as f1:
#     f1.write(text)
#
# # 20
# with open("text.txt","r") as f:
#     text=f.readlines()
# b=[]
# for i in s:
#     if i.strip != "  ":
#         b.append(i)
#
# # 21
# with open("text.txt","r") as f:
#     text=f.readlines()
# if len(text)>3:
#     text=text[:-3]
# with open("text.txt","w") as f1:
#     f1.writelines(text)
#
# # 22
# k=int(input("k="))
#
# with open("text.txt","r") as f:
#     text=f.readlines()
# if len(text)>k:
#     text=text[:k]
# with open("text.txt","w") as f1:
#     f1.writelines(text)
#
# # 23
# with open("text.txt","r") as f:
#     text=f.readlines()
# with open("copy.txt","w") as f1:
#     if len(text)>k:
#         f1.writelines(text[-k:])
#
# 24
with open("copy.txt","r") as f:
    s=f.readlines()
    count=0
    for item in s:
        if item[:4]=="    ":
            count+=1
print(count)


# 26
with open("copy.txt","r") as f:
    s=f.readlines()
    count=0
    for item in s:
        if item[:5]=="     ":
            count+=1
print(count)




# # 29
#
# with open("text.txt","r") as f:
#     text=f.read()
# words=text.split()
# longest=max(words,key=len)
# print("Eng uzun so'z=",longest)
# # 30
# with open("text.txt","r") as f:
#     text=f.read()
# words=text.split()
# shortest=min(words[::-1],key=len)
# print("Eng qisqa so'z=",shortest)










































