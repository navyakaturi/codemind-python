n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
for i in l:
    if l.count(i)==1:
        print(i)
        break
else:
    print(-1)