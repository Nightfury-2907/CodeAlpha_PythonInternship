# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 330
}

# Get user input
portfolio = {}
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in database.")
        continue
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

# Calculate total investment
total_investment = 0
for stock, qty in portfolio.items():
    investment = stock_prices[stock] * qty
    total_investment += investment
    print(f"{stock}: {qty} shares x {stock_prices[stock]} = {investment}")

print(f"Total Investment Value: {total_investment}")

# Save to file
with open("portfolio_summary.txt", "w") as f:
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty} shares x {stock_prices[stock]} = {stock_prices[stock] * qty}\n")
    f.write(f"\nTotal Investment Value: {total_investment}")
