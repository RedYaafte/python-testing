import unittest, os

from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(balance=1000, log_file="transaction_logs.txt")

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500)

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_logs.txt"))

    def test_count_transactions(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)
