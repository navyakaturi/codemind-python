n=int(input())
l=list(map(int,input().split()))
c=l.count(0)
for i in l:
    if i!=0:
        print(i,end=' ')
for k in range(c):
    print(0,end=' ')