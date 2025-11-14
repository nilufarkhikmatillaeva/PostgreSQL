# # 26
# n=int(input("n="))
# s="abcdef"
# if len(s)>n:
#     s=s[-n:]
# else:
#     s="."*(n-len(s))+s
# print(s)
# # 27
# n1=int(input("n1="))
# n2=int(input("n2="))
# s1="abcdefgh"
# s2="schoolteacher"
# s=s1[:n1]+s2[-n2:]
# print(s)
#
# # 28
# s="cucumber"
# s1="ccc"
#
# for i in s:
#     if i=="c":
#         s1+="cc"
#     else:
#         s1+=i
# print("s1=",s1)
# # 29
# s="coca cola"
# s1="abs"
# new_s=" "
# for i in s:
#     if i=="c":
#         new_s+=s1+i
#     else:
#         new_s+=i
# print(new_s)
#
#
# # 30
# s1='cool'
# s2='come cut copy'
# for i in s2:
#     if i =='c':
#         s2+=s1
#     else:
#         s2+=i
# print(s2)
# # 31
# s1="I am learning python"
# s2="learn"
# if s2 in s1:
#     print(True)
#
# else:
#     print(False)
# # 32
# s1="man i man can write man code in python man"
# s2="man"
# count=0
# for i in range(len(s1)-len(s2)+1):
#     if s1[i:i+len(s2)]==s2:
#         count+=1
# print(count)
# # 33
# s1="man absman djx man"
# s2="man"
# index=s1.find(s2)
# if index != -1:
#     result=s1[:index]+s1[index+len(s2):]
# else:
#     result=s1
# print(result)
#
#
#
# # 34
# s='abco dbabcoo dhbabc'
# s2='abc'
# # s1=s[::-1]
# # s3=s2[::-1]
# # s0=s1.replace(s3,"",1)
# # print(s0[::-1])
#
# index=0
# for i in range(len(s)-len(s2)):
#     if s[i:len(s2)+i] == s2:
#         index = 1
# s0=s[:index]+s[index+len(s2):]
# print(s0)
# # 35
#
#
# # 36
# s='abco dbabcoo dhbabc gfe'
# s2='abc'
# s3='mem'
# index=0
# s0=s[::-1].replace(s2[::-1],s3,1)
# print(s0[::-1])
# for i in range(len(s)-len(s2)):
#     if s[i:len(s2)+i] == s2:
#         index = 1
#         s.replace(s2,s3)
# # 37
# S1 = "abs abbb dcab bbac abbbc"
# S2 = "bbb"
# S3 = "aaa"
# pos = S1.rfind(S2)   # find last position
# if pos != -1:
#     result = S1[:pos] + S3 + S1[pos+len(S2):]
# else:
#     result = S1
#
# print(result)
# # 38
# s1="abs abbb dcab bbac abbbc"
# s2="aaa"
# s3="bbb"
# result=s1.replace(s2,s3)
# print(result)
# # 39
# s1="you are my best friend"
# index1=s1.find(" ")
# index2=s1.find(" ",index1+1)
# if index1 == index2:
#     print(0)
# else:
#     print(s1[index1+1:index2])
#
#
# # 40
# s="abcd def ghjk lmnop pqrs"
# index1=s.find(" ")
# index2=s.rfind(" ")
# if index1==index2:
#     print(0)
# else:
#     print(s[index1:index2])
# # 41
# s='Men Toshkent shaxrida yashayman'
# words=s.split()
# print(words)
#
# # 42
# s = "OLMA ANOR QOZOQ TUT GUL QIRQ"
# words = s.split()
# count = 0
# for w in words:
#     if w[0] == w[-1]:
#         count += 1
# print(count)
# # 43
# s = input("s = ")
# words = s.split()
# count = 0
# for w in words:
#     if 'A' in w:
#         count += 1
# print(count)
# # 44
# s = input("s = ")
# words = s.split()
# count = 0
# for w in words:
#     if w.count('A') == 3:
#         count += 1
# print(count)
# # 45
# s = input("s = ")
# words = s.split()
# lengths = [len(w) for w in words]
# print(min(lengths))
#
# # 46
# s=int(input("s = "))
# words = s.split()
# lengths = [len(w) for w in words]
# print(max(lengths))
#length = [len(w) for w in a]
#
# 48
s="absja ndksn eonekxle lnwlml wkdwsdw nksnkn aooaoa "
a=s.split()
print(a)
s1=[]
for item in a:
    x=0
    s0=item[0]
    for j in item[1:]:
         if j == s[0]:
             s0+="."
         else:
             s0+=j
    s1.append(s0)
print(s1)

# 50 need 100%
s='olma  olcha   anor   banan  nok'
s1=s[0]
for i in range(1,len(s)):
    if s[i] == ' ':
        if s[i-1] == s[i]:
            s.removeprefix(s[i])
        s1.join(s[:])
print(s1)
# 53
# # 55
# s='anf djns jankd nnakd akandj anjsbakj'
# a=s.split()
# max=a[0]
# for i in range(len(a)):
#     if a[i]>max:
#         max=a[i]
# print(max)
#
# # 51
# s = input("Satrni kiriting: ")
# punctuations = ".,;:!?-—'\"()[]{}"
#
# count = 0
# for char in s:
#     if char in punctuations:
#         count += 1
#
# print("Tinish belgilari soni:", count)

# f=open("list2.py",'r')
# s=f.read()
# print(s)
# f.close()
# 5








