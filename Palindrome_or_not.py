n=input()
n=n.lower()
a=""
for i in n[::-1]:
    a+=i
if a==n:
    print("True")
else:
    print("False")