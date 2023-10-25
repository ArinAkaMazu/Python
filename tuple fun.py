mytuple=(10,20,30,40,50)
temp=list(mytuple)
temp.append(60)
temp[1]=100
del temp[3]
mytuple=tuple(temp)
print(mytuple)