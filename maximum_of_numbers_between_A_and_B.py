n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
s=[]
for i in l:
    if a<=i and b>=i:
        c+=1
        s.append(i)
if c==0:
    print("-1")
else:
    print(max(s))
        