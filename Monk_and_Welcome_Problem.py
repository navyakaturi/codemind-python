n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
for i in range(n):
    x=l[i]
    y=k[i]
    z=x+y
    print(z,end=' ')