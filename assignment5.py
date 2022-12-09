
#input: an array A and indecies i and j
#ouput: an array where A[i] and A[j] have been swapped
def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

#input: an unsorted array A of integers
#output: an array A sorted in decreasing order(for each iteration) and the number of total comparisons
def selection_sort(array):
    comp_count = 0
    for i in range(len(array)-1):
        m = i
        # Find the largest element in A[i .. n-1]
        for j in range(i+1, len(array)):
            if array[j] > array[m]:
                m = j
            comp_count += 1
        swap(array, i, m)
        print(f'{array}')
    print(f'Fully Sorted: {array}')
    print(f'Total Number of Comparisons: {comp_count}')

# input: An array of integers.
# output: An array sorted in decreasing order(for each iteration), the number of comparisons 
# and the number of swaps
def bubble_sort(array):
    comp_count = 0
    swap_count = 0
    for i in range(len(array)-1) :
        for j in range(len(array)-i-1):
            if array[j+1] > array[j] :
                swap(array, j+1, j)
                swap_count +=1
            comp_count +=1
        print(array)
    print(f'Fully Sorted: {array}')
    print(f'Total Number of Comparisons: {comp_count}')
    print(f'Total Number of Swaps: {swap_count}')

#input: a real number x and any non-negative integer p
#output: the calculated p'th power of a real number x (total)
def power(x, p):
    total = 1
    for i in range(p):
        total *= x
    return total

#input: an array A and a number we 'plug-in' as x
#output: solution of the polynomial  
def evaluate(A, x):
    total = 0
    for element in A:
        total += element * power(x, A.index(element))
    return total



def main():
    print("Selection Sort\n------------------------")
    a1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
    selection_sort(a1)
    print('\n\n')
    #-----------------------------------------------
    a2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
    selection_sort(a2)
    print('\n\n')
    #-----------------------------------------------
    a3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]
    selection_sort(a3)
    print('\n\n')
    #-----------------------------------------------
    print("Bubble Sort\n------------------------")
    a4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
    bubble_sort(a4)
    print('\n\n')
    #-----------------------------------------------
    a5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
    bubble_sort(a5)
    print('\n\n')
    #-----------------------------------------------
    a6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
    bubble_sort(a6)
    print('\n\n')
    #-----------------------------------------------
    print('Polynomial Evaluation\n------------------------')
    poly = [12.3, 40.7, -9.1, 7.7, 6.4, 0, 8.9]
    solved = evaluate(poly, 5.4)
    print(f'Solved Polynomial: {solved}')

if __name__ == '__main__':
    main()

