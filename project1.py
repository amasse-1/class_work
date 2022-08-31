# Class: CSC6003A_FA2022F1_Foundations of Programming 1
# 
# Author: Anthony Masse
# 
# Created on: 8/30/2022
# 
# Description: This code is calculating the circumference, area, and volume 
# of a circle/sphere using the radius given by the user. 
# 
# 
import math

#getting the value of pi
pi = math.pi

#getting the radius from the user
radius = float(input("Enter the radius: \n"))

#calculating the circumference of the circle using radius
C = (2.0 * (pi * radius))

#making sure it is only 5 decimal places behind the decimal point
C = round(C, 5)

# printing the circumference to the user
print('The circumference of a circle with a radius of '+ str(radius) + ' is ' + str(C))

#calculating the area of the circle using radius
A = pi*(math.pow(radius, 2))

#making sure it is only 5 decimal places behind the decimal point
A = round(A, 5)

# printing the area to the user
print('The area of a circle with a radius of '+ str(radius) + ' is ' + str(A))

#calculating the volume of the sphere using radius
V = (4/3) * pi * (math.pow(radius, 3))

#making sure it is only 5 decimal places behind the decimal point
V = round(V, 5)

# printing the volume to the user
print('The volume of a sphere with a radius of '+ str(radius) + ' is ' + str(V))







