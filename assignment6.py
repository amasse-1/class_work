import math

#input: a positive integer n
#output: the number of digits in the binary expansion of n/2
def num_of_bin(n):
    if n == 1:
        return 1 
    elif n > 1:
        return 1+num_of_bin(math.floor(n/2))

#input positive integer n
#ouput: return the sum of the sqaures
def sum_of_squares(n):
    if n == 1:
        return 1
    elif n > 1:
        #squared plus the sum of squares of n - 1
        #example: 5^2 + 4^2 + .... + 1^2
        return n**2 + sum_of_squares(n - 1)


def main():
    print('Function #1: ')
    a1 = num_of_bin(32)
    print(f'32 has {a1} binary digits')

    a2 = num_of_bin(75)
    print(f'75 has {a2} binary digits')

    print('\n')

    print('Function #2: ')
    a3 = sum_of_squares(5)
    print(f'Sum of squares of 5 is: {a3}')

    a4 = sum_of_squares(10)
    print(f'Sum of squares of 10 is: {a4}')



if __name__ == "__main__":
    main()
