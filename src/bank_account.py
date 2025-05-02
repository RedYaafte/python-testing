from dataclasses import dataclass


@dataclass
class BankAccount:
    balance: float = 0
    log_file: str = None

    def __post_init__(self):
        self._log_transaction("Create account.")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount: float) -> float:
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}, New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance

    def get_balance(self) -> float:
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance
