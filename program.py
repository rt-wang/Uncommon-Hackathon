from pyxel import *
from background import *
from player import Player
from background import Tilemap, sprite
init(128, 128, fps=10)
load('astronaut.pyxres')

tm = Tilemap()
#player = Player()
player_x = 1
player_y = 1

def draw_sprite(player_x, player_y, frame):
    if frame == 1:
        sprite(player_x, player_y, 0,0)
        sprite(player_x, player_y+1, 0,1)
        sprite(player_x+1, player_y, 1,0)
        sprite(player_x+1, player_y+1, 1,1)
    else:
        sprite(player_x, player_y, 2,0)
        sprite(player_x, player_y+1, 2,1)
        sprite(player_x+1, player_y, 3,0)
        sprite(player_x+1, player_y+1, 3,1)

from background import Tilemap
init(64, 64, fps=3)

load('astronaut.pyxres')

tm = Tilemap()

player = Player(0, 0)
player_x = 1
player_y = 1
while True:
    move = False
    px = player_x
    py = player_y
    pl = (player_x//8, player_y//8)
    cls(0)

    # player movement
    if btn(KEY_RIGHT):
        player_x += 1
        move = True
        player_x = tm.scroll(player_x)
    elif btn(KEY_LEFT):
        player_x -= 1
        move = True
    elif btn(KEY_UP):
        player_y -= 1
        move = True
    elif btn(KEY_DOWN):
        player_y += 1
        move = True
    

    if tm.get(0, player_x%8, player_y%8) == (0, 1) and (player_x//8, player_y//8) == pl:
        player_x = px
        player_y = py 
    elif tm.get(0, player_x%8, player_y%8) == (1, 1):
        player_x = 1
        player_y = 1
    tm.x = player_x//8
    tm.y = player_y//8
    if move == True:
        draw_sprite(player_x,player_y, 2)
    draw_sprite(player_x,player_y, 1)
    tm.draw(0)
    flip()

