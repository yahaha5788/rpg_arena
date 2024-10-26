from random import randint
from .character import characterBase

class centaur(characterBase):

    def __init__(self, c, name, strength, health, maxhealth, defense, speed, focus, constitution, dexterity, accuracy, weight, target, usern, targetn, arrows):
        self.name = name
        self.c = c
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
        self.arrows = arrows

    def shootArrow(self, target):
        thisdoesstuff = True