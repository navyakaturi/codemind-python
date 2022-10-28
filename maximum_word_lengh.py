n=input()
w=n.split()
max=len(w[0])
for i in range(1,len(w)):
    if max<len(w[i]):
        max=len(w[i])
print(max)