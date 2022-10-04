n=int(input())
a=str(n)
b=len(a)
t=n
k=0
l=0
while n!=0:
    s=n//10
    d=n%10
    n=s
    l=l+d**b
    b-=1
if(l==t):
    print("True")
else:
    print("False")
    