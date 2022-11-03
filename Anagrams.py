n=input()
m=input()
n=n.lower()
m=m.lower()
for i in n:
    if i not in m:
        print("False")
        break
else:
    print("True")