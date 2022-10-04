n=input()
m=input()
x=len(n)
c=0
for i in range(x):
    if n[i]==m:
        c+=1
    i+=1
if c>=1:
    print(c)
else:
    print("-1")