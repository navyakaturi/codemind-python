n=int(input())
l=list(map(int,input().split()))
if len(set(l))>=3:
    p=list(set(l))
    p.sort(reverse=True)
    print(p[2])
else:
    p=list(set(l))
    print(max(p))