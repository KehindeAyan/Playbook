from other.user import *
from other.post import *
from other.comment import *

# user
user_1 = User('Sophie','Kinsella','I love sunset and I want to go to the Mars','Writer','Surprise',1, 123)
user_2 = User('Jocko','Willink','I am a former navy seal. That says a lot','Author','Equals',2, 321)

print("user " + user_1.fullname())
print("user " + user_2.bio)
print("user " + user_1.email)
print("user " + user_2.company)
print("user " + str(user_1.ID))
print("password " + str(user_1.password))

userList = []
userList.append(user_1)
userList.append(user_2)

# post
post_1 = Post('Stand in Your Love', 'The song kind of came out of nowhere for me. I had not been doing too much songwriting at the time as I had just released my album The War Is Over, and wasnt in a season of thinking much about new songs.',1,user_1.ID)
post_2 = Post('Stand in Your Love', 'The song kind of came out of nowhere for me. I had not been doing too much songwriting at the time as I had just released my album The War Is Over, and wasnt in a season of thinking much about new songs.',2,user_2.ID)

print("post " + post_1.title)
print("post " + post_2.description)
print("post " + str(post_2.ID))
print("user " + str(user_1.ID))

postList = []
postList.append(post_1)
postList.append(post_2)


# comment
comment_1 = Comment('Automatic Machine Learning for the Enterprise. Driverless AI automates feature engineering, model building, visualization and interpretability.',1,post_2.ID,user_1.ID)
comment_2 = Comment('Sparkling Water combines the fast, scalable machine learning algorithms of H2O with the capabilities of Spark.',2,post_1.ID,user_2.ID)

print("post " + str(post_1.ID))

commentList = []
commentList.append(comment_1)
commentList.append(comment_2)


# Print full name of post creator
post_UserID = post_2.UserID

for User in userList:
    if User.ID == post_UserID:
        print("The user who created this post is " + User.fullname())

# Print bio of post creator
post_UserID = post_2.UserID

for u in userList:
    if u.ID == post_UserID:
        print("The bio is " + u.bio)


# Print post title and description of comment
comment_PostID = comment_1.PostID

for p in postList:
    if p.ID == comment_PostID:
        print("Post Title " + p.title)
        print("Post Description " + p.description)


# print the user ID if the password is the same with the input
def printID():
    user_Password = input("type password")
    for user in userList:
        print(user.fullname() + "fullname")
        if str(user.password) == user_Password:
            print(user.fullname())
            
printID()