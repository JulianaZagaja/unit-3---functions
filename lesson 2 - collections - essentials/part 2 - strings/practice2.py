def format_phone_number(phone):
    cleaned_number = ""
    for char in phone:
        if char.isdigit():
            cleaned_number += char
    if not len(cleaned_number) == 10:
        return "invalid"
    return (f"({cleaned_number[0:3]}) {cleaned_number[3:6]}-{cleaned_number[6:]}")

print(format_phone_number("555-123-4567"))
print(format_phone_number("(555) 123 4567"))
print(format_phone_number("5551234567"))
print(format_phone_number("123"))

def sanitize_filename(filename):
    clean_filename = filename.lower().replace(" ", "_")
    
    special = "._-"
    clean_filename2 = ""
    for char in clean_filename:
        if char.isdigit() or char.isalpha() or char in special:
            clean_filename2 += char
    
    if clean_filename2.endswith(".txt"):
        result = clean_filename2
    else:
        if "." in clean_filename2:
            dot_pos = clean_filename2.rfind(".")
            clean_filename2 = clean_filename2[:dot_pos]
        result = clean_filename2 + ".txt"
    
    
    max_len = len(clean_filename2) - 4
    if max_len > 50:
        return "invalid"
    
    return result

print(sanitize_filename("Ancient Scroll.txt"))
print(sanitize_filename("Quest 2042! (Epic)"))
print(sanitize_filename("notes"))
print(sanitize_filename("X"*60))


#alt solution given
# def sanitize_filename(filename):
#     clean = filename.lower().replace(" ", "_")
    
#     safe = ""
#     for char in clean:
#         if char.isalnum() or char in ".-_":
#             safe += char
            
#     if not safe.endswith(".txt"):
#         if "." in safe:
#             safe = safe[:safe.rfind(".")]
#         safe += ".txt"
        
#     if len(safe) > 50:
#         safe = safe[:46] + ".txt"
    
#     return safe
