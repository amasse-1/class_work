import java.util.Scanner;
import java.util.Stack;
/**
 * Project 5: Plan and execute a maintenance task
 * An implemented program that reads a list of integers numbers 
 * from the scanned input and saves it to a Stack (instead of a linked list) 
 * and is sorted from smallest to largest
 * 
 * Previous version: project_4.java, using Linked List
 * 
 * @author Anthony Masse
 * @version 2.0
 * @since Week 5 of CSC6301
 * 
 */
public class project_5{
    
    /**
         * Returns a sorted version of the stack provided to the method. Using the 
         * Bubble Sort Algorithm, the stack is sorted from smallest to largest.
         * Renamed sort stack as implementation has changed from Linked List
         * to Stack 
         * 
         * @author Anthony Masse
         * @param nums an unsorted stack
         * @return nums - a now sorted version stack of integers 
         * @since Week 5 of CSC6301
         * 
         */
    public static Stack<Integer> sort_stack(Stack<Integer> nums){
        for(int i = 0; i < nums.size() - 1; i++){ // for loop 1
            
            for(int j = 0; j < nums.size() - i - 1; j++){ // for loop 2
            
                if(nums.get(j) > nums.get(j+1)){
                    int tmp = nums.get(j);
                    nums.set(j, nums.get(j+1));
                    nums.set(j+1, tmp);
                
                }
            
            }
        
        }
        //returns stack nums now sorted
        return nums;
    }

    /**
     * Main Method of project_5 class
     * @param args default parameter for a main method - not used
     * @author Anthony Masse
     * @since Week 5 of CSC6301
     */
    public static void main(String[] args) {

        //initiating linked list and scanner
        Stack<Integer> nums = new Stack<>();
        Scanner sc = new Scanner(System.in); 

        // adding each integer into the nums linked list
        System.out.println("Please enter a list of numbers seperated by line(type 'x' to stop): ");
        while(sc.hasNextInt()){
            nums.add(sc.nextInt());
        }

        sc.close(); // close scanner

        //printing original version, sorting, printing sorted version
        System.out.println("Stack: " + nums);
        Stack<Integer> sorted = sort_stack(nums);
        System.out.println("Sorted Stack: " + sorted);
    }
}