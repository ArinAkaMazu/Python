from collections import OrderedDict
mylist=[10,20,10,20,10,20,30,40]
list2=(OrderedDict.fromkeys(mylist))
for x in list2:
    print( x,"occured", mylist.count(x))