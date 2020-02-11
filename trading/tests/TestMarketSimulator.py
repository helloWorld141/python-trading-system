import unittest
from trading.LiquidityProvider import LiquidityProvider

class TestMarketSimulator(unittest.TestCase):
    def setUp(self):
        self.liquidityProvider = LiquidityProvider()

    def testAddLiquidity(self):
        pass

if __name__ == '__main__':
    unittest.main()