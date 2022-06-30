from blog.models import users,posts
# print(users)
session={}
def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid session u must login")
    return wrapper

def authentication(*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user
# print(authentication(username="akhil",password="Password@123"))

class LoginView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authentication(username=username,password=password)
        if user:
            session["user"]=user[0]
        # print(session)

class PostlistView:
    @signin_required
    def get(self):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        # print(kwargs)
        post=kwargs.get("data")
        usersId=session["user"]["id"]
        post["userId"]=usersId
        posts.append(post)
        print("posted successfully")
        print(posts[-1])

class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        userid=session["user"]["id"]
        mypost=[post for post in posts if post["userId"]==userid]
        return mypost
class Addlike:
    @signin_required
    def post(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts  if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post["liked_by"])
log_in=LoginView()
log_in.post(username="richard",password="Password@123")
all_post=PostlistView()
# print(all_post.get())
# my_post=MyPostListView()
# print(my_post.get())
my_post={"postId":9,"title":"hello good morning","content":"content","liked_by":[]}
all_post.post(data=my_post)
like=Addlike()
like.post(postid=1)