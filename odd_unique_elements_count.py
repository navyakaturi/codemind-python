n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
for i in range(0,n):
    if l[i] in a:
        continue
    if l[i]%2!=0:
        a.append(l[i])
        c+=1
print(c)