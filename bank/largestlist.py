from functools import reduce
num=[9,38,8,78]#largest no
# num=[3,30,34,5,9]
strlst=[str(n) for n in num]
print(strlst)
largest_no=reduce(lambda n1,n2:(n1+n2) if (n1+n2)>(n2+n1) else (n2+n1),strlst)
print(largest_no)


lst=[3,4,5,6,2]
# 3 sum pair 9,12