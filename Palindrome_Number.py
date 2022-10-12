t=int(input())
for i in range(t):
    n=int(input())
    k=0
    a=n
    while n!=0:
        s=n//10
        d=n%10
        k=k*10+d
        n=s
    if(a==k):
        print("True")
    else:
        print("False")