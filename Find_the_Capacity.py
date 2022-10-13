a,b,c=map(int,input().split())
x=2*a*b*c*512
y=x//1024
print("{}KB".format(y))