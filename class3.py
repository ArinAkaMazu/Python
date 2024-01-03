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
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    # Override the display_attributes method to include employee_id
    def display_attributes(self):
        super().display_attributes()
        print(f"Employee ID: {self.employee_id}")

# Example usage:
# Create Employee instances
employee1 = Employee(name="walter white", age=25, employee_id="E123")
employee2 = Employee(name="thomas shelby", age=30, employee_id="E456")

# Display attributes for each employee
print("Attributes of employee1:")
employee1.display_attributes()

print("\nAttributes of employee2:")
employee2.display_attributes()
