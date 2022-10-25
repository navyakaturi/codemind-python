n=int(input())
l=list(map(int,input().split()))
d=0
a=[]
for i in range(0,n):
    if l[i] in a:
        continue
    if l.count(l[i])==l[i]:
        a.append(l[i])
if len(a)==0:
    print('-1')
else:
    print(min(a),max(a))