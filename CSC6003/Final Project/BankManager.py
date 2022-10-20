from Bank import *
from Account import *
from BankUtility import *
from CoinCollector import *


class BankManager:
    def __init__(self):
        bank = Bank()
        while True:
            option = input('''============================================================
                What do you want to do?
                1. Open an account
                2. Get account information and balance
                3. Change PIN
                4. Deposit money in account
                5. Transfer money between accounts
                6. Withdraw money from account
                7. ATM withdrawal
                8. Deposit change
                9. Close an account
                10. Add monthly interest to all accounts
                11. End Program
============================================================\nOption: ''')
            #opening an account
            if(option == '1'):
                print('OPEN ACCOUNT')
                new_account = Account()
                acc_first = BankUtility.promptUserForString('first name')
                acc_last = BankUtility.promptUserForString('last name')
                ssn = BankUtility.promptUserForString('ssn')

                acc_num = BankUtility.generateRandomInteger(10000000,99999999)
                for i in range(0, bank.max_accounts):
                    if(bank.accounts[i] != None):
                        if(str(acc_num) != bank.accounts[i].getAccountNumber()):
                            pass
                        else: 
                            acc_num = BankUtility.generateRandomInteger(10000000,99999999)

                new_account.setAccountNumber(str(acc_num))
                new_account.setFirstName(acc_first)
                new_account.setLastName(acc_last)
                new_account.setSSN(ssn)
                new_account.setPin()
                new_account.setBalance()
                bank.addAccountToBank(new_account)
                new_account.setPin(str(BankUtility.generateRandomInteger(1000,9999)))
                #prints account info
                print(new_account.__repr__())

            #get account info
            elif(option == '2'):
                acc = BankManager.promptForAccountNumberAndPIN(bank)
                if(acc != None):
                    print(acc)
            
            #change pin
            elif(option == '3'):
                acc = BankManager.promptForAccountNumberAndPIN(bank)
                x = True
                while x == True:
                    new_pin = BankUtility.promptUserForString('new pin')
                    if(new_pin.isdigit()):
                        if(int(new_pin) < 1000 or int(new_pin) > 9999):
                            print('New pin not four digits')
                        else:
                            confirm = input('Enter new PIN again to confirm:')
                            if(new_pin != confirm):
                                print('Pin does not match, try again!')
                            elif(new_pin == confirm):
                                acc.setPin(new_pin)
                                print('PIN updated')
                                x = False
                    elif(not new_pin.isdigit()):
                        print(f'{new_pin} is not a number')
                    

            #deposit money into the account
            elif(option == '4'):
                acc = BankManager.promptForAccountNumberAndPIN(bank)
                am = eval(input("Enter amount to deposit in dollars and cents (e.g. 2.57):\n"))
                acc.deposit(round(am,2))
                print(f'New balance: ${acc.getBalance()}')

            #transfer
            elif(option == '5'):
                print('Account to Transfer From:')
                acc1 = BankManager.promptForAccountNumberAndPIN(bank)
                if(isinstance(acc1, Account)):
                    print('Account to Transfer To:')
                    acc2 = BankManager.promptForAccountNumberAndPIN(bank)
                    if(isinstance(acc2, Account)):
                        tran = BankUtility.promptUserForString('transfer')
                        if(isinstance(tran, float)):
                            acc1.withdraw(tran)
                            acc2.deposit(tran)
                            print('Transfer Complete')
                print(f'Balance of Account: {acc1.getAccountNumber()} is: ${acc1.getBalance()}')
                print(f'Balance of Account: {acc2.getAccountNumber()} is: ${acc2.getBalance()}')
                
            #withdraw account
            elif(option == '6'):
                acc = BankManager.promptForAccountNumberAndPIN(bank)
                if(isinstance(acc, Account)):
                    a = BankUtility.promptUserForString('withdraw account')
                    w = round(float(a), 2)
                    acc.withdraw(w)
                    print(f'New Balance: ${acc.getBalance()}')
                
            #withdraw atm
            elif(option == '7'):
                acc = BankManager.promptForAccountNumberAndPIN(bank)
                if(isinstance(acc, Account)):
                    atm = BankUtility.promptUserForString('withdraw atm')
                    if(isinstance(atm, int)):
                        #above 20
                        if(atm >= 20):
                            twenty = int(input('Number of 20-dollar bills: '))
                            ten = int(input('Number of 10-dollar bills: '))
                            fives = int(input('Number of 5-dollar bills:'))
                            total = (twenty * 20) + (ten * 10) + (fives * 5)
                            if(total == atm):
                                acc.withdraw(atm)
                                print(f'New Balance: ${acc.getBalance()}')
                            else:
                                print('Invalid Bills')
                        #above 10
                        elif((not (atm >= 20)) and (atm >= 10)):
                            ten = int(input('Number of 10-dollar bills: '))
                            fives = int(input('Number of 5-dollar bills:'))
                            total = (ten * 10) + (fives * 5)
                            if(total == atm):
                                acc.withdraw(atm)
                                print(f'New Balance: ${acc.getBalance()}')
                            else:
                                print('Invalid Bills')
                        #equal to 5
                        elif(atm == 5 ):
                            acc.withdraw(atm)
                            print(f'New Balance: ${acc.getBalance()}')
                        #less than 5
                        elif(atm < 5):
                            print("Invalid amount")

                    else:
                        print ("Invalid input")
            
            #adding coins to account
            elif(option == '8'):
                acc = BankManager.promptForAccountNumberAndPIN(bank)
                if(isinstance(acc, Account)):
                    coins = input('Deposit coins: ')
                    dep = CoinCollector.parseChange(coins)
                    acc.deposit(dep)
                    print(f'${dep} in coins deposited into account')
                    print(f'New balance: ${acc.getBalance()}')

            #close an account
            elif(option == '9'):
                acc = BankManager.promptForAccountNumberAndPIN(bank)
                if(isinstance(acc, Account)):
                    print(f'Account {acc.getAccountNumber()} has been closed')
                    bank.removeAccountFromBank(acc)

            #add interest
            elif(option == '10'):
                percent = eval(input('Enter annual interest rate percentage (e.g. 2.75 for 2.75%):\n'))
                bank.addMonthlyInterest(percent)
                for i in range(0, bank.max_accounts):
                    if(bank.accounts[i] != None):
                        print(f'Bank account number: {bank.accounts[i].getAccountNumber()} has gained monthly interest of {percent}%.')
                        print(f'New Balance is: ${bank.accounts[i].getBalance()}')
           
            #close
            elif(option == '11'):
                break
    @staticmethod    
    def promptForAccountNumberAndPIN(bank):
        
        # implement promptForAccountNumberAndPIN here
        acc_num = BankUtility.promptUserForString('account number')
        acc = bank.findAccount(acc_num)
        if(acc != None):
            pin = BankUtility.promptUserForString('pin')
        
            if(isinstance(acc, Account) and acc.isValidPIN(pin)):
                return acc
            elif(acc.isValidPIN(pin) == False):
                return "Invalid Pin"
            elif(acc == None):
                return print(f'Account not found for account number: {acc_num}')


if __name__ == '__main__':
    BankManager()
