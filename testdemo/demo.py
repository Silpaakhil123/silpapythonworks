#import functions from another package

#import and package statement
from mathoperations.operations import *
print(add(10,20))
print(cube(3))

#another import method
# from mathoperations import operations
# print(operations,add(10,20))

#from .operations import*  (used in present package)
# import mathoperations.operations
# mathoperations.operations.add()