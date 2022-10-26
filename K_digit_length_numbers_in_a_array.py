n,k=map(int,input().split())
l=list(map(int,input().split()))
x=[]
c=0
for i in l:
    if i<0:
        i=i*(-1)
    j=str(i)
    a=len(j)
    if k==a:
        c+=1
print(c)