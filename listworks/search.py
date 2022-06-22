# lst1=[10,11,11,12,13,14,14,14]
# dup_lst=[]
# for i in range(0,len(lst1)):
#     for j in range((i+1),len(lst1)):
#         if lst1[i]==lst1[j]:
#             dup_lst.append(lst1[j])
# print(dup_lst)

# binary search

arr=[10,11,12,13,14,15,16]
arr.sort()
flag=0
elem=16
low=0
upp=len(arr)-1
while(low<=upp):
    mid=(low+upp)//2
    if elem==arr[mid]:
        flag=1
        break
    elif elem>arr[mid]:
        low=mid+1
    elif elem<arr[mid]:
        upp=mid-1
print("found" if flag>0 else "not found")