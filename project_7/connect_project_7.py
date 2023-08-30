import mysql.connector
from os import system, name

#database level
class connect_project_7:
    def __init__(self):
        def clear():
            # for windows
            if name == 'nt':
                _ = system('cls')
 
            # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')
        
        user = 'root'
        password = input('Please enter root password: ')

        try:
            self.myDB = mysql.connector.connect(
                #host = host --> did not need host
                user = user,
                password = password,
                database = 'FamilyPlanning',
            )
            clear()
        except: 
            clear()
            raise Exception("Could not connect to database")  
        
    def get_cursor(self):
        return self.myDB.cursor()

    def get_family_members(self):
        self.family = list() #cookbook list object
        if(self.myDB.is_connected): # if the db is connected then continue
            family_cursor = self.myDB.cursor() #initiate cursor object
            family_cursor.execute('SELECT MemberName FROM Family;') #execute db query
            for c in family_cursor: 
                self.family.append(c[0])
            return self.family
        else:
            raise Exception("Could not connect to database") 
        


    def get_Tasks(self, member):
        self.tasks = list() # recipe list object
        if(self.myDB.is_connected): # if the db is connected then continue
            task_cursor = self.myDB.cursor() #initiate cursor object
            task_cursor.execute(f'call getTasks("{member}");') #execute db query
            for c in task_cursor: 
                self.tasks.append(c[0])
            return self.tasks
        else:
           raise Exception("Could not connect to database") 
    
    def get_DueDate(self, member):
        self.duedates = list() # recipe list object
        if(self.myDB.is_connected): # if the db is connected then continue
            due_date_cursor = self.myDB.cursor() #initiate cursor object
            due_date_cursor.execute(f'call getTaskDueDates("{member}");') #execute db query
            for c in due_date_cursor: 
                self.duedates.append(c[0])
            return self.duedates
        else:
            raise Exception("Could not connect to database") 

    def close(self):
        self.myDB.close()

