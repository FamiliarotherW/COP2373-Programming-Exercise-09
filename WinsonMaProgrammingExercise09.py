# WinsonMaProgrammingExercise9.py 

class BankAcct:
    #Representing a bank account

    def __init__(self, name, acct_num, amount, interest_rate):
        #BankAcct object
        self.name = name
        self.acct_num = acct_num
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        #Adjusts the interest rate
        self.interest_rate = new_rate

    def deposit(self, deposit_amount):
        #Deposits money
        if deposit_amount > 0:
            self.amount += deposit_amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, withdraw_amount):
        #Withdraws money 
        if 0 < withdraw_amount <= self.amount:
            self.amount -= withdraw_amount
        else:
            print("Insufficient funds.")

    def get_balance(self): 
        #Returns the current balance of the account
        return self.amount

    def calculate_interest(self, days):
        #Calculates interest 
        interest = self.amount * (self.interest_rate / 365) * days
        return interest

    def __str__(self):
        #Returns a string representation
        return f"Account: {self.acct_num}\nName: {self.name}\nBalance: ${self.amount:.2f}\nInterest Rate: {self.interest_rate:.2%}"

def test_bank_acct():
    #Tests 
    account = BankAcct("Winson", "0001", 500.00, 0.03)
    print(account)

    account.deposit(200.00)
    print(f"Balance after deposit: ${account.get_balance():.2f}") 

    account.withdraw(100.00)
    print(f"Balance after withdrawal: ${account.get_balance():.2f}") 

    account.adjust_interest_rate(0.04)
    print(f"New interest rate: {account.interest_rate:.2%}")

    interest = account.calculate_interest(60)
    print(f"Interest earned: ${interest:.2f}")

if __name__ == "__main__":
    test_bank_acct()