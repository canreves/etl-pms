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
    
    
    def get_average_cost(self, asset_aid: str) -> float:
        if asset_aid in self.assets:
            asset = self.assets[asset_aid]
            total_cost = 0.0
            total_quantity = 0
            
            for transaction in self.transactions:
                if transaction["aid"] == asset_aid and transaction["transaction_type"] == "BUY":
                    total_cost += transaction["quantity"] * transaction["price"]
                    total_quantity += transaction["quantity"]
            
            return total_cost / total_quantity if total_quantity > 0 else 0.0
        else:
            print(f"Asset {asset_aid} not found in portfolio.")
            return 0.0
        
    def get_profit_loss(self, asset_aid: str) -> float:
        if asset_aid in self.assets:
            asset = self.assets[asset_aid]
            average_cost = self.get_average_cost(asset_aid)
            return (asset.asset_price - average_cost) * asset.quantity
        else:
            print(f"Asset {asset_aid} not found in portfolio.")
            return 0.0
        
    
    def get_portfolio_summary(self):
        summary = {
            "name": self.name,
            "total_value": self.get_portfolio_value(),
            "assets": {},
            "transactions": self.transactions
        }
        
        for aid, asset in self.assets.items():
            summary["assets"][aid] = {
                "quantity": asset.quantity,
                "average_cost": self.get_average_cost(aid),
                "current_price": asset.asset_price,
                "profit_loss": self.get_profit_loss(aid)
            }
        
        return summary
    
    
    def print_portfolio_summary(self):
        summary = self.get_portfolio_summary()
        print(f"\n{'='*70}")
        print(f"Portfolio: {summary['name']}")
        print(f"{'='*70}")
        print(f"{'Asset':<10} {'Qty':<8} {'Avg Cost':<12} {'Current':<12} {'Profit/Loss':<12}")
        print(f"{'-'*70}")
        
        for aid, data in summary["assets"].items():
            print(f"{aid:<10} {data['quantity']:<8} ${data['average_cost']:<11.2f} ${data['current_price']:<11.2f} ${data['profit_loss']:<11.2f}")
        
        print(f"{'-'*70}")
        print(f"Total Value: ${summary['total_value']:.2f}")
        print(f"{'='*70}\n")