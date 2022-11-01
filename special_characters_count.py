n=input()
c=0
for i in n:
    if i.islower() or i.isupper() or i.isdigit() or i==' ':
        pass
    else:
        c+=1
print(c)