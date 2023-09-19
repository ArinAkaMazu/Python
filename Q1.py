a=int(input("entre 1st no: "))
b=int(input("entre 2nd no: "))
c=int(input("entre 3rd no: "))
d=int(input("entre 4th no: "))
if(a>b and a>c and a>d):
    print("a is big")
elif(b>a and b>c and b>d):
    print("b is big")
elif(c>a and c>b and c>d):
    print("c is big")
else:
    print("d is big")