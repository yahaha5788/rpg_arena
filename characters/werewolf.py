from charBase.character import characterBase
from random import randint
from engine import usern, target, p1morphed, p2morphed

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

        return