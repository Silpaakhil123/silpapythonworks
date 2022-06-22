#reverse

# num=123
# while(num!=0):
#     lastdigit=num%10
#     print(lastdigit,end=" ")
#     num=num//10

#
# num=123
# res=0
# while(num!=0):
#     lastdigit=num%10
#     res=(res*10)+lastdigit
#     num=num//10
# print(res)

num=123
res=""
while(num!=0):
    lastdigit=num%10
    res+=str(lastdigit)
    num=num//10
print(res)