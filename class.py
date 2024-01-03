class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_attributes(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
person_instance = Person(name="John Doe", age=25)
print("Initial attributes:")
person_instance.display()
person_instance.set_attributes(name="Tony stark", age=30)
person_instance.display()