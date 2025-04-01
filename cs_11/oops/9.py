# Practice Question : C

class BankAccount:
    def __init__(self, account_number, account_holder_name):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount:.2f}. Current balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount:.2f}. Current balance: ₹{self.balance:.2f}")

    def get_balance(self):
        return self.balance

account = BankAccount("1234567890", "Ram Balram")
print(f"Initial balance: ₹{account.get_balance():.2f}")
account.deposit(1000.0)
account.withdraw(500.0)
account.withdraw(600.0)  # Insufficient balance