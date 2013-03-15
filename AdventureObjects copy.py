#
# Contains initializers for all objects in the game and associated functions.
#
# Unfinished
#

import random

class CharacterSetup:
    '''Creates a character with atributes and all!'''

    def __init__(self, name, raceChoice, classChoice):

        self.Name = name
        self.level = 1
        self.experience = 0
        self.Race = raceChoice
        self.Class = classChoice
        self.maxHealth = 100.0
        self.armour = None
    
        if raceChoice == '1':

            self.strength = 7.5
            self.swiftness = 5.0
            self.defense = 5.0
            self.meleeAbility = 7.5
            self.rangeAbility = 7.5
            self.magicAbility = 5.0
            self.magicPoints  = 50.0

        elif raceChoice == '2':

            self.strength = 5.0
            self.swiftness = 7.5
            self.defense = 4.0
            self.meleeAbility = 5.0
            self.rangeAbility = 10.0
            self.magicAbility = 7.5
            self.magicPoints = 75.0

        elif raceChoice == '3':

            self.strength = 10.0
            self.swiftness = 2.5
            self.defense = 6.0
            self.meleeAbility = 10.0
            self.rangeAbility = 2.5
            self.magicAbility = 2.5
            self.magicPoints = 25.0


        if classChoice == '1':

            self.maxHealth += 10.0
            self.strength += 5.0
            self.swiftness -= 1.0
            self.defense += 2.0
            self.meleeAbility += 2.5
            self.rangeAbility += 1.5
            self.magicAbility += 0
            self.magicPoints += 0

        elif classChoice == '2':

            self.maxHealth -= 10.0
            self.strength -= 2.0
            self.defense -= 1.0
            self.swiftness += 2.5
            self.meleeAbility -= 2.0
            self.rangeAbility -= 1.0
            self.magicAbility += 5.0
            self.magicPoints += 25.0
        
        elif classChoice == '3':

            self.maxHealth += 5.0
            self.strength += 1.0
            self.defense += 1.0
            self.swiftness += 5.0
            self.meleeAbility += 2.0
            self.rangeAbility += 1.0
            self.magicAbility += 0
            self.magicPoints -= 25.0

        elif classChoice == '4':

            self.maxHealth += 5.0
            self.strength += 0
            self.defense -= 1.0
            self.swiftness += 2.5
            self.meleeAbility += 1.0
            self.rangeAbility += 2.5
            self.magicAbility += 1.0
            self.magicPoints += 15.0

        self.stats = [{'Level':self.level}, {'Experience':self.experience}, {'Max Health':self.maxHealth}, {'Strength':self.strength}, {'Swiftness':self.swiftness}, {'Defense':self.defense}, {'Melee Ability':self.meleeAbility}, {'Range Ability':self.rangeAbility}, {'Magic Ability':self.magicAbility}, {'Magic Points':self.magicPoints}]


class Pack:
    '''Creates a character's initial inventory.'''
    
    def __init__(self):
        
        self.Inventory = {}

        self.Inventory['Food'] = [['apple', 1]]
        self.Inventory['Weapons'] = [['wood sword', 1]]
        self.Inventory['Potions'] = []
        self.Inventory['Runes'] = []
        self.Inventory['Coins'] = 5


def createWeapon(wType):
    '''Master function for creating weapon objects'''
    
    if wType == 'woodsword':

        return WoodSword()

    elif wType == 'sword':

        return Sword()

    elif wType == 'bow':

        return Bow()

    elif wType == 'staff':

        return Staff()

    elif wType == 'magic staff':

        return MagicStaff()

    elif wType == 'mace':

        return Mace()

    elif wType == 'dagger':

        return Dagger()


class Sword:
    '''Sword weapon object.'''
    def __init__(self):

        self.meleeDamage = 15
        self.rangeDamage = 0
        self.armourPierceCoefficient = 2.5
        self.bleedProb = 0.3
        self.blockHelp = 2.5
        self.magicUse = False
        
        self.description = 'An iron sword. Great for cutting things!'


