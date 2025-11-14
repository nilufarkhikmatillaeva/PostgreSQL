# # 1
# ch = input("Belgi kiriting: ")
# print("ASCII kodi:", ord(ch))
# # 2
# n = int(input("n = "))
# print("Belgi:", chr(n))
# # 3
# ch = input("Belgi kiriting: ")
# print("Oldingi belgi:", chr(ord(ch) - 1))
# print("Keyingi belgi:", chr(ord(ch) + 1))
# # 4
# n = int(input("n = "))
# for i in range(n):
#     print(chr(65 + i), end=" ")   # 65 = 'A'
# 5
n = int(input("n = "))
for i in range(n):
    print(chr(122 - i), end=" ")  # 122 = 'z'
# 6
ch = input("Belgi kiriting: ")
if ch.isdigit():
    print("digit")
elif ch.isalpha():
    print("lotin")
else:
    print("nol")
# 7
s = input("Satr kiriting: ")
print("Birinchi belgi kodi:", ord(s[0]))
print("Oxirgi belgi kodi:", ord(s[-1]))
# 8
n = int(input("n = "))
ch = input("Belgi kiriting: ")
print(ch * n)
# 9
s1 = input("1-satr: ")
s2 = input("2-satr: ")
print(s1 + s2)
# 10
s = input("Satr kiriting: ")
print(s[::-1])
# 11
s = input("Satr kiriting: ")
print(" ".join(s))
# 12
s = input("Satr kiriting: ")
n = int(input("n = "))
print(("*" * n).join(s))
# 13
s = input("Satr kiriting: ")
count = 0
for ch in s:
    if ch.isdigit():
        count += 1
print("Raqamlar soni:", count)
# 14
s = input("Satr kiriting: ")
count = 0
for ch in s:
    if 'A' <= ch <= 'Z':
        count += 1
print("Katta harflar soni:", count)
# 15
s = input("Satr kiriting: ")
count = 0
for ch in s:
    if ('a' <= ch <= 'z') or ('а' <= ch <= 'я'):
        count += 1
print("Kichik harflar soni:", count)


