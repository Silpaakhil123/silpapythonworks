lst=[10,2,30,4]
squares=list(map(lambda n:n**2,lst))
print(squares)
cubes=list(map(lambda n:n**3,lst))
print(cubes)
num_out=list(map(lambda n:n+1 if n>5 else n-1,lst))
print(num_out)