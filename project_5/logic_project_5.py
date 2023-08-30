from connect_project_5 import connect_project_5

#business logic level
class logic_project_5:
    def __init__(self):
        self.weekdays = {'Monday': 1, 'Tuesday': 1, 'Wednesday': 1, 'Thursday': 1, 'Friday': 1} #will update 
        self.db = connect_project_5()
        self.groceries = list()

    def select_cookbook(self):
        self.cookbooks = self.db.get_cookbooks() # list of cookbooks retreived from db
        count = 1
        #printing cook books to show the user. 
        for i in self.cookbooks:
            print(f'{count}: {i}')
            count+=1
        #get the cookbook from the user 
        num = int(input('\nPlease select the number of the cookbook you would like to use: '))

        #loop to make sure that the number is a valid number. 
        while True:
            if (num <= (len(self.cookbooks)+1)):
                break
            else:
                print('That is not a valid number. Please try again.')
        #returning the necessary cookbook
        return self.cookbooks[num-1]
    
    def select_recipe(self, cookbook):
        self.recipes = self.db.get_recipes(cookbook) # list of recipes retreived from db
        count = 1
        #printing recipes to show the user. 
        for i in self.recipes:
            print(f'{count}: {i}')
            count+=1
        #get the recipe from the user 
        num = int(input('\nPlease select the number of the recipe you would like to use: '))

        #loop to make sure that the number is a valid number. 
        while True:
            if (num <= (len(self.recipes)+1)):
                break
            else:
                print('That is not a valid number. Please try again.')
        #returning the necessary recipe
        return self.recipes[num-1]
    
    def needed_ingredients(self, recipe):
        self.ingredients = self.db.get_ingredients(recipe)
        #adding the ingredients to the grocery list if 
        for i in self.ingredients:
            if (i not in self.groceries):
                self.groceries.append(i)

    
    def recipe_to_day(self, recipe):
        count = 1
        #list the weekday for the user

        for i in self.weekdays.keys():
            if(self.weekdays[i] == 1):
                print(f'{count}: {i}')
            count+=1

        day = int(input('Which day would you like to have this recipe?: '))
        #make sure the day is a valid number
        while True:
            if (day <= (len(self.weekdays)+1)):
                break
            else:
                print('That is not a valid number. Please try again.')
        x = list(self.weekdays)[day-1] # gets the day
        self.weekdays[x] = recipe # sets the recipe
        print(f'{x} recipe is set') #lets the user know which day was set

    def close(self):
        self.db.close()