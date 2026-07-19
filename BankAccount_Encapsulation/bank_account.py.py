class BankAccount:
    def __init__(self):
        self.__balance = 5000

    def get_balance(self):
        return self.__balance

    def set_balance(self,amount):
        if  amount >= 0 :
            self.__balance = amount
            print("Balance Updated Successfully!")

        else:
            print("Invalid Balance!")
           

account = BankAccount()


while True:
    print("\n===== Bank Account Menu =====")
    print("1. Check Balance")
    print("2. Update Balance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Current Balance: ₹{account.get_balance()}")

    elif choice == "2":
        amount = float(input("Enter New Balance: "))
        account.set_balance(amount)

    elif choice == "3":
        print("Thank you for using Bank Account System!")
        break

    else:
        print("Invalid Choice! Please try again.")

