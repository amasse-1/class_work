from random import randint

class BankUtility:
    
    def __init__(self):
        pass
        
    def promptUserForString(prompt):
        # for first name
        if(prompt == 'first name'):
            n_prompt = input("Enter Account Owner's First Name: ")
        #for last name
        elif(prompt == 'last name'):
            n_prompt = input("Enter Account Owner's Last Name: ")
        #for acc. number
        elif(prompt == 'account number'):
            n_prompt = input("Enter Account Number: ")
        #for ssn
        elif(prompt == 'ssn'):
            n_prompt = input("Enter Account Owner's SSN (9 digits): ")
        #for pin
        elif(prompt == 'pin'):
            n_prompt = input("Enter PIN: ")
        #for new pin
        elif(prompt == 'new pin'):
            n_prompt = input("Enter New PIN: ")
        #for deposit
        elif(prompt == 'deposit'):
            n_prompt = input("Enter amount to deposit in dollars and cents (e.g. 2.57): ")
        #for transfer
        elif(prompt == 'transfer'):
            n_prompt = float(input("Enter amount to transfer in dollars and cents (e.g. 2.57): "))
        #for account withdrawal
        elif(prompt == 'withdraw account'):
            n_prompt = input("Enter amount to withdraw in dollars and cents (e.g. 2.57): ")
        #for atm withdrawal
        elif(prompt == 'withdraw atm'):
            n_prompt = int(input("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000): "))
        #for coins
        elif(prompt == 'coins'):
            n_prompt = input("Deposit Coins: ")
            
        return n_prompt 

    def promptUserForPositiveNumber(prompt):
        # implement promptUserForPositiveNumber here
        if(prompt == 'pos'): #gets the prompt
            while True: #loops until positive
                pos = eval(input("Enter a number (e.g. 2.57): ")) #user input
                if(isinstance(pos, float)): #checks to make sure it is a valid number
                    if(pos <= 0):
                        print("Amount cannot be negative. Try again!") #no negatives here
                    else:
                        break #breaks when positive
                else:
                    print("Not a valid number. Try again!")
                
        return pos #returns positive number
    
    def generateRandomInteger(min, max):
        # generates random number between min and max amount
        gen = randint(min, max)
        
        return gen # returns random number
    
    def convertFromDollarsToCents(amount):        
        # implement convertFromDollarsToCents here
        amount = '{:,.2f}'.format(amount)
        #gets rid of decimal point
        tmp = amount.replace('.', '')

        #amount in cents
        amount_cents = int(tmp)

        return amount_cents #returns cents

    
    '''
      Checks if a given string is a number (long)
      This does NOT handle decimals.
      
      YOU DO NOT NEED TO CHANGE THIS METHOD
      THIS IS FREE FOR YOU TO USE AS NEEDED
      
      @param numberToCheck String to check
      @return true if the String is a number, false otherwise
     '''
    def isNumeric(numberToCheck):
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False
