class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        print(f"your balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"your balance is {self.balance}")



#user = Account(3000)

#user.withdraw(200)


