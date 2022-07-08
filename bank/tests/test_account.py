import unittest
from bank.account import Account
from bank.client import Client

class TestAccount(unittest.TestCase):
    
    # fixture == resources nécessaire au test
    def setUp(self):
        self.client = Client(1)
        self.account = Account(1, self.client)
    
    # def testOverdraft(self):
    #     self.account.withdraw(600)
    #     self.assertTrue(self.account.overdraft)
    
    def testBalance(self):
        self.assertEqual(500.00, self.account.getBalance())
    
    def tearDown(self) -> None:
        del self.client
        del self.account
    
if __name__ == "__main__":
    unittest.main()