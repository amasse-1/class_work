import os
from random import randint
import shutil

#Project 5
#Author: Anthony Masse
#OS tested on: Windows 11
#Programming Language: Python

#Requirements:
#Your program should ask the user the name of the folder to be created
# if the folder exists, the folder has to be removed and a new one created;

#Once created, your program should generate 100 random number from 0 to 1000 and
# save them in a file named "numbers100.txt" inside the created folder.

#The program must perform system calls to your operating system in order
# to check if the folder exists, if so, delete it, and then create the folder.

#get current working directory
os.getcwd()

#get folder name
folder_name = input("Please enter the name of the folder you would like to create:")

#get new directory path
path = os.path.abspath(folder_name)

try:
    
    #try creating directory
    os.mkdir(folder_name)
    print(f"{folder_name} created")

except OSError as error:

    print(f"{folder_name} already exists...")
    print("Deleting old directory and creating new")

    # remove old directory (shutil will get rid of non-empty folders)
    shutil.rmtree(path)

    # create new directory
    os.mkdir(folder_name)

    #let user know
    print("New directory created")

#change directory
os.chdir(path)

#creating file and write to it
f1 = open("numbers100.txt", "w")
count = 0
for i in range(0, 100):
    num = randint(0, 1000)
    f1.write(f"{num}\n")
    count+=1
f1.close() #close file
