def isprim(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
for i in range(2,n+1):
    if n%i==0 and isprim(n//i):
        print(i,n//i)
        break
else:
    print(-1)