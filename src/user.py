from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    email: str
    accounts: list = field(default_factory=list)

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        return sum(account.get_balance() for account in self.accounts)
