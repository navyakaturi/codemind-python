n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in l:
    if k>=i:
        c+=i
print(c)