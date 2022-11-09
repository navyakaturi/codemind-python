n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    m.append(i*i)
m.sort()
for i in m:
    print(i,end=' ')