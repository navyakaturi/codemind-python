n=input()
n.lower()
s=n.split()
l=len(s)
a=[]
v='a,e,i,o,u'
for i in s:
    c=0
    for j in range(0,len(i)):
        if i[j] in v:
            c+=1
    x=c
    a.append(x)
d=0
x=min(a)
for i in a:
    if i==x:
        d+=1
print(d)