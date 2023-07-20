import java.util.Scanner;
import java.util.LinkedList;
/**
 * Project 4: Linked List and Collections Frameworks
 * An implemented program that reads a list of integers numbers 
 * from the scanned input and saves it to a Linked List and is sorted
 * from sdmallest to largest
 * 
 * @author Anthony Masse
 * @version 1.0
 * @since Week 4 of CSC6301
 * 
 */
public class project_4{


    /**
         * Returns a sorted version of the linked list provided to the method. Using the 
         * Bubble Sort Algorithm, the linked list is sorted from smallest to largest. 
         * 
         * @author Anthony Masse
         * @param nums an unsorted linked list
         * @return nums - a now sorted version linked list of integers 
         * @since Week 4 of CSC6301
         * 
         */
    public static LinkedList<Integer> sort_list(LinkedList<Integer> nums){

        for(int i = 0; i < nums.size() - 1; i++){ // for loop 1
            
            for(int j = 0; j < nums.size() - i - 1; j++){ // for loop 2
            
                if(nums.get(j) > nums.get(j+1)){
                    int tmp = nums.get(j);
                    nums.set(j, nums.get(j+1));
                    nums.set(j+1, tmp);
                
                }
            
            }
        
        }
        //returning sorted list
        return nums;        
    }

    /**
     * Main Method of project_4 class
     * @param args default parameter for a main method - not used
     * @author Anthony Masse
     * @since Week 4 of CSC6301
     */
    public static void main(String[] args) {

        //initiating linked list and scanner
        LinkedList<Integer> nums = new LinkedList<>();
        Scanner sc = new Scanner(System.in); 

        // adding each integer into the nums linked list
        System.out.println("Please enter a list of numbers seperated by line(type 'x' to stop): ");
        while(sc.hasNextInt()){
            nums.add(sc.nextInt());
        }

        sc.close(); // close scanner

        //printing original version, sorting, printing sorted version
        System.out.println("Linked List: " + nums);
        LinkedList<Integer> sorted = sort_list(nums);
        System.out.println("Sorted Linked List: " + sorted);
    }
}

