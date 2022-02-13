from sys import exit

#Every function in this module is surrounded with a try_catch block when being called to ensure
#it does not return an error when being called
def gold_room():
    print("This room is full of gold. How many kilograms do you take?")

    choice = float(input("> "))
    if choice < 50:
        print("Nice, you're not greedy, you win!")

        try:
            play_again()

        except KeyboardInterrupt as e:
            exit(0)

    else:
        try:
            dead("You greedy bastard!")

        except KeyboardInterrupt as e:
            exit(0)

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")

    try:
        hint()

    except KeyboardInterrupt as e:
        exit(0)

def hint():
    print("How are you going to move the bear?")
    bear_moved = False
    while True:
        choice = input("> ")

        if "take honey" in choice:

            try:
                dead("The bear looks at you then slaps your face off.")

            except KeyboardInterrupt as e:
                exit(0)

        elif "taunt bear" in choice and not bear_moved:
            print("The bear has moved from the door.")
            print("You can open it now.")
            bear_moved = True

        elif "taunt bear" in choice and bear_moved:
            try:
                dead("The bear gets pissed off and chews your leg off.")

            except KeyboardInterrupt as e:
                exit(0)

        elif ("open door" or "open it" in choice) and bear_moved:
#This is while loop with a try_except block of code to account for ValueErrors in the type of user input at gold_room function
            while True:
                try:
                    gold_room()

                except ValueError as e:
                    print("\n\t*Please input a number*\n")

        elif "hint" in choice:
            print("You might want to try taunting the bear")

        else:
            print("I got no idea what that means.\n\n\t\t*Tell me if you would like a hint*\n")

            try:
                hint()

            except KeyboardInterrupt as e:
                exit(0)

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for you life or let it eat your head?")

    choice = input("> ")

    if "flee" in choice:

        try:
            start()

        except KeyboardInterrupt as e:
            exit(0)



    elif "head" in choice:
        try:
            dead("Well that was tasty!")

        except KeyboardInterrupt as e:
            exit(0)

    else:
        try:
            cthulhu_room()

        except KeyboardInterrupt as e:
            exit(0)



def dead(why):
    print(why, "Good job!")

    try:
        play_again()

    except KeyboardInterrupt as e:
        exit(0)

def play_again():
    print("\n\n\t\t\t*Would you like to play again?*")
    choice = input("\n> ")

    if "yes" in choice:
        try:
            start()

        except KeyboardInterrupt as e:
            exit(0)

    if "no" in choice:
        print("Until next time, Ciao!")
        exit(0)

    else:
        print("\nAcceptable choices are yes or no only!")

        try:
            play_again()

        except KeyboardInterrupt as e:
            exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        try:
            bear_room()

        except KeyboardInterrupt as e:
            exit(0)



    elif choice == "right":
        try:
            cthulhu_room()

        except KeyboardInterrupt as e:
            exit(0)



    else:
        try:
            dead("You stumble around the room until you starve.")

        except KeyboardInterrupt as e:
            exit(0)

try:
    start()

except KeyboardInterrupt as e:
    exit(0)
