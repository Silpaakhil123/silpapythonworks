#hcf or gcd

num1=36
num2=18
limit=0
limit = num1 if num1<num2 else num2
#limit = min(num1,num2)
for i in range(2,(limit+1)):
    if(num1%i==0 and num2%i==0):
        hcf=i
print(hcf)

#hcf for 3 no:s
num1=15
