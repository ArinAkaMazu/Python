class LoonyToons:
    real=False
class doc(LoonyToons):
    def speak():
        print("Doc says whats up doc")
class daffy(doc):
    def speak():
        print("Daffy says \"whats up duck\""    )
daffy.speak()
doc.speak()
print(doc.real)
print(daffy.real)