class Employee:

    def __init__(self,**kwargs):
        self.e_id=kwargs.get("e_id")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")

    def __str__(self):
        return self.name
emp=Employee(e_id=121,name="akhil",role="hr")
# print(employee)
class Department:

    def __init__(self,**kwargs):
        employ=kwargs.get("emply")
        if employ.role=="admin":
            self.dep_name=kwargs.get("dep_name")
            self.emply=kwargs.get("emply")
        else:
            print("no privilage")
    def __str__(self):
        return self.dep_name

department=Department(dep_name="developer",emply=emp)
# print(department)
# get
# post
# put/patch
# delete