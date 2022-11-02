s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
w1=s1.split()
w2=s2.split()
c=[]
for i in w2:
    if i in w1:
        c.append(i)
print(*c)
        