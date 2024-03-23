from pyxel import *
from background import *
from player import Player
from background import Tilemap, sprite
init(256, 256, fps=6)
load('astronaut.pyxres')

tm = Tilemap()
#player = Player()
player_x = 1
player_y = 1
scroll_x = 0
scroll_y = 0

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
def openSafe(safe, player_x):
    for pos in safe_pos:
        if player_x == safe.x and player_y == safe.y:
            set_tool(safe.object)
            return True
        else:
            return False

while True:
    move = False
    px = player_x
    py = player_y
    pl = (player_x//8, player_y//8)
    cls(0)

    # player movement
    if btn(KEY_RIGHT):
        move = True
        player_x = tm.x_scroll(player_x, 1)
    elif btn(KEY_LEFT):
        move = True
        player_x = tm.x_scroll(player_x, -1)
    elif btn(KEY_UP):
        move = True
        player_y = tm.y_scroll(player_y, -1)
    elif btn(KEY_DOWN):
        player_y = tm.y_scroll(player_y, 1)
        move = True
    

    tm.draw(1)
    if move == True:
        draw_sprite(player_x,player_y-\
            , 2)
    draw_sprite(player_x, player_y, 1)
    flip()

