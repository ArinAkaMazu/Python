class doc:
    def __init__(self,speak,eat):
        self.speak=speak
        self.eat=eat
    def display(self):
        print("doc says",self.speak)
        print("Doc eats",self.eat)
class LoonyToons(doc):
    def default(self):
        print("is a cartoon")
bugs=LoonyToons("Whats up doc","Carrot")
bugs.display()
bugs.default()