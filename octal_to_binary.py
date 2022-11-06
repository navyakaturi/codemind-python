n=int(input())
s=str(n)
l=list(s)
k=""
for i in l:
    j=""
    num=(int)(i)
    while num>0:
        if num%2==0:
            j+='0'
        else:
            j+='1'
        num=num//2
    if len(j)!=3:
        for i in range(len(j),3):
            j+='0'
    k+=j[::-1]
print((int)(k))        