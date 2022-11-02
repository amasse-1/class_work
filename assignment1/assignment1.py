"""
Class: CSC6013 - Discrete Structures and Algorithms

Assignment: Programming Assignment 1

Author: Anthony Masse

Created: 10/25/2022

Updated: 10/25/2022 
"""
from linkedlist import LinkedList #I made a small edit for importing the LinkedList class

class project1:
    def main():
        #create empty list
        a = list()

        #read file and append to list
        data_file = open("data.txt", "r")
        for x in data_file:
            a.append(int(x))
        
        #close file    
        data_file.close()
        
        #sort the list
        a.sort()

        L = LinkedList()
        L.insertBeginning(a[0])
        for i in range(1, len(a)):
            L.insertCurrentNext(a[i])
            L.nextCurrent()
        #reset current for adding or removing
        L.resetCurrent()

        #while the user input is an integer
        while True:
            user = eval(input("Please enter an intger: "))
            if(isinstance(user, int)):
                break
            else:
                print("Input has to be an integer! Try again!")
        
        #loops through 
        while True:
            #if user is greater than the last number, adds it at the end
            if(user > L.Current.Data and L.Current.Next == None):
                L.insertCurrentNext(user)
                L.printList(f"{user} has been added to the Linked List")
                break
            #if the user input is the same as the data, it gets removed
            elif(user == L.Current.Next.Data):
                L.removeCurrentNext()
                L.printList(f"{user} is removed from the Linked List")
                break
            elif(user == L.Current.Data):
                L.removeBeginning()
                L.printList(f"{user} is removed from the Linked List")
                break
            #if the user is greater than the current number but is less than the next, add it in between
            elif(L.Current.Next.Data > user and user > L.Current.Data):
                L.insertCurrentNext(user)
                L.printList(f"{user} has been added to the Linked List")
                break
            #goes to the next node
            elif(user > L.Current.Next.Data):
                L.nextCurrent()
            
project1.main()