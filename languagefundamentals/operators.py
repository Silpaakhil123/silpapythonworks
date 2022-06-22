#arithmetical operators(+,_,/,*,%,**,//)

num1=3
num2=10
print(num1+num2)
print(num2-num1)
print(num1*num2)
print(num2/num1)
print(num1**num2)#num1 multiplies num2 times
print(num2//num1)#floor division
print(num2%num1)#reminder

#relational operators(>,<,==,>=,<=,!=)

print(10<20)
print(10!=10)
print(10>=10)
print(False==False)
print(True==1)
print(False==0)
print(True<False)

#bitwise operators(&,|,^)

#x      y   x&y x|y x^y
#0      0   0   0   0
#0      1   0   1   1
#1      0   0   1   1
#1      1   1   1   0

print(2&4)#0
#0010<=2
#0100<=4
print(2|4)#6

#increment and decrement

i+=1#increment, i++ not work in python
i-=1#decrement, i-- not work in python