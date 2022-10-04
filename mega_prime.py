from math import*
n=int(input())
k=0
s='2357'
for i in range(2,int(sqrt(n))+1):
    if n%i==0:
        k+=1
if k==0:
    while n!=0:
        r=n%10
        if str(r) not in s:
            print("Not Mega Prime")
            break
        n=n//10
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")