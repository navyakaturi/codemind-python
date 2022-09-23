a,b=map(int,input().split())
i=2
lcm=1
while True:
    if a%i==0 and b%i==0:
        a=a//i
        b=b//i
        lcm=lcm*i
        
    else:
        i+=1
        if a<i or b<i:
            break
print(lcm*a*b)