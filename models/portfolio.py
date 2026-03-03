class Portfolio:
    def __init__(self, p_name: str):
        self.name = p_name
        self.assets = {}
        self.transactions = []

    def add_asset(self, asset: Asset):
        self.assets[asset.aid] = f"{asset.quantity} at {asset.avg_cost}$"
        self.transactions.append(f"Added asset {asset.aid} with quantity {asset.quantity} at average cost {asset.avg_cost}$.")
