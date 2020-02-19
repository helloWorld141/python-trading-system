class Order(object):
    def __init__(self, id: int, price: int, quantity: int, side: str, action: str):
        self.id = id
        self.price = price
        self.quantity = quantity
        self.side = side
        self.action = action