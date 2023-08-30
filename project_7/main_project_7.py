from logic_project_7 import logic_project_7

#main class for user (user level)
def main():
    #our db and logic connection
    db = logic_project_7()

    #small intro
    print('Welcome to Family Planning! To help you and your family take care of everyday tasks!')
    print("Now let's get started reviewing your taks")

    while True:
        print('Please review your options: ')
        print('\t 1. -> View Members of the Family.')
        print('\t 2. -> See if a family member has any tasks.')
        print('\t 3. -> See if someone has tasks that have due dates.')
        print('\t 4. -> to close out this application.')
        x = int(input("Choice?: "))

        if(x == 1):
            db.printFamily()
        elif(x == 2):
            member = input('Please enter the family members name: ')
            db.printAllTasks(member)
        elif(x == 3):
            member = input('Please enter the family members name: ')
            db.printMemberDueDates(member)
        elif(x == 4):
            print('Thank you!')
            break
        else:
            print('That is not an option, please try again')
        
    db.close()


if __name__ == '__main__':
    main()
