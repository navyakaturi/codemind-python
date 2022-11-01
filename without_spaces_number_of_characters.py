n=input()
s=n.split()
l=len(s)
c=0
for i in s:
    for j in range(0,len(i)):
        c+=1
print(c)