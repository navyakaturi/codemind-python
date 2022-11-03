n=input()
n=n.lower()
s=n.split()
c=0
for j in s:
    a=""
    for i in j[::-1]:
        a+=i
    if a==j:
        c+=1
print(c)