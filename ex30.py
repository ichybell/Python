people = 30
cars = 40
trucks = 15

#Evaluates the number of cars vs people and executes the block of code for whichever statement
#runs true
#Else is only executed if both if and elif remain false
if cars > people & cars == people:
    print("We should take the cars.")

elif cars < people and cars == people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

#Evaluates the number of trucks vs the number of cars and executes the block of code for
#whichever statement runs true
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
elif trucks != cars:
    print("This is just to determine which elif block of code will execute")
else:
    print("We still can't decide")
#Evaluates the number of trucks vs the number of people and executes the block of code for
#whichever statement runs true
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
