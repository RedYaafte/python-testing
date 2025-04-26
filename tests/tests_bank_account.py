import unittest

from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(balance=1000)

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500)

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)
