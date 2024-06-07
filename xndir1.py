#xndir_1 (Bank account)
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,x):
        self.balance += x
        return f"{self.account_holder}'s balance is {self.balance}"
    def withdraw(self,y):
        self.balance -= y
        return f"{self.account_holder}'s balance is {self.balance}"
    def get_balance(self):
        return self.balance
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance,interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def deposit(self, x):
        return super().deposit(x + self.interest_rate * x/100)
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance,overdraft_fee):
        super().__init__(account_holder, balance)
        self.overdraft_fee = overdraft_fee
    def withdraw(self, y):
        self.balance -= y
        if 0 > self.balance:
            y -= y * self.overdraft_fee/100
        return f"{self.account_holder}'s balance is {self.balance} withdrew ${y}"
account_1 = CheckingAccount("Ronaldo",150000,5)
print(account_1)
