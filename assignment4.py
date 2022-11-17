def divisible(array, pos_int): #input array and positive integer
    if(pos_int >= 0):
        count = 0
        for i in array:
            if(i % pos_int == 0):
                count += 1
        return count #ouput count


def smallest_gap(array): #input array
    smallest = 1000
    for i in array:
        for j in array:
            if(i > j):
                x = i - j
                if(x < smallest):
                    smallest = x
            elif(j > i):
                x = j - i
                if(x < smallest):
                    smallest = x
    return smallest # output


def mult_matrix(n, matrix1, matrix2): # three inputs n, matrix1, and matrix 2
    new_matrix = [[0  for col in range(n)] for row in range(n)] #fills the matrix with zeros
    for m1_row in range(n): # for matrix 1 rows
        for m2_col in range(n): # for matrix 2 columns
            for m2_row in range(n): # for matrix 2 rows

                #fill in the matrix at the corerct points
                new_matrix[m1_row][m2_col] += matrix1[m1_row][m2_row] * matrix2[m2_row][m2_col]

    return new_matrix # output matrix



def main():
    #inputs 
    a1 = [20,21,25,28,33,34,35,36,41,42]
    pos_int1 = 7
    
    #output  =  function(inputs)
    results1 = divisible(a1, pos_int1) 

    #print output 1
    print(f"Count of Divisible: {results1}")

    #inputs
    b1 = [18,54,76,81,36, 48, 99]
    pos_int2 = 9

    #output  =  function(inputs)
    results2 = divisible(b1, pos_int2)

    #print output 2
    print(f"Count of Divisible: {results2}")

    print("\n\n")
    #-----------------------------------------------#

    #input
    a2 = [50, 120, 250, 100, 20, 300, 200]
    b2 = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]

    #outputs = function(inputs)
    results1 = smallest_gap(a2)
    results2 = smallest_gap(b2)

    #print outputs
    print(f"Smallest Gap: {results1}")
    print(f"Smallest Gap: {results2}")

    print("\n\n")
    #-----------------------------------------------#

    #input dimensions (n x n)
    n1 = 2
    n2 = 3

    #input matricies set 1
    mat1 = [[2,7],[3,5]]
    mat2 = [[8,-4],[6,6]]

    #input matricies set 2
    mat3 = [[1,0,2],[3,-2,5],[6,2,-3]]
    mat4 = [[.3, .25, .1],[.4, .8, 0],[-.5, .75, .6]]

    #outputs = function(inputs)
    new1 = mult_matrix(n1, mat1, mat2)
    new2 = mult_matrix(n2, mat3, mat4)

    #printing outputs
    print(f"Matrix multiplication with two {n1}x{n1} Matricies: ")
    for i in new1:
        print(f'{i}\n')
    
    print(f"Matrix multiplication with two {n2}x{n2} Matricies: ")
    for i in new2:
        print(f'{i}')

    print("\n\n")
if __name__ == '__main__':
    main()