class WoodSword:
    '''Wooden sword weapon object.'''
    def __init__(self):

        self.meleeDamage = 5.0
        self.rangeDamage = 0
        self.armourPierceCoefficient = 0.5
        self.bleedProb = 0
        self.blockHelp = 1.0
        self.magicUse = False

        self.description = 'A crappy wooden sword. Not good for very much...'


class Bow:
    '''Bow weapon object.'''
    def __init__(self):

        self.meleeDamage = 2.0
        self.rangeDamage = 10.0
        self.armourPierceCoefficient = 2.0
        self.bleedProb = 0.1
        self.blockHelp = 0
        self.magicUse = False

        self.description = 'A simple wooden bow. Good for range attack!'


class Staff:
    '''Staff weapon object.'''
    def __init__(self):

        self.meleeDamage = 7.5
        self.rangeDamage = 0
        self.armourPierceCoefficient = 0
        self.bleedProb = 0
        self.blockHelp = 2.0
        self.magicUse = True
        self.deathRuneUse = False
        self.magicBenefit = 5.0

        self.description = 'A simple wooden staff. Decent for melee, decent for magic! Cannot be used for death runes.'


class MagicStaff:
    '''A magic staff object.'''
    def __init__(self):

        self.meleeDamage = 7.5
        self.rangeDamage = 0
        self.armourPierceCoefficient = 0
        self.bleedProb = 0
        self.blockHelp = 2.0
        self.magicUse = True
        self.deathRuneUse = True
        self.magicBenefit = 15.0

        self.description = 'A magic staff. Great for magic use! Required for death runes.'

        
class Mace:
    '''Mace weapon object.'''
    def __init__(self):

        self.meleeDamage = 17.5
        self.rangeDamage = 0
        self.armourPierceCoefficient = 1.5
        self.bleedProb = 0.15
        self.blockHelp = 1.0
        self.magicUse = False

        self.description = 'An iron mace. Great for melee combat!'


class Dagger:
    '''Dagger weapon object.'''
    def __init(self):

        self.meleeDamage = 12.0
        self.rangeDamage = 0
        self.armourPierceCoefficient = 4.0
        self.bleedProb = 0.4
        self.blockHelp = 1.0
        self.magicUse = False

        self.description = 'An iron dagger. Great for melee combat!'

class Arrow:
    '''An arrow used for bows'''
    def __init__(self):
        
        self.damage = 10

        self.description = 'An arrow for a bow!'

class TrollClaws:
    '''The claws of a Cave Troll!'''
    def __init__(self):

        self.damage = 17.5

class Rune:
    '''A rune for magic'''
    def __init__(self, rType):

        if rType == 'fire':

            self.type = 'fire'
            self.damage = 12.5
            self.burn = True
            self.freeze = False
            self.instaDeathProb = 0.15

            self.description = 'A fire rune that causes burns.'

        elif rType == 'water':

            self.type = 'water'
            self.damage = 7.5
            self.burn = False
            self.freeze = False
            self.instaDeathProb = 0

            self.description = 'A water rune.'
            
        elif rType == 'ice':

            self.type = 'ice'
            self.damage = 10.0
            self.burn = False
            self.freeze = True
            self.instaDeathProb = 0.05

            self.description = 'An ice rune that causes freezing.'

        elif rType == 'death':

            self.type = 'death'
            self.damage = 25.0
            self.burn = False
            self.freeze = False
            self.instaDeathProb = 0.25

            self.description = 'A death rune that is very powerful. Prone to causing instant death!'


class Apple:
    '''A food object.'''

    def __init__(self):

        self.healthBenefit = 5.0
        self.Tasty = True


class Pie:
    '''A food object'''

    def __init__(self):

        self.healthBenefit = 7.5
        self.Tasty = True


class Cabbage:
    '''A food object'''

    def __init__(self):

        self.healthBenefit = 2.5
        self.Tasty = False


