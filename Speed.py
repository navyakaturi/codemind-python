t=int(input())
for k in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    ma=l[0]
    c=1
    for i in range(1,len(l)):
        if l[i]<ma:
            ma=l[i]
            c+=1
    print(c)