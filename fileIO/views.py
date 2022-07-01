# fail_s=open("failed.txt","r")
# students=open("students.txt","r")
# passed_s=open("passed.txt","w")
# studs=[stud.rstrip("\n") for stud in students]
# failed=[fail.rstrip("\n") for fail in fail_s]
# passed_students=set(studs)-set(failed)
# for st in passed_students:
#     st+="\n"
#     passed_s.write(st)
ap=open("passed.txt","a")
name="silpa"
ap.write(name)

