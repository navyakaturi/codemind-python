n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in range(0,n,1):
    x=l.count(m)
print(x)