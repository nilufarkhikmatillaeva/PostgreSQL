# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s= a>b>c or c>b>a
# print(s)

# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s= a>0 and b>0 and c>0
# print(s)

# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s= a>0 or b>0 or c>0
# print(s)
#
# a=int(input("a="))
# if a%2==0:
#     print('Even')
# else :
#     print('Odd')
#
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if a>=b and a>=c:
#     print(f"the largest number is {a}")
# elif b>=a and b>=c:
#     print(f"the largest number is {b}")
# else:
#     print(f"the largest number is {c}")
#
# n=int(input("n="))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# n=int(input("n="))
# for x in range(2,n+1):
#     is_prime=True
#     for i in range(2,x):
#         if x%i==0:
#             is_prime=False
#             break
#     if is_prime:
#       print(x, end=" ")

# n=int(input("n="))
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)


# i=0
# while i<10:
#     i+=1
#     print(i)

# n=int(input("n="))
# bor=False
# while n>0:
#     k=n%10
#     if k==7:
#         bor=True
#     n=n//10
#
# if bor:
#     print("bor")
# else:
#     print("yo'q")


# n=int(input("n="))
# count=0
# while n>0:
#     k=n%10
#     if k%2==0:
#       count+=1
#     n=n//10
# if count>0:
#     print(f"{count} ta juft raqam bor ")
# else:
#     print("yo'q")

# n=int(input("n="))
# count=0
# while n>0:
#     k=n%10
#     if k>5:
#         count+=1
#     n=n//10
# if count>0:
#     print(f"{count} ta raqam")
# else:
#     print("yo'q")

# n=int(input("n="))
# pos=0
# sum=0
# while n>0:
#     k=n%10
#     pos+=1
#     if pos%2==1:
#         sum+=k
#     n=n//10
# print(sum)

# n=int(input("n="))
# count=0
# while n>0:
#     k=n%10
#     if k%2==1:
#         count+=k
#     n=n//10
# print(count)
# task3
# n=int(input("n="))
# bor=False
# while n>0:
#     k=n%10
#     if k==0:
#         bor=True
#     n=n//10
# if bor:
#     print("bor")
# else:
#     print("yo'q")
# n=10
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)
# n = 10
# while n > 0:
#     print(n)
#     n -= 1

# nums=[3,12,7,5,10]
# print(max(nums))
# print(min(nums))
s=1
for i in range(1,20):
   if i%3==0:
       print(i)
