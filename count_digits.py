n=int(input())
l=list(map(int,input().split()))
x=[]
for i in l:
    if i<0:
        i=i*(-1)
    a=str(i)
    b=len(a)
    x.append(b)
print(*x)
        