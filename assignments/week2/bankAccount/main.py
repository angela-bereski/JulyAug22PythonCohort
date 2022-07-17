class BankAccount:
    int_rate= 0.01
    balance= 0

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
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        a_float= self.balance * self.int_rate
        import math
        print(f"Interest: ${math.ceil(a_float*100)/100}")
        return self

account_1= BankAccount(0.01, 0)
account_2= BankAccount(0.01, 0)

account_1.deposit(500).deposit(400).deposit(250).withdraw(300).yield_interest().display_account_info()

account_2.deposit(125).deposit(375).withdraw(55).withdraw(24).withdraw(12).withdraw(44.02).yield_interest().display_account_info()

