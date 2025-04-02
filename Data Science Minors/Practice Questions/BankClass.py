class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount = 0):
        self.balance -= amount
        print()

    def deposit(self, amount = 0):
        self.balance += amount

account1 = BankAccount()
print(account1.balance)
account1.deposit(amount=100)
print(account1.balance)
account1.withdraw(amount=20)
print(account1.balance)
