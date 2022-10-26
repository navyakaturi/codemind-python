n=int(input())
a=list(map(int,input().split()))
x=[]
for i in a:
    rem=0
    y=i
    while i!=0:
        s=i//10
        r=i%10
        rem=rem*10+r
        i=s
    x.append(rem)
print(*x)