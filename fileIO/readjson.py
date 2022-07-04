import json

with open("blogs.json",encoding="utf-8") as f:
    data=json.load(f)
    print(data)
print(len(data))

# number of post by userid 1
post_by_1=[post for post in data if post["userId"]==1]
print(len(post_by_1))

#total no of likes for postid 6
num_likes=[len(post["liked_by"]) for post in data if post["postId"]==6]
print(num_likes)

# number post liked by user 2
like_count=len([post for post in data if 2 in post["liked_by"]])
print(like_count)


