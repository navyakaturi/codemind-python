n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    c=abs(c-i)
if c%4==0:
    print("X")
else:
    print("Y")