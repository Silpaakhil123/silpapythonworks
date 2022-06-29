class staff:
    id:int
    name:str
    role:str

    def __init__(self,*args,**kwargs):
        self.id=kwargs.get("id")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")

    def __str__(self):
        return self.name

user=staff(id=10,name="rahul",role="admin")
print(user)