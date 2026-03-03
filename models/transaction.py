class Transaction:
    def __init__(self, aid: str, date: str, transaction_type: str, quantity: int, price: float):
        self.aid = aid
        self.date = date
        self.transaction_type = transaction_type
        self.quantity = quantity
        self.price = price
        
    def transaction_process(self):
        if self.transaction_type == "BUY":
            print(f"Bought {self.quantity} of {self.aid} at {self.price} on {self.date}.")
            dict = {
                "aid": self.aid,
                "date": self.date,
                "transaction_type": self.transaction_type,
                "quantity": self.quantity,
                "price": self.price
            }
            return dict
        elif self.transaction_type == "SELL":
            print(f"Sold {self.quantity} of {self.aid} at {self.price} on {self.date}.")
            dict = {
                "aid": self.aid,
                "date": self.date,
                "transaction_type": self.transaction_type,
                "quantity": self.quantity,
                "price": self.price
            }
            return dict
        else:
            print("Invalid transaction type.")