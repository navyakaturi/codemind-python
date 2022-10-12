n=int(input())
t=n
k=0
while n>0:
    r=n%10
    s=n//10
    rem=1
    while r>0:
        rem=r*rem
        r-=1
    k=k+rem
    n=s
if k==t:
    print("The number {} is a strong number".format(t))
else:
    print("The number {} is not a strong number".format(t))