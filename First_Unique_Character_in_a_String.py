s=input()
s=s.lower()
for i in range(0,len(s),1):
    if s.count(s[i])==1:
        print(i)
        break
else:
    print("-1")