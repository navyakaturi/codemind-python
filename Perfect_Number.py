n=int(input())

k=0
i=1
for i in range(1,n):
    if n%i==0:
        k=k+i
        i+=1
if k==n:
    print("True")
else:
    print("False")