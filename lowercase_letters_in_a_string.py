n=input()
l=len(n)
c=0
for i in range(0,l):
    if 90<=ord(n[i]):
        c+=1
print(c)