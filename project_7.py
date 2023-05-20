from math import log2
from random import randint

def myFunction(x):
    #added the less than zero part to contribute 
    if(x==0) or (x < 0):
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x)) ** 3
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x)*2)**3
    else:
        return (log2(x)**2) - x

def h_climb_1():
        max = 0
        for i in range(0,9999):
            x=i
            #getting the left of the current state, right of the current state, and the current state itself
            left_x = myFunction(x-1)
            center_x = myFunction(x)
            right_x = myFunction(x+1)

            #if the current state is greater than the left and right values, then the local maximum was found 
            if(center_x >= left_x) and (center_x >= right_x):
                max = center_x
        #if the right of the current state is greater than the left value of the current state, increase x
        #to find the highest value
            elif(right_x > center_x):
                x = x + 1
        # else decrease x
            elif(center_x < left_x):
                x = x - 1

        print(f'x-value: {x}\nMax Value: {max}')


#where the random x is chosen at random between 1 and 9998
def h_climb_2():
    while True:
        x = randint(1,9998)

        #getting the left of the current state, right of the current state, and the current state itself
        left_x = myFunction(x-1)
        center_x = myFunction(x)
        right_x = myFunction(x+1)

        #if the current state is greater than the left and right values, then the local maximum was found 
        if(center_x >= left_x) and (center_x >= right_x):
            break
        #if the right of the current state is greater than the left value of the current state, increase x
        #to find the highest value
        elif(right_x > left_x):
            x = x + 1
        # else decrease x
        elif(right_x < left_x):
            x = x - 1

    print(f'x-value: {x}\nMax Value: {center_x}')


if __name__ == '__main__':
    h_climb_1()
    h_climb_2()

