t=int(input())
for k in range(t):
    m=list(map(int,input().split()))
    l=list(map(int,input().split()))
    k=list(map(int,input().split()))
    d=sorted(k+l)
    for i in range(len(d)-1):
        print(d[i],end=' ')
    print(d[len(d)-1])