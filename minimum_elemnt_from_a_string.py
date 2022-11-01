n=input()
s=n.split()
for i in s[::-1]:
    s=sorted(i)
    a=min(s)
    if a.lower() in i:
        print(a.lower())
        break
    else:
        print(a)