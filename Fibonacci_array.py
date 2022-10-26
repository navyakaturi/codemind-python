n=int(input())
l=list(map(int,input().split()))
c=0
if n<=2:
    print("no")
else:
    for i in range(2,n):
        if l[i-1]+l[i-2]==l[i]:
            c+=1
        else:
            print("no")
            break
    if c==(n-2):
        print("yes")