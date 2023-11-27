import re
txt="for more info contact at 9853467855"
pattern=re.search("[6-9]\d{9}",txt)
print(pattern)
if pattern:
    print("yes match")
else:
    print("no match")