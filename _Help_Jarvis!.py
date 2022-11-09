t=int(input())
for i in range(t):
    s=input()
    p=[]
    for i in s:
        p.append(i)
    p.sort()
    for i in range(len(p)-1):
        if int(p[i+1])-int(p[i])!=1:
            print("NO")
            break
    else:
        print("YES")