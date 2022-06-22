#for loop

# for i in range (1,10):
#     print(i)#1,2,....9

# for i in range(1,50,3):#range(start,stop,step)
#     print(i)#1,4,7,10.....49

# numbers=range(10,0,-1)
# for i in numbers:
#     print(i)

#break=>exit from current loop
for i in range (1,10):
    if(i==5):
        break
    print(i)#1,2,3,4

#continue=>skip current statement
for i in range (1,10):
    if(i==5):
        continue
    print(i)#1,2,3,4,6,7,8,9

#pass =>do nothing