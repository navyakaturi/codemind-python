l=list(map(int,input().split()))
l1=list(map(int,input().split()))
for i in range(0,len(l1)-1,2):
    for j in range(l1[i+1]):
        print(l1[i],end=' ')