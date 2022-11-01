n=input()
l=len(n)
c=0
for i in range(0,l):
    if 65<=ord(n[i])<=91:
        c+=1
print(c)