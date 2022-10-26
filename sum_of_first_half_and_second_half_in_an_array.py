n=int(input())
l=list(map(int,input().split()))
a=n//2
b=0
c=0
for i in range(0,a):
    c+=l[i]

for i in range(a,n):
    b+=l[i]
print(c)
print(b)