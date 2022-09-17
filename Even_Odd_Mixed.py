n=int(input())
rev=0
odd=0
while n>0:
    r=n%10
    n=n//10
    if r%2==0:
        rev+=1
    else:
        odd+=1
if rev>1 and odd==0:
    print("Even")
elif rev==0 and odd>1:
    print("Odd")
else:
    print("Mixed")
