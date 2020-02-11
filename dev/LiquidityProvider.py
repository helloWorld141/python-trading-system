class LiquidityProvider(object):
    def __init__(self, lp_2_gateway):
        """
            @param lp_2_gateway : type collections.deque : push message to gateway
        """        
        self.lp_2_gateway = lp_2_gateway