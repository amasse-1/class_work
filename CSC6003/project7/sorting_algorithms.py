"""

Project 7: Sorting Algorithms 
Author: Anthony Masse
Last Updated 10/17/2022
Class: CSC6003 - Foundations of Programming 1

"""


from random import randint
from datetime import datetime
from mergeSort import merge_sort
from insertionSort import insertion_sort

class sorting_algorithms:
    
    def __doc__(self):
        """
        Class Sorting Algorithms

        Imports:
        -------------------------
        randint : to generate a random integer from 0 to 100
        datetime : to get the time in milliseconds that the algorithms take to run
        merge_sort : to run the merge sort algorithm
        selection_sort : to run the selection sort algorithm

        Methods:
        --------------------------
        merge_sort_test : this method gets the start time, runs the merge sort on the given data set
                          and after the sorting is completed, it gets the end time. It returns the 
                          total duration of the sorting algorithm to run and the name of the sorting 
                          algorithm used (which is Merge Sort).

        insertion_sort_test: this method gets the start time, runs the insertion sort on the given data set
                            and after the sorting is completed, it gets the end time. It returns the 
                            total duration of the sorting algorithm to run and the name of the sorting 
                            algorithm used (which is Insertion Sort).

        main : this method creates two lists of number in which needs to be sorted we attain a copy of
               the originals for displaying purposes. It then determines which sorting algorithm is faster/
               better at sorting the data set generated. 

        """
    def merge_sort_test(l):

        start = datetime.now()  #gets the start time
        start_ms = start.timestamp() * 1000  #gets start time in ms

        new_l = merge_sort(l) #runs merge sort on the list and returns the merged list

        end = datetime.now() #gets the end time
        end_ms = end.timestamp() * 1000 #gets end time in ms


        merge_ms = end_ms - start_ms #gets the total duration
        return merge_ms, 'Merge Sort', new_l #returns all the necessary info

    def insertion_sort_test(l):
        start = datetime.now()  #gets the start time
        start_ms = start.timestamp() * 1000  #gets start time in ms

        insertion_sort(l) # runs insertion sort

        end = datetime.now() #gets the end time
        end_ms = end.timestamp() * 1000 #gets end time in ms


        insertion_ms = end_ms - start_ms #gets the total duration
        return insertion_ms, 'Insertion Sort' #returns all the necessary info


def main():

    l = list()
    l2 = list()

    for i in range(0,10000):
        x = randint(0,100)
        l.append(x)
        l2.append(x)
        
    
    l_copy = l.copy()
    l2_copy = l2.copy()


    time_1, name1, merged_l = sorting_algorithms.merge_sort_test(l)
    time_2, name2 = sorting_algorithms.insertion_sort_test(l2)

    #displays the results in ms
    print('\n')
    print(f'{name1} took {time_1} ms')
    print(f'{name2} took {time_2} ms')
    print('\n')

    #displays which is better
    if(time_1 > time_2):
        print(f'The better algorithm is: {name2} won by {time_1 - time_2} ms')
    elif(time_2 > time_1):
        print(f'The better algorithm is: {name1} won by {time_2 - time_1} ms')
    elif(time_1 == time_2):
        print(f'{name1} is just as good as {name2}')

    #print(f'Unsorted List 1: {l_copy}\n\n')
    #print(f'Sorted List 1: {merged_l}\n\n')
    #print(f'Unsorted List 2: {l2_copy}\n\n')
    #print(f'Sorted List 2: {l2}')



if __name__ == '__main__':
    main()






