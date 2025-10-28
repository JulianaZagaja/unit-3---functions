# #1
# email = "John.Smith@Gmail.COM"
# normalized = email.lower()
# username = normalized.split("@")[0]
# domain = normalized.split("@")[1]
# print(username, domain)

# #prints john.smith gmail.com

# #2
# text = "The Quick Brown Fox"
# words = text.split()
# initials = ""
# for word in words:
#     initials += word[0].lower()
# print(initials)

# #prints tqbf

#3
def extract_domain(email):
    count = email.count("@")
    
    if count != 1:
        return "Invalid Email"
    
    diffparts = email.lower().split("@")
    domain = diffparts[1]
    return domain

print(extract_domain("john@gmail.com"))
print(extract_domain("JANE@YAHOO.COM"))
print(extract_domain("missing.at.sign.come"))
print(extract_domain("too@@many@signs.com"))
    


# #4
# message = "Hello123World456"
# digits = ""
# for char in message:
#     if char.isdigit():
#         digits += char
# print(digits)

# #prints 123456

#5
# filename = "my-document.txt"
# name_only = filename.replace(".txt", "")
# safe_name = name_only.replace("-", "_")
# result = safe_name.upper()
# print(result)

#prints MY_DOCUMENT

#6
# data = "apple,banana,cherry,date"
# items = data.split(",")
# longest = items[0]
# for item in items:
#     if len(item) > len(longest):
#         longest = item
# print(longest)

#prints banana

#7
def filter_numbers(text):
    result = ""
    for char in text:
        if not char.isdigit():
            result += char
    return result

print(filter_numbers("Hello123World456"))
print(filter_numbers("Test 1 2 3"))
print(filter_numbers("Price: $29.99"))
print(filter_numbers("No numbers here!"))


#8
# url = "https://example.com/users/profile"
# parts = url.split("/")
# protocol = parts[0]
# domain = parts[2]
# path = "/".join(parts[3:])
# print(f"{protocol}//{domain}/{path}")

#prints 
#https://example.com/users/profile

#9
def count_character_types(text):
    spaces = 0
    digits = 0
    letters = 0
    
    for char in text:
        if char == " ":
            spaces += 1
        elif char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
            
    return letters, digits, spaces

print(count_character_types("Hello 123"))
print(count_character_types("Test2024!"))