class AgeException(Exception):
    pass
minage= 18
try:
    age = 15
    if age < minage:
        raise AgeException
    else:
        print("Eligible to Vote")    
except AgeException:
    print("minor")