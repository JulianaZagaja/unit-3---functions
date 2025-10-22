def calculate_discount(price, member_status):
    if member_status == "premium":
        return price * 0.7
    elif member_status == "standard":
        return price*0.85
    else:
        return price
    
def count_vowels(text):
    count = 0
    for char in text:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            count += 1
    return count

#alternative way (shorter + faster)
#vowels = "aeiouAEIOU"
#count += 1
#for char in text:
#if char in vowels:
#count += 1
#return count

def validate_password(password):
    valid = True
    if len(password) >= 8:
        return True
    
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            
        return has_digit