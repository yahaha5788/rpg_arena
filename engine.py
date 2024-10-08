from characters.human import human
from characters import knight
from characters import brute
from characters import elf
from characters import werewolf

human1 = human("Human1", 11, 100, 100, 10, 10, 10,10 ,17, 8, 180, "normal", 0)
human2 = human("Human2", 11, 100, 100, 10, 10, 10,10 ,17, 8, 180,"normal", 0)
knight1 = knight.knight("Knight1", 13, 100, 100, 12, 7, 9, 8, 13, 9, 215, "normal", 0)
knight2 = knight.knight("Knight2", 13, 100, 100, 12, 7, 9, 8, 13, 9, 215,"normal", 0)
brute1 = brute.brute("Brute1", 15, 90, 90, 9, 9, 8, 7, 14, 8, 195,"normal", 0)
brute2 = brute.brute("Brute2", 15, 90, 90, 9, 9, 8, 7, 14, 8, 195,"normal", 0)
elf1 = elf.elf("Elf1", 9, 100, 100, 10, 13, 12, 13, 11, 8, 145, "normal", 0)
elf2 = elf.elf("Elf2", 9, 100, 100, 10, 13, 12, 13, 11, 8, 145,"normal", 0)
werewolf1 = werewolf.werewolf("Werewolf1", 11, 100, 100, 9, 12, 9, 8, 12, 9, 170, "normal", 6)
werewolf2 = werewolf .werewolf("Werewolf2", 11, 100, 100, 9, 12, 9, 8, 12, 9, 170, "normal", 6)

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
