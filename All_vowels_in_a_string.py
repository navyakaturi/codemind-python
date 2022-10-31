n=input()
l=len(n)
a=0
b=0
c=0
d=0
e=0
for i in range(0,l):
    if n[i]=='a':
        a+=1
    if n[i]=='e':
        b+=1
    if n[i]=='i':
        c+=1
    if n[i]=='o':
        d+=1
    if n[i]=='u':
        e+=1
if a>=1 and b>=1 and c>=1 and d>=1 and e>=1:
    print("True")
else:
    print("False")