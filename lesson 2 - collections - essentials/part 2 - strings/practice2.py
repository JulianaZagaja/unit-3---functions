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