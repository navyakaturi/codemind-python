n=input()
n=n.lower()
n=n.replace(' ','')
c=[]
for i in n:
    if i in c:
        continue
    if n.count(i)==1:
        c.append(i)
c=sorted(c)
c=''.join(c)
print(c)