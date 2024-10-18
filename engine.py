from arenacharacters import human, human1, human2
from arenacharacters import knight, knight1, knight2
from arenacharacters import brute, brute1, brute2
from arenacharacters import elf, elf1, elf2
from arenacharacters import werewolf, werewolf1, werewolf2
from arenacharacters import dwarf, dwarf1, dwarf2
from arenacharacters import golem, golem1, golem2

choosing1 = True
choosing2 = True
playing = True

def checkIfAlive():
    if player1.isAlive() == False:
        exit("Player 2 wins!")
    elif player2.isAlive() == False:
        exit('Player 1 wins!')

while playing:
    print("""
    Human
    Elf
    Brute
    Knight
    Werewolf
    Dwarf
    Golem (Untested)
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
        elif select1.lower() == 'dwarf':
            player1 = dwarf1
            character1 = "Dwarf"
            break
        elif select1.lower() == 'golem':
            player1 = golem1
            character1 = 'Golem'
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
        elif select2.lower() == 'dwarf':
            player2 = dwarf2
            character2 = "Dwarf"
            break
        elif select2.lower() == 'golem':
            player2 = golem2
            character2 = 'Golem'
            break
        else:
            print("Invalid input")

    player1.target = player2 #assigns the targets
    player2.target = player1
    turn_number = 0

    while player1.isAlive() and player2.isAlive():

        print("Player 1's turn")
        player1.moveSelect() #Player 1 attacks
        checkIfAlive()
        print("Player 2's turn")
        player2.moveSelect() #player 2 attacks
        checkIfAlive()
        print(f"Player 1's health ({character1}): " + str(player1.health))
        print(f"Player 2's health ({character2}): " + str(player2.health))
        turn_number += 1
        print(f'Number of turns so far: {turn_number}')

