n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[]
for i in range(0,n):
    if a[i] in x:
        continue
    if a[i] not in b:
        x.append(a[i])
for i in range(0,m):
    if b[i] in x:
        continue
    if b[i] not in a:
        x.append(b[i])
print(*x)