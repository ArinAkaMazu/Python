# Given sets
myset1 = {"Sunday", 10, 20, True}
myset2 = {"Sunday", True}

# (i) Union
union_set = myset1.union(myset2)

# (ii) Intersection
intersection_set = myset1.intersection(myset2)

# (iii) Difference
difference_set = myset1.difference(myset2)

# Printing the results
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
