pattern="ABAACCD"
# rec={}
# for char in pattern:
#     if char in rec:
#         print(f"first recursive character is {char}")
#         break
#     else:
#         rec[char]=1

char_count={}
rec_char=[]
for char in pattern:
    if char in char_count:
        rec_char.append(char)

    else:
        char_count[char]=1
print(rec_char[1])

