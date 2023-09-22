mylist=["sunday","monday","tuesday","wednesday"]
size=len(mylist)
for i in range(0,size//2):
    mylist[i],mylist[size-1-i]=mylist[size-1-i],mylist[i]
print(mylist)