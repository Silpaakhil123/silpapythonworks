#q2:create a function prime_range(low,upp) return all prime no:s between low to up range
from isprime import *
def prime_range(low,upp):
    for i in range(low,upp+1):
        if is_prime(i):
            print(i)
    return
prime_range(1,50)