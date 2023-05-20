#double array queue 
class Queue:
    def __init__(self):
        self.a_in = []
        self.a_out = []
    def enqueue(self, d):
        self.a_in.append(d)
    def dequeue(self):
        if(self.a_out == []):
            for d in self.a_in:
                self.a_out.append(d)
            self.a_in = []
        return self.a_out.pop(0)

from random import randrange

#testing the queue
def test_queue(initialSize, probDeq, probEnq):
    q = Queue()
    cheap, costly = 0,0
    s = initialSize 
    for i in range(s):
        q.enqueue(1) #intializing the size of the queue
    m = 2 * s
    for i in range(100000):
        if (randrange(100) < probDeq):
            if (s > 0):
                q.dequeue() 
                s -= 1
        else: # where the probability of enqueue
            if (s == m):
                q.enqueue(1)
                m = m*2
                s += 1
                costly += 1
            else:
                q.enqueue(1) # enters one as a random number
                s += 1
                cheap += 1
    print("Initial size:", initialSize, "\nProb Dequeue:", probDeq, "out of 100 \nProb Enqueue:", probEnq, "out of 100")
    print("Costly: {:7} ({:3.1}%)".format(costly,(100*(costly/(costly+cheap)))))
    print("Cheap: {:7} ({:3.1}%)".format(cheap,(100*(cheap/(costly+cheap)))))
#main 
def main():
    again = 'y' # defauly value to run while loop
    while(again == 'y'):
        size = -1 #default value to run while loop
        while(size <= 0):
            size = int(input('Please enter the intial size of the queue (greater than 0): '))
        deq = 100 #default value to run while loop
        while (deq > 67 or deq < 33):
            deq = int(input('Please enter the probability of dequeue (max of 67, min of 33): '))
        enq = 100 - deq

        test_queue(size, deq, enq)
        again = input('Try again? (y/n): ')
    
if __name__ == '__main__':
    main()
