n=int(input())
l=list(map(int,input().split()))
c=0
b=0
a=n//2
for i in range(0,a):
    c+=l[i]
for i in range(a,n):
    b+=l[i]
print(abs(c-b))
