from random import randint
from math import ceil as ceiling

#base for all characters

class characterBase:
    def __init__(self, name, strength, health, maxhealth, defense, speed, focus, constitution, dexterity, accuracy, weight, state, morphtimeavailable):
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
        self.state = state
        self.morphtimeavailable = morphtimeavailable
        self.weight = weight #used for bodyslam

    def getStats(self):
        print("Stats for " + self.name + ":")
        print("Strength: " + self.strength)
        print("Health: " + self.health)
        print("Defense: " + self.defense)
        print("Speed: " + self.speed)
        print("Focus: " + self.focus)
        print("Dexterity: " + self.dexterity)
        print("Constitution: " + self.constitution)
        print("Accuracy: " + self.accuracy)

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
            print(f"{usern}'s attack missed!")
            return 0

    def bodyslamAttack(self, target):
        hits = randint(0, 4)
        if hits == 0:
            damagemultiplier = self.weight / 16
            damage = 1.8 * damagemultiplier
            damage_dealt = target.takeDamage(damage)
            self_damage = self.health / 18
            self.health -= self_damage
            return damage_dealt
        else:
            print(f"{usern}'s attack missed!")
            self_damage = self.health / 18
            self.health -= self_damage
            return 0

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

class human(characterBase):

    def stabAttack(self, target):
        hits = randint(0, self.accuracy + 3)
        if hits != 0:
            damage = self.strength * 1.3
            damage_dealt = target.takeDamage(damage)
            return damage_dealt
        else:
            print(f"{usern}'s move missed!")
            return 0

    def slashAttack(self, target):
        hits = randint(0, self.accuracy)
        if hits != 0:
            avgmultiplier = self.strength * self.dexterity
            avgmultiplier /= 13
            damage = 1.3 * avgmultiplier
            damage_dealt = target.takeDamage(damage)
            return damage_dealt
        else:
            print(f"{usern}'s move missed!")
            return 0

    def moveSelect(self):
        choosingmove = True

        while choosingmove:
            move = input("""
            Available moves:

            Punch
            KicK
            Bodyslam
            Stab
            Slash

            Select your move: 
            """)
            if move.lower() == 'punch':
                self.punchAttack(target); break
            elif move.lower() == 'kick':
                self.kickAttack(target); break
            elif move.lower() == 'bodyslam':
                self.bodyslamAttack(target); break
            elif move.lower() == 'stab':
                self.stabAttack(target); break
            elif move.lower() == 'slash':
                self.slashAttack(target); break
            else:
                print('Invalid input.')

        return 0

class knight(characterBase): #knight has high strength and defense, 100 health, low focus and constitution and midrange but not good dexterity

    def stabAttack(self, target):
        hits = randint(0, self.accuracy - 1)
        if hits != 0:
            damage = self.strength * 1.5
            damage_dealt = target.takeDamage(damage)
            return damage_dealt
        else:
            print(f"{usern}'s move missed!")
            return 0

    def slashAttack(self, target):
        hits = randint(0, self.accuracy)
        if hits != 0:
            avgmultiplier = self.strength * self.dexterity
            avgmultiplier /= 13
            damage = 1.6 * avgmultiplier
            damage_dealt = target.takeDamage(damage)
            return damage_dealt
        else:
            print(f"{usern}'s move missed!")
            return 0

    def moveSelect(self):
        choosingmove = True

        while choosingmove:
            move = input("""
            Available moves:

            Punch
            Kick
            Bodyslam
            Stab
            Slash

            Select your move: 
            """)
            if move.lower() == 'punch':
                self.punchAttack(target); break
            elif move.lower() == 'kick':
                self.kickAttack(target);break
            elif move.lower() == 'bodyslam':
                self.bodyslamAttack(target); break
            elif move.lower() == 'stab':
                self.stabAttack(target); break
            elif move.lower() == 'slash':
                self.slashAttack(target); break
            else:
                print('Invalid input.')

        return 0

