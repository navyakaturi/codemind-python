n=int(input())
l=list(map(int,input().split()))
c=min(l)
for i in range(len(l)):
    for j in range(i,len(l)):
        c=max(sum(l[i:j+1]),c)
print(c)