  
from BankAccount import BankAccount

class user:
    def __init__(self,name,email): 
        self.name=name
        self.email=email
        self.account=BankAccount()
    def make_deposite (self, amount):
        self.account.deposit(amount)
    def make_withdrawal(self, amount=0):
        self.account.withdraw(amount) 
    def display_user_balance(self):
        print("User Name: "+self.name +", User Balance: ", end=" ")
        self.account.display_account_info()
    def transfer_money(self, other_user, amount):
        if self.make_withdrawal(amount):
            other_user.make_deposite(amount)
            return True
        return False    

sahar =user("sahar", "murrarsahar@gmail.com")
sahar.account.deposit(500)
sahar.display_user_balance()
sahar.account.display_account_info()
sireen = user("sireen", "user2@gmial.com")
sahar.transfer_money(momen, 400)

sahar.display_user_balance()
momen.display_user_balance()