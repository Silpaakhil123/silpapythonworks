# ********************************
master_word="abbcceddffggt"
chk_word="egg"

mw_dict={}
flag=0
for char in master_word:
    if char in mw_dict:
        mw_dict[char]+=1
    else:
        mw_dict[char]=1
for char in chk_word:
    if char in mw_dict:
        curr_count=mw_dict[char]
        if curr_count>0:
            mw_dict[char]-=1
        elif curr_count==0:
            flag=1
            break
    else:
        flag=1
        break
print(True if flag==0 else False)
