n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
s=0
for i in l:
    if i>=a and i<=b:
        c.append(i)
        s+=1
if s==0:
    print("-1")
else:
    print(*c)
        