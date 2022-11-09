n=int(input())
l=list(map(int,input().split()))
d=0
for i in l:
    d=max(l.count(i),d)
l.sort()
for i in l:
    if l.count(i)==d:
        print(i)
        break