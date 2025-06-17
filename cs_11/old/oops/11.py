# Practice Program : G
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Current Balance: ${self.balance}")

# Test the class
account = BankAccount("12345678", 500)
account.deposit(200)
account.withdraw(100)
account.display_balance()
