class BankAccount:
    def __init__(self, accountNumber, balance, password):
        self.accountNumber = accountNumber
        self._balance = balance  
        self.__password = password
    
    def get_balance(self):    
        return self._balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            raise ValueError("Balance cannot be negative")
    
    def get_password(self):
        return self.__password
    
    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
        else:
            raise ValueError("Password must be at least 8 characters long")
    
    class SavingsAccount:
        def __init__(self,accountNumber, balance, password):
            super().__init__(accountNumber, balance, password)
            
        def display_info(self):
            print(f"Balance: {self.get_balance()}")
            print(f"password: {self.get_password()}")
            
    
account = BankAccount(123456, 1000, "securepassword")
print(f"AccountNumber: {account.accountNumber}")

print("Balance (via getter):", account.get_balance())
print("Password (via getter):", account.get_password())
account.set_balance(1500)  
account.set_password("newsecurepassword")  
            
     
#it's nesseccary to use getter and setter when an attribute is private otherwise it's not possible to access