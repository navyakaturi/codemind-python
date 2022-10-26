n=int(input())
l=list(map(int,input().split()))
x=[]
for i in l:
    a=str(i)
    b=len(a)
    x.append(b)
print(x.count(min(x)))