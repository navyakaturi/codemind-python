n=input()
s='a,e,i,o,u,A,E,I,O,U'
l=[]
for i in n:
    if i in s:
        l.append(i)
print(len(l))