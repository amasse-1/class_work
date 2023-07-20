'''
Project 7
-- version: 2.0
-- Author: GK
-- Edited by: Anthony Masse
'''

import random

def guess():
    '''Returns a random integer between 2 and 5000.'''
    return random.randint(2, 5000)

def isPrime(x):
    '''Returns True or False based on if the number x is a prime or not. '''
    #Edited to create a faster use rather than checking every individual number from 0 to x.
    if(x > 1):
        #if greater than 1, from 2 to 
        for i in range(2, int(x/2)+1):
            if(x % i) == 0:
                #if there is no remainder return false
                return False
            else:
                #else if there is a remainder return True
                return True

def findPrimes(num):
    primes = []
    for i in range(num):
        p = guess()
        while not isPrime(p):
            p = guess()
        primes += [p]
    return primes

import cProfile
cProfile.run('print(findPrimes(500)[:10])')

