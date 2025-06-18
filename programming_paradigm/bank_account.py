class BankAccount:
    _shared_balance =None # to be modified by instance method

    def __init__(self,account_balance=0):
        if BankAccount._shared_balance is None:
            BankAccount._shared_balance = account_balance
        
    
    def deposit(self, amount):
        BankAccount._shared_balance +=amount
        #self.account_balance=BankAccount._shared_balance
            
    def withdraw(self, amount):
        if BankAccount._shared_balance>= amount:
            BankAccount._shared_balance-= amount
            #self.account_balance = BankAccount._shared_balance
            return True
        return False    
    
    def display_balance(self):
        print(f'Current Balance: ${BankAccount._shared_balance}')