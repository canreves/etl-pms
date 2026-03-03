class Portfolio:
    def __init__(self, p_name: str):
        self.name = p_name
        self.assets = {}
        self.transactions = {}

    def add_asset(self, asset: Asset):
        self.assets[asset.aid] = asset
        self.transactions[asset.aid] = f"Added asset {asset.aid} with quantity {asset.quantity} at price {asset.asset_price}$."
        

    def buy_asset(self, asset: Asset, quantity: int):
        if asset.aid in self.assets:
            self.assets[asset.aid].quantity += quantity
            self.transactions[asset.aid] = f"Bought {quantity} of {asset.aid} at price {asset.asset_price}$."
        else:
            print(f"Asset {asset.aid} not found in portfolio. Please add it first.")
        
