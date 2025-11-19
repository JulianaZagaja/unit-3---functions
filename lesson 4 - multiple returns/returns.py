def search_data(query):
    if query == "":
        return None
    if query == "empty":
        return 0
    if query == "error":
        return False
    return len(query)

#None = "No Value"
#Meaning: absence of value, not set, not found
#Use for: Missing Data, search failures, optional parameters
result = None
print(result is None) #True - identity check
print(result == None) #True - equality check
print(not result) #True - falsy check

#2 Return Type - Boolean False
#Meaning - Explicit false condition, validation failure, negative result
# Use for: validation result, boolean operations, success/failure status
result = False
print(result is False) #True - identity check
print(not result) #True - boolean negation
print(result == 0) #True - falsy check

#3 Return Zero - A Valid Number
result = 0
print(result == 0) #True - numeric equality
print(not result) #True - (falsy in boolean context)
print(result is None) #False - different objects
print(result is False) #False - different types

#Multiple returns - python packs multiple returns into a tuple!
def calculate_room(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter #turns into a tuple (area, perimeter)

result = calculate_room(10, 5)
print(result)
print(type(result))

print(type(42)) #int
print(type((42,))) #tuple for single item
no_parentheses = 1,2,3
print(type(no_parentheses))

#unpacking tuple
area_result, perimeter_result = calculate_room(20, 6)
print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}")

#practice 1: student analyzer

def analyze_grades(grades):
    avg = sum(grades) / len(grades)
    lowestgrade = 100
    highestgrade = 0
    passed = True
    if not grades:
        return 0,0,0,False
    for grade in grades:

        if grade > highestgrade:
            highestgrade = grade
        if grade < lowestgrade:
            lowestgrade = grade
        if grade < 60:
            passed = False

    return avg, highestgrade, lowestgrade, passed

print(analyze_grades([85, 92, 78, 90]))
print(analyze_grades([]))
print(analyze_grades([85, 80, 80]))