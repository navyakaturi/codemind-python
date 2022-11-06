n=int(input())
k=str(n)
x=n+(int)(k[::-1])
while True:
    k=str(x)
    if k==k[::-1]:
        break
    else:
        x+=(int)(k[::-1])
print(x)