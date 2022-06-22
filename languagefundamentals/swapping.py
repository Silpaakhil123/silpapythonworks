num1 = 10
num2 = 20
number before swapping num1= 10 and num2= 20
print(f"number before swapping num1= {num1} and num2= {num2}")

#using 3rd variables

#temp = num1  # temp=10
#num1 = num2  # num1=20
#num2 = temp  # num2=10
# after swapping
#print(f"number after swapping num1= {num1} and num2= {num2}")

#without using 3rd variables

# num1=num1+num2#num1=10+20=30
# num2=num1-num2#num2=30-20=10
# num1=num1-num2#num1=30-10=20
#print(f"number after swapping num1= {num1} and num2= {num2}")

#python shorthand

(num1,num2)=(num2,num1)
print(f"number after swapping num1= {num1} and num2= {num2}")