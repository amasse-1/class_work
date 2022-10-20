import math
from random import randint


class Account:
    
    # add methods as getters and setters for attributes
    def setAccountNumber(self, account_num = randint(10000000,99999999)):
        self.account_num = account_num
    def getAccountNumber(self):
        return self.account_num

    def setFirstName(self, first_name):
        self.first_name = first_name
    def getFirstName(self):
        return self.first_name

    def setLastName(self, last_name):
        self.last_name = last_name
    def getLastName(self):
        return self.last_name

    def setSSN(self, ssn):
        self.ssn = ssn
    def getSSN(self):
        return self.ssn

    def setPin(self, pin = randint(1000,9999)):
        self.pin = pin
    def getPin(self):
        return self.pin

    def setBalance(self, balance = 0):
        self.balance = balance
    def getBalance(self):
        return round(self.balance,2)
    

    def deposit(self,amount):
        # implement deposit here 
        balance = self.getBalance()
        if(balance >= 0):
            new_balance = balance + amount
        else:
            print("Invalid Amount! Try Again later!")
        self.setBalance(new_balance)

    
  
    def withdraw(self,amount):
        
        # implement withdraw here
        balance = self.getBalance()
        #checks to make sure the balance is not 0 and the amount is not more than the balance
        if(balance > 0 and amount <= balance):
            new_balance = balance - amount
            self.setBalance(new_balance)
        else:
            print("Invalid Amount! Try Again later!")
         
    
    
    def isValidPIN(self, pin):
        
        
        check = str(self.getPin())
        if(pin == check):
            return True
        else:
            return False 
    
    
    # all objects have a toString method - this indicates you are providing
    # your own version
    def __repr__(self):
        # converting to a correct currency format
        return """
        ==================================================
        Account Number: {0}\n
        Owner's First Name: {1}\n
        Owner's Last Name: {2}\n
        Owner's SSN: {3}\n
        PIN: {4}\n
        Balance: ${5}\n
        ==================================================""".format(self.getAccountNumber(), self.getFirstName(), self.getLastName(),
                                self.getSSN(), self.getPin(), self.getBalance())           
        
    def __init__(self):
        pass

