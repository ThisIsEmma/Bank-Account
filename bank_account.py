#  Define a bank Account class 

from random import randint

class BankAccount:
    def __init__(self, full_name, account_type, account_number = int(''.join([str(randint(0,9)) for i in range(8)])), balance = 0):
        self.full_name = full_name
        self.account_type = account_type
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = amount + self.balance
        print(f'Amount deposited: {"{0:.2f}".format(amount)} new balance: ${"{0:.2f}".format(self.balance)}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
            self.balance -= 10
            print('$10 overdraft fee applied to the account.')
        else:
            self.balance -= amount
            print(f'Amount withdrawn: ${"{0:.2f}".format(amount)} new balance: ${"{0:.2f}".format(self.balance)} ')

    def get_balance(self):
        print(f'Hello {self.full_name}, your account currently has a balance of: ${"{0:.2f}".format(self.balance)}. Have a wonderful day!')
        return self.balance

    def add_interest(self):
        if self.account_type == 'saving':
            monthly_interest_rate = 0.001 # Based on a yearly interest rate of 1.2%, monthly equal 0.1% or 0.001
            interest = round(self.balance * monthly_interest_rate, 2)
            self.balance += interest
            print(f'Added ${interest} interest to saving in {self.full_name} account')
        else:
            monthly_interest_rate = 0.00083 # Based on a yearly interest rate of 1%, monthly equal 0.083% or 0.00083
            interest = round(self.balance * monthly_interest_rate, 2)
            self.balance += interest
            print(f'Added ${interest} interest to checking in {self.full_name} account')
        
    def print_statement(self):
        print(f'{self.full_name}\nAccount No.: ****{str(self.account_number)[4:]}\nBalance: ${self.balance}')
        

# Create 3 different bank accounts examples:

liz_account = BankAccount('Liz Truss','checking')
rishi_account = BankAccount('Rishi Sunak','checking')
royal_account = BankAccount('Charles III', 'checking')

# Accounts using methods implemented above: 

liz_account.deposit(1500)
royal_account.withdraw(50) 
royal_account.deposit(60)
rishi_account.print_statement()
liz_account.add_interest()
liz_account.get_balance()

mitchell = BankAccount('mitchell', 'checking', account_number = '03141592') #assigned account # 03141592 per assignment requirement.
mitchell.deposit(400000)
mitchell.print_statement()
mitchell.add_interest()
mitchell.print_statement()
mitchell.withdraw(150)
mitchell.print_statement()

# Stretch challenge 

# Add attribute for saving account:

liz_account.account_type = 'saving'
liz_account.add_interest()

# Create a list called: bank. Add all of your accounts to bank: 

bank = [liz_account, royal_account, rishi_account, mitchell]

for accounts in bank:
    accounts.add_interest()

