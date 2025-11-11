#Q1: 1300, 1500, 2700, 1500
#Output 1: 4
#Output 2: 7000

#Q2:
#Output: 0x9F1aB3c...

#Q3 Code writing

def portfolio_value(holdings, prices):
    total = 0
    for key, value in holdings.items():
        total += value * prices[key]
    return f"${total:.2f}"

    
holdings = {"BTC": 0.5, "ETH": 8.2, "SOL": 50}
prices = {"BTC": 62400, "ETH": 2480, "SOL": 142}

print(portfolio_value(holdings, prices))