import time
import random


def print_pause(print_massage):
    print(print_massage)
    time.sleep(2)


def beginning(a, b):
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + b + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.")


def cave(a, b):
    if "sword" in a:
        print_pause("You're now inside the cave..")
        print_pause("it's so dark you berly see anything"
                    "you take a look around but it's empty")
        print_pause("You go back to the field.")
    else:
        print_pause("You're now inside the cave..")
        print_pause("It's such a dark place.")
        print_pause("but the sunshine comes through.")
        print_pause("You find some gold and a silver sword!")
        print_pause("You left your old dagger and took "
                    "the silver sword with you.")
        print_pause("You walk back to the field.")
        a.append("sword")
        field(a, b)

def house(a, b):
    print_pause("You open the door of the hunted house.")
    print_pause("You are walking inside "
                "all of the sudden there was a " + b + ".")
    print_pause("OMG! it\'s the " + b + "'s house!")
    print_pause("The " + b + " is attacking you!")
    if "sword" not in a:
        print_pause("You think you can handle it, "
                    "With your small dagger.")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run?")
        if choice2 == "1":
            if "sword" in a:
                print_pause("" + b + " moves to attack,"
                            "you with your new sword.")
                print_pause("you believe you can handle it"
                            "with your new sword"
                            "you take a deep breath and starts to attack"
                            "with all you got.")
                print_pause("The " + b + "started to take steps back"
                            "but you finshed him befor getting away")
                print_pause("You got rid of the " + b +
                            ". You won!\n")
            else:
                print_pause("You tried..")
                print_pause("but the " + b + " needs more than a dagger.")
                print_pause("You lost:(\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("You run back to the field. ")
            field(a, b)
            break


def field(a, b):
    print_pause("Enter 1 to go inside of the house.")
    print_pause("Enter 2 to go inside into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)")
        if choice1 == "1":
            house(a, b)
            break
        elif choice1 == "2":
            cave(a, b)
            break


def play_again():
    again = input("Would you like to play again? (y/n)")
    if again == "y":
        print_pause("\n\n\n Cool:) let's play again ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n okay! bye.\n\n")
    else:
        play_again()
def play_game(): 
    a = []
    b = random.choice(["wicked fairie", "scary wizard",
                       "dragon", "seial killer"])
    beginning(a, b)
    field(a, b)
play_game()