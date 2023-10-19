import re
txt="for more info you can visit our url: lordsuni.edu"
pattern=re.findall("((https?://)?(www\.)?)?[a-zA-Z0-9\-._]+\.[a-zA-Z]{2,3}",txt)
print(pattern)
if pattern:
    print("yes match")
else:
    print("not match")