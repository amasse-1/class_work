import os

#current os name
sys = os.name

#get user input either linx-based file path or windows
file_path = input("Please enter the file path you'd like to use: ") 

if sys == "nt": # if windows, change to \
    file_path = file_path.replace("/", "\\")
elif sys == "posix": # if mac or linux, change to / 
    if file_path[0].isalpha():
        old_path = file_path.split(":")
        file_path = old_path[1]
        file_path = file_path.replace("\\", "/")
    else:
        file_path = file_path.replace("\\", "/")

# by changing directory to the file path given by the user,
# it will include drive as well
os.chdir(file_path) 
print("Current path:", os.path.abspath(os.getcwd()))


