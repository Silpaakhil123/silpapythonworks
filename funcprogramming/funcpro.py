from functools import reduce
# map
# filter
# reduce
lst=[10,2,30,4]
squares=list(map(lambda n:n**2,lst))
print(squares)
cubes=list(map(lambda n:n**3,lst))
print(cubes)
num_out=list(map(lambda n:n+1 if n>5 else n-1,lst))
print(num_out)

gt_ten=list(filter(lambda n:n>10,lst))
print(gt_ten)
evens=list(filter(lambda n:n%2==0,lst))
print(evens)

sums=reduce(lambda n1,n2:n1+n2,lst)
print(sums)
product=reduce(lambda n1,n2:n1*n2,lst)
print(product)
maximum=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(maximum)
minimum=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(minimum)