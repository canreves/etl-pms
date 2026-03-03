from models.asset import Asset
from models.transaction import Transaction


apple = Asset("AAPL", 100000, 112.5)

aapl_buy = Transaction("AAPL", "2023-01-01", "BUY", 50, 115.0)

aapl_buy.transaction_process()