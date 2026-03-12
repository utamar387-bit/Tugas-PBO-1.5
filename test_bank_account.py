import unittest
from bank_account import BankAccount

# KODE Python yang di uji
class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Ridho", 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 800)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_invalid_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_invalid_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

if __name__ == "__main__":
    unittest.main()