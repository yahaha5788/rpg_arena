from charBase.character import characterBase
from random import randint

class elf(characterBase):

    def magicAttack(self, target):
        damage = self.focus * 1.3
        damage_dealt = target.takeDamageFromMagic(damage)
        self.damageCounter(damage_dealt)
        return damage_dealt

    def heal(self):
        damage_healed = randint(4, 9)
        if damage_healed + self.health > self.maxhealth:
            print("Healing Failed!")
            return 0
        else:
            self.health += damage_healed
            print(f"{self.usern} healed {damage_healed} damage")
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
                self.punchAttack(self.target); break
            elif move.lower() == 'kick':
                self.kickAttack(self.target); break
            elif move.lower() == 'bodyslam':
                self.bodyslamAttack(self.target); break
            elif move.lower() == 'magic':
                self.magicAttack(self.target); break
            elif move.lower() == 'heal':
                self.heal(); break
            else:
                print('Invalid input.')

        return 0