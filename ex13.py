#Writing a script that accepts arguments

from sys import argv
# read the WYSS section for how to run this

#The lines below ask for extra user input for the provided questions to deal with a study question
fourth= input("What is your fourth variable ?")
fifth= input("What is your fifth variable ?")
sixth= input("What is your sixth variable ?")

#The line below takes arguments as variables which are passed as the command is run
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)
print("Your fifth variable is:", fifth)
print("Your sixth variable is:", sixth)
