# super-->>to refer parent class
# self-->>to point current instance
# ->str return string value >>type hint

##overriding

class Parent:
    def properties(self):
        self.props={"mobile":"nokia","bike":"bullet"}
        return self.props
class Child(Parent):
    def properties(self):
        props=super().properties()
        props["car"]="swift"
        return props
ch=Child()
print(ch.properties())
