#word count
text="hai hello hai hello hai hello hai hai hai hai hello"
word=text.split(" ")
w_c={}
for w in word:
    if w in w_c:
        w_c[w]+=1
    else:
        w_c[w]=1
print(w_c)

# first recursive
# text="ABACBDE"
# rec={}
# lst=[]
# for char in text:
#     if char in rec:
#         lst.append(char)
#         print("first recursive:", {lst[0]})
#         break
#     else:
#         rec[char]=1

# sec_rec
text1="ABACBDE"
rec1={}
lst1=[]
for char in text1:
    if char in rec1:
        lst1.append(char)
        print("first recursive:", {lst1[1]})
        break
    else:
        rec1[char]=1
print("first recursive:", {lst1[1]})