from random import seed
from trading.model.dto import Order
import random
import uuid
import copy

class LiquidityProvider(object):
    def __init__(self, lp_2_gateway=None):
        """
            @param lp_2_gateway : type collections.deque : push message to gateway
        """
        self.lp_2_gateway = lp_2_gateway
        self.orders: List[Order] = []
        seed(25)

    def generateRandomOrder(self):
        id = uuid.uuid1().int
        price = random.randint(8, 12)
        quantity = random.randint(1,10) * 100
        side = random.choice(['buy','sell'])
        action = random.choice(['modify', 'delete']) if self.lookupOrder(id) else 'new'

        order = Order(id, price, quantity, side, action)
        self.orders.append(order)

        if not self.lp_2_gateway:
            print('simulation mode')
            return order
        self.lp_2_gateway.append(copy.deepcopy(order))



    def lookupOrder(self, id: int):
        order = filter(lambda o: o.id == id, self.orders)
        return order

    def insertManualOrder(self, order: Order):
        pass
