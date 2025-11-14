# 10
f=open("text.txt","r")
s=f.read()
f1=open("copy.txt","w")
f1.write(s[::-1])
f1.close()
# 11
f=open("text.txt","r")
s=f.read().split()
f1=open("ztoq.txt","w")
for i in range(len(s)):
    if i%2==1:
        f1.write(s[i]+' ')
f2=open("zjuft.txt","w")
for i in range(len(s)):
    if i%2==0:
        f2.write(s[i]+'\n')
f.close()
f1.close()
f2.close()
# 12
f=open("text.txt","r")
s=f.read()
f1=open("ztoq.txt","w")
f2=open("zjuft.txt","w")
for i in s.split():
    if int(i)%2==1:
        f1.write(i+' ')
    else:
        f2.write(i+' ')
f.close()
f1.close()
f2.close()
# 13
f=open("text.txt","r")
s=f.read().split()
n=[int(i) for i in s]
musbat=[]
manfiy=[]
for i in n:
    if i>0:
        musbat.append(i)
    else:
        manfiy.append(i)
musbat.reverse()
manfiy.reverse()
f1=open("zjuft.txt","w")
f2=open("ztoq.txt","w")

for i in musbat:
    f1.write(str(i)+'\n')
for i in manfiy:
    f2.write(str(i)+'\n')
f.close()
f1.close()
f2.close()
# 14
f=open("text.txt","r")
s=f.read().split()
count=0
orta_arif=0
for i in range(0,len(s)):
    count+=int(s[i])
    orta_arif=count/(i+1)
print(orta_arif)
f.close()
# 15
f=open("text.txt","r")
s=f.read().split()
count=0
for i in range(len(s)):
    if i%2==0:
        count+=int(s[i])
print(count)
f.close()
# 16 ================================
f = open("text.txt", "r")
s = f.read().split()
a = [int(x) for x in s]

series = 1
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        series += 1

print("Seriyalar soni:", series)

f.close()
# 17
f = open("text.txt", "r")
s = f.read().split()
a = [int(x) for x in s]

f1 = open("copy.txt", "w")
count = 1
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        count += 1
    else:
        f1.write(str(count) + " ")
        count = 1
f1.write(str(count) + " ")
f.close()
f1.close()


# 18
f=open("text.txt","r")
s=f.read().split()
a=[float(i) for i in s]
loc_min=0
for i in range(1,len(a)-1):
    if a[i]<a[i-1] and a[i]<a[i+1]:
        loc_min=a[i]
        print(loc_min)
        break
f.close()
# 19
f=open("text.txt","r")
s=f.read().split()
a=[float(i) for i in s]
loc_max=0
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        loc_max=a[i]
        print(loc_max)
        break
f.close()
# 20
f=open("text.txt","r")
s=f.read().split()
a=[float(i) for i in s]
count=0
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        count+=1
    elif a[i]<a[i-1] and a[i]<a[i+1]:
        count+=1
print(count)
f.close()
# 21
f=open("text.txt","r")
a=[float(i) for i in f.read().split()]
loc_min=[]
for i in range(1,len(a)-1):
    if a[i]<a[i-1] and a[i]<a[i+1]:
        loc_min.append(i)
loc_min.sort()
f1=open("copy.txt","w")
for i in loc_min:
    f1.write(str(i)+' ')

# 22
f = open("text.txt", "r")
a = [float(i) for i in f.read().split()]
f.close()

extremum = []
for i in range(1, len(a)-1):
    if (a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1]):
        extremum.append(i)

extremum.sort(reverse=True)

f1=open("copy.txt", "w")
for i in extremum:
    f1.write(str(i) + ' ')
f1.close()
# 23

# 25
f=open("text.txt","r")
a = [float(i) for i in f.read().split()]

a = [x**2 for x in a]

f1=open("copy.txt", "w")
for x in a:
    f1.write(str(x) + ' ')
# 26
f=open("text.txt","r")
s=f.read().split()
a=[float(i) for i in s]
f.close()

mx=max(a)
mn=min(a)
i1=a.index(mx)
i2=a.index(mn)
a[i1],a[i2]=a[i2],a[i1]

f1=open("copy.txt","w")
for i in a:
    f1.write(str(i)+' ')
f1.close()

# 27
f=open("text.txt","r")
s=f.read().split()
a=s[::-1]
f.close()

f1=open("copy.txt","w")
for i in a:
    f1.write(i+' ')
f1.close()
# 28
f=open("text.txt","r")
s=f.read().split()
a=[float(i) for i in s]








# 29
f=open("text.txt","r")
s=f.read().split()
a=s[:10]
f.close()

f1=open("copy.txt","w")
for i in a:
    f1.write(i+' ')
f1.close()

# 30
f=open("text.txt","r")
s=f.read().split()
half=len(s)//2
a=s[:half]
f.close()

f1=open("copy.txt","w")
for i in a:
    f1.write(i+' ')
f1.close()
# 31
f=open("text.txt","r")
s=f.read().split()
a=s[-10:]
f.close()

f1=open("copy.txt","w")
for i in a:
    f1.write(i+' ')
f1.close()
# 32
f=open("text.txt","r")
s=f.read().split()
half=len(s)//2
a=s[half:]
f.close()

f1=open("copy.txt","w")
for i in a:
    f1.write(i+' ')
f1.close()

# 33
f=open("text.txt","r")
s=f.read().split()
a=[]
for i in range(0,len(s),2):
    a.append(s[i])
f.close()

f1=open("copy.txt","w")
for i in a:
    f1.write(i+' ')
f1.close()
# 34
f=open("text.txt","r")
s=f.read().split()
a=[int(i) for i in s]
f.close()

b=[]
for i in a:
    if i>=0:
        b.append(i)

f1=open("copy.txt","w")
for i in b:
    f1.write(str(i)+' ')
f1.close()
# 35
f=open("text.txt","r")
s=f.read().split()
f.close()
















