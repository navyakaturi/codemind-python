n=int(input())
m=int(input())
for a in range(n,m+1,1):
    if a>1:
        for i in range(2,a,1):
            if a%i==0:
                break
        else:
            print(a)