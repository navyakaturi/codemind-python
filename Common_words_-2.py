n=input()
m=input()
n=n.lower()
m=m.lower()
s1=n.split()
s2=m.split()
c=0
for i in s1:
    if i in s2:
        if s1.count(i)==1 and s2.count(i)==1:
            c+=1
print(c)