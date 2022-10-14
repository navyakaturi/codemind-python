n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in l:
    if i%2==0:
        a=a+i
for i in l:
    if i%2!=0:
        b=b+i
print(a+b)