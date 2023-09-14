import java.util.Scanner;
/*
 * Project 2
 * Convert prime.cpp to Java
 * Author: Anthony Masse
 */
class Prime{
    public static boolean isPrime(int n){
        if(n <=1 ){
            return false;
        } 
        else if(n <= 3){
            return true;
        } 
        else if ((n % 2 == 0 )|| (n % 3 == 0)){
            return false;
        }
        for (int i = 5; i * i <= n; i += 6){
            if (n % i == 0 || n % (i + 2) == 0){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // initiate the scanner
        int number; // number used to store user input
        do {
            System.out.print("Enter a positive number (0 or negative to exit): ");
            number = sc.nextInt();
            if(number <= 0){
                break;
            } else if(Prime.isPrime(number)){
                System.out.println(number+" is a prime number.");
            }else{
                System.out.println(number+" is not a prime number.");
            }
        } while (true);
        sc.close(); // close the scanner
    }
}