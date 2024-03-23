from pyxel import *
from background import *
from player import Player
from object import Safe
from background import Tilemap, sprite
init(256, 256, fps=15)
load('astronaut.pyxres')

tm = Tilemap()
# player = Player()
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

knife = Safe("knife", 25, 24, "ehewif") # 25 24 27 26 (top left, lower right)
suit = Safe("suit", 25, 4, "awhef") # 25 4 27 5
letter = Safe("letter", 9, 26, "awejfio") # 9 26 11 28
key = Safe("key", 27, 26, "whaeh")
rations = Safe("rations", 27, 5, "rations")
backpack = Safe("backpack", 11, 28, "waejf")

safes = [knife, suit, letter, key, rations, backpack]
# code for opening safe, only uncomment after object.py is done

def openSafe(safes, player_x, player_y):
    
    text(10, 10, f"ur coords: {player_x}, {player_y}", 7)
    for safe in safes: # dont for each position in the safe positions
        text(20, 20, f"safe coords: {safe._x}, {safe._y}", 2)
        if player_x <= safe._x + 1 and player_x >= safe._x - 1 and player_y <= safe._y + 1 and player_y >= safe._y - 1: # check for collision
            # set_tool(safe.text) # sets the tool that has been picked up from safe
            # text(safe.x, safe.y, safe.text, 7) # displays text where the safe is opened
            text(10, 10, "Would you like to open the safe? Y/N", 3)
            if btnp(KEY_Y):
                text(10, 20, "Not so fast... First you must solve a riddle. (Press A to continue)", 7)
                if btnp(KEY_A):
                    safe.open_safe()
                else:
                    text(10, 20, "Ok. Sad :'(.", 6)
            else:
                text(10, 20, "Very sad :'(", 5)
            
                
    return True


while True:
    move = False
    px = player_x
    py = player_y
    #pl = (player_x//8, player_y//8)
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
    

    tm.draw(0)
    if move:
        draw_sprite(player_x,player_y, 2)
    draw_sprite(player_x,player_y, 1)
    openSafe(safes, player_x, player_y)
    flip()

