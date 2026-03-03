class Asset:
    def __init__(self, aid: str, quantity: int, avg_cost: float):
        self.aid = aid
        self.quantity = quantity
        self.avg_cost = avg_cost

    def get_total_value(self) -> float:
        return self.quantity * self.avg_cost