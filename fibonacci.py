n=int(input())
a=0
b=1
if n==a:
    print(a)
else:
    print(a,b,end=" ")
for i in range(3,n+1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c