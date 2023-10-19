import re
txt="your exams will start on 21|12|2023 and will end on 01|01|2024"
pattern=re.findall("\d{2}\|\d{2}\|\d{4}",txt)
print(pattern)
if pattern:
    print("yes match")
else:
    print("not match")