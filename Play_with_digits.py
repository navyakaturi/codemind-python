n=int(input())
a=list(map(int,input().split()))
rem=0
for i in a:
    y=i
    while i!=0:
        s=i//10
        r=i%10
        rem=rem+r
        i=s
print(rem)