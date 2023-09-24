English=int(input("enter the marks"))
Hindi=int(input("enter the marks"))
Maths=int(input("enter the marks"))
Science=int(input("enter the marks"))
SS=int(input("enter the marks"))
total=English+Hindi+Science+Maths+SS
print(total)
percentage=(total/(5*100))*100
print("Percentage:",percentage)
if (percentage>=90):
    print("A grade")
elif (percentage>=80):
    property("B grade")
elif (percentage>=70):
    print("C grade")
elif (percentage>=60):
    print("D grade")
elif (percentage<50):
    print("Fail")