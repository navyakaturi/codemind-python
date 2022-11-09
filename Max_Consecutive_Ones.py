n=int(input())
l=list(map(int,input().split()))
c=1
ma=1
if 1 not in l:
    print(0)
else:
    for i in range(len(l)-1):
        if l[i]==1 and l[i+1]==1:
            c+=1
            if c>ma:
                ma=c
        else:
            c=1
    print(ma)