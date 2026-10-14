
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("Welcome to Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    portfolio.append(
        (stock, quantity, price, investment)
    )

print("\n----- Portfolio Summary -----")

for stock, quantity, price, investment in portfolio:
    print(
        f"{stock}: {quantity} shares x "
        f"${price} = ${investment}"
    )

print(f"\nTotal Investment: ${total_investment}")

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")

    for stock, quantity, price, investment in portfolio:
        file.write(
            f"{stock}: {quantity} shares x "
            f"${price} = ${investment}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}\n")

print("Portfolio saved to portfolio.txt")
