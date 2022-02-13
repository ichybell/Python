numbers = []
#This is a function to print out the list numbers[] and
#to append counted numbers to the list upto a specific defined value by the variable j
#and to increment by the defined value at l
def numbers_counter(j,l):
    i = 0
    while i < j:
        print(f"At the top is i is {i}")
        numbers.append(i)

        i = i + l
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

#numbers_counter(int(input("What number would you like to count upto? \n")), int(input("What number would you like it to increment by?")))
#print("The numbers: ")

#    print(num)

#This is a numbers_counter function similar to the one above except it uses for_loops
#instead of while loops
def numbers_counter_two(j,l):
    i=0
    for i in range(i,j+1,l):
        print(f"At the top is i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

numbers_counter_two(int(input("What number would you like to count upto? \n")), int(input("What number would you like it to increment by?")))
print("The numbers: ")

for num in numbers:
    print(num)
