#include <iostream>
using namespace std;

/*
Project 1:  Converting Python Code
Converting python code to anotherlanguage (in this case C++)
IDE used: Visual Studio Code
Compiler: g++

Python Code to convert:

def fact():
    n = int(input("Enter a positive integer: "))
    while ((n < 0)):
        n = int(input("Sorry, only positive numbers, enter again: "))
    if (n == 0):
        print("The factorial of 0 is 1")
    else:
        f = 1
        for i in range(1, n+1):
            f *= i
        print("The factorial of ", n ," is ", f)

*/

void fact(){
    int n;
    cout << "Enter a positive integer: ";
    cin >> n; // user input to n variable
    while (n < 0) // if it is not a positive number, loop. 
    {
        cout << "Sorry, only positive numbers, enter again: ";
        cin >> n; // user input to n variable (again)
    }
    if (n == 0) // if n == 0
    {
        cout << "The factorial of 0 is 1";
    } else {
        int f = 1;
        for (int i = 1; i < n+1; i++)
        {
            f *= i;
        }
        cout << "The factorial of " << n << " is " << f << endl; // 
    }
}

int main(){ // main
    fact(); // fact function
    return 0;
}