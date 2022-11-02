n=input()
n=n.replace(' ','')
min=ord(n[0])
max=ord(n[0])
for i in range(1,len(n)):
    if ord(n[i])<min:
        min=ord(n[i])
        a=chr(min)
    if ord(n[i])>max:
        max=ord(n[i])
a=chr(min)
b=chr(max)
for i in n:
    x=n.count(a)
    y=n.count(b)
print(a,end=" ")
print(x,end=' ')
print(b,end=' ')
print(y)