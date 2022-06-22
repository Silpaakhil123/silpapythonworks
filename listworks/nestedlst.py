lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]
# num greater than 16 fom sub lst
# for sub_lst in lst:
#     for num in sub_lst:
#         if num>16:
#             print(num)
# print(max(lst))

# # flatten lst
# print(lst)
# flatten_lst=[]
# for sub_lst in lst:
#     for num in sub_lst:
#         flatten_lst.append(num)
# print(flatten_lst)
# flatten_lst.sort()
# print(flatten_lst)
# print(max(flatten_lst))

# list comprehension
flatt_lst=[num for sub_lst in lst for num in sub_lst]
print(flatt_lst)
num_gt_sixt=[num for num in flatt_lst if num>16]
print(num_gt_sixt)
odd_nos=[num for num in flatt_lst if num%2!=0]
print(odd_nos)
sum_ev=sum([num for num in flatt_lst if num%2==0])
print(sum_ev)
num_gt_twfi=[num+1 if num>25 else num-1 for num in flatt_lst ]
print(num_gt_twfi)


# eg model for product file
# js_s=[fw for fw in frameworks if fw[1] =="javascript"]
# print(js_s)