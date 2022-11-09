r=list(map(int,input().split()))
l=[]
for i in range(r[0]):
    c=list(map(int,input().split()))
    l.append(c)
for i in range(len(l)):
    p=0
    for j in range(len(l[i])):
        p=max(l[j][i],p)
    print(p)