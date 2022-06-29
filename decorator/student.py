
class Course:
    def post(self,**kwargs):
        self.c_id=kwargs.get("c_id")
        self.c_name=kwargs.get("c_name")
        # self.user=kwargs.get("user")
    def __str__(self):
        return self.c_name

class Batch:
    def post(self,**kwargs):#b_code,b_name,course

            self.b_code=kwargs.get("b_code")
            self.b_name=kwargs.get("b_name")
            self.course=kwargs.get("course")

    def __str__(self):
        return self.b_name

class Student:
    def post(self,**kwargs):#st_name,gender,mob_no,batch

            self.st_name=kwargs.get("st_name")
            self.gender=kwargs.get("gender")
            self.mob_no=kwargs.get("mob_no")
            self.batch=kwargs.get("batch")

    def __str__(self):
        return self.st_name
dj=Course()
dj.post(c_id=101,c_name="django")
bigd=Course()
bigd.post(c_id=201,c_name="bigdata")
djb1=Batch()
djb1.post(b_code=1000,b_name="djmay1_2k22",course=dj)
bdb1=Batch()
bdb1.post(b_code=2001,b_name="bdmay1_2k22",course=bigd)
akhil=Student()
akhil.post(st_name="akhil",gender="male",mob_no=98765,batch=djb1)
sarath=Student()
sarath.post(st_name="sarath",gender="male",mob_no=12345,batch=djb1)
arun=Student()
arun.post(st_name="arun",gender="male",mob_no=1987,batch=bdb1)
print(akhil.batch.course.c_name)
print(arun.batch.course)
print(sarath.batch)