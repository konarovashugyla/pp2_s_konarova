'''
Create a bank account class that has attributes owner, balance and two methods
deposit and withdraw. Withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test
to make sure the account can't be overdrawn.
'''
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.current = 0
    
    def deposit(self, money):
        self.current = self.current+ money
        print(f"Your current deposit is {money} tenge")
    
    def withdraw(self, money):
        self.current -= money
        if self.current>=0:
            print(f"You took {money} tenge ")
        else:
            print(f" Money is not enough!")