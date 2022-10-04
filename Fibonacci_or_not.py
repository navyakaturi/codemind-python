n=int(input())
a=0
b=1
if(n==1 or n==2):
    print("True")
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    i+=1
    if(n==c):
        print("True")
        break
else:
    print("False")