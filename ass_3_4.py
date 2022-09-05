# Create a BankAccount class
# It should have similar attributes of a conventional bank
# It should have methods that implement the deposit and withdrawal functionality of a bank account

class BankAccount:
    Min_balance = 1000

    def __init__(self, account_name, account_number, account_balance):
     self.account_name = account_name
     self.account_number = account_number
     if account_balance<=BankAccount.Min_balance:
        self.account_balance=account_balance
     else:
        self.account_balance = BankAccount.Min_balance

    def Deposit(self):
        amount=float(input("enter the amount you would like to deposit: "))
        self.account_balance += amount
        print("Another money just land your account: ", amount)
        print("\n the total money wey you get now with us na: ", self.account_balance)

    def Withdrawal(self):
        amount = float(input("Enter amount to be Withdrawn from your account: "))
        if self.account_balance>=amount:
            self.account_balance-=amount
            print("\n You just commot:", amount, "from your accnt:")
        else:
            print("\n Insufficient balance  ")
 
eniola_account = BankAccount(account_name= "Eniola Osadare", account_number=9875236200, account_balance=2000)

print("Your balance is", eniola_account.Min_balance)

eniola_account.Deposit()
eniola_account.Withdrawal()

