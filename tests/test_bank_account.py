import unittest, os
from unittest.mock import patch

from src.bank_account import BankAccount
from src.exceptions import WithdrawalTimeRestrictionError


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

    @patch("src.bank_account.datetime")
    def test_withdraw(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
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

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_outside_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 22
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    def test_deposit_multiple_ammounts(self):
        test_cases = [
            {"amount": 100, "expected_balance": 1100},
            {"amount": 3000, "expected_balance": 4000},
            {"amount": 4500, "expected_balance": 5500},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(
                    balance=1000, log_file="transaction_logs.txt"
                )
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected_balance"])
