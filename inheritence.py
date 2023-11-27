class person:
    myvar1=10
    myvar2=20
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is",self.name)
        print("age is",self.age)
class faculty(person):
    def __init__(self, name,age,f_id, f_salary):
        super().__init__(name,age)
        self.f_id=f_id
        self.f_salary=f_salary
    def display(self):
        print("name is",self.name)
        print("age is",self.age)
        print('faculty ID',self.f_id)
        print('faculty salary',self.f_salary)
f1=faculty('Walter White',27,101,35000)
f2=faculty('Patrick Batemen',30, 102, 45000)
f1.display()
f2.display()
