from .knight import knight
from .werewolf import werewolf
from .brute import brute
from .elf import elf
from .human import human
from .dwarf import dwarf

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
dwarf1 = dwarf("Dwarf1", 13, 90, 90, 13, 8, 8, 8, 12, 8, 200, 'player2', 'Player 1', 'Player 2')
dwarf2 = dwarf("Dwarf2", 13, 90, 90, 13, 8, 8, 8, 12, 8, 200, 'player1', 'Player 2', 'Player 1')