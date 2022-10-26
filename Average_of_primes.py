n=int(input())
l=list(map(int,input().split()))
d=0
e=0
for i in l:
    c=0
    for j in range(1,i):
        
        if i%j==0:
            c+=1
    if c==1:
        d+=1
        e+=i
a=e/d
print("{:.2f}".format(a))