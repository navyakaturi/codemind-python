n=int(input())
i=1
k=0
for i in range(1,n):
    if(n%i==0):
        k=k+i
    i+=1
if(k>n):
    print("True")
else:
    print("False")