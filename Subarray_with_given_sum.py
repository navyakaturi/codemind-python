t=int(input())
for k in range(t):
    n=list(map(int,input().split()))
    l=list(map(int,input().split()))
    f=0
    for i in range(len(l)):
        c=0
        for j in range(i,len(l)):
            c+=l[j]
            if c==n[1]:
                f=1
                print(i+1,j+1)
                break
        if f==1:
            break
    if f==0:
        print(-1)