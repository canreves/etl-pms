class Asset:
    def __init__(self, aid: str, asset_price: float, quantity: int):
        self.aid = aid
        self.asset_price = asset_price
        self.quantity = quantity
        
    def get_asset_value(self) -> float:
        return self.asset_price * self.quantity
    
    def update_price(self, new_price: float):
        self.asset_price = new_price