class Student:
    """Student Class
    
    Methods:
    ---------------------------------
    __init__ : constructer method for the student class

    display : display method to display the name and age of the student
    
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:", self.age)

class Engineer(Student):
    """
    Engineer Student class

    Parent class: 
    --------------
    Student 

    Methods:
    -------------------------------
    __init__ : uses __init__ from student class and adds a courses variable

    dislay : uses display method from student class and adds the display for the student courses
    """
    def __init__(self, name, age, courses):
        super().__init__(name, age)
        self.courses = courses
    
    def displayEngineer(self):
        super().display()
        for i in range(0,len(self.courses)):
            print("Course", i+1, ":",self.courses[i])

class Doctor(Student):
    """
    Student Doctor class

    Parent class:
    ---------------
    Student
    
    Methods:
    --------------------
    __init__ : uses __init__ from student class and adds a hospital variable

    dislay : uses display method from student class and adds the display for the student's hospital
    
    """
    def __init__(self, name, age, hospital):
        super().__init__(name, age)
        self.hospital = hospital
    
    def displayDoctor(self):
        super().display()
        print("Hospital:",self.hospital)

def main():
    #initialize the doctor and engineer student objects
    doc = Doctor("Jane", "32", "MGH")
    eng = Engineer("Sam", "22", ["Python 101", "Java 102", "SQL 200"])

    #displays the doctors atrributes
    doc.displayDoctor()
    #displays the engineers attributes
    eng.displayEngineer()

if __name__ == '__main__':
    main()