#print("silpa")
#range(1,10)
#type(2)
#sum(range(1,10))
# min(range(1,10))
# max()
# sorted()
#functions
def add_numbers(n1,n2):
    return n1+n2
print(add_numbers(10,20))

def sub_numbers(n1,n2):
    return n1-n2
print(sub_numbers(20,5))

def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1#(turnery operator)
print(smart_sub(5,10))

def smart_chk(num):
    return "even" if num%2==0 else "odd"
print(smart_chk(15))

#startswith

name="akhil"
print(name.startswith("s"))

#endswith

def validate_gmail(email):
    return email.endswith("@gmail.com")
print(validate_gmail("ac@gmail.com"))

#create a function that will return factorial of a number

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(factorial(5))

#q1:create a function is_prime(num) will return true if number is prime or not
#q2:create a function prime_range(low,upp) return all prime no:s between low to up range

#lambda function: to concise the code

add=lambda n1,n2:n1+n2
print(add(1,2))
cube=lambda n:n**3