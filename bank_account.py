#  Define a bank Account class 

from unicodedata import name


class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = amount + self.balance
        print(f'Amount deposited: {"{0:.2f}".format(amount)} new balance: ${"{0:.2f}".format(self.balance)}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds.')
            self.balance -= 10
        else:
            self.balance -= amount
            print(f'Amount withdrawn: ${"{0:.2f}".format(amount)} new balance: ${"{0:.2f}".format(self.balance)} ')
    def get_balance(self):
        print(f'Hello {self.full_name}, your account currently has a balance of: ${"{0:.2f}".format(self.balance)}. Have a wonderful day!')
        return self.balance
        

myAccount = BankAccount('Edith','0001', 100)

myAccount.deposit(50)
myAccount.withdraw(500)
myAccount.get_balance()