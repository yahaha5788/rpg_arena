from arenacharacters import human
from arenacharacters import knight
from arenacharacters import brute
from arenacharacters import elf
from arenacharacters import werewolf

#initializations for characters
human1 = human("Human1", 11, 100, 100, 10, 10, 10,10 ,17, 8, 180, 'player2', 'Player 1', 'Player 2')
human2 = human("Human2", 11, 100, 100, 10, 10, 10,10 ,17, 8, 180,'player1', 'Player 2', 'Player 1')
knight1 = knight("Knight1", 13, 100, 100, 11, 7, 9, 8, 13, 9, 215, 'player2', 'Player 1', 'Player 2')
knight2 = knight("Knight2", 13, 100, 100, 11, 7, 9, 8, 13, 9, 215,'player1', 'PLayer 2', 'Player 1')
brute1 = brute("Brute1", 15, 90, 90, 9, 9, 8, 7, 14, 8, 195,'player2', "Player 1", 'Player 2')
brute2 = brute("Brute2", 15, 90, 90, 9, 9, 8, 7, 14, 8, 195,'player1', 'Player 2', 'Player 1')
elf1 = elf("Elf1", 9, 100, 100, 10, 13, 12, 13, 11, 8, 145, 'player2', 'Player 1', 'Player 2')
elf2 = elf("Elf2", 9, 100, 100, 10, 13, 12, 13, 11, 8, 145,'player1', 'Player 2', 'Player 1')
werewolf1 = werewolf("Werewolf1", 11, 100, 100, 9, 12, 9, 8, 12, 9, 170, False, 6, 0, 'player2', 'Player 1', 'Player 2')
werewolf2 = werewolf("Werewolf2", 11, 100, 100, 9, 12, 9, 8, 12, 9, 170, False, 6, 0, 'player1', 'Player 2', 'Player 1')

choosing1 = True
choosing2 = True
playing = True

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

    player1.target = player2
    player2.target = player1

    while player1.isAlive() and player2.isAlive():
        turn_number = 0
        print("Player 1's turn")
        player1.moveSelect()
        print("Player 2's turn")
        player2.moveSelect()
        print(f"Player 1's health ({character1}): " + str(player1.health))
        print(f"Player 2's health ({character2}): " + str(player2.health))
        turn_number += 1
        print(f'Number of turns so far: {turn_number}')

    if player1.isAlive and not player2.isAlive():
        print("Player 1 wins!")

    elif player2.isAlive and not player1.isAlive():
        print("Player 2 wins!")

    playagain = input("Would you like to play again? Y/N")
    if playagain.lower == 'y':
        print("Again!")
    else:
        playing = False
