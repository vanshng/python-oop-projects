class ATM:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        print("\n---------------------------------------------")
        print(f"Account Holder : {self.account_holder}")
        print(f"Current Balance : ₹{self.balance}")
        print("---------------------------------------------")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Amount!")
            return

        self.balance += amount
        print(f"\nAmount ₹{amount} deposited successfully.")
        print(f"Current Balance : ₹{self.balance}")
        print("---------------------------------------------")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Amount!")

        elif amount > self.balance:
            print("Insufficient Balance!")

        else:
            self.balance -= amount
            print(f"\nAmount ₹{amount} withdrawn successfully.")
            print(f"Current Balance : ₹{self.balance}")
            print("---------------------------------------------")



atm = ATM("Vansh", 4500)


while True:
    print("\n============= ATM =============")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amount = int(input("Enter Amount: ₹"))
        atm.deposit(amount)

    elif choice == 3:
        amount = int(input("Enter Amount: ₹"))
        atm.withdraw(amount)

    elif choice == 4:
        print("\nThank you for using the ATM!")
        break

    else:
        print("Invalid Choice! Please try again.")