
#q1:create a function is_prime(num) will return true if number is prime or not

def is_prime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    return True if flag==0 else False
print(is_prime(6))