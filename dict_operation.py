mydict={1:"apple",2:"Mango",3:"banana"}
mydict2={4:"Papaya",5:"Grape",6:"melon"}
mydict.pop(2)
print("popped dict",mydict)
mydict.popitem()
print("popped item dict",mydict)
mydict2=mydict.copy()
print("Copied dict",mydict)
mydict.update({2:"Pear"})
print("updated dict",mydict)