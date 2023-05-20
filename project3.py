#CSC6023: Advanced Algorithms
#Project 3: Tribonacci sequence (Dynamic Programming)
#@author: Anthony Masse

def tribo(n):
    if(n < 4 and n > 0):
        return 1
    else:
        return (tribo(n-1) + tribo(n-2) + tribo(n-3))
    
def main():
    x = 1
    while x > 0:
        x = int(input('Please enter the position of the element in the Tribonacci sequence: '))
        if(x <= 0):
            break
        print(f'\nThe {x}-th element of Tribonacci is: {tribo(x)} ')

if __name__ == '__main__':
    main()
