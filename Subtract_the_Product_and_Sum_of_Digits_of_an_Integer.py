n=int(input())
a=1
b=0
while n>0:
    r=n%10
    a=a*r
    b=b+r
    n=n//10
print(a-b)
    