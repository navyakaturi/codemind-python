n=input()
a=input()
l=len(n)
for i in range(0,l):
    if n[i]==a:
        print("True")
        print(i)
        break
else:
    print("False")