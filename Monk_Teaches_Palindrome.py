t=int(input())
for i in range(t):
    n=input()
    l=len(n)
    x=n[-1::-1]
    if x==n:
        if l%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")