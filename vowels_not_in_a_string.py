n=input()
l=len(n)
a=0
b=0
c=0
d=0
e=0
for i in range(1,l):
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
if a==0:
    print('a',end=' ')
if b==0:
    print('e',end=' ')
if c==0:
    print('i',end=' ')
if d==0:
    print('o',end=' ')
if e==0:
    print('u',end=' ')
if a!=0 and b!=0 and c!=0 and d!=0 and e!=0:
    print("0")