account={"user_name":"silpa",
         "acc_no":"123",
         "acc_type":"savings",
         "balance":5000}
print(account.get("user_name"))
print(account.get("acc_type"))

# if "balance" in account:
#     account["balance"]=5000
# else:
#     account["balance"]=1000

# account["balance"]= 5000 if "balance" in account else 1000

if account["balance"] >2000:
    account["balance"]+=10
else:
    account["balance"]+=2
print(account)
