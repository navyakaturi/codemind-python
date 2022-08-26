n=int(input())
k=0
for i in range(n):
    if i*(i+1)==n:
        k=1
        break
if k==1:
    print("YES")
else:
    print("NO")