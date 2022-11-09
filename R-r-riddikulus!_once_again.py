n=list(map(int,input().split()))
l=list(map(int,input().split()))
if n[1]>=n[0]:
    n[1]=n[1]%n[0]
d=l[n[1]:]+l[:n[1]]
for i in d:
    print(i,end=' ')