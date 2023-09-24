# Sample string
my_string = "hello, World! 123"

# string.upper(): Converts the string to uppercase
upper_case = my_string.upper()
print("Upper case:", upper_case)

# string.lower(): Converts the string to lowercase
lower_case = my_string.lower()
print("Lower case:", lower_case)

# string.capitalize(): Capitalizes the first character of the string
capitalized = my_string.capitalize()
print("Capitalized:", capitalized)

# string.title(): Capitalizes the first character of each word in the string
title_case = my_string.title()
print("Title case:", title_case)

# string.lstrip(): Removes leading whitespace from the string
stripped_left = my_string.lstrip()
print("Left-stripped:", stripped_left)

# string.rstrip(): Removes trailing whitespace from the string
stripped_right = my_string.rstrip()
print("Right-stripped:", stripped_right)

# string.replace(): Replaces a substring with another substring
replaced = my_string.replace("hello", "Hi")
print("Replaced:", replaced)

# string.find(): Returns the lowest index of a substring in the string
index = my_string.find("World")
print("Index of 'World':", index)

# string.startswith(): Checks if the string starts with a specified prefix
starts_with = my_string.startswith("hello")
print("Starts with 'hello':", starts_with)

# string.endswith(): Checks if the string ends with a specified suffix
ends_with = my_string.endswith("123")
print("Ends with '123':", ends_with)

# string.split(): Splits the string into a list of substrings based on a delimiter
split_list = my_string.split(", ")
print("Split:", split_list)

# string.join(): Joins elements of an iterable into a string using the current string as a separator
joined = ", ".join(["apple", "banana", "cherry"])
print("Joined:", joined)

# string.isdigit(): Checks if all characters in the string are digits
is_digit = my_string.isdigit()
print("Is digit:", is_digit)

# string.isalnum(): Checks if all characters in the string are alphanumeric
is_alphanumeric = my_string.isalnum()
print("Is alphanumeric:", is_alphanumeric)

# string.isupper(): Checks if all characters in the string are uppercase
is_upper = my_string.isupper()
print("Is uppercase:", is_upper)

# string.islower(): Checks if all characters in the string are lowercase
is_lower = my_string.islower()
print("Is lowercase:", is_lower)

# string.strip(): Removes leading and trailing whitespace from the string
stripped = my_string.strip()
print("Stripped:", stripped)

# string.rfind(): Returns the highest index of a substring in the string
rindex = my_string.rfind("l")
print("Reverse Index of 'l':", rindex)

# string.isalpha(): Checks if all characters in the string are alphabetic
is_alpha = my_string.isalpha()
print("Is alphabetic:", is_alpha)

# string.isnumeric(): Checks if all characters in the string are numeric
is_numeric = my_string.isnumeric()
print("Is numeric:", is_numeric)
