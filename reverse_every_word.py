n=input()
s=n.split()
l=len(s)
for i in range(0,l):
    x=s[i]
    print(x[::-1],end=' ')