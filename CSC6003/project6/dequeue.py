"""
Class: CS6003-Foundations of Programming 1

Programming Project 6: Dequeue in Python

Created: 10/5/2022
Updated: 10/6/2022

Author: Anthony Masse

"""

class Dequeue:
    def __doc__(self):
        """
        class name: Dequeue

        Methods
        --------------------------
        __init__ : initializes a 'dequeue' (A double ended queue) or an array in this case

        addFront : adds data to the front of the dequeue

        addBack : adds data to the back of the dequeue

        removeFront : removes the front most data item from the dequeue

        removeBack : removes the last data item from the dequeue

        isEmpty : determines if the dequeue is empty or not, made so no one can remove nothing

        display : displays the contents of the dequeue in numerical order
        
        """
    def __init__(self):
        self.dequeue = []

    def addFront(self, data):
        self.dequeue.insert(0, data)

    def addBack(self, data):
        self.dequeue.append(data)
    
    def removeFront(self):
        self.dequeue.pop(0)

    def removeBack(self):
        self.dequeue.pop()

    def isEmtpy(self):
        if(self.dequeue == []):
            return True
        else:
            return False

    def display(self):
        for i in range(0,len(self.dequeue)):
            print(i+1,"): " ,self.dequeue[i])

#main
def main():
    d = Dequeue()
    while (True):
        choice = input("Add or Remove?(Press x to exit): ")
        choice.upper()
        #gives user the choice to exit loop
        if(choice.upper() == "X"):
            break
        #adds data to the dequeue
        elif(choice.upper() == "ADD"):
            #gets data from user
            data = input("Please enter something to put into the front or back of the dequeue: ")
            #front or back of the dequeue
            fb = input("Would you like to add this to the front or the back of the dequeue?: ")
            #adds front
            if(fb.upper() == "FRONT"):
                d.addFront(data)
            #adds back
            elif(fb.upper() == "BACK"):
                d.addBack(data)
            else:
                print("That was not a valid answer. Please try again.")
        elif(choice.upper() == "REMOVE"):
            #makes sure its not empty
            if(d.isEmtpy() != True):
                #front or back of the dequeue
                fb = input("Would you like to remove from the front or the back of the dequeue?: ")
                if(fb.upper() == "FRONT"):
                    d.removeFront()
                elif(fb.upper() == "BACK"):
                    d.removeBack()
                else:
                    print("That was not a valid answer. Please try again.")
            #displays when empty
            else:
                print("The dequeue is empty please add before removing")
        else:
            print("That was not a valid answer. Please try again.")
        #after adding or removing the dequeue will be displayed
        d.display()

if __name__ == '__main__':
    main()