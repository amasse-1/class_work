package main

/*
Project 3: Convert Python (tribo.py) to Go
CSC6303: Systems and Languages Survey
Author: Anthony Masse
*/

import "fmt"

func tribonacci(n int) []int { //paramenter integer n, returns integer array
	if n <= 0 {
		return nil // nil == null or in this circumstance nil will be an empty array ([])
	} else if n == 1 {
		return []int{0} // return [0]
	} else if n == 2 {
		return []int{1} //return [1]
	} else {
		fib_seq := []int{1, 1, 1} // initialize array
		for i := 3; i < n; i++ {
			next_num := fib_seq[i-1] + fib_seq[i-2] + fib_seq[i-3]
			fib_seq = append(fib_seq, next_num)
		}
		return fib_seq // returning sequence
	}
}

func main() {
	fmt.Print(tribonacci(20))
}
