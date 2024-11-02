class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds for this operation."):
        self.message = message
        super().__init__(self.message)

class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Cannot withdraw, balance is too low.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance is ${self.balance}.")

    def transfer_to(self, another_account, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Cannot transfer, balance is too low.")
        elif amount > 0:
            self.withdraw(amount)
            another_account.deposit(amount)
            print(f"Transferred ${amount} to account {another_account.account_number}.")
        else:
            print("Transfer amount must be positive.")

try:
    acc1 = BankAccount("Alice", "1001", 500)
    acc2 = BankAccount("Bob", "1002", 300)

    acc1.deposit(200)
    acc1.check_balance()
    acc1.withdraw(100)
    acc1.transfer_to(acc2, 300)
    acc1.check_balance()
    acc2.check_balance()
except InsufficientFundsError as e:
    print(e)
