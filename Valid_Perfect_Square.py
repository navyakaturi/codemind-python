n=int(input())
for i in range(n):
    a=int(input())
    for i in range(1,a+1,1):
        if a==i*i:
            print("True")
            break
    else:
        print("False")