class jjk:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
class student(jjk):
    def __init__(self, name, age,grade) -> None:
        super().__init__(name, age)
        self.grade=grade
    def display(self):
        print(self.name,"is",self.age,"years old, and is a",self.grade,"curse user")
u1=student("gojo storu",27,"special grade")
u2=student("Kento nanami",30,"1st grade")
u1.display()
u2.display()