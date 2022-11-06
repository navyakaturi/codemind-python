import math
p,r,t=map(int,input().split())
k=1+(r/100)
j=pow(k,t)
c=p*j
print("{:.2f}".format(c))