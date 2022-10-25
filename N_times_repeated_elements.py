n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
a=[]
for i in range(0,n):
    if l.count(l[i])==k:
        x=l[i]
        a.append(x)
        c+=1
b=set(a)
for i in (b):
    print(i,end=' ')
if c==0:
    print('-1')