class brute(characterBase):

    def overpower(self, target):
        hits = randint(0, 3)
        if hits == 0:
            damage = self.strength * 1.7
            damage_dealt = target.takeDamage(damage)
            self_damage = ceiling(damage_dealt / 17)
            self.health -= self_damage
            return damage_dealt
        else:
            print(f"{usern}'s move missed!")

    def moveSelect(self):
        choosingmove = True

        while choosingmove:
            move = input("""
            Available moves:

            Punch
            KicK
            Bodyslam
            Overpower

            Select your move: 
            """)
            if move.lower() == 'punch':
                self.punchAttack(target); break
            elif move.lower() == 'kick':
                self.kickAttack(target); break
            elif move.lower() == 'bodyslam':
                self.bodyslamAttack(target); break
            elif move.lower() == 'overpower':
                self.overpower(target); break
            else:
                print('Invalid input.')

        return 0

class elf(characterBase):

    def magicAttack(self, target):
        damage = self.focus * 1.3
        damage_dealt = target.takeDamageFromMagic(damage)
        return damage_dealt

    def heal(self):
        damage_healed = randint(7, 13)
        if damage_healed + self.health > self.maxhealth:
            print("Healing Failed!")
            return 0
        else:
            self.health += damage_healed
            return damage_healed

    def moveSelect(self):
        choosingmove = True

        while choosingmove:
            move = input("""
            Available moves:

            Punch
            KicK
            Bodyslam
            Magic
            Heal

            Select your move: 
            """)
            if move.lower() == 'punch':
                self.punchAttack(target); break
            elif move.lower() == 'kick':
                self.kickAttack(target); break
            elif move.lower() == 'bodyslam':
                self.bodyslamAttack(target); break
            elif move.lower() == 'magic':
                self.magicAttack(target); break
            elif move.lower() == 'heal':
                self.heal(); break
            else:
                print('Invalid input.')

        return 0

class werewolf(characterBase):

    def morph(self):
        if self.state != 'wolf':
            self.state = 'wolf'
            if self.name == 'Werewolf1':
                p1morphturnsleft = self.morphtimeavailable
                p1morphed = True
            elif self.name == 'Werewolf2':
                p2morphturnsleft = self.morphtimeavailable
                p2morphed = True
            else:
                print('you fucking messed something up')
        else:
            print('You are already morphed.')

    def bite(self, target):
        if self.state == 'wolf':
            accuracy = self.accuracy
            hits = randint(0,accuracy)
            if hits != 0:
                damage = self.strength * 1.2
                damage_dealt = target.takeDamage(damage)
                return damage_dealt
            else:
                print(f"{usern}'s move missed!")
        else:
            print("You are not morphed!")

    def scratch(self, target):
        if self.state == 'wolf':
            accuracy = self.accuracy - 3
            hits = randint(0, accuracy)
            if hits != 0:
                damage = self.strength * 1.5
                damage_dealt = target.takeDamage(damage)
                return damage_dealt
            else:
                print(f"{usern}'s move missed!")
        else:
            print("You are not morphed!")

    def moveSelect(self):
        choosingmove = True

        while choosingmove:
            if usern == 'Player 1':
                if p1morphed == True:
                    move = input("""
                                Available moves:

                                Punch
                                KicK
                                Bodyslam
                                Morph
                                Bite
                                Scratch

                                Select your move: 
                                """)
                else:
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
            elif usern == 'Player 2':
                if p2morphed == True:
                    move = input("""
                                Available moves:

                                Punch
                                KicK
                                Bodyslam
                                Morph
                                Bite
                                Scratch

                                Select your move: 
                                """)
                else:
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
                self.punchAttack(target); break
            elif move.lower() == 'kick':
                self.kickAttack(target); break
            elif move.lower() == 'bodyslam':
                self.bodyslamAttack(target); break
            elif move.lower() == 'morph':
                self.morph(); break
            elif move.lower() == 'bite':
                self.bite(target); break
            elif move.lower() == 'scratch':
                self.scratch(target); break
            else:
                print('Invalid input.')

        return 0

