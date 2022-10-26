n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[]
for i in range(0,n):
    if a[i] in x:
        continue
    if a[i] in b:
        x.append(a[i])
print(len(x))