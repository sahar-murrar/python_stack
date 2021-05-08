class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            return True
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
            return False

    def display_account_info(self):
        print("Balance: "+ str(self.balance))

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate   * self.balance

if __name__ == "__main__":

    sahar = BankAccount(30, 5000)
    sireen = BankAccount(20, 3500)
    # making 3 despoites and 1 withdraw for the first user
    sahar.deposit(100)
    sahar.deposit(1050)
    sahar.deposit(70)

    sahar.withdraw (300)
    sahar.yield_interest()
    sahar.display_account_info()

    # making 2 despoites and 4 withdraw for the second user
    sireen.deposit(2400)
    sireen.deposit(50)

    sireen.withdraw(100) 
    sireen.withdraw(10)  
    sireen.withdraw(1000)
    sireen.withdraw(890)         
    sireen.yield_interest()
    sireen.display_account_info()   





