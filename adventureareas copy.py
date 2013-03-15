#
# This module contains functions devoted to presenting setting contexts.
#

import time as t
import AdventureHelpers as ah

def goToTown(beenToTown):
    '''Places character in town. Will contain options to navigate through town.'''

    for i in range(3):
        print("...")
        t.sleep(.5)

    if beenToTown == False:

        beenToTown = True

        print("Welcome to Valenall! My name is Sildor, the Earl's steward.\n It appears it is your first time here, is that correct?")
        
        valid = ['yes', 'no', 'y', 'n']

        answer = ah.choiceCheck(valid)

        if answer == 'yes' or answer == 'y':

            print
            print("Excellent! I will take you on a tour of Valenall right away.")
            townTour()

        else:

            print
            print("Of course, I'll let you be on your way then!")

    #
    # Unfinished
    #


def townTour():
    '''Runs through a tour of the town.'''
    
    print
    print("We'll start with the lower disctrict. If you could follow me please.")

    for i in range(3):
        print("...")
        t.sleep(.5)

    print("Here on our left is the smithy. Here you can purchase all manner of weapons.")

    t.sleep(.25)
    print
    print("And on our right you'll see the general store where you can purchase\n food and potions.")

    t.sleep(.25)
    print
    print("And finally, up ahead we have the Mage's Guild. There you can purcahse\n runes for use in magical combat.")

    t.sleep(.25)
    print
    print("Alright then, that's the lower district. I'll show you up to the Earl's Castle next.")

    for i in range(3):
        print("...")
        t.sleep(.5)

    print
    print("Here we are, the Earl's Castle!")
    print
    print("*walks in door*")

    t.sleep(.25)

    #
    # Unfinished
    #
    
