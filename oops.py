class person:
    myvar1=10
    myvar2=20
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is",self.name)
        print("age is",self.age)
p1=person('Sugaro Geto',27)
p2=person('Satoru Gojo',30)
p1.display()
p2.display()