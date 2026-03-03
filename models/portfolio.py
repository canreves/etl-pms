from models.asset import Asset
from models.transaction import Transaction

class Portfolio:
    def __init__(self, p_name: str):
        self.name = p_name
        self.assets = {}
        self.transactions = []


    def buy_asset(self, asset: Asset, quantity: int):
        if asset.aid not in self.assets:
            asset.quantity = quantity
            self.assets[asset.aid] = asset
            
        else:
            self.assets[asset.aid].quantity += quantity
        
        self.transactions.append({
            "aid": asset.aid,
            "transaction_type": "BUY",
            "quantity": quantity,
            "price": asset.asset_price  
        })
        

    def sell_asset(self, asset: Asset, quantity: int):
        if asset.aid in self.assets and self.assets[asset.aid].quantity >= quantity:
            self.assets[asset.aid].quantity -= quantity
            
            self.transactions.append({
                "aid": asset.aid,
                "transaction_type": "SELL",
                "quantity": quantity,
                "price": asset.asset_price  
            })
        else:
            print(f"Not enough quantity of {asset.aid} to sell.")
            
    def get_portfolio_value(self) -> float:
        total_value = 0.0
        for asset in self.assets.values():
            total_value += asset.quantity * asset.asset_price
        return total_value