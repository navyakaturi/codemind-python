n=input()
c=0
for i in n:
    if i.isdigit()==True:
        p=int(i)
        c+=p
print(c)