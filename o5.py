class BankAccount:
    def __init__(self,acc_num,acc_hol,acc_bal):
        self.account_number = acc_num
        self.account_holder_name = acc_hol
        self.account_balance = acc_bal

    def deposit(self,amo_unt):
        self.d_amount = amo_unt
        self.account_balance = self.d_amount + self.account_balance
        return f"Amount added to the balance. Total Balance : {self.account_balance}"
    
    def withdraw(self,amo_unt):
        self.w_amount = amo_unt
        self.account_balance = self.account_balance - self.w_amount
        if self.account_balance < 0:
            return "insufficient balance"
        else:
            return f"Amount deducted from account. Total Balance : {self.account_balance}"
    
    def get_balance(self):
        if self.account_balance < 0:
            return "Insufficient Balance"
        else:
            return f"Total Balance : {self.account_balance}"
    
account = BankAccount("123","abc",0)
print(account.deposit(1000))
print(account.withdraw(1005))
print(account.get_balance())