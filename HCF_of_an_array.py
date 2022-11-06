n=int(input())
arr=list(map(int,input().split()))
arr.sort()
k=arr[0]
i=1
while i<n:
    if arr[i]%k==0:
        i+=1
    else:
        k=arr[i]%k
print(k)