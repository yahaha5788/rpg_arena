from .character import characterBase
from random import randint

class golem(characterBase):

    def __init__(self, name, strength, health, maxhealth, defense, speed, focus, constitution, dexterity, accuracy, weight, target, usern, targetn, minweight, isgolem):
        self.name = name
        self.strength = strength #multiplier for physical moves, should be around 10
        self.health = health #health should be at least 100
        self.maxhealth = maxhealth #maxhealth should be the same as health, used for healing moves
        self.defense = defense #defense should be around 10
        self.speed = speed #speed is out of 10, unused so far
        self.focus = focus #focus is a number from 10 to 20,
        self.dexterity = dexterity #dexterity is a number from 10 to 20, stat for handheld item accuracy (stab, slash attacks)
        self.constitution = constitution #constitution should be a number around 10, is defense for takeDamageFromMagic
        self.accuracy = accuracy #accuracy is a number around 7 - 9, used in randint(0, accuracy) to check if the move hits or not
        self.weight = weight #used for bodyslam
        self.target = target
        self.usern = usern
        self.targetn = targetn
        self.minweight = minweight
        self.isgolem = isgolem

    def rockWtVariation(self):
        r = randint(10, 17)
        return r

    def loseRock(self, r):
        self.weight -= r
        if self.weight <= self.minweight:
            self.isgolem = False
        else:
            self.isgolem = True

    def rockSmash(self, target):
        if self.isgolem:
            wt = self.weight / 20
            avgmultiplier = self.getStrengthVariation() * wt
            damage = avgmultiplier / 15
            damage_dealt = target.takeDamage(damage)
            self.loseRock(self.rockWtVariation())
            return damage_dealt
        else:
            print(f"You don't have enough rock to use this move!")
            return 0

    def rockThrow(self, target):
        if self.isgolem:
            hits = randint(0, 7)
            if hits != 0:
                rockwt = randint(65, 75)
                damage = self.getStrengthVariation() * rockwt
                damage /= 58
                damage_dealt = target.takeDamage(damage)
                self.loseRock(rockwt)
                return damage_dealt
            else:
                print(f"{self.usern}'s move missed!")
                return 0
        else:
            print("You do not have enough rock to use this move!")
            return 0

    def moveSelect(self):
        choosingmove = True

        while choosingmove:
            move = input("""
            Available moves:

            Punch
            KicK
            Bodyslam
            Rock Smash
            Rock Throw 

            Select your move: 
            """)
            if move.lower() == 'punch':
                self.punchAttack(self.target); break
            elif move.lower() == 'kick':
                self.kickAttack(self.target); break
            elif move.lower() == 'bodyslam':
                self.bodyslamAttack(self.target); break
            elif move.lower() == 'rock smash':
                self.rockSmash(self.target); break
            elif move.lower() == 'rock throw':
                self.rockThrow(self.target); break
            else:
                print('Invalid input.')

        return 0