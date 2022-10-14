n=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    k=k+i
a=k/n
print("{:.2f}".format(a))