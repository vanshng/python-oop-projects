class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"₹{amount} deposited successfully.")
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Current Balance: ₹{self.balance}")


account = BankAccount("Vansh", 1000)

account.display_balance()
account.deposit(200)
account.withdraw(600)

