n=input()
n=n.lower()
n=n.replace(' ','')
c=[]
for i in n:
    if i in c:
        continue
    c.append(i)
print(len(c))