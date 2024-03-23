from pyxel import *
from background import *
from player import Player
from background import Tilemap
init(64, 64, fps=3)

load('astronaut.pyxres')

tm = Tilemap()

player = Player(0, 0)
player_x = 1
player_y = 1

while True:
    px = player_x
    py = player_y
    pl = (player_x//8, player_y//8)
    cls(0)
    if btn(KEY_RIGHT):
        player_x = tm.scroll(player_x)
    elif btn(KEY_LEFT):
        player_x -= 1
    elif btn(KEY_UP):
        player_y -= 1
    elif btn(KEY_DOWN):
        player_y += 1
    if tm.get(0, player_x%8, player_y%8) == (0, 1) and (player_x//8, player_y//8) == pl:
        player_x = px
        player_y = py 
    elif tm.get(0, player_x%8, player_y%8) == (1, 1):
        player_x = 1
        player_y = 1
    tm.player_x = player_x//8
    tm.player_y = player_y//8
    sprite(player_x % 4, player_y % 4, 0, 0)
    sprite(player_x % 4, player_y % 4 + 1, 0, 1)
    sprite(player_x % 4 + 1, player_y % 4, 1, 0)
    sprite(player_x % 4 + 1, player_y % 4 + 1, 1, 1)
    tm.draw(0)
    flip()
