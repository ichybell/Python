#This is a variable to store the various types of people who exist in relation to knowledge of binary
types_of_people = 10

#This is a varibale to store a string and output it saying the types of people stored in the previous variable, types_of_people
x = f"There are {types_of_people} types of people"

#This are two variables which stores strings and print them out using the third variable below
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#This is  command to print the previous already formatted variables
print(x)
print(y)

#This is a command to print the variables again but this time as varibales contained within a string hence the formatting is needed for proper rendering
print(f"I said: {x}")
print(f"I also said: '{y}'")

#These are variables, the first one having been assigned a boolean value and the second one a string with the curly braces used an argument field to be filled if necessary or would otherwise be left as just a string.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#This is to print the previous string, joke_evaluation, with an argument provided using the .format to be formatted correctly as a boolean value.
print(joke_evaluation.format(hilarious))

#These are strings stored in varibales
w= "This is the left side of..."
e= "a string with a right side."

#This is the printing of the above strings, w and e, while concatenating them.
print(w + e)
