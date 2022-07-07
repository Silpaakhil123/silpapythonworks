import json
import random
try:
    with open("follow.json",encoding="utf-8") as f:
        data=json.load(f)
    print(data)
    all_users=[user["id"] for user in data]
    my_followings=[user["followers"] for user in data if user["username"]=="akhil"][0]
    my_id=[user["id"] for user in data if user["username"]=="akhil"].pop()
    to_follow=set(all_users)-set(my_followings)
    to_follow.remove(my_id)
    suggest=random.sample([*to_follow],2)# [*to_follow]==destructuring///list(to_follow)
    print(suggest)


except Exception as e:
    print(e.__class__)

#eg of destructuring
# lst=[1,2,3,4]
# st={*lst}
# print(st)