s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=s1.replace(' ','')
s2=s2.replace(' ','')
c=[]
for i in s2:
    if i in c:
        continue
    if i not in s1:
        c.append(i)
for j in s1:
    if j in c:
        continue
    if j not in s2:
        c.append(j)
c=sorted(c)
c=''.join(c)
if len(c)==0:
    print("-1")
else:
    print(c)