from dequeue import Dequeue
import unittest

class test_Dequeue(unittest.TestCase):

    def test_isEmpty(self):
        d = Dequeue()
        #the dequeue should start off empty
        self.assertTrue(d.isEmtpy())
        d.addBack(10)
        #after adding 10, it should not be empty
        self.assertFalse(d.isEmtpy())

    def test_addFront(self):
        d = Dequeue()
        #adds to the front
        d.addFront(12)
        #checks its in there
        self.assertEqual(d.dequeue[0], 12)
        #adds to the fron
        d.addFront(5)
        #checks to see if it was added to the front
        self.assertEqual(d.dequeue[0], 5)

    def test_addBack(self):
        d = Dequeue()
        #adds to the back
        d.addBack(12)
        #checks that its in there
        self.assertEqual(d.dequeue[0], 12)
        #adds another to the back
        d.addBack(0)
        #checks that its added to the back
        self.assertEqual(d.dequeue[1], 0)

    def test_removeFront(self):
        d = Dequeue()
        #adds 3 items
        d.addFront(1)
        d.addFront(2)
        d.addFront("hi")
        #removed from the front
        d.removeFront()
        #checks to see that it is removed from the front
        self.assertEqual(d.dequeue[0], 2)

    def test_removeBack(self):
        d = Dequeue()
        #adds 3 items
        d.addFront('pie')
        d.addFront(10)
        d.addFront("Hello world")
        #removes the first item added
        d.removeBack()
        #gets the length of the dequeue
        x = len(d.dequeue)
        #makes sure the last one is not pie
        self.assertNotEqual(d.dequeue[x-1], "pie")
        self.assertEqual(d.dequeue[x-1], 10)

#main
def main():
    test_Dequeue.test_isEmpty()
    test_Dequeue.test_addFront()
    test_Dequeue.test_addBack()
    test_Dequeue.test_removeFront()
    test_Dequeue.test_removeBack()


if __name__ == "__main__":
    unittest.main()
