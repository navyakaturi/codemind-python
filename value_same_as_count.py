n=int(input())
l=list(map(int,input().split()))
c=0
a=[]
for i in range(0,n):
    if l.count(l[i])==l[i]:
        a.append(l[i])
        c+=1
b=set(a)
d=len(b)
print(d)