from dataclasses import dataclass


@dataclass
class BankAccount:
    balance: float = 0

    def deposit(self, amount: float) -> float:
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount > 0:
            self.balance -= amount
        return self.balance

    def get_balance(self) -> float:
        return self.balance
