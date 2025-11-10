#output = 2300 
#It just checks every number in the list and peak is the highest number, so as every number gets checked, the one of the highest value will become peak and it would print 2300

#output = "WOW WOW LFG"
#It splits the string into a list of words, then for word in words if the length of thne word is less than or equal to 5, it would add it into filtered, which is an empty message. Then when you print it, it would remove any unnecessary spaces from the beginning or end of the message, printing "WOW WOW LFG".

def find_top_donor(donations):
    topdonor = ""
    highestamount = 0
    for key, value in donations.items():
       if value > highestamount:
           highestamount = value
           topdonor = key
    return topdonor
    
donations = {
    "neon": 250,
    "vibe": 180,
    "lunar": 400,
    "pixel": 150
}

print(find_top_donor(donations))