from Account import *
from BankUtility import *

class Bank:
    
    accounts = list()
    max_accounts = 100
    accounts = [None] * max_accounts

    def addAccountToBank(self, account):
        
        # implement addAccountToBank here
        for i in range(0,Bank.max_accounts):
            if(Bank.accounts[i] == None ):
                Bank.accounts[i] = account
                return True
            elif(Bank.accounts[Bank.max_accounts-1] != None):
                print("No more accounts available")
                return False

    def removeAccountFromBank(self, account):

        # implement removeAccountFromBank here
        for i in range(0, Bank.max_accounts):
            #makes sure it is not none
            if(Bank.accounts[i] != None):
                #checks the accoun given with the account in the list
                if(Bank.accounts[i].getAccountNumber() == account.getAccountNumber()):
                    #remove at index i
                    Bank.accounts.pop(i)
                    return True
            else:
                return False
        

    
    def findAccount(self, accountNumber):
        
        for i in range(0, Bank.max_accounts):
            if(Bank.accounts[i] != None):
                if(Bank.accounts[i].getAccountNumber() == accountNumber):
                    return Bank.accounts[i]
            else:
                print(f'Account not found for account number: {accountNumber}')
                return None
    

    def addMonthlyInterest(self, percent):
        new_percent = percent / 100
        for i in range(0, Bank.max_accounts):
            if(Bank.accounts[i] != None):
                #calculates monthly interest
                mon_int = (Bank.accounts[i].getBalance() * (new_percent / 12))
                #deposits into the account
                Bank.accounts[i].deposit(mon_int)

    
    def _init__(self):
        pass
