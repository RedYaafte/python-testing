import os, unittest

from faker import Faker

from src.user import User
from src.bank_account import BankAccount


class UserTests(unittest.TestCase):

    def setUp(self):
        self.faker = Faker(locale="es")
        self.user = User(
            name=self.faker.name(),
            email=self.faker.email(),
        )

    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(
            name=name_generated,
            email=email_generated,
        )

        self.assertEqual(user.name, name_generated)
        self.assertEqual(user.email, email_generated)
        self.assertIsNotNone(user)
        self.assertIsInstance(user, User)

    def test_user_with_multiple_accounts(self):

        for _ in range(3):
            bank_account = BankAccount(
                balance=self.faker.random_int(min=100, max=2000, step=50),
                log_file=self.faker.file_name(extension=".txt"),
            )
            self.user.add_account(bank_account)

        expected_value = self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(expected_value, value)

    def tearDown(self):
        for account in self.user.accounts:
            os.remove(account.log_file)
