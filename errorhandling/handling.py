#try=> block doubtful code
#except=>block handling code
#raise=> key word custom error throw
#finally=>block clean up processing

# num1=int(input("enter num 1: "))
# num2=int(input("enter num 2: "))
# try:
#     res=num1/num2
#     print(f"result={res}")
# except Exception as e:
#     print(e)
# finally:
#     print("file operation")

# age=int(input("enter the age: "))
# if (age<18):
#     raise Exception("not eligible for booster dose")
# else:
#     print("eligible")

ph_no=input("enter the phone no: ")
if (len(ph_no)!=10):
    raise Exception("invalid ph no:")
else:
    print("valid ph no:")