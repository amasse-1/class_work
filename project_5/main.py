from logic_project_5 import logic_project_5

#main class for user (user level)
def main():
    #our db and logic connection
    db = logic_project_5()

    #small intro
    print('Welcome to your FoodWeekly! Your favorite food app!')
    print("Now let's get started with your weekly meals:")

    while True:
        count = 0
        for i in db.weekdays.values():
            if (isinstance(i, int)):
                count += i

        if (count == 0):
            break
        else:
            #business logic functions
            cookbook = db.select_cookbook()
            recipe = db.select_recipe(cookbook)
            db.recipe_to_day(recipe)

    print('\nNow that we have your recipes for the week, here they are: ')
    for i, j in db.weekdays.items():
        print(f'\t- {i}: {j}')


    print('Finally, we have your meals for the week so here is your grocery list full of ingredients: ')
    for i in db.weekdays.values():
        db.needed_ingredients(i)
    for j in db.groceries:
        print(f'\t -{j}')

    print('Thank you!')
    db.close()
    



if __name__ == '__main__':
    main()
