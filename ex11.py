print("How old are you?", end=' ')

# I am utilising the int function for the variable below as expected input can only be an integer

age= int(input())
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end='')
weight=input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

city= input("What city do you come from?")
job= input("What job do you do?")
interest= input("Anything else interesting about you?")

print(f"I can't believe you get to work as a {job} and especially in {city}. \n{interest} is also great!")
