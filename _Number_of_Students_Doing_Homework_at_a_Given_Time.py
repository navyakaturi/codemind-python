n=int(input())
l=list(map(int,input().split()))
n1=int(input())
l1=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(l)):
    if k in range(l[i],l1[i]+1):
        c+=1
        
print(c)