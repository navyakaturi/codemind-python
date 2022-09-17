n=int(input())
rev=0
t=n

if n<0:
    
    
    n=n*(-1)
    
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if t<0:
    print(rev*(-1))
else:
    print(rev)