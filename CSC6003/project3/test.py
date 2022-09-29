from Battleship_AM import *
import unittest


class testBattelhsip(unittest.TestCase):
    def test_hitOrMiss(self):
        myBoard = setupBoard(grid)
        myBoard = drawBoard(grid)
        #creating a hit anmd a miss on the board
        myBoard[1][1] = 'X'
        myBoard[2][2] = 'O'
        #testing if function will return hit ot miss
        self.assertEqual(hitOrMiss(myBoard, 1, 1), 'HIT')
        self.assertEqual(hitOrMiss(myBoard, 2, 2), 'MISS')

    def test_setupBoard(self):
        setupBoard(grid)
        count = 0
        for i in range(1, grid_size):
            for j in range(1, grid_size):
                if(grid[i][j] == 'S'):
                    count +=1
        #num_of_ships is 5, which means the count should be 5
        self.assertEqual(count,num_of_ships)

        count = 0
        for i in range(1, grid_size):
            for j in range(1, grid_size):
                if(grid[i][j] == '.'):
                    count +=1
        #since there are 100 spots there should be 95 spots open
        self.assertEqual(count, 95)

    def test_isGameOver(self):
        #set up and draw board
        setupBoard(grid)
        drawBoard(grid)
        #There will be no 'X' only 'S' which means it will continue the game
        self.assertEqual(isGameOver(grid), False)
        #replacing the 'S' with 'X'
        for i in range(1, grid_size):
            for j in range(1, grid_size):
                if(grid[i][j] == 'S'):
                    grid[i][j] = 'X'
        #now that the 'X' have replaced the 'S', the game is over
        self.assertEqual(isGameOver(grid), True)

if __name__ == "__main__":
    unittest.main()
