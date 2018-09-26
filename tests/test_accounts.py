import unittest
from src.accounts import accounts, add_account, login


class TestAccount(unittest.TestCase):

    # Tests for User Sign up
    def test_add_account(self):
        add_account("eddy wizzy", "geometric")
        self.assertIn("geometric", accounts)

    def test_missing_name_field(self):
        create_account = add_account("", "8")
        self.assertIn("Please fill missing fields", create_account)

    def test_missing_password_field(self):
        create_account = add_account("am cleaners", "")
        self.assertIn("Please fill missing fields", create_account)

    def test_name_exists(self):
        create_account = add_account("eddy wizzy", "geometric")
        self.assertIn('This name already exists', create_account)

    def test_passwords_exists(self):
        create_account = add_account("eddy", "geometric")
        self.assertIn("This password already exists", create_account)

    # Tests for Login
    def test_login(self):
        login_user = login("fahad makabugo", "geometric")
        self.assertTrue(login_user)

    def test_missing_name_field_login(self):
        login_user = login("", "geometric")
        self.assertIn("Please fill missing fields", login_user)

    def test_missing_password_field_password(self):
        login_user = login("eddy wizzy", "")
        self.assertIn("Please fill missing fields", login_user)

    def test_name_does_not_exist(self):
        login_user = login("emma", "geometric")
        self.assertIn('Name does not exist', login_user)

    def test_passwords_does_not_exist(self):
        login_user = login("eddy wizzy", "cruel")
        self.assertIn('Password does not exist', login_user)




