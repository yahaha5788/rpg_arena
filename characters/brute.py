from charBase.character import characterBase
from random import randint
from math import ceil as ceiling

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
            print(f"{self.usern}'s move missed!")

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
                self.punchAttack(self.target); break
            elif move.lower() == 'kick':
                self.kickAttack(self.target); break
            elif move.lower() == 'bodyslam':
                self.bodyslamAttack(self.target); break
            elif move.lower() == 'overpower':
                self.overpower(self.target); break
            else:
                print('Invalid input.')

        return 0
