""" 
 Class: CSC6003A_FA2022F1_Foundations of Programming 1

Prorgramming Project 2

 Author: Anthony Masse

 Created on: 9/8/2022
 Updated on: 9/15/2022
 
 Description: This code is takes two user-given positive number and checks to see if the first number is divisble 
 by the second number and lets you know if it is divisble or is not divisble. 
""" 

def main():

	while(True): # while there is not error or user interruption, continue

		#get user input for the first number
		num1 = eval(input("Please enter your first positive number: "))

		#checks if the user-given number is a positive number
		if num1 <= 0:
			print("Your number was not positive! Error! Try again later!")
			break

		#making sure the first number from the number is actually a number. 
		if type(num1) != float and type(num1) != int:
			print('That is not a number or a float! Error! Try again later')
			break

		#get user input for the second number
		num2 = eval(input("Please enter your second positive number: "))

		#checks if the user-given number is a positive number
		if num2 <= 0:
			print("Your number was not positive! Error! Try again later!")
			break
		
		#making sure the second number from the number is actually a number. 
		if type(num2) != float and type(num2) != int:
			print('That is not a number or a float! Error! Try again later')
			break

		#call the function and input arguments (the two positive numbers) into function
		user_answer = divideEvenly(num1,num2)
		
		#once the user finds a divisible pair, break out of the loop
		if(user_answer == True):
			print('Your first number is divisible by your second number! Goodbye!')
			break

def divideEvenly(num1, num2):
	#checks to see if there is a remainder of 0 or not and gives True/False if it is evenly divisible
	if num1 % num2 == 0:
		return True
		
	else: 
		print("Your first number is not divisible by your second number! Try again!")	
		

main()
