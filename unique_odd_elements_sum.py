n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
for i in range(0,n):
    if l[i] in a:
        continue
    if l[i]%2!=0:
        c+=l[i]
        a.append(l[i])
print(c)