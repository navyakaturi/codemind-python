s=input()
w=s.split()
min=len(w[0])
for i in range(1,len(w)):
    if len(w[i])<len(w[0]):
        min=len(w[i])
print(min)