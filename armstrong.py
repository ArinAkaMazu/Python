num=int(input("enter a value to be checked:  "))
temp=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+ rem*rem*rem
    num=num//10
if(sum==temp):
 print("is armstrong")
else:
 print("not")