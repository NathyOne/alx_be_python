class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount: float):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount: float):
        if self.account_balance < amount:
            return print("insufficient balance")
        self.account_balance -= amount
        return self.account_balance

    def display_balance(self):
        print(f"current balance: {self.account_balance}")
