stock_prices = {
    "AAPL": 180,    
    "TSLA": 250,    
    "GOOGL": 140, 
    "MSFT": 400,    
    "AMZN": 170,    
    "NFLX": 500     
}
print("===== STOCK PORTFOLIO TRACKER =====")
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, "- $", price)
n = int(input("\nHow many different stocks do you own? "))
total_investment = 0
portfolio_details = []
for i in range(n):
    print(f"\nStock {i+1}")
    stock_name = input("Enter stock name: ").upper()
    if stock_name not in stock_prices:
        print("Stock not available!")
        continue
    quantity = int(input("Enter quantity: "))
    investment = stock_prices[stock_name] * quantity
    total_investment += investment
    portfolio_details.append(
        f"{stock_name} | Quantity: {quantity} | Value: ${investment}"
    )
    print("Investment Value =", investment)
print("\n===== PORTFOLIO SUMMARY =====")
for item in portfolio_details:
    print(item)
print("\nTotal Investment Value = $", total_investment)
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=================\n\n")
    for item in portfolio_details:
        file.write(item + "\n")
    file.write("\nTotal Investment Value = $" + str(total_investment))
print("\nReport saved successfully in 'portfolio.txt'")