n=input()
s=n.split()
for i in s:
    min=ord(i[0])
    for j in range(1,len(i)):
        if ord(i[j])<min:
            min=ord(i[j])
    print(chr(min),end=' ')
    break
for i in s[::-1]:
    max=ord(i[0])
    for j in range(1,len(i)):
        if ord(i[j])>max:
            max=ord(i[j])
    print(chr(max),end=' ')
    break