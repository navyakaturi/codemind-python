n=int(input())
s=str(n)
if s.count('0')>1 or s.count('1')>1 or s.count('2')>1 or s.count('3')>1 or s.count('4')>1 or s.count('5')>1 or s.count('6')>1 or s.count('7')>1 or s.count('8')>1 or s.count('9')>1:
    print("Not Unique Number")
else:
    print("Unique Number")