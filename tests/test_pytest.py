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


def test_deposit_negative_amount(tear_down):
    account = BankAccount(balance=1000, log_file="transaction_logs.txt")
    with pytest.raises(ValueError):
        account.deposit(amount=-100)


@pytest.mark.parametrize(
    "initial_balance, deposit_amount, expected_result, expect_exception",
    [
        (1000, -100, None, ValueError),  # Negative deposit, should raise ValueError
        (1000, 0, None, ValueError),  # Zero deposit, should raise ValueError
        (1000, 100, 1100, None),  # Valid positive deposit
        (500, 50.5, 550.5, None),  # Valid positive deposit with float
    ],
)
def test_deposit_parametrized(
    initial_balance, deposit_amount, expected_result, expect_exception, tear_down
):
    account = BankAccount(balance=initial_balance, log_file="transaction_logs.txt")

    if expect_exception:
        with pytest.raises(expect_exception):
            account.deposit(deposit_amount)
    else:
        result = account.deposit(deposit_amount)
        assert result == expected_result
