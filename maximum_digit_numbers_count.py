p=list(map(int,input().split()))
l=list(map(int,input().split()))
c=0
d=0
for i in l:
    if i in l:
        if len(str(i))>=c:
            c=len(str(i))
for i in l:
    if len(str(i))==c:
        print(i,end=' ')