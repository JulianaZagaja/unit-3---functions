'''
Python
create:[1,2,3]
add: .append(val)
remove end: pop()  
'''

daily_likes = [500, 600, 750, 400]
usernames = ["@nasa", "@tswift", "@netflix"]
mixed_data = [500, "likes", "@user123", True]

first_day = daily_likes[0] #500
last_day = daily_likes[-1] #400
third_day = daily_likes[2] #750

first_three = daily_likes[0:3] #[500, 600, 750]
last_two = daily_likes[-2:] #[750, 400]

# length = len()
# max = max()
# min = min()
# sum = sum()

#code along - post analyzer
def analyze_post(likes_list):
    if likes_list:
        total = sum(likes_list)
        average = total /len(likes_list)
        best_day = max(likes_list)
        return (average, best_day)

def format_usernames(handles):
 formatted = []
 for username in handles:
     formatted.append("@" + username)
 return formatted

result = format_usernames(["nasa", "tswift", "netflix"])
print(result)

def filter_trending_posts(likes_list):
    trending = []
    for viral in likes_list:
        if viral > 1000:
            trending.append(viral)
        return trending

print(filter_trending_posts([500, 1200, 800, 1500]))


