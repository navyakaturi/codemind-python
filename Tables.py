n,r=map(int,input().split())
i=1
i=(i%2!=0)
for i in range(1,r+1,2):
    print(n,'x',i,'=',n*i)