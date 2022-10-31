n=input()
n.lower()
s=n.split()
l=len(s)
c=0
v='a,e,i,o,u'
for j in s:
    c=0
    for i in range(0,len(j)):
        if j[i] in v:
            c+=1
    print(c,end=' ')