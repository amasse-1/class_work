import mysql.connector
from os import system, name

#database level
class connect_project_5:
    def __init__(self):
        def clear():
            # for windows
            if name == 'nt':
                _ = system('cls')
 
            # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')
        
        #host = input('Please enter the host connection details: ') -> did not need to use host
        user = input('Please enter the user name: ')
        password = input('Please enter password: ')


        self.myDB = mysql.connector.connect(
            #host = host --> did not need host
            user = user,
            password = password,
            database = 'MealPlanning',
        )
        clear()

    def get_cookbooks(self):
        self.cookbooks = list() #cookbook list object
        if(self.myDB.is_connected): # if the db is connected then continue
            cursor = self.myDB.cursor() #initiate cursor object
            cursor.execute('select CookbookName from cookbook;') #execute db query
            for c in cursor: #loop to add cookbooks to a list
                self.cookbooks.append(c[0])
            return self.cookbooks
        else:
            print('Database not connected at this time. Try again later.')

        

    def get_recipes(self, cookbook_name):
        self.recipes = list() # recipe list object
        if(self.myDB.is_connected): # if the db is connected then continue
            cursor = self.myDB.cursor() #initiate cursor object
            cursor.execute(f'select RecipeName from recipe where CookbookName="{cookbook_name}";') #execute db query
            for c in cursor: #loop to add recipes to a list
                self.recipes.append(c[0])
            return self.recipes
        else:
            print('Database not connected at this time. Try again later.')
    

    def get_ingredients(self, recipe_name):
        self.ingredients = list() # ingredient list object
        if(self.myDB.is_connected): # if the db is connected then continue
            cursor = self.myDB.cursor() #initiate cursor object
            #execute db query 
            cursor.execute(f'''select i.IngredientName from meal m
	                        join ingredients i on i.id = m.IngredientId
	                        join recipe r on r.RecipeName = m.RecipeName
                            where r.RecipeName = "{recipe_name}"
	                        order by r.RecipeName, i.IngredientName;''')
            for c in cursor: #loop to add ingredients to a list
                self.ingredients.append(c[0])
            return self.ingredients
        else:
            print('Database not connected at this time. Try again later.')

    def close(self):
        self.myDB.close()
