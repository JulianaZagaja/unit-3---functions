def safe_divide(a,b):
    try:
        result = a / b
        return result
    # except:
    #     print("Can not divide by zero!")
    #     return None
    except ZeroDivisionError:
        print("Can not divide by zero!")
        return None
    except TypeError:
        print("That is not a valid number!")
        return None
    except:
        print("An error occured")
print(safe_divide(10, 2)) #5.0
print(safe_divide(10,0)) #Can not divide by zero! Returns None
print(safe_divide(10,"hello"))

def safe_operations(a,b,lst,key,d):
    try:
        print(f"Division result: {a/b}")
        #type error
        print("Access list element:", lst[2]) #Index error
        print("Access Dictionary Key:" ,d[key])
        print(f"Add numbers: {a + b}")
    except ZeroDivisionError:
        print("cannot divide by 0")
    except IndexError:
        print("List index out of range!")
    except KeyError:
        print(f"Key {key} not found")
    # except TypeError:
    #     print("Invalid types for operation") 
    except Exception as e:
        print("Some other error occured", e)
        
print(safe_operations(10,2,[1,2],"Tom", {"John": 15}))


def calculate_price_per_item(total_cost, num_items):
    try:
        itemprice = total_cost / num_items
        return round(itemprice, 2)
    except ZeroDivisionError:
        return "No items to calculate"
    
print(calculate_price_per_item(200, 4))

def parse_age(age):
    try:
        return int(age)
    except ValueError:
        return None
    
print(parse_age("25"))