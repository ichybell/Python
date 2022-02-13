#The following is a function to see the cheese_count and no of boxes_of_crackers for a party
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes_of_crackers")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#The following is the function executed with the explanation given in the print function
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
#The following lines assign variables to integers
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#The following is the function executed with the explanation given in the print function above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#The following is the function executed with the explanation given in the print function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
#The following is the function executed with the explanation given in the print function
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("We can also ask input directly from the user:")
print("Please input the number of pieces of cheese you would like for the party")
amount_of_cheese = int(input(">"))

print("Please input the number of crackers you would like for the party")
amount_of_crackers = int(input(">"))

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Let us try using the contents of a file as arguments
#currentline= open("numbers.txt", "r").readline()
#cheese_and_crackers(currentline, amount_of_crackers)
