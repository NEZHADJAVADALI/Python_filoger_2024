class BankAccount:
    def __init__(self, accountNumber, balance, password):
        self.accountNumber = accountNumber
        self._balance = balance
        self.__password = password

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount > 0:
            self._balance = amount
        else:
            print("Invalid balance amount!")

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password


class SavingsAccount(BankAccount):
    def __int__(self, accountNumber, balance, password):
        super().__init__(accountNumber, balance, password)

    def access_balance_directly(self):
        try:
            return self._balance
        except AttributeError as e:
            print(f"Error: {e}")

    def access_password_directly(self):
        try:
            return self.__password
        except AttributeError as e:
            print(f"Error: {e}")

    def access_balance_via_getter(self):
        return self.get_balance()

    def access_password_via_getter(self):
        return self.get_password()


bank_account = BankAccount("123456789", 5000, "securepassword")
print(bank_account.accountNumber)

try:
    print(bank_account._balance)
except AttributeError as e:
    print(f"Error: {e}")

try:
    print(bank_account.__password)
except AttributeError as e:
    print(f"Error: {e}")

print(bank_account.get_password())
print(bank_account.get_password())

bank_account.set_balance(6000)
bank_account.set_balance("newsecurepass")

print(bank_account.get_balance())
print(bank_account.get_password())






