from models.asset import Asset
from models.transaction import Transaction
from models.portfolio import Portfolio


# Creating Portfolio
portfolio = Portfolio("My Investment Portfolio")

# Creating Assets
apple = Asset("AAPL", 115.0, 0)
google = Asset("GOOGL", 145.5, 0)

# Test 1: First Buy
portfolio.buy_asset(apple, 50)
print(f"Portfolio Assets: {portfolio.assets}")
print(f"AAPL Quantity: {portfolio.assets['AAPL'].quantity}")
print(f"Transactions: {portfolio.transactions}\n")

# Test 2: 2nd Buy (same asset)
portfolio.buy_asset(apple, 30)
print(f"AAPL Quantity: {portfolio.assets['AAPL'].quantity}")
print(f"Transactions: {portfolio.transactions}\n")

# Test 3: New Asset Buy
portfolio.buy_asset(google, 25)
print(f"GOOGL Quantity: {portfolio.assets['GOOGL'].quantity}")
print(f"Total Assets: {len(portfolio.assets)}")
print(f"Transactions: {portfolio.transactions}\n")


# Test 4: Selling Assets
portfolio.sell_asset(apple, 20)
print(f"AAPL Quantity after selling: {portfolio.assets['AAPL'].quantity}")
print(f"Transactions: {portfolio.transactions}\n")

# Test 5: Selling more than available quantity
portfolio.sell_asset(apple, 100)
print(f"AAPL Quantity after failed sale: {portfolio.assets['AAPL'].quantity}")
print(f"Transactions: {portfolio.transactions}\n")

# Test 6: Portfolio value calculation
portfolio_value = portfolio.get_portfolio_value()
print(f"Total Portfolio Value: {portfolio_value}\n")        


# Test 7: Average Cost Calculation
average_cost = portfolio.get_average_cost("AAPL")
print(f"Average Cost of AAPL: {average_cost}\n")

# Test 8: Printing final portfolio state
print(f"Final Portfolio Assets: {portfolio.assets}")
print(f"Final Portfolio Transactions: {portfolio.transactions}")


