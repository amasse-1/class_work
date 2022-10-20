class CoinCollector:

    # constructor so you cannot instantiate this class
    def __init__(self):
        pass

    def parseChange(coins):
        #starts at total
        total = 0

        coins = coins.upper()
        # implement parseChange here
        for i in coins:
            #pennies
            if(i == 'P'):
                total = total + 0.01
            #nickels
            elif(i == 'N'):
                total = total + 0.05
            #dimes
            elif(i == 'D'):
                total = total + 0.10
            #quarters
            elif(i == 'Q'):
                total = total + 0.25
            #half dollars
            elif(i == 'H'):
                total = total + 0.50
            #whole dollars
            elif(i == 'W'):
                total = total + 1.00
            else:
                #if there is invalid coins, print this
                print (f"Invalid coin: {i}")

        #returns total change in correct format
        return round(total,2)
    
