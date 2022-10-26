n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
c=[]
for i in l:
    if a<=i and b>=i:
        s+=1
        c.append(i)
if s==0:
    print("-1")
    
else:
    print(min(c))

    