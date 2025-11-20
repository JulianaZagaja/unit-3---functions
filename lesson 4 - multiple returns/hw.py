
#Q1

def search_user_database(query):
    query = query.strip()
    if not query:
        return None, "No search query", False
    if not query.isalpha():
        return False, "Invalid characters", False
    if query == "john":
        return 3, "Found 3 users", True
    else:
        return 0, "No users found", True


#Q2

def analyze_book_pages(pages):
    if not pages:  
        return 0, 0, 0.0, False
    
    count = len(pages)
    total = sum(pages)
    avg = total / count
    has_long = any(p > 500 for p in pages)
    
    return count, total, avg, has_long


#q1 test cases


result, message, success = search_user_database("")
print(result, message, success)  # None, "No search query", False

result, message, success = search_user_database(" ")
print(result, message, success)  # None, "No search query", False

result, message, success = search_user_database("user123")
print(result, message, success)  # False, "Invalid characters", False

result, message, success = search_user_database("user@email")
print(result, message, success)  # False, "Invalid characters", False

result, message, success = search_user_database("admin")
print(result, message, success)  # 0, "No users found", True

result, message, success = search_user_database("john")
print(result, message, success)  # 3, "Found 3 users", True

#q2 test cases

count, total, avg, has_long = analyze_book_pages([250, 180, 620, 310])
print(count, total, avg, has_long)  # 4, 1360, 340.0, True

count, total, avg, has_long = analyze_book_pages([200, 150, 300])
print(count, total, avg, has_long)  # 3, 650, 216.67, False

count, total, avg, has_long = analyze_book_pages([])
print(count, total, avg, has_long)  # 0, 0, 0.0, False

count, total, avg, has_long = analyze_book_pages([500, 400, 300])
print(count, total, avg, has_long)  # 3, 1200, 400.0, False

count, total, avg, has_long = analyze_book_pages([501, 400, 300])
print(count, total, avg, has_long)  # 3, 1201, 400.33, True
