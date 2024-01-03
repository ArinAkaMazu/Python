class Person:
    # Class variable to keep track of the total number of persons
    total_persons = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Increment the total number of persons when a new instance is created
        Person.total_persons += 1

    def set_attributes(self, name, age):
        self.name = name
        self.age = age

    def display_attributes(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Example usage:
# Create Person instances
person1 = Person(name="John Doe", age=25)
person2 = Person(name="JFK", age=30)

# Display attributes for each person
print("Attributes of person1:")
person1.display_attributes()

print("\nAttributes of person2:")
person2.display_attributes()

# Display total number of persons
print(f"\nTotal number of persons created: {Person.total_persons}")
