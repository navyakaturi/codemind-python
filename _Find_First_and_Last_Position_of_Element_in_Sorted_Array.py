n=int(input())
l=list(map(int,input().split()))
k=int(input())
if k not in l:
    print(-1,-1)
else:
    g=l.index(k)
    print(g,g+l.count(k)-1)