#add variable strength stats for moves (using randint to decide plus/minus)
human1 = human("Human1", 11, 100, 100, 10, 10, 10,10 ,17, 8, 180, "normal", 0)
human2 = human("Human2", 11, 100, 100, 10, 10, 10,10 ,17, 8, 180,"normal", 0)
knight1 = knight("Knight1", 13, 100, 100, 12, 7, 9, 8, 13, 9, 215, "normal", 0)
knight2 = knight("Knight2", 13, 100, 100, 12, 7, 9, 8, 13, 9, 215,"normal", 0)
brute1 = brute("Brute1", 15, 90, 90, 9, 9, 8, 7, 14, 8, 195,"normal", 0)
brute2 = brute("Brute2", 15, 90, 90, 9, 9, 8, 7, 14, 8, 195,"normal", 0)
elf1 = elf("Elf1", 9, 100, 100, 10, 13, 12, 13, 11, 8, 145, "normal", 0)
elf2 = elf("Elf2", 9, 100, 100, 10, 13, 12, 13, 11, 8, 145,"normal", 0)
werewolf1 = werewolf("Werewolf1", 11, 100, 100, 9, 12, 9, 8, 12, 9, 170, "normal", 6)
werewolf2 = werewolf("Werewolf2", 11, 100, 100, 9, 12, 9, 8, 12, 9, 170, "normal", 6)

playing = True
choosing1 = True
choosing2 = True
p1morphturnsleft = 0
p2morphturnsleft = 0
p1morphed = False
p2morphed = False

while playing:
    print("""
    Human
    Elf
    Brute
    Knight
    Werewolf
    """)

    while choosing1:
        select1 = input("Player 1, select your character: """)
        if select1.lower() == 'human':
            player1 = human1
            character1 = "Human"
            break
        elif select1.lower() == 'elf':
            player1 = elf1
            character1 = "Elf"
            break
        elif select1.lower() == 'brute':
            player1 = brute1
            character1 = "Brute"
            break
        elif select1.lower() == 'knight':
            player1 = knight1
            character1 = "Knight"
            break
        elif select1.lower() == 'werewolf':
            player1 = werewolf1
            character1 = "Werewolf"
            break
        else:
            print("Invalid input")

    while choosing2:
        select2 = input("Player 2, select your character: ")
        if select2.lower() == 'human':
            player2 = human2
            character2 = "Human"
            break
        elif select2.lower() == 'elf':
            player2 = elf2
            character2 = "Elf"
            break
        elif select2.lower() == 'brute':
            player2 = brute2
            character2 = "Brute"
            break
        elif select2.lower() == 'knight':
            player2 = knight2
            character2 = "Knight"
            break
        elif select2.lower() == 'werewolf':
            player2 = werewolf2
            character2 = 'Werewolf'
            break
        else:
            print("Invalid input")

    while player1.isAlive() and player2.isAlive():
        turn_number = 0
        print("Player 1's turn")
        target = player2; user = player1; usern = 'Player 1'
        player1.moveSelect()
        print("Player 2's turn")
        target = player1; user = player2; usern = 'Player 2'
        player2.moveSelect()
        print(f"Player 1's health ({character1}): " + str(player1.health))
        print(f"Player 2's health ({character2}): " + str(player2.health))
        turn_number += 1
        print(f'Number of turns so far: {turn_number}')
        if character1 or character2 == 'Werewolf':
            if player1.name == 'Werewolf1':
                p1morphturnsleft -= 1
                if p1morphturnsleft  <= 0:
                    p1morphed = False
            if player2.name == 'Werewolf2':
                p2morphturnsleft -= 1
                if p2morphturnsleft <= 0:
                    p2morphed = False

    if player1.isAlive and not player2.isAlive():
        print("Player 1 wins!")

    elif player2.isAlive and not player1.isAlive():
        print("Player 2 wins!")

    playagain = input("Would you like to play again? Y/N")
    if playagain.lower == 'y':
        print("Again!")
    else:
        playing = False
