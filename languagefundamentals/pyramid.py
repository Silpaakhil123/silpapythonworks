#full pyramid
# for row in range(1,5):
#      for space in range(1,5-row):
#          print(end=" ")
#      for col in range(1,row+1):
#          print("#", end=" ")
#      print()
#hollow full pyramid
for row in range(1,5):
    for col in range(1,8):
    #     print(" ",end=" ")
    # for col in range(1,5-row):
        if row == 4 or col + row == 4 or col - row == 2:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()
    # for space in range(1, 5 - row):



# if row==4 col+row==4 col-row==2
# for row in range(1, 5):
#      for col in range(5,row,-1):
#          print("#", end=" ")
#      print()