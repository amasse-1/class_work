from connect_project_7 import connect_project_7

#business logic level
class logic_project_7:
    def __init__(self):
        self.db = connect_project_7()

    def printFamily(self):
        members = self.db.get_family_members()
        count = 1
        for i in members:
            print(f'{count}.) {i}')
            count += 1

    def printAllTasks(self, member):
                tasks = self.db.get_Tasks(member)
                print(f"{member}'s Tasks:")
                for j in tasks:
                    print(f'   - {j}')

    def printMemberDueDates(self, member):
        duedates = self.db.get_DueDate(member)
        print(f"{member}'s upcoming Due Dates:")
        for j in duedates:
            print(f'   - {j}')

    def close(self):
        self.db.close()