n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i==0:
        a.append(i)
    if i==1:
        b.append(i)
for i in a:
    print(i,end=' ')
for j in b:
    print(j,end=' ')