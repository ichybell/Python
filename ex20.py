from sys import argv

script, input_file = argv
#This is a function to read the file provided and display all content
def print_all(f):
    print(f.read())
#This is a function to position the reader of the file object depending on the number of bytes
def rewind(f):
    f.seek(0)
#This is a function to print each line of the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")
#This is the current_line variable to be used in line count currently set to 1
current_line = 1
print_a_line(current_line, current_file)
current_line +=1
#The current_line variable has been incremented by 1 hence it is now at position 2
print_a_line(current_line, current_file)
#The current line variable has been incremented by 1 again hence it is now at position 3
current_line += 1
print_a_line(current_line, current_file)
