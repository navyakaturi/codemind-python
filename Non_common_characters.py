s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=s1.replace(' ','')
s2=s2.replace(' ','')
c=[]
for i in s1:
    if i in c:
        continue
    if i not in s2:
        c.append(i)
for j in s2:
    if j in c:
        continue
    if j not in s1:
        c.append(j)
print(len(c))