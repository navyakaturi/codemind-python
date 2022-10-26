n=int(input())
l=list(map(int,input().split()))
k=int(input())
d=0
for i in l:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1 and i>=k:
        d+=1
print(d)