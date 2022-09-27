import unittest
from project4 import Rectangle, Parallepiped

class test_Rectangle(unittest.TestCase):

    def test_rectangle(self):
        #creating rectangle class object
        r = Rectangle(10,5)

        #testing length and width
        self.assertEqual(r.length, 10)
        self.assertNotEqual(r.length, 21)
        self.assertEqual(r.width, 5)
        self.assertNotEqual(r.width, 27)

        #testing perimeter method as well as area method
        self.assertEqual(r.perimeter(), 30)
        self.assertEqual(r.area(), 50)
        
        #I could not find a way to test the display method
        
class test_Parallepiped(unittest.TestCase):

    def test_parallepiped(self):
        #creating parallepiped class object
        p = Parallepiped(20, 10, 5)

        # testing length width and height
        self.assertEqual(p.height, 20)
        self.assertNotEqual(p.height, 100)
        self.assertEqual(p.length, 10)
        self.assertNotEqual(p.length, 25)
        self.assertEqual(p.width, 5)
        self.assertNotEqual(p.width, 6)

        # testing the parent class (Rectangle) methods
        self.assertEqual(p.area(), 50)
        self.assertNotEqual(p.area(), 51)
        self.assertEqual(p.perimeter(), 30)
        self.assertNotEqual(p.perimeter(), 400)

        #testing the volume method
        self.assertEqual(p.volume(), 1000)
        self.assertNotEqual(p.volume(), 1011)

        #I could not find a way to test the display method

unittest.main()