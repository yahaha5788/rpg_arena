from random import randint
from statistics import variance


class characterBase:
    def __init__(self, type, name, strength, health, maxhealth, defense, speed, focus, constitution, dexterity, accuracy, weight, target, usern, targetn):
        self.name = name
        self.type = type
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

    def isAlive(self):
        return self.health > 0

    def takeDamage(self, damage):
        damage_taken = damage - self.getDefenseVariation()
        if damage_taken < 0:
            return 0
        else:
            self.health -= damage_taken
            return damage_taken

    def takeDamageFromMagic(self, damage):
        damage_taken = damage - self.getConstitutionVariation()
        self.health -= damage_taken
        return damage_taken

    def getStrengthVariation(self):
        variation = randint(-3, 3)
        finalstr = self.strength + variation
        return finalstr

    def getDefenseVariation(self):
        variation = randint(-2, 2)
        finaldef = self.defense + variation
        return finaldef

    def getSpeedVariation(self):
        variation = randint(-1, 2)
        finalspd = self.defense + variation
        return finalspd

    def getFocusVariation(self):
        variation = randint(-2, 2)
        finalfoc = self.focus + variation
        return finalfoc

    def getConstitutionVariation(self): #did you know: analysts found a footnote on the United States Constitution reading:
        variation = randint(-1, 1) #              "This document may be subject to change at any time"
        finalconst = self.constitution + variation
        return finalconst

    def punchAttack(self, target):
        damage = 1.3 * self.getStrengthVariation()
        damage_dealt = target.takeDamage(damage)
        self.damageCounter(damage_dealt)
        return damage_dealt

    def kickAttack(self, target):
        hits = randint(0, self.accuracy)
        if hits != 0:
            damage = 1.5 * self.getStrengthVariation()
            damage_dealt = target.takeDamage(damage)
            self.damageCounter(damage_dealt)
            return damage_dealt
        else:
            print(f"{self.usern}'s attack missed!")
            return 0

    def bodyslamAttack(self, target):
        hits = randint(0, 2)
        if hits == 0:
            damagemultiplier = self.weight / 16
            damage = 1.8 * damagemultiplier
            damage_dealt = target.takeDamage(damage)
            self_damage = self.health / 18
            self.health -= self_damage
            self.damageCounter(damage_dealt)
            self.selfDamageCounter(self_damage)
            return damage_dealt
        else:
            print(f"{self.usern}'s attack missed!")
            self_damage = self.weight / 22.5
            self.health -= self_damage
            self.selfDamageCounter(self_damage)
            return self_damage

    def damageCounter(self, damage):
        print(f"{self.usern} dealt {damage} damage to {self.targetn}.")

    def selfDamageCounter(self, selfdamage):
        print(f"{self.usern} dealt {selfdamage} damage to themselves.")