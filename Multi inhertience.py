class LoonyToons:
    real=False
class Bugs(LoonyToons):
    def doc():
        print("Ehh whats up doc")
class Daffy(Bugs):
    def duck():
        print("Whats up duck")
daffy=Daffy()
daffy.real()