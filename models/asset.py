class Asset:
    def __init__(self, aid: str, asset_price: float, quantity: int):
        self.aid = aid
        self.asset_price = asset_price
        self.quantity = quantity