n=input()
s=n.split()
for i in s:
    min=ord(i[0])
    max=ord(i[0])
    for j in range(1,len(i)):
        if ord(i[j])<min:
            min=ord(i[j])
        if ord(i[j])>max:
            max=ord(i[j])
    a=chr(min)
    b=chr(max)
    print(a,b,end=' ')