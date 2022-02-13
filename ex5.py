#This is a python program to learn about strings

name = 'Zed A. Shaw'
age = 35 # not a lcie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#This is a variable to change values into standard formats
#The first varibale has a round function represented by round()
height_in_cm= round(float(height / 0.3970079))
weight_in_kg= float(weight / 2.20462262)

print(f"{height_in_cm}, {weight_in_kg}")

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actualy that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this ;ine is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
