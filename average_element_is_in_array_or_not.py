n=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    k=k+i
if k//n in l:
    print("True")
else:
    print("False")