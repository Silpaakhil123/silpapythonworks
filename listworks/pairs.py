# lst = [2, 3, 6, 4]
# sum=10
# for i in range(0,len(lst)):
#     for j in range((i+1),len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print(lst[i],lst[j])
#             break

lst = [2, 3,4, 6, 4]
lst.sort()
low = 0
upp = len(lst) - 1
element = 8
while (low < upp):
    cur_sum = lst[upp] + lst[low]
    if element == cur_sum:
        print(f"pairs {lst[upp]},{lst[low]}")
        break
    elif cur_sum > element:
        upp -= 1
    elif cur_sum < element:
        low += 1
