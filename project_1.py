import random #random mopdule

'''
Player and BoardGame classes Documented within this Project 1 Python File

@Author: Anthony Masse
'''
    
class Player():
    '''This is a player class used within the board game class'''

    def __init__(self, Name, health, attack, defense):
        '''Intialize new players with name, health, attack and defense values'''
        self.setName(Name)
        self.setHealth(health)
        self.setAttack(attack)
        self.setDefense(defense)
    
    def setName(self,Name):
        '''Set method for player name'''
        self.Name = Name

    
    def getName(self):
        '''Get method for player name'''
        return self.Name

    
    def setHealth(self,heatlh):
        '''Set method for player health'''
        self.Health = int(heatlh)
    
    
    def getHealth(self):
        '''Get method for player health'''
        if(self.Health < 0):
            print('Player has no more health points')
        else:
            return self.Health
    
    
    def setAttack(self,attack):
        '''Set method for player attack'''
        self.Attack = int(attack)
    
    
    def getAttack(self):
        '''Get method for player attack'''
        return self.Attack
    
    
    def setDefense(self,defense):
        '''Set method for player defense'''
        self.Defense = int(defense)
    
    
    def getDefense(self):
        '''Get method for player defense'''
        return self.Defense


class BoardGame():

    '''Class to initiate the board game and run the board game from start to end'''
    
    def start(self):
        '''Start Game Function'''
        print('Starting Game')


    def num_of_players(self,num):
        '''A function counts the number of players and returns the player count'''
        player_count = num
        return player_count
    

    def end(self):
        '''End Game Function'''
        print('Ending Game')


    def move(self,type = str, player1 = Player, player2 = Player):
        '''A function that uses move type (a string) and two players (from the Player class)'''
        if type == 'attack':
            #if type is attack then we determine the damage and player2's healthh points
            print(f'{player1.Name} attacked {player2.Name}')
            damage = random.randint(0,100)
            #If health is less than the damage, the player no longer has any health points
            if player2.getHealth() <= damage:
                print(f'{player2.Name} has no more life points')
            else:
                #if the health is greater than we can determine the damage to the player's health
                currentHealth = player2.getHealth()
                player2.setHealth((currentHealth - damage))
                print(f'{player2.Name}s health went down {damage} points to {player2.getHealth()}')


def main():
    '''Main Function for this program'''
    game = BoardGame() #the consturctor for the board game
    print(f'BoardGame class: \n\t{BoardGame.__doc__}\n')

    #Initiate Players
    print(f'Player class: \n\t{Player.__doc__}\n')
    player1 = Player(Name='Bob', health=100, attack=2, defense=3)
    player2 = Player(Name='Joe', health=100, attack=3, defense=1)
    
    game.start() #start game

    #Attack Moves
    game.move(type='attack', player1=player1, player2=player2)
    game.move(type='attack', player1=player2, player2=player1)


    game.end()#end game

if __name__ == '__main__':
    main()