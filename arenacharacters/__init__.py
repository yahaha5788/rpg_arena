from .knight import knight
from .werewolf import werewolf
from .brute import brute
from .elf import elf
from .human import human
from .dwarf import dwarf
from .golem import golem
from .centaur import centaur

human1=human(      'Human',   "Human1",   11,100,100,10,10,10,10 ,17,8, 180,'player2','Player 1','Player 2')
human2=human(      'Human',   "Human2",   11,100,100,10,10,10,10 ,17,8, 180,'player1','Player 2','Player 1')
knight1=knight(    'Knight',  "Knight1",  13,100,100,11,7, 9, 8,  13,9, 215,'player2','Player 1','Player 2')
knight2=knight(    'Knight',  "Knight2",  13,100,100,11,7, 9, 8,  13,9, 215,'player1','PLayer 2','Player 1')
brute1=brute(      'Brute',   "Brute1",   15,90, 90, 9, 9, 8, 7,  14,8, 195,'player2',"Player 1",'Player 2')
brute2=brute(      'Brute',   "Brute2",   15,90, 90, 9, 9, 8, 7,  14,8, 195,'player1','Player 2','Player 1')
elf1=elf(          'Elf',     "Elf1",     9, 100,100,10,13,12,13, 11,8, 145,'player2','Player 1','Player 2')
elf2=elf(          'Elf',     "Elf2",     9, 100,100,10,13,12,13, 11,8, 145,'player1','Player 2','Player 1')
werewolf1=werewolf('Werewolf',"Werewolf1",11,100,100,9, 12,9, 8,  12,9, 160,'player2','Player 1','Player 2',False, 6, 0)
werewolf2=werewolf('Werewolf',"Werewolf2",11,100,100,9, 12,9, 8,  12,9, 160,'player1','Player 2','Player 1',False, 6, 0)
dwarf1=dwarf(      'Dwarf',   "Dwarf1",   13,90, 90, 13,8, 8, 8,  12,8, 200,'player2','Player 1','Player 2')
dwarf2=dwarf(      'Dwarf',   "Dwarf2",   13,90, 90, 13,8, 8, 8,  12,8, 200,'player1','Player 2','Player 1')
golem1=golem(      'Golem',   "Golem1",   17,130,130,14,4, 5, 4,  7, 9, 345,'player2','Player 1','Player 2',190, True)
golem2=golem(      'Golem',   "Golem2",   17,130,130,14,4, 5, 5,  7, 9, 345,'player1','Player 2','Player 1',190, True)
centaur1=centaur(  "Centaur", "Centaur1", 14,100,100,11,11,11,12, 12,10,225,'player2','Player 1','Player 2',25)
centaur2=centaur(  "Centaur", "Centaur2", 14,100,100,11,11,11,12, 12,10,225,'player1','Player 2','Player 1',25)