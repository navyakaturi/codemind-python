n=int(input())
l=list(map(int,input().split()))
m=int(input())
k=list(map(int,input().split()))
d=[]
for i in range(len(k)):
    if k[i]<=len(d):
        d.insert(k[i],l[i])
    else:
        d.append(l[i])
for i in d:
    print(i,end=' ')