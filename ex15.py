#The following line imports argv module from sys package
from sys import argv

#The following line assigns the argv module two arguments to be provided by the user as they run the command
script, filename = argv
#The following line takes the file and assigns it to the txt variable for further processing.
#This is called a file object
#The default method of opening a file is in read mode, 'r' unless otherwise specified
txt = open(filename)
#The following lines prints to screen the name of the file provided from the argv argument
#and uses the read command to display the output of the txt variable.
print(f"Here's your file {filename}:")
print(txt.read())
#The following lines requests the user for input for a filename to display
print("Type the filename again:")
file_again = input(">")
#The following line takes the file and assigns it to the txt_again variable for further processing.
txt_again = open(file_again)
#The line below uses the read command to display the contents of the txt_again variable.
print(txt_again.read())

txt.close()
txt_again.close()
