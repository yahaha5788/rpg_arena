from random import randint

class characterBase:
    def __init__(self, name, strength, health, maxhealth, defense, speed, focus, constitution, dexterity, accuracy, weight, target, usern):
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

    def isAlive(self):
        return self.health > 0

    def takeDamage(self, damage):
        damage_taken = damage - self.defense
        self.health -= damage_taken
        return damage_taken

    def takeDamageFromMagic(self, damage):
        damage_taken = damage - self.constitution
        self.health -= damage_taken
        return damage_taken

    def getStrengthVariation(self):
        variation = randint(-3, 3)
        finalstr = self.strength + variation
        return finalstr

    def punchAttack(self, target):
        damage = 1.3 * self.getStrengthVariation()
        damage_dealt = target.takeDamage(damage)
        return damage_dealt

    def kickAttack(self, target):
        hits = randint(0, self.accuracy)
        if hits != 0:
            damage = 1.5 * self.strength
            damage_dealt = target.takeDamage(damage)
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
            return damage_dealt
        else:
            print(f"{self.usern}'s attack missed!")
            self_damage = self.health / 13
            self.health -= self_damage
            print(f"{self.usern} did {self_damage} damage to themselves")
            return self_damage

    def damageCounter(self, damage):
        print(f"{self.usern}")