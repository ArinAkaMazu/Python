class animal:
    legs=4
    def alive():
        print("This animal is nice and alive")
class pets:
    def home():
        print("pets are kept at home")
class dog(animal,pets):
    pass
dog.alive()
dog.home()
print(dog.legs)