l=int(input())
r=int(input())
for i in range(l,r+1):
    k=str(i)
    if k==k[::-1]:
        print(i,end=" ")