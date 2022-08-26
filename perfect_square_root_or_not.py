n=int(input())
i=1
for i in range(n):
    if(n==i*i):
        i+=1
        print("True")
        break
else:
    print("False")