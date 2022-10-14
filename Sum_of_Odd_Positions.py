n=int(input())
l=list(map(int,input().split()))
o=0
for i in range(0,len(l)):
    if i%2!=0:
        o=o+l[i]
print(o)
    