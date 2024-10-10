from random import randint
from .character import characterBase

class dwarf(characterBase):

    def axeSlice(self, target):
        hits = randint(0, 9)
        if hits != 0:
            damageaverage = self.dexterity * self.getStrengthVariation()
            damageaverage /= 12
            damage = damageaverage * 1.3
            damage_dealt = target.takeDamage(damage)
            self.damageCounter(damage_dealt)
            return damage_dealt
        else:
            print(f"{self.usern}'s move missed!")
            return 0

    def moveSelect(self):
        choosingmove = True

        while choosingmove:
            move = input("""
            Available moves:

            Punch
            Kick
            Bodyslam
            Slice

            Select your move: 
            """)
            if move.lower() == 'punch':
                self.punchAttack(self.target); break
            elif move.lower() == 'kick':
                self.kickAttack(self.target); break
            elif move.lower() == 'bodyslam':
                self.bodyslamAttack(self.target); break
            elif move.lower() == 'slice':
                self.axeSlice(self.target); break
            else:
                print('Invalid input.')

        return 0
