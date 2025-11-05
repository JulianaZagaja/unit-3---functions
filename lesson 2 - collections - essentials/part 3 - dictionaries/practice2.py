def calculate_engagement_rate(post):
    if not post["views"] or post["views"] == 0:
        return "0"
    engagement = post["likes"] + post["comments"] + post["shares"]
    rate = engagement / post["views"] 
    rate2 = rate*100
    return f"{rate2:.2f}"
    
    
post = {"views": 1000, "likes": 50, "comments": 10, "shares": 5}
print(calculate_engagement_rate(post))