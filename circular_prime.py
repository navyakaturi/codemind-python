n=int(input())
r=0
c=0
c1=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
while n!=0:
    s=n//10
    d=n%10
    r=r*10+d
    n=s
for i in range(1,r+1):
    if(r%i==0):
        c1=c1+1
if(c<=2) and (c1<=2):
    print("circular prime")
elif(c<=2 and c1>2):
    print("prime but not a circular prime")
else:
    print("not prime")