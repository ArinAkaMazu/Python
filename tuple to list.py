mytuple=(10,20,30,40)
temp=list(mytuple)
list2=[]
for i in temp:
    x=i+5
    list2.append(x)
mytuple=tuple(list2)
print(mytuple)