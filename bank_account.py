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

    def add_interest(self):
        monthly_interest_rate = 0.00083
        interest = self.balance * monthly_interest_rate
        self.balance += interest
        
    def print_statement(self):
        print(f'{self.full_name}\nAccount No.: ****{self.account_number[4:]}\nBalance: ${self.balance}')
        


liz_account = BankAccount('Liz Truss','00123457', 1500)
rishi_account = BankAccount('Rishi Sunak','88978432', 1600)
royal_account = BankAccount('Charles III','74212378', 5000)

liz_account.deposit(1500)
royal_account.withdraw(500)
rishi_account.print_statement()
liz_account.add_interest()
liz_account.get_balance()