import os

import pytest

from src.bank_account import BankAccount


@pytest.fixture
def tear_down():
    yield
    print("tear down")
    if os.path.exists("transaction_logs.txt"):
        os.remove("transaction_logs.txt")


@pytest.mark.parametrize(
    "amount, expected_balance",
    [
        (100, 1100),
        (3000, 4000),
        (4500, 5500),
    ],
)
def test_deposit_multiple_ammounts(amount, expected_balance, tear_down):
    account = BankAccount(balance=1000, log_file="transaction_logs.txt")
    new_balance = account.deposit(amount=amount)
    assert new_balance == expected_balance
