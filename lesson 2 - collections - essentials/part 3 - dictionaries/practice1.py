#Q1

#Output: {"key_a" : "value1", "key_b": 150, "key_d": 50}
#Output 2: False

#Q2
# Total: 120
#data["val_z"] = 60

#Q3

# def get_user_bio(user):
#     bio = user.get("bio")
#     if not bio:
#         return "No bio available"
#     else:
#         return bio

# print(get_user_bio({"username": "coder", "bio": "Python enthusiast"}))

#Q4
# user 1 prints : 60
# user 2 prints: 160

#Q5
#prints count = 2

#Q6
# def get_total_engagement(post):
#     likes = post.get("likes")
#     comments = post.get("comments")
#     shares = post.get("shares")
#     if not likes:
#         likes = 0
#     if not comments:
#         comments = 0
#     if not shares:
#         shares = 0
#     sum = likes + comments + shares
#     return sum

# print(get_total_engagement({"likes": 100, "comments": 20, "shares": 10}))
# print(get_total_engagement({"likes": 50, "comments": 5}))
# print(get_total_engagement({"views": 1000}))

#Q7
# Output 1 : 3
# Output 2: 3

#Q8
#Output 1 (dict_a): {"key1": "value1", "key2": 200, "key3": 50}
#Output 2 (dict_c): {"key1": "value1", "key2": 100, "key4": True}

#Q9
def find_most_followers(users):
    if not users:
        return None
    most_followers = 0
    for user in users:
        if user["followers"] > most_followers:
           most_followers = user["followers"]
           user_topfollowers = user["username"]
    return user_topfollowers

users = [
    {"username": "alex", "followers": 1000},
    {"username": "sam", "followers": 5000},
    {"username": "jordan", "followers": 3000}
]

print(find_most_followers(users))