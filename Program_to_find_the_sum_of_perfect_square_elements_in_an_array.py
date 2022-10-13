n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    for j in range(1,i+1):
        if j*j==i:
            c+=i
print(c)