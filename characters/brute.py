from charBase.character import characterBase
from random import randint
from engine import usern, target
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
