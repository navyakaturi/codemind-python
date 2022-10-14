n=int(input())
l=list(map(int,input().split()))
ec=0
oc=0
for i in l:
    if i%2==0:
        ec=ec+i
        
for i in l:
    if i%2!=0:
        oc=oc+i
print(abs(ec-oc))
