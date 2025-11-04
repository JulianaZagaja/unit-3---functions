#2 
def find_top_players(players, min_score):
    result = []
    for player in players:
        if player["score"] >= min_score:
            result.append(player["username"])
    return result

players = [
    {"username": "DragonSlayer", "score": 8500},
    {"username": "NinjaMaster69", "score": 6200},
    {"username": "MegaDog", "score": 9100},
    {"username": "ShadowAssassin", "score": 5800}
]

result = find_top_players(players, 7000)
print(result)

#3
#It would print
#total songs: 9
#first song: EYE OF THE TIGER
#last song: BLINDING LIGHTS

#4
def calculate_cart_total(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total

cart = [
    {"item": "Laptop", "price": 899.99, "quantity": 1},
    {"item": "Mouse", "price": 24.99, "quantity": 2},
    {"item": "Keyboard", "price": 79.99, "quantity": 1},
    {"item": "USB Cable", "price": 9.99, "quantity": 3}
]

total = calculate_cart_total(cart)
print(f"Total: ${total:.2f}")