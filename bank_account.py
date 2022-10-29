#  Define a bank Account class 

from unicodedata import name


class BankAccount:
    def __init__(self, full_name, account_type, account_number, balance):
        self.full_name = full_name
        self.account_type = account_type
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

    def add_interest(self):
        if self.account_type == 'saving':
            monthly_interest_rate = 0.001
            interest = self.balance * monthly_interest_rate
            self.balance += interest
            print('added interest to saving')
        else:
            monthly_interest_rate = 0.00083
            interest = self.balance * monthly_interest_rate
            self.balance += interest
            print('added interest to checking')
        
    def print_statement(self):
        print(f'{self.full_name}\nAccount No.: ****{self.account_number[4:]}\nBalance: ${self.balance}')
        

# Create 3 different bank account examples:

liz_account = BankAccount('Liz Truss','checking', '00123457', 1500)
rishi_account = BankAccount('Rishi Sunak','checking','88978432', 1600)
royal_account = BankAccount('Charles III', 'checking', '74212378', 5000)

# Accounts using methods implemented above: 

liz_account.deposit(1500)
royal_account.withdraw(500)
rishi_account.print_statement()
liz_account.add_interest()
liz_account.get_balance()

mitchell = BankAccount('mitchell', 'checking', '03141592', 0)
mitchell.deposit(400000)
mitchell.print_statement()
mitchell.add_interest()
mitchell.print_statement()
mitchell.withdraw(150)
mitchell.print_statement()

# Stretch challenge - Add attribute for saving account:

liz_account.account_type = 'saving'
liz_account.add_interest()

