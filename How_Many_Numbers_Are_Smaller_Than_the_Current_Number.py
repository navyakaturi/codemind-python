n=int(input())
l=list(map(int,input().split()))
k=sorted(l)
for i in l:
    print(k.index(i),end=' ')