import time
import random


def choose():
    question = input()
    while question != "1" and question != "2":
        print("Please enter 1 or 2.")
        question = input()
    return question


def start():
    print()
    print_pause("You find yourself standing in an open field,")
    ("filled with grass and yellow wildflowers.")
    time.sleep(1)
    print("Rumor has it that a " + danger + " is somewhere around here,")
    ("and has been terrifying the nearby village.")
    time.sleep(1)
    print("In front of you is a house.")
    time.sleep(1)
    print("To your right is a dark cave.")
    time.sleep(1)
    print("In your hand you hold your trusty (but not very effective) dagger.")
    time.sleep(1)
    print()
    print("Enter 1 to knock on the door of the house.")
    print("Enter 2 to peer into the cave.")


def house(danger):
    time.sleep(1)
    print("You approach the door of the house.")
    time.sleep(1)
    print("You are about to knock when the door opens")
    ("and out steps a " + danger + ".")
    time.sleep(1)
    print("Eep! This is the " + danger + "'s house!")
    time.sleep(1)
    print("The " + danger + " attacks you!")
    time.sleep(1)
    print("You feel a bit under-prepared for this,")
    ("what with only having a tiny dagger.")
    time.sleep(1)
    print("Enter 1 to fight.")
    time.sleep(1)
    print("Enter 2 to run away.")
    time.sleep(1)


def house_con_espada(danger):
    time.sleep(1)
    print("You approach the door of the house.")
    time.sleep(1)
    print("You are about to knock when the door")
    ("opens and out steps a " + danger + ".")
    time.sleep(1)
    print("Eep! This is the " + danger + "'s house!")
    time.sleep(1)
    print("The " + danger + " attacks you!")
    time.sleep(1)
    print("Enter 1 to fight.")
    time.sleep(1)
    print("Enter 2 to run away.")
    time.sleep(1)


def fight_sin_espada(danger):
    time.sleep(1)
    print("You do your best...")
    time.sleep(1)
    print("but your dagger is no match for the " + danger + ".")
    time.sleep(1)
    print("You have been defeated!")
    print("GAME OVER")
    time.sleep(1)
    print("Would you like to play again? (1 for yes/2 for no)")
    # Things that happen when the player fights without a sword


def fight_con_espada(danger):
    print()
    print("As the " + danger + " moves to attack,")
    ("you unsheath your new sword.")
    time.sleep(1)
    print("The Sword of Ogoroth shines brightly in")
    ("your hand as you brace yourself for the attack.")
    time.sleep(1)
    print("But the " + danger + " takes one look at your")
    ("shiny new toy and runs away!")
    time.sleep(1)
    print("You have rid the town of the " + danger + ". You are victorious!")
    time.sleep(1)
    print("Would you like to play again? (1 for yes/2 for no)")
    # Things that happen to the player in the house


def start_con_espada():
    print("You walk back out to the field.")
    time.sleep(1)
    print("Enter 1 to knock on the door of the house.")
    time.sleep(1)
    print("Enter 2 to peer into the cave.")
    time.sleep(1)
    print("(Please enter 1 or 2.)")


def cave_sin_espada():
    print()
    print("You peer cautiously into the cave.")
    time.sleep(1)
    print("It turns out to be only a very small cave.")
    time.sleep(1)
    print("Your eye catches a glint of metal behind a rock.")
    time.sleep(1)
    print("You have found the magical Sword of Ogoroth!")
    time.sleep(1)
    print("You discard your silly old dagger and take the sword with you.")
    time.sleep(1)
    print("You walk back out to the field.")
    time.sleep(1)
    print("Enter 1 to knock on the door of the house.")
    time.sleep(1)
    print("Enter 2 to peer into the cave.")
    time.sleep(1)
    print("(Please enter 1 or 2.)")
    # Things that happen to the player goes in the cave without the sword


def cave_con_espada():
    print()
    print("You peer cautiously into the cave.")
    time.sleep(1)
    print("You've been here before, and gotten all the good stuff.")
    ("It's just an empty cave now.")
    time.sleep(1)


def start_sin_espada():
    print()
    print("You walk back out to the field.")
    time.sleep(1)
    print("Enter 1 to knock on the door of the house.")
    time.sleep(1)
    print("Enter 2 to peer into the cave.")
    time.sleep(1)
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
