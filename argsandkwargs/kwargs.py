def details(**kwargs):#passing multiple values as a dictionary
    print(kwargs)
details(name="silpa",place="kollam")

def add_no(**kwargs):
    print(sum([v for k,v in kwargs.items()]))
    print(sum([v for v in kwargs.values()]))

add_no(n1=10,n2=20,n3=30,n4=40)