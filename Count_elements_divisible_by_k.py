n,k=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(0,n):
    if (a[i])%k==0:
        x.append(a[i])
print(len(x))