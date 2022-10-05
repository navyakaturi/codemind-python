n=int(input())
r=0
r1=0
m=n**2
while n!=0:
    s=n//10
    k=n%10
    r=r*10+k
    n=s
    p=r**2
while p!=0:
    s1=p//10
    k1=p%10
    r1=r1*10+k1
    p=s1
if(m==r1):
    print("True")
else:
    print("False")