class user:
    def __init__(self,name,email,account_balance=0): #any parameter we didn't give it a defualt value it means that it is a mandatory and we should privide it when creating a new user, but if we give it a default value this means that it is optional and we don't have to give a value for it, if we didn't give it a value it will take the default one.
        self.name=name
        self.email=email
        self.account_balance=account_balance
    def make_deposite (self, amount):
        self.account_balance+=amount
        return self #in chaining we have to return self
    def make_withdrawal(self, amount=0):
        if amount <= self.account_balance:
            self.account_balance-=amount
            return self #in chaining we have to return self  
    def display_user_balance(self):
        print("User Name: "+self.name +", User Balance: "+ str(self.account_balance))
    def transfer_money(self, other_user, amount):
        if self.make_withdrawal(amount):
            other_user.make_deposite(amount)
            return True
        return False    

sahar =user("sahar", "murrarsahar@gmail.com", 1200)
sahar.make_deposite(100).make_deposite(200).make_deposite(300).make_withdrawal(50).display_user_balance() #this is called chaining which is keep attaching new method calls to the end of the previous one
momen = user("momen", "user2@gmial.com", 2000)
sahar.transfer_money(momen, 400)

sahar.display_user_balance()
momen.display_user_balance()