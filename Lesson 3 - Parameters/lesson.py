#using keyword arguments
def create_gamer(username, level, xp, rank, online):
    '''Create a gamer profile.'''
    return {
    "username": username,
    "level": level,
    "xp": xp,
    "rank": rank,
    "online": online
    }
    
player1 = create_gamer(username="BTStudent",
                       level=25,
                       rank="Gold",
                       xp=10000,
                       online=True
                       )
print(player1)

def send_message(sender, recipient, message, urgent):
    return f"{sender} --> {recipient}: {message} (Urgent: {urgent})"

sender1 = send_message(sender = "Alex",
                       recipient= "Jordan",
                       message = "Check Discord",
                       urgent = True)

print(sender1)

def post_content(username, text, likes=0, retweets=0):
    return f"@{username}: {text} | ❤️ {likes} 🔁 {retweets}"

poster = post_content("techguru", "Python is amazing!")

print(poster)

# *args - accept any # of values

def sum_scores(*scores):
    '''Sum ANY number of scores'''
    total = 0
    for score in scores:
        total += score
    return total

result = sum_scores(10, 20, 30)
result2 = sum_scores(10, 20, 30, 55, 68)