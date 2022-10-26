n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=0
for i in l:
    b=0
    for j in range(1,i):
        if i%j==0:
            b+=1
    if b==1 and i<=k:
        a+=1
print(a)