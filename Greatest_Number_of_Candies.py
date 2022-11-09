n=int(input())
l=list(map(int,input().split()))
p=int(input())
for i in l:
    if i+p>=max(l):
        print(True,end=' ')
    else:
        print(False,end=' ')
print(k)