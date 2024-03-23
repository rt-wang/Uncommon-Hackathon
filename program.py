from pyxel import *
from background import *
from player import Player
from background import Tilemap, sprite
init(256, 256, fps=15)
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

# code for opening safe, only uncomment after object.py is done
# def openSafe(safe, player_x):
#     for pos in safe_pos: # dont for each position in the safe positions
#         if player_x == safe.x and player_y == safe.y: # check for collision
#             set_tool(safe.object) # sets the tool that has been picked up from safe
#             text(safe.x, safe.y, safe.text, 7) # displays text where the safe is opened
#             return True
#         else:
#             return False

while True:
    move = False
    px = player_x
    py = player_y
    #pl = (player_x//8, player_y//8)
    cls(0)

    # player movement
    if btn(KEY_RIGHT):
        move = True
        player_x = tm.right_scroll(player_x)
    elif btn(KEY_LEFT):
        move = True
        player_x = tm.left_scroll(player_x)
    elif btn(KEY_UP):
        player_y -= 1
        move = True
    elif btn(KEY_DOWN):
        player_y += 1
        move = True
    

    tm.draw(1)
    if move:
        draw_sprite(player_x,player_y, 2)
    draw_sprite(player_x,player_y, 1)
    flip()

