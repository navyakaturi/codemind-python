n=int(input())
l=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if (l[i]%2)!=0:
        x=l[i]
        print(x)
        break