class Carrot:
    '''A food object'''

    def __init__(self):

        self.healthBenefit = 2.5
        self.Tasty = True


class MeatStew:
    '''A food object'''

    def __init__(self):

        self.healthBenefit = 10.0
        self.Tasty = True


class Beer:
    '''A food object'''

    def __init__(self):

        self.healthBenefit = 3.0
        self.Tasty = True


class HealthPotion:
    '''A potion object'''

    def __init__(self):

        self.healthBenefit = 25.0
        self.taste = "Eww... tastes like cough syrup."

class MagicPotion:
    '''A potion object'''

    def __init__(self):

        self.magicBenefit = 25.0
        self.taste = "Tastes kind of like... glitter."


class StrenghtPotion:
    '''A potion object'''

    def __init__(self):

        self.strenghtBenefit = 2.5
        self.taste = "Tastes like POWER!"


class Ogre:

    def __init__(self):

        self.health = 75
        self.weapon = Mace()
        self.meleeDamage = self.weapon.meleeDamage

        self.dropItems = ['apple', 'cabbage', 'meat stew', 'mace', 'health potion']

        self.description = 'An ugly ogre'

    def attack(self):

        return round(self.meleeDamage * random.uniform(0.5, 1.5))

    def dropItem(self):

        return random.choice(self.dropItems)


class Goblin:

    def __init__(self):

        self.health = 40
        self.weapon = WoodSword()
        self.meleeDamage = self.weapon.meleeDamage

        self.dropItems = ['carrot', 'cabbage', 'wooden sword']

        self.description = 'An ugly goblin'

    def attack(self):

        return round(self.meleeDamage * random.uniform(0.5, 1.5))

    def dropItem(self):

        return random.choice(self.dropItems)


class CaveTroll:

    def __init__(self):

        self.health = 80
        self.weapon = TrollClaws()
        self.meleeDamage = self.weapon.damage

        self.dropItems = ['cabbage', 'magic potion']

        self.description = 'An ugly cave troll'

    def attack(self):

        return round(self.meleeDamage * random.uniform(0.5, 1.5))

    def dropItem(self):

        return random.choice(self.dropItems)


class Mage:

    def __init__(self):

        self.health = 60
        self.weapon = Staff()
        self.meleeDamage = self.weapon.meleeDamage

        self.dropItems = ['carrot', 'apple', 'magic potion', 'staff', 'magic staff']

        self.description = 'An evil mage'

    def attack(self):

        return round(self.meleeDamage * random.uniform(0.5, 1.5))

    def dropItem(self):

        return random.choice(self.dropItems)


class Bandit:

    def __init__(self):

        self.health = 50
        self.weapon = Dagger()
        self.meleeDamage = self.weapon.meleeDamage

        self.dropItems = ['cabbage', 'dagger']

        self.description = 'A rouge bandit'

    def attack(self):

        return round(self.meleeDamage * random.uniform(0.5, 1.5))

    def dropItem(self):

        return random.choice(self.dropItems)

        
class Warrior:

    def __init__(self):

        self.health = 80
        self.weapon = Sword()
        self.meleeDamage = self.weapon.meleeDamage

        self.dropItems = ['meat stew', 'sword', 'dagger', 'health potion', 'strength potion']

        self.description = 'A lone warrior'

    def attack(self):

        return round(self.meleeDamage * random.uniform(0.5, 1.5))

    def dropItem(self):

        return random.choice(self.dropItems)


class DarkElf:

    def __init__(self):

        self.health = 65
        self.weapon = MagicStaff()
        self.meleeDamage = self.weapon.meleeDamage

        self.dropItems = ['fire runes', 'death runes', 'dagger', 'cabbage', 'pie', 'magic staff', 'staff']

        self.description = 'An evil dark elf'

    def attack(self):

        return round(self.meleeDamage * random.uniform(0.5, 1.5))

    def dropItem(self):

        return random.choice(self.dropItems)

