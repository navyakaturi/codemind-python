n=input()
n=n.lower()
s=n.split()
c=0
for i in s:
    min=ord(i[0])
    for j in range(1,len(i)):
        if ord(i[j])<min:
            min=ord(i[j])
    c+=min
d=0
for i in s:
    max=ord(i[0])
    for j in range(1,len(i)):
        if ord(i[j])>max:
            max=ord(i[j])
    d+=max
print(d-c)