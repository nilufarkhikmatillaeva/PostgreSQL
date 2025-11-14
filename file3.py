# # "".join(s),
#
# # 32
# count=0
# with open("text.txt","r") as f:
#     s=f.readlines()
# for i in s:
#     if i.strip()=="c":
#         print(i)
#         break
# # 34
# with open("text,txt","r") as f:
#     s=f.readlines()
#     max=len(s[0])
#     for i in range(len(s)):
#         if max<len(s[i]):
#             max=len(s[i])
#
#     for i in range(len(s)):
#         k=max-len(s[i])
#         s[i]=k*" "+s[i]
#
# # 35
# with open("text,txt","r") as f:
#     s=f.readlines()
#     text="        "



contacts={
    997856363:{
        "name":"Ziyoda",
        "phone": "+998997856363",
        "email":"xamidullaeva@gmail.com"
    },
    908684868:{
        "name":"Amina",
        "phone":"+998908684868",
        "email":"xamidova@gmail.com"
    },
    972342323:{
        "name":"Aziza",
        "phone": "+998972342323",
        "email":"xakimova@gmail.com"
    }
}

def add_contact(d:dict):
    name=input("name:")
    phone=input("phone:")
    email=input("email:")
    s={phone:{
        "name":name,
        "phone":phone,
        "email":email
    }}
    d.update(s)
def view_contact(d:dict):
    for k,v in d.items():
        print(f"id. {k}. name:{v['name']} phone:{v['phone']}")

def contact_manager(d:dict):
    while True:
        kod=input(" 1.view contacts \n 2.add contacts \n 3.break")
        if kod=="1":
            view_contact(d)
        elif kod=="2":
            add_contact(d)
        else:break
contact_manager(contacts)


email = input("Email: ")
phone = input("Phone: ")

import re

if re.match(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+', email):
    print("Valid email")
else:
    print("Invalid email")

if re.match(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', phone):
    print("Valid phone")
else:
    print("Invalid phone")






