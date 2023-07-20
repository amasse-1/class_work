import java.util.Arrays;
/**
 * Project 2: Bubble Sort -
 * A class to perform integer based array sorting 
 * using the BubbleSort Algorithm. 
 * 
 * @author Anthony Masse
 * @version 1.0
 * @since Week 2 of CSC6301
 */
public class project_2 {

    /**
     * Bubble Sort method of the project_2 class - 
     * 
     * Returns a sorted array of integers based off of an input array of integers
     * using the bubblesort algorithm. 
     * 
     * @param xArray unsorted(or sorted) array of integers
     * @since Week 2 of CSC6301
     */
    public static void bubbleSort(int[] xArray){
        // length/size of the array
        int size = xArray.length; 

        for(int i = 0; i < size - 1; i++){
            for(int j = 0; j < size - i - 1; j++){
                if(xArray[j] > xArray[j + 1]){
                    // create temporary integer for reassignment
                    int temp = xArray[j];
                    // swapping integers at each index, while reassigning temp value
                    xArray[j] = xArray[j + 1]; 
                    xArray[j + 1] = temp;
                }
            }
        }
    }

    /**
     * Main Method of project_2 class
     * @param args default parameter for a main method - not used
     * @since Week 2 of CSC6301
     */
    public static void main(String[] args) {
        int[] myArray = {2, 45, 37, 21, 31, 50, 29, 22, 67, 88, 56};

        System.out.println("Unsorted Array: " + Arrays.toString(myArray));

        project_2.bubbleSort(myArray);

        System.out.println("Sorted Array: " + Arrays.toString(myArray));
    }

}
