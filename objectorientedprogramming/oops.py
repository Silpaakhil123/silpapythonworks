class student:
    name:str
    cls:int
    roll_no:int
    percentage:str
    def __init__(self,name,cls,roll_no,percentage):
        self.name=name
        self.cls=cls
        self.roll_no=roll_no
        self.percentage=percentage

    def print_student(self):
        print(self.name,self.cls,self.roll_no,self.percentage)
# p1=student()
# p2=student()
# p1.det_student("silpa",10,43,"80%")
# p2.det_student("akhil",10,5,"80%")

p1=student("silpa",10,43,"80%")
p2=student("akhil",10,5,"80%")
p1.print_student()
p2.print_student()
# >>constructor<<
# intializing instance variables
# __init__---constructor name
# construstor calls while creates object
