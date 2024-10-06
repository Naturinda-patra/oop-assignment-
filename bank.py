class BankAccount:
    # Class variable for interest rate
    interest_rate = 0.05

    def __init__(self, account_holder):
        # Instance variables
        self.account_holder = account_holder
        self.balance = 0.0

    # a method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {amount} into {self.account_holder}'s account.")

    # a method to withdraw money
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account.")
        else:
            print(f"Insufficient amount to withdraw {amount} from {self.account_holder}'s account.")

    # a method to apply interest to the balance
    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Applied interest to {self.account_holder}'s account. Interest: {interest}")

    # a method to display account information
    def display_account_info(self):
        print(f"Account holder: {self.account_holder}, Current balance: {self.balance}")

# BankAccount with different account holders
account1 = BankAccount("patrah")
account2 = BankAccount("clancie")

# deposits and withdrawals for patrah's account
account1.deposit(1000)
account1.withdraw(200)
account1.apply_interest()
account1.display_account_info()

# deposits and withdrawals for clancie's account
account2.deposit(1500)
account2.withdraw(300)
account2.apply_interest()
account2.display_account_info()
