class BankAccount:
    def __init__(self,balance):
        self._balance = balance

    def deposit(self,amount):
        self.amount = amount
        self._balance = self.amount + self._balance
    
    def withdraw(self, amount):
        self.amount = amount
        if self._balance >= self.amount:
            self._balance = self._balance - self.amount
        else:
            print('insufficient balance')
        
    def get_balance(self):
        return f"balance in account: {self._balance}"
    
acc = BankAccount(1000)
print(acc.get_balance())
acc.withdraw(700)
print(acc.get_balance())
acc.withdraw(300)
print(acc.get_balance())
acc.withdraw(30)