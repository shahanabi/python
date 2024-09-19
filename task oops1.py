class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}. New balance: {self._balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew: {amount}. New balance: {self._balance}.")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return f"Current balance: {self._balance}"

# Example usage:
account = BankAccount("Anand", 2000)
print(account.check_balance())  
account.deposit(1000)             
account.withdraw(500)            
print(account.check_balance())  
