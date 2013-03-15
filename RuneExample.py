import random

# Magical Effect Functions. Can be wrappped in Spell or a Rune

def toad():
	def _toad(user, target):
		action_text.append = target.name + " has turned into a toad."
		target.description += "A lively toad. "

		return action_text
	return _toad
def burn(damage):
	def _burn(user, target):
		action_text = target.name + " has engulfed in a blaze!"
		target.take_damage(damage)
		target.description += "Engulfed in flame. "

		return action_text
	return _burn

def shock(damage):
	def _shock(user, target):
		action_text = target.name + " has been electrocuted!"
		target.take_damage(damage)
		target.description += "Singed. "

		return action_text
	return _shock

def death():
	def _death(user, target):
		action_text.append(target.name + " has fallen over from a sudden heart attack!")
		target.description += "Deceased. "

		return action_text

	return _death

class Rune:
	#Runes are one time use, and have built-in failure rate.
	def __init__(self, name, failure, description,*effects):
		self.name = name
		self.effects = effects
		self.description = description
		self.failure = failure
		self.used = False

	def use(self, user, target):
		action_text = [user.name + " cast "+self.name+" on " + target.name + "!"]
		if random.randint(1,100) > (self.failure * 100):
			action_text.append("It failed!")
			#role reversed if failure
			for effect in self.effects:
				action_text.append(effect(target, user)) 
		else:
			for effect in self.effects:
				action_text.append(effect(user, target))

		self.used = True

		for action in action_text:
			#this text can be handled locally, printed, or passed up to a GUI to handle.
			print action

class Spell:
	#Spells are multiple uses, and have failure rate based on magical proficiency.
	def __init__(self, name, difficulty, description, *effects):
		self.name = name
		self.func = effects
		self.difficulty = difficulty
		self.description = description

	def use(self, user, target):
		action_text = [user.name + " cast "+self.name+" on " + target.name + "!"]
		if random.randint(1, 100) > (user.magic_ability / self.difficulty):
			action_text.append("It failed!")
			for effect in self.effects:
				action_text.append(effect(target, user)) 
		else:
			for effect in self.effects:
				action_text.append(effect(user, target))

		for action in action_text:
			print action

class TestPerson:

	def __init__(self, name):
		self.name = name
		self.description = "Empty."
		self.magic_ability = 4

	def take_damage(self, damage):
		print self.name + " took " + str(damage)

def fire_rune():
	effects = burn(12.5)
	return Rune("Fire", 0.15, "A fire rune.", effects)

def multi_rune():
	effects = burn(12.5), shock(10.0)
	return Rune("Fire and Shock",  0.20, "A multi rune.", *effects)


person = TestPerson("Person")
baddie = TestPerson("Baddie")

person_rune = multi_rune()
baddie_rune = fire_rune()

print person.description
print baddie.description
person_rune.use(person, baddie)
baddie_rune.use(baddie, person)










