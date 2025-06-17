from account import Account

class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self,balance)

    def withdraw(self, amount):
        if amount <= 10000:
            super().withdraw(amount)
        else:
            print("you have exceeded your limit")

    def deposit(self, amount):
        super().deposit(amount)


user = SavingsAccount(50000)

user.deposit(14000)