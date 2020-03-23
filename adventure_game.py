import time
import random

enemy = [pirate, troll, monster, zombie]

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairy  is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty(but not very effective) dagger.")


def fight(weapon):
    if "sword" in weapon:
        print_pause("As the pirate moves to attack, you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
        print_pause("But the pirate takes one look at your shiny new toy and runs away!")
        print_pause("You have rid the town of the pirate. You are victorious!")
        # exit the game
    else:
        print_pause("You do your best…")
        print_pause("But your dagger is no match for the wicked fairie.")
        print_pause(" You have been defeated!")
        while True:
            choice = input("Would you like to play again? (y/n)").lower()
            if choice == "y":
                print_pause("Excellent!Restarting the game.")
                play_game()
                break
            elif choice == "n":
                print_pause("Thanks for playing! See you next time.")
                break
                # exit the game


def run_away():
    print_pause("You run back into the field. Luckily, you don’t seem to have been followed.")
    house_or_cave(weapon)

def fight_or_runaway(weapon):
    choice = input("Would you like to (1)fight (2)run away?")
    if choice == "1":
        fight(weapon)
    elif choice == "2":
        run_away()
    else:
        while True:
            answer = input("Would you like to play again? (y/n)").lower()
            if answer == "y":
                fight_or_runaway(weapon)
                break
            elif answer == "n":
                print_pause("Thanks for playing! See you next time.")
                break
                # exit the game

def house(weapon):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a gorgon.")
    print_pause("Eep! This is the gorgon’s house!")
    print_pause("The gorgon attacks you!")
    print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
    fight_or_runaway(weapon)

def cave(weapon):
    if "sword" in weapon:
        print_pause("You peer cautiously into the cave.")
        print_pause("You’ve been here before, and gotten all the good stuff.")
        print_pause("It’s just an empty cave now.")
        print_pause("You walk back out to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with you.")
        print_pause("You walk back out to the field.")
        weapon.append("sword")
    house_or_cave(weapon)
    
def house_or_cave(weapon):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    
    while True:
        choice = input("(Please enter 1 or 2:)")
        if choice == "1":
            house(weapon)
            break
        elif choice == "2":
            cave(weapon)
            break

def play_game():
    weapon = []
    intro()
    house_or_cave(weapon)

play_game()