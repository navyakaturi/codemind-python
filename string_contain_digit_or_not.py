n=input()
a=n.count('0')+n.count('1')+n.count('2')+n.count('3')+n.count('4')+n.count('5')+n.count('6')+n.count('7')+n.count('8')+n.count('9')
if a==0:
    print("Doesn't contain digit")
else:
    print("Contains",a,"digit")