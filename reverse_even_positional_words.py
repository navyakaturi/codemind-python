n=input()
s=n.split()
l=len(s)
for i in range(0,l,1):
    if i%2==0:
        x=s[i]
        print(x[::-1],end=' ')
    else:
        print(s[i],end=' ')