n=input()
s=n.split()
c=0
for i in s:
    min=ord(i[0])
    max=ord(i[0])
    for j in range(1,len(i)):
        if ord(i[j])<min:
            min=ord(i[j])
        if ord(i[j])>max:
            max=ord(i[j])
    print(max-min,end=' ')