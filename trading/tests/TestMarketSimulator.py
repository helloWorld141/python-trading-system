import unittest
from trading.LiquidityProvider import LiquidityProvider

class TestMarketSimulator(unittest.TestCase):
    def setUp(self):
        self.liquidityProvider = LiquidityProvider()

    def testAddLiquidity(self):
        self.liquidityProvider.generateRandomOrder()
        self.assertEqual(self.liquidityProvider.orders[0]['id'], 0)
        self.assertEqual(self.liquidityProvider.orders[0]['side'], 'buy')
        self.assertEqual(self.liquidityProvider.orders[0]['quantity'], 700)
        self.assertEqual(self.liquidityProvider.orders[0]['price'], 11)

if __name__ == '__main__':
    unittest.main()