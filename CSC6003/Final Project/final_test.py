import unittest
from BankUtility import *
from CoinCollector import *
from Account import *
from Bank import *

class test_account(unittest.TestCase):
    def test_deposit(self): 
        a = Account()
        a.setBalance(10)
        self.assertEqual(a.getBalance(),10)
        a.deposit(10)
        self.assertEqual(a.getBalance(),20)

        b = Account()
        b.setBalance()
        b.deposit(10)
        self.assertEqual(b.getBalance(),10)
    
    def test_withdraw(self):
        a = Account()
        a.setBalance()
        self.assertEqual(a.getBalance(),0)
        a.deposit(10)
        self.assertEqual(a.getBalance(),10)
        a.withdraw(5)
        self.assertEqual(a.getBalance(),5)
        a.withdraw(1.55)
        self.assertEqual(a.getBalance(), 3.45)

        b = Account()
        b.setBalance()
        b.deposit(100)
        b.withdraw(99.99)
        self.assertEqual(b.getBalance(), 0.01)

    def test_isValidPin(self):
        a = Account()
        a.setPin('1234')
        self.assertFalse(a.isValidPIN('4321'))
        self.assertTrue(a.isValidPIN('1234'))

        b = Account()
        b.setPin('3212')
        self.assertFalse(b.isValidPIN('1111'))
        self.assertFalse(b.isValidPIN('3211'))
        self.assertTrue(b.isValidPIN('3212'))

class test_CoinCollector(unittest.TestCase):
    def test_parseChange(self):
        cc = CoinCollector.parseChange('PPP')
        self.assertEqual(cc, 0.03)

        cc2 = CoinCollector.parseChange('WWWHXPPPPP')
        self.assertEqual(cc2, 3.55)

        cc3 = CoinCollector.parseChange('PNDQHWX')
        self.assertEqual(cc3, 1.91)

class test_BankUtility(unittest.TestCase):
    def test_isNumeric(self):
        self.assertFalse(BankUtility.isNumeric('Hello World'))
        self.assertTrue(BankUtility.isNumeric('12'))

    def test_generateRandomInteger(self):
        x = BankUtility.generateRandomInteger(0,5)
        self.assertLessEqual(x,5)
        self.assertGreaterEqual(x,0)

        y = BankUtility.generateRandomInteger(0,100)
        self.assertLessEqual(y,100)
        self.assertGreaterEqual(y,0)

    def test_convertFromDollarsToCents(self):
        cents = BankUtility.convertFromDollarsToCents(22.50)
        self.assertEqual(cents, 2250)

        cents2 = BankUtility.convertFromDollarsToCents(31.52)
        self.assertEqual(cents2, 3152)

        cents3 = BankUtility.convertFromDollarsToCents(0.52)
        self.assertEqual(cents3, 52)

class test_Bank(unittest.TestCase):
    def test_addAccountToBank(self):
        a = Account()
        a.setAccountNumber()
        a.setBalance(100)
        a.setFirstName('Bob')
        a.setLastName('Smith')
        a.setPin('1234')
        a.setSSN('000000000')
        self.assertTrue(Bank.addAccountToBank(self, a))

        b = Account()
        b.setAccountNumber()
        b.setBalance(10)
        b.setFirstName('Jane')
        b.setLastName('Smith')
        b.setPin('4321')
        b.setSSN('000000001')
        self.assertTrue(Bank.addAccountToBank(self, b)) 

        Bank.max_accounts = 2

        c = Account()
        c.setAccountNumber()
        c.setBalance(10)
        c.setFirstName('Will')
        c.setLastName('Jackson')
        c.setPin('1111')
        c.setSSN('000000002')
        self.assertFalse(Bank.addAccountToBank(self, c)) 

    def test_removeAccountToBank(self):
        Bank.max_accounts = 100

        a = Account()
        a.setAccountNumber('20000000')
        a.setBalance(100)
        a.setFirstName('Bob')
        a.setLastName('Smith')
        a.setPin('1234')
        a.setSSN('000000000')
        Bank.addAccountToBank(self, a)

        b = Account()
        b.setAccountNumber('10000000')
        b.setBalance(100)
        b.setFirstName('Jane')
        b.setLastName('Smith')
        b.setPin('4321')
        b.setSSN('000000001')
        Bank.addAccountToBank(self, b)
        self.assertTrue(Bank.removeAccountFromBank(self, a))
        self.assertTrue(Bank.removeAccountFromBank(self, b))

        c = Account()
        c.setAccountNumber('30000000')
        c.setBalance(10)
        c.setFirstName('Will')
        c.setLastName('Jackson')
        c.setPin('1111')
        c.setSSN('000000002')
        self.assertFalse(Bank.removeAccountFromBank(self, c))

    def test_findAccount(self):
        a = Account()
        a.setAccountNumber()
        a.setBalance(100)
        a.setFirstName('Bob')
        a.setLastName('Smith')
        a.setPin('1234')
        a.setSSN('000000000')
        Bank.addAccountToBank(self, a)

        b = Account()
        b.setAccountNumber('54332123')
        b.setBalance(200)
        b.setFirstName('Jane')
        b.setLastName('Smith')
        b.setPin('4321')
        b.setSSN('000000001')
        self.assertIsInstance(Bank.findAccount(self, a.getAccountNumber()), Account)
        self.assertIsNone(Bank.findAccount(self, '54332123'))

    def test_addMonthlyInterest(self):
        Bank.max_accounts = 100
        a = Account()
        a.setAccountNumber()
        a.setBalance(100)
        a.setFirstName('Bob')
        a.setLastName('Smith')
        a.setPin('1234')
        a.setSSN('000000000')
        Bank.addAccountToBank(self,  a)

        b = Account()
        b.setAccountNumber()
        b.setBalance(200)
        b.setFirstName('Jane')
        b.setLastName('Smith')
        b.setPin('4321')
        b.setSSN('000000001')
        Bank.addAccountToBank(self, b)

        Bank.addMonthlyInterest(self, 2.5)
        self.assertEqual(a.getBalance(), 100.21)
        self.assertEqual(b.getBalance(), 200.42)

        

def main():
    test_account.test_deposit()
    test_account.test_withdraw()
    test_account.test_isValidPin()
    test_CoinCollector.test_parseChange()
    test_BankUtility.test_isNumeric()
    test_BankUtility.test_generateRandomInteger()
    test_BankUtility.test_convertFromDollarsToCents()
    test_Bank.test_addAccountToBank()
    test_Bank.test_removeAccountToBank()
    test_Bank.test_findAccount()
    test_Bank.test_addMonthlyInterest()
    

if __name__ == '__main__':
    unittest.main()
