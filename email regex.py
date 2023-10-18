import re
txt="welcome contact here at: lords.uni@gmail.com"
pattern=re.findall("[a-zA-Z0-9-._]+@[a-zA-Z0-9]+\.[a-z].*",txt)
print(pattern)
if pattern:
    print("yes match")
else:
    print("not match")