# Create a BankAccount class with the following attributes:
# balance and account_number. The class should also have the
# following methods: deposit(amount), withdraw(amount), and info().

class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def info(self):
        return f"Account number: {self.account_number}\nBalance: {self.balance}"


account1 = BankAccount(100, 123456)
account1.deposit(25)
print(account1.info())

account1.withdraw(50)
print(account1.info())


