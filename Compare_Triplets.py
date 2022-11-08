l=list(map(int,input().split()))
k=list(map(int,input().split()))
c1=0
c2=0
for i in range(len(l)):
    if l[i]>k[i]:
        c1+=1
    if k[i]>l[i]:
        c2+=1
print(c1,c2)