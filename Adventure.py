#
# A text based adventure game!
#
# Created by: woodD
#
# Version: 1.0
#
# Last updated: 15.3.2013
#

import random as r
import time as t
import AdventureObjects as ao
import AdventureHelpers as ah
import AdventureAreas as areas


def main():
    '''Main wrapper function for game'''

    print
    print("What would you like to do?")
    print("\t(1) Play new game.")
    print("\t(2) Continue last saved game.")
    print("\t(3) Read general instructions.")
    print("\t(4) View READ_ME file (contains general information about\n \t    'Adventure Game')")
    print
    print("If this is your first time playing Adventure game, please make sure\n to fully read the directions.")

    valid = ['1', '2', '3', '4']
    choice = ah.choiceCheck(valid)

    if choice == '1':

        playNewGame()

    elif choice == '2':
        pass
        # Not yet implemented

    elif choice == '3':
        pass
        # Not yet implemented
        
    elif choice == '4':
        pass
        # Not yet implemented

def setup():
    '''Setup for character at beginning of game.'''

    global character, pack
    
    print
    print("What is your name, oh mighty adventurer?")
    print
    name = raw_input("... ")

    t.sleep(0.5)
    
    print
    print("And what is your race?")
    print("\t(1) Human")
    print("\t(2) Elf")
    print("\t(3) Orc")

    validRaceChoice = ['1', '2', '3']
    raceChoice = ah.choiceCheck(validRaceChoice)
    
    t.sleep(0.5)
    
    print
    print("And what is your class?")
    print("\t(1) Warrior")
    print("\t(2) Mage")
    print("\t(3) Assassin")
    print("\t(4) Ranger")

    validClassChoices = ['1', '2', '3', '4']
    classChoice = ah.choiceCheck(validClassChoices)

    print
    print("All fine choices, oh mighty adventurer!")

    character = ao.CharacterSetup(name, raceChoice, classChoice)
    pack = ao.Pack()
    

def playNewGame():
    '''Initializes game'''

    global startedPlotLine, beenToTown
    startedPlotLine, beenToTown = False, False

    print

    setup()
    
    t.sleep(1.5)
    
    print
    print("You wake up to the sunrise, you're not sure where you are...")
    print("It appears you're somewhere in the middle of a forest.")
    print("You feel dizzy, you look down at you hands, they're covered in blood.")
    print
    print("You look over to your left, and you see pack laying on the ground.")
    print
    print("What will you do?")
    print("Open pack? ")

    validPackOptions = ['yes', 'no', 'y', 'n']
    packChoice = ah.choiceCheck(validPackOptions)

    if packChoice == 'no':
        
        print
        print("You pick up the pack and decide to check what's in it later then.")
        print

    else:

        print
        print("Your pack inventory is:")
        print
        print(pack.Inventory)
        print
    
    print("Standing up, you see two paths in front of you.")
    print("One path leads to the left, further into the woods, the other to the right, towards what looks like a town.")

    print
    print("Which way will you go?")
    print("(R)ight or (L)eft?")

    validDirections = ['r', 'right', 'l', 'left']

    direction = ah.choiceCheck(validDirections)

    if direction == 'r':

        areas.goToTown(beenToTown)

    else:

        areas.goToWoods()

    #
    # Unfinished
    #


if __name__ == '__main__':
    pass
    # Calls main function on module import!
    #main()
