"""
Class: CSC6013 - Discrete Structures and Algorithms

Assignment: Programming Assignment 2

Author: Anthony Masse

Created: 10/31/2022

Updated: 10/31/2022 
"""
from exampleDict import readPeople #to read the people in the data file
from linkedlist import LinkedList  #to use the linked list implementation
     
def stack():
    #read the file and puts them in a dictionary of "everyone"
    everyone = readPeople("people.csv")
    #create a linked list called stack (for our stack)
    stack = LinkedList()
    #inserts the names of the people in our stack
    for i in everyone.keys():
        #stacks add at the beginning
        stack.insertBeginning(everyone[i].getName())
        stack.nextCurrent()
    #while the stack is not empty
    while stack.Header is not None :
        length = stack.length()
        user = int(eval(input('Please input an integer 1 to 4: ')))
        if(user > 4 or user < 1):
            print("Invalid number, try again!")
            #added length in linked list
        elif(user > length):
            print(f"Please enter a number under or equal to {length}")
        
        else:
            for i in range(user):
                #removed from the beginning because stacks are last in first out
                x = stack.removeBeginning()
                #tells the user what has been removed aka the x amount of people removed
                print(f'{x} has been removed.')
                print('--------')
            if(stack.Header is not None):
                #tells what is the now first element in the stack
                print(f'-> {stack.Header.Data} is at the front of the stack')
                
            else:
                print("That is the end of the stack. Goodbye!")

stack()