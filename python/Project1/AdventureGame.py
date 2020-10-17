import time
import random
pausa = 1


def choose():
    question = input()
    while question != "1" and question != "2":
        print("Please enter 1 or 2.")
        question = input()
    return question


def print_pause(story):
    print(story)
    time.sleep(pausa)


def start():
    print()
    print_pause("You find yourself standing in an open field,")
    ("filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + danger + " is somewhere around here,")
    ("and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty")
    ("(but not very effective) dagger.")
    print()
    print("Enter 1 to knock on the door of the house.")
    print("Enter 2 to peer into the cave.")


def house(danger):
    time.sleep(1)
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens")
    ("and out steps a " + danger + ".")
    print_pause("Eep! This is the " + danger + "'s house!")
    print_pause("The " + danger + " attacks you!")
    print_pause("You feel a bit under-prepared for this,")
    ("what with only having a tiny dagger.")
    print("Enter 1 to fight.")
    print("Enter 2 to run away.")
    time.sleep(1)


def house_con_espada(danger):
    time.sleep(1)
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door")
    ("opens and out steps a " + danger + ".")
    print_pause("Eep! This is the " + danger + "'s house!")
    print_pause("The " + danger + " attacks you!")
    print("Enter 1 to fight.")
    print("Enter 2 to run away.")
    time.sleep(1)


def fight_sin_espada(danger):
    time.sleep(1)
    print_pause("You do your best...")
    print_pause("but your dagger is no match for the " + danger + ".")
    print("You have been defeated!")
    print_pause("GAME OVER")
    print("Would you like to play again? (1 for yes/2 for no)")
    # Things that happen when the player fights without a sword


def fight_con_espada(danger):
    print()
    print_pause("As the " + danger + " moves to attack,")
    ("you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in")
    ("your hand as you brace yourself for the attack.")
    print_pause("But the " + danger + " takes one look at your")
    ("shiny new toy and runs away!")
    print_pause("You have rid the town of the " + danger + ".")
    ("You are victorious!")
    print("Would you like to play again? (1 for yes/2 for no)")
    # Things that happen to the player in the house


def start_con_espada():
    print_pause("You walk back out to the field.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("(Please enter 1 or 2.)")


def cave_sin_espada():
    print()
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and")
    ("take the sword with you.")
    print_pause("You walk back out to the field.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("(Please enter 1 or 2.)")
    # Things that happen to the player goes in the cave without the sword


def cave_con_espada():
    print()
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the good stuff.")
    ("It's just an empty cave now.")


def start_sin_espada():
    print()
    print_pause("You walk back out to the field.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("(Please enter 1 or 2.)")


def runaway():
    print("You run back into the field. Luckily,")
    ("you don't seem to have been followed.")


def end():
    print("Thanks for playing! See you next time.")


lista = ["dragon", "troll", "pirate", "wicked dairie"]
danger = random.choice(lista)

room = 0
start()
while True:
    answer = choose()
    if room == 0:
        if answer == "1":
            room = 2
            house(danger)
        else:
            room = 1
            cave_sin_espada()

    elif room == 2:
        if answer == "1":
            room = 3
            fight_sin_espada(danger)
        else:
            room = 4
            runaway()
            room = 0.5
            start_sin_espada()

    elif room == 0.5:
        if answer == "1":
            room = 2
            house(danger)
        else:
            room = 1
            cave_sin_espada()
            start_con_espada()

    elif room == 1:
        if answer == "1":
            room = 2.5
            house_con_espada(danger)
        else:
            room = 3.5
            cave_con_espada()
            start_con_espada()

    elif room == 3:
        if answer == "1":
            room = 0
            start()
        else:
            room = 7
            end()

    elif room == 1.5:
        if answer == "1":
            room = 2.5
            house_con_espada(danger)
        else:
            room = 3.5
            cave_con_espada()
            start_con_espada()

    elif room == 2.5:
        if answer == "1":
            room = 4.5
            fight_con_espada(danger)
        else:
            room = 6.5
            runaway()
            room = 1.5
            start_con_espada()

    elif room == 4.5:
        if answer == "1":
            room = 0
            start()
        else:
            room = 7
            end()

    elif room == 3.5:
        if answer == "1":
            room = 2.5
            house_con_espada(danger)
        else:
            room = 3.5
            cave_con_espada()
            start_con_espada()
