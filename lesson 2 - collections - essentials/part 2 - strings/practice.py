#Q3

def create_username(first_name, last_name):
    username = first_name + "_" + last_name
    lowercase = username.lower()
    return lowercase

print(create_username("John", "Smith"))
print(create_username("MARY", "Jones"))
print(create_username("Alex", "TAYLOR"))

#alt solution

def create_username(first_name, last_name):
    return(f"{first_name}_{last_name}".lower())

#Q6

def check_email(email):
    email_lower = email.lower()
    if "@" in email_lower and email_lower.endswith(".com"):
        return True
    else:
        return False
    
print(check_email("test@gmail.com"))
print(check_email("user@yahoo.COM"))

# #alt way

# def check_email(email):
#     email_lower = email.lower()
#     return "@" in email_lower and email_lower.endswith(".com")

def create_slug(title):
    titleclean = title.strip()
    title_lower = titleclean.lower()
    slug = title_lower.replace(" ","-")
    return slug
    
print(create_slug("My First Blog Post"))
print(create_slug("  Python Tutorial  "))
print(create_slug("Web Development 101"))