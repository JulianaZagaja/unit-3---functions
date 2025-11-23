#Q3

def get_phone_number(contacts, name):
    try:
        return contacts[name]
    except KeyError:
        return "Contact not found"
    

contacts = {"Mom": "555-0123", "Dad": "555-0456", "Best Friend": "555-0789"}
print(get_phone_number(contacts, "Mom"))

contacts = {"Mom": "555-0123", "Dad": "555-0456", "Best Friend": "555-0789"}
print(get_phone_number(contacts, "Boss"))

contacts = {"Mom": "555-0123", "Dad": "555-0456", "Best Friend": "555-0789"}
print(get_phone_number(contacts, "Best Friend"))


#Q4

def get_song(playlist, position):
    try:
        return playlist[position]
    except IndexError:
        return "Position out of range"
    except TypeError:
        return "Position must be an integer"
    
playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, 2))

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, 20))

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, "first"))

#Q5

def calculate_test_average(scores):
    try:
        total = sum(scores)
        count = len(scores)
        average = total / count
        return round(average, 2)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return "Invalid score data"
    
print(calculate_test_average([88, 92, 76, 95, 84]))

print(calculate_test_average([78.5, 92.0, 85.5]))

print(calculate_test_average([]))