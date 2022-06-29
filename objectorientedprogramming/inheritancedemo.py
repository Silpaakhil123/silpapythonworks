class Parent:
    def phone(self):
        print("galaxy a52s")
    def bike(self):
        print("rr310")
class Child(Parent):
    def phone(self):
        print("iphone")
    def bike(self):
        print("bullet")
ch=Child()
ch.bike()
ch.phone()
# parent class and child class have same method and signature-->>overriding
# same method and different signature--
# >>method overloading