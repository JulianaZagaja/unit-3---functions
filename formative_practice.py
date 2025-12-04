#Q15:
#check the errors:
#One error would be that you need to check if the lisy is empty or doesn't have anythign in it before you end up dividing (ZeroDivisionError)

#Q16:
#C. required -> *args -> defaults -> **kwargs

#Q17:
#fill in the blank:
#1. .strip -> clean = text.strip()
#2. .upper -> upper = text.upper()
#3. .split -> words = text.strip().split()
#4. len -> length = len(text.strip())

#Q18.
#def validate_password(password):
#if not password:
#  return False, "empty password"
    
#if len(password) < 8:
#  return False, "too short"
    
#return True, "valid"


#Q19:
# def create_inventory(item_name, *quantities, location="Warehouse"):
#     total = sum(quantities) if quantities else 0
#     return {
#         "item": item_name,
#         "total": total,
#         "location": location
#     }

#Q20:
# def safe_list_access(items, index):
#     try:
#         value = items[index]
#         return value, True
#     except IndexError:
#         return None, False