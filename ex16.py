from sys import argv

script, filename = argv

print(f"We're going to erase {filename}. ")
print(f"If you don't want that, hit CTRL-C (^C).")
print(f"If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w+')
#Truncating the file below again is redundant as above, we have already
#opened file in 'w' mode referring to only write mode which already erases the contents of the file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.seek(0)
print(f"Here are the contents of {filename}:")
print(target.read())

print("And finally, we close it.")
target.close()
