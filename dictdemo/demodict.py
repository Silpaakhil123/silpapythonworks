student={"reg_no":34015802037,"name":"silpa.s","branch":"mscelectronics","passout":2020}
print(student["reg_no"])
print(student["name"])
print(student["branch"])

print("percentage" in student)
student["percentage"]="80%"
print(student)

print("college" in student)
student["college"]="college of applied science"
print(student)

student["percentage"]="81%"
print(student)