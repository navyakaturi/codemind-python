n=int(input())
l=list(map(int,input().split()))
ec=0
oc=0
for i in range(0,len(l)):
    if i%2==0:
        ec=ec+l[i]
        
for i in range(0,len(l)):
    if i%2!=0:
        oc=oc+l[i]
print(abs(ec-oc))
        
    