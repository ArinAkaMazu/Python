mylist=["sunday","monday","tuesday","wednesday"]
size=len(mylist)
temp=mylist[size -1]
for i in range(size -1,0,-1):
    mylist[i]=mylist[i-1]
mylist[0]=temp
print(mylist)