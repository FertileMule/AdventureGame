#
# All helper functions used in Adventure game are in this module.
#
# Unfinished
#

def choiceCheck(valid):
    '''Takes a list of valid choices and asks for user input.
        Returns user choice if valid, else repeats prompt.'''

    while True:

        print
        choice = raw_input("... ").lower()

        if choice in valid:

            break

        else:

            print("That's not a valid choice!")
            continue

    return choice


def levelUp(c):
    '''Level's up the user's character and updates the stat list.'''
    
    c.level += 1
    c.maxHealth += 10
    c.strength += 1.0
    c.swiftness += 1.0
    c.defense += 1.0
    c.meleeAbility += 1.0
    c.rangeAbility += 1.0
    c.magicAbility += 1.0
    c.magicPoints += 10

    c.stats = [{'Level':c.level}, {'Experience':c.experience}, {'Max Health':c.maxHealth}, {'Strength':c.strength}, {'Swiftness':c.swiftness}, {'Defense':c.defense}, {'Melee Ability':c.meleeAbility}, {'Range Ability':c.rangeAbility}, {'Magic Ability': c.magicAbility}, {'Magic Points':c.magicPoints}]

    print
    print("Congratulations! You're now level {}!".format(c.level))
    print("You can view your stats at the in game menu!")


def printStats(statList):
    '''Prints the character's stats list.'''

    print

    for element in statList:

        print str(element)[1:len(str(element))-1]

