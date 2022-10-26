#  Define a bank Account class 

from unicodedata import name


class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = amount + self.balance
        print(f'Amount deposited: {amount} new balance: ${self.balance}')

myAccount = BankAccount('Edith','0001', 100)

myAccount.deposit(50)