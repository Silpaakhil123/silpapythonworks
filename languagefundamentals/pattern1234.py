
#1st pattern

#   c1  c2  c3  c4
#r1 1   2   3   4
#r2 1   2   3   4
#r3 1   2   3   4

# for row in range(1,4):
#     for col in range(1,5):
#         print(col,end=" ")
#     print()

#2nd pattern

#1  1   1
#2  2   2
#3  3   3
#4  4   4

# for row in range(1,5):
#     for col in range(1,4):
#         print(row,end=" ")
#     print()

#3rd pattern

#1
#12
#123
#1234

# for row in range(1,5):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()

#4th pattern

#1
#22
#333
#4444

# for row in range(1,5):
#     for col in range(1,row+1):
#         print(row,end=" ")
#     print()

#5th pattern

#
# #
# # #
# # # #

# for row in range(1,5):
#     for col in range(1,row+1):
#         print("#",end=" ")
#     print()

#6th pattern

#   #   #   #
#   #   #
#   #
#
for row in range(1, 5):
     for col in range(5,row,-1):
         print("#", end=" ")
     print()


