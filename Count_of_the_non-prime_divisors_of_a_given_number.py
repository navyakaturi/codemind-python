n=int(input())
import math
def prime(n):
    for i in range(2,((int)(math.sqrt(n))+1)):
        if n%i==0:
            return 1
c=0
for i in range(1,n+1):
    if n%i==0:
        if i==1:
            c+=1
        if prime(i)!=1:
            continue
        else:
            c+=1
print(c)