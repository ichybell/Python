print("""You enter a dark room with two doors.
Do you go through door #1, door #2 or door #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear")

    bear = input("> ")

    if bear =="1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Bluberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
elif door == "3":
    print("You are the real hero for choosing this")
    print("You are now in the Endgame. \nWhat do you do?")
    print("1. Kill Thanos Antman butt style?")
    print("2. Do it the same way as in the actual Endgame?")
    print("3. I don't really care?")

    endgame= input("> ")

    if endgame == "1":
        print("That takes some real courage. Your nation honors you!")
    elif endgame == "2":
        print("Well, a lesser man would have chosen a riskier path.")
    elif endgame == "3":
        print("Well, dissapointing nonetheless but admirable that you chose to deceive thyself")
    else:
        print(f"At the end of the day, {endgame} is your choice really.")

else:
    print("You stumble aroud and fall on a knife and die. Good job!")
