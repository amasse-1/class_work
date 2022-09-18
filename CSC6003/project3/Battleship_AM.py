import random

"""
    -------BATTLESHIP-------
    Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
    How it will work:
    1. A 10x10 grid will have 5 ships randomly placed about
    2. You can choose a row and column to indicate where to shoot
    3. For every shot that hits or misses it will show up in the grid
    4. If all ships are shot, game over

    Legend:
    1. "." = water
    2. "S" = ship position
    3. "O" = water that was shot with bullet, a miss because it hit no ship
    4. "X" = ship sunk!
Class: CS6003 Foundations of Programming 1
Author: Anthony Masse (with help from GK)
Last Updated: 9/18/2022
Description: Battelship using 2 dimensional arrays

"""
# Global variable for grid size
grid_size=11
# Global variable for grid
grid = [ ['']*grid_size for i in range(grid_size) ]
# Global variable for number of ships to place
num_of_ships = 5

def drawBoard(myBoard):
# implement draw board here
        for i in range(0,grid_size):
            print(('+---+')*11)
            for j in range(0,grid_size):
                print('|', myBoard[i][j], end = ' |')
            print('\n'+('+---+')*11)
        return myBoard

def setupBoard(myBoard):
    # implement setup board here
    i = j = 0
    while i < grid_size:
        while j < grid_size:
            myBoard[0][j] = str(j-1) #I have to subtract 1 to get the 0-9 in the grid
            myBoard[i][0] = str(i-1) #I have to subtract 1 to get the 0-9 in the grid
            myBoard[i][j] = '.' # fill in empty spaces with '.'
            myBoard[0][0] = " " # have the top left corner be empty
            j += 1
        j = 0
        i += 1
    # now place the ships
    for i in range(0,num_of_ships):
        randomRow = random.randint(1, grid_size - 1) #to make sure the ships aren't being placed in the numbers
        randomCol = random.randint(1, grid_size - 1) #to make sure the ships aren't being placed in the numbers
        myBoard[randomRow][randomCol] = 'S' # where the random column and row are, place a ship or 'S'
    return myBoard

def hitOrMiss(myBoard, row, col):
    # implement the hit or miss functionality here
    if(myBoard[row][col] == 'S'): #if there is a ship, change it to X and print HIT
        myBoard[row][col] = 'X'
        print('HIT')
        return('HIT')
    elif(myBoard[row][col] == 'X'): # if there is already an X print HIT
        print('HIT')
        return('HIT')
    elif(myBoard[row][col] == '.'): # if there is not a ship, change to O and print MISS
        myBoard[row][col] = 'O'
        print('MISS')
        return('MISS')
    elif(myBoard[row][col] == 'O'): # if you already missed, print MISS
        print('MISS')
        return('MISS')

def isGameOver(myBoard):
    # check if there are ships remaining on the grid.
    # if there are ships remaining, return false else return true
    hit_count = 0 # the amount of hits on the board
    for i in range(0,grid_size):
        for j in range(0,grid_size):
            if(myBoard[i][j] == 'X'): 
                hit_count += 1
    if(hit_count == num_of_ships): # if the amount of hits equals the number of ships, the game ends
        return True
    elif(hit_count != num_of_ships): # if the amount of hits doesn't equals num_of_ships, game continues
        return False

def main(myBoard):
    # here do everything like  
    #   set up the board
    setupBoard(myBoard)
    #   till the game is over
    while(isGameOver(myBoard) != True):
    #     draw the board
        drawBoard(myBoard)
    #     ask for a row and column and check it is a hit or a miss
        col = int(eval(input('Enter a column(X): ')))
        col = col + 1 # to count for the grid layout
        if((col < 1) or (col > 10)): # to check for invalid columns
            print('Invalid column')
        row = int(eval(input('Enter a row(Y): ')))
        row = row + 1 # to count for the grid layout
        if((row < 1) or (row > 10)): # to check for invalid rows
            print('Invalid row')
        
        hitOrMiss(myBoard, row, col)
        # when the game is over, print that message!
    print('You win! Sunk all ships!')
    print('Game over!')
    
#to start the game
main(grid)
