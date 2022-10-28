n=int(input())
l=list(map(int,input().split()))
x=[]

for i in l:
    if i%2==0:
        x.append(i)
for i in l:
    if i%2!=0:
        x.append(i)

print(*x)
