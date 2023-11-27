myset={1,2,3,4,5}
myset2={10,11,12}
myset.add(7)
print("added value",myset)
myset.update(myset2)
print("updated set",myset)
myset.pop()
print("popped value",myset)
myset3=myset.union(myset2)
print("unioun value",myset3)