from charBase.character import characterBase
from random import randint

class werewolf(characterBase):

    def __init__(self, name, strength, health, maxhealth, defense, speed, focus, constitution, dexterity, accuracy, weight, morphed, morphtimeavailable, morphturnsleft, target, usern):
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
        self.morphed = morphed # True = morphed, False = not morphed
        self.morphtimeavailable = morphtimeavailable
        self.weight = weight #used for bodyslam
        self.target = target
        self.usern = usern
        self.morphturnsleft = morphturnsleft #set to 0


    def morph(self, turns):
        if self.morphed == False:
            self.morphed = True
            self.morphturnsleft = turns
        else:
            print('You are already morphed.')

    def bite(self, target):
        if self.morphed == True:
            accuracy = self.accuracy
            hits = randint(0,accuracy)
            if hits != 0:
                damage = self.strength * 1.2
                damage_dealt = target.takeDamage(damage)
                return damage_dealt
            else:
                print(f"{self.usern}'s move missed!")
        else:
            print("You are not morphed!")

    def scratch(self, target):
        if self.morphed == True:
            accuracy = self.accuracy - 3
            hits = randint(0, accuracy)
            if hits != 0:
                damage = self.strength * 1.5
                damage_dealt = target.takeDamage(damage)
                return damage_dealt
            else:
                print(f"{self.usern}'s move missed!")
        else:
            print("You are not morphed!")

    def checkMorph(self, turnsleft, ismorphed):
        if turnsleft == 0 and ismorphed == True: #when the player runs out of morph turns
            self.morphed = False
            print('You are not morphed anymore!')
        elif turnsleft != 0 and ismorphed == True: # is morphed
            self.morphturnsleft -= 1
            print(f"You have {turnsleft} morph turns left.")
        else: #is not morphed
            self.morphed = False

    def moveSelect(self):
        choosingmove = True

        while choosingmove:
            move = input("""                          
            Available moves:

            Punch
            KicK
            Bodyslam
            Morph
            Bite (requires morph)
            Scratch (requires morph)

            Select your move: 
            """)
            if move.lower() == 'punch':
                self.punchAttack(self.target)
                self.checkMorph(self.morphturnsleft, self.morphed)
                break
            elif move.lower() == 'kick':
                self.kickAttack(self.target)
                self.checkMorph(self.morphturnsleft, self.morphed)
                break
            elif move.lower() == 'bodyslam':
                self.bodyslamAttack(self.target)
                self.checkMorph(self.morphturnsleft, self.morphed)
                break
            elif move.lower() == 'morph':
                self.morph(self.morphtimeavailable)
                self.checkMorph(self.morphturnsleft, self.morphed)
                break
            elif move.lower() == 'bite':
                self.bite(self.target)
                self.checkMorph(self.morphturnsleft, self.morphed)
                break
            elif move.lower() == 'scratch':
                self.scratch(self.target);
                self.checkMorph(self.morphturnsleft, self.morphed)
                break
            else:
                print('Invalid input.')

        return