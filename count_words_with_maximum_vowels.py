n=input()
n.lower()
s=n.split()
l=len(s)
a=[]
v='a,e,i,o,u'
for j in s:
    c=0
    for i in range(0,len(j)):
        if j[i] in v:
            c+=1
    x=c
    a.append(x)
d=0
x=min(a)
for i in a:
    if i==x:
        d+=1
print(d)