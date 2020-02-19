from random import seed
from trading.model.dto import Order

class LiquidityProvider(object):
    def __init__(self, lp_2_gateway=None):
        """
            @param lp_2_gateway : type collections.deque : push message to gateway
        """        
        self.lp_2_gateway = lp_2_gateway
        self.orders = []
        seed(25)

    def generateRandomOrder(self):
        #TODO
        pass

    def lookupOrder(self, id: int):
        #TODO
        pass

    def insertManualOrder(self, order: Order):
        #TODO
        pass
