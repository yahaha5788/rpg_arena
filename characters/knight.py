from charBase.character import characterBase
from random import randint

class knight(characterBase):
    def stabAttack(self, target):
        hits = randint(0, self.accuracy - 1)
        if hits != 0:
            damage = self.strength * 1.5
            damage_dealt = target.takeDamage(damage)
            self.damageCounter(damage_dealt)
            return damage_dealt
        else:
            print(f"{self.usern}'s move missed!")
            return 0

    def slashAttack(self, target):
        hits = randint(0, self.accuracy)
        if hits != 0:
            avgmultiplier = self.strength * self.dexterity
            avgmultiplier /= 13
            damage = 1.6 * avgmultiplier
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
            Stab
            Slash

            Select your move: 
            """)
            if move.lower() == 'punch':
                self.punchAttack(self.target); break
            elif move.lower() == 'kick':
                self.kickAttack(self.target);break
            elif move.lower() == 'bodyslam':
                self.bodyslamAttack(self.target); break
            elif move.lower() == 'stab':
                self.stabAttack(self.target); break
            elif move.lower() == 'slash':
                self.slashAttack(self.target); break
            else:
                print('Invalid input.')

        return 0