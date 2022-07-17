class BankAccount:
    int_rate= 0.02
    balance= 0
    all_accounts= []

    def __init__(self, int_rate, balance):
        self.int_rate= int_rate
        self.balance= balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance= self.balance + amount
        return self

    def withdraw(self, amount):
        self.balance= self.balance - amount
        return self

    def display_account_info(self):
        print(f"Account Balance: ${self.balance}")
        return self

    def yield_interest(self):
        a_float= self.balance * self.int_rate
        import math
        print(f"Interest: ${math.ceil(a_float*100)/100}")
        return self
    
    @classmethod
    def account_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()

class SavingsAccount:
    int_rate= 0.02
    balance= 0
    all_accounts= []

    def __init__(self, int_rate, balance):
        self.int_rate= int_rate
        self.balance= balance
    
    def deposit(self, amount):
        self.balance= self.balance + amount
        return self

    def withdraw(self, amount):
        self.balance= self.balance - amount
        return self

    def display_account_info(self):
        print(f"Savings Account Balance: ${self.balance}")
        return self

    def yield_interest(self):
        a_float= self.balance * self.int_rate
        import math
        print(f"Interest: ${math.ceil(a_float*100)/100}")
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.savings= SavingsAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_deposit_savings(self, amount):
        self.savings.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def make_withdrawal_savings(self, amount):
        self.savings.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self
    
    def display_user_balance_savings(self):
        print(f"User: {self.name}")
        self.savings.display_account_info()
        return self
    
    def transfer_money(self, amount, other_user):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

angela = User("Angela Bereski", "angelakbereski@gmail.com")

angela.make_deposit(1000).make_withdrawal(40)

angela.display_user_balance()

angela.make_deposit_savings(4000).make_withdrawal_savings(90)

angela.display_user_balance_savings()

kyle = User("Kyle Ogilvie", "kogilvie686@gmail.com")

angela.transfer_money(50, kyle)