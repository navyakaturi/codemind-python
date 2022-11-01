n=input()
s=n.split()
l=len(s)
c=0
v='a,e,i,o,u,A,E,I,O,U'
for i in s:
    x=len(i)
    if i[0] in v:
        if i[x-1] not in v:
            c+=1
print(c)