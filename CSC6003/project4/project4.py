
class Rectangle:
    
    #__doc__ is used to we wont need any comments unless necessary
    def __doc__(self):
        """
        Name : Rectangle

        Description: This class is a Rectangle class.
        
        Methods
        ------------------

        __init__ : takes length and width to contruct a class object.

        perimeter : calculates the perimeter of a rectnagle based on length and width.

        area : calculates the area of a rectangle based on the width and length provided in 
        the __init__ method.

        display : prints out length, width, perimeter, and area

        """

    def __init__(self, length, width):
        """Contsturcter for Rectangle class"""    
        self.length = length
        self.width = width


    def perimeter(self):
        """calculates perimeter"""
        perimeter = 2*(self.length + self.width)
        return perimeter
    
    def area(self):
        """calculates area"""
        area = self.width * self.length
        return area

    def display(self):
        """displays necessary information for the user"""
        print("Length: ", self.length)
        print("Width: ", self.width)
        print("Perimeter: ", self.perimeter())
        print("Area: ", self.area())

class Parallepiped(Rectangle):

    #__doc__ is used to we wont need any comments unless necessary
    def __doc__(self):
        """Name : Parallepiped
        
        Description: This is a Parallepiped class.
        
        Parent class : Rectangle

        Methods
        -----------------------
        __init__ : constructor method takes height, length, and width, all of int types

        volume : determines the volume of the parallepiped with height and the rectangle 
        class area method  

        display : prints height and volume of a parallepiped along with the parent class display
        """

    def __init__(self, height, length, width):
        """Contsturcter for Parallepiped class"""
        self.height = height
        super().__init__(length, width) # uses parent class __init__ for length and width

    def volume(self):
        """Calculates volume with height and area"""
        volume = super().area() * self.height #calculates height multiplied by (parent class method) area
        return volume

    def display(self):
        """displays necessary information for the user"""
        super().display() # uses the parent class display method and adds the height and volume
        print("Height: ", self.height)
        print("Volume: ", self.volume())
    
#this makes sure that when the classes are imported they don't automatically run without us wanting it to
if __name__ == "__main__":
    while(True):
        length = eval(input("Please enter the length of the base Rectangle: "))
        if(type(length) == int):
            break
        else:
            print("Try again! (maybe an integer this time).")

    while(True):
        width = eval(input("Please enter the width of the base Rectangle: "))
        if(type(width) == int):
            break
        else:
            print("Try again! (maybe an integer this time).")

    while(True):
        height = eval(input("Please enter the height of the Parallepiped: "))
        if(type(height) == int):
            break
        else:
            print("Try again! (maybe an integer this time).")
    rect = Rectangle(length, width)     #takes user input and puts it into a class object
    para = Parallepiped(height, rect.length, rect.width) #takes user input and puts it into a class object
    para.display() #displays all information

