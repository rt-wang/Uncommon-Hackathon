from pyxel import *
from background import *
from player import Player
from object import Safe
from background import Tilemap, sprite
init(256, 256, fps=6)
load('astronaut.pyxres')

tm = Tilemap()
player = Player(1,1)
player._tools.append("knife") # temp
player_x = 1
player_y = 1
scroll_x = 0
scroll_y = 0

face_left = False

def draw_sprite(player_x, player_y, frame):
    if frame == 1:
        sprite(player_x, player_y, 0,0)
        sprite(player_x, player_y+1, 0,1)
        sprite(player_x+1, player_y, 1,0)
        sprite(player_x+1, player_y+1, 1,1)
    elif frame == 2:
        sprite(player_x, player_y, 2,0)
        sprite(player_x, player_y+1, 2,1)
        sprite(player_x+1, player_y, 3,0)
        sprite(player_x+1, player_y+1, 3,1)
    elif frame == 3:
        sprite(player_x, player_y, 2,2)
        sprite(player_x, player_y+1, 2,3)
        sprite(player_x+1, player_y, 3,2)
        sprite(player_x+1, player_y+1, 3,3)
    elif frame == 4:
        sprite(player_x, player_y, 4,2)
        sprite(player_x, player_y+1, 4,3)
        sprite(player_x+1, player_y, 5,2)
        sprite(player_x+1, player_y+1, 5,3)
    elif frame == 5:
        if face_left:
            sprite_2(player_x, player_y, 28, 48, flip = True)
        else:
            print(True)
            sprite_2(player_x, player_y, 28, 48, flip = False)

knife = Safe("knife", 25, 9, "ehewif") # 25 24 27 26 (top left, lower right)
tank = Safe("tank", 25, 9, "awhef") # 25 4 27 5
letter = Safe("letter", 4, 25, "awejfio") # 9 26 11 28 # letter is just a read object
key = Safe("key", 4, 25, "whaeh")
rations = Safe("rations", 28, 28, "rations")
backpack = Safe("backpack", 28, 28, "waejf")

safes = [knife, tank, letter, key, rations, backpack]
# code for opening safe, only uncomment after object.py is done

def displaySafe(safes, player_x, player_y):        
    rect(19 + tm.scroll_x * 8, 18 + tm.scroll_y * 8, 150, 10, 0)
    text(20 + tm.scroll_x * 8, 20 + tm.scroll_y * 8, "Would you like to open the safe? Y/N", 7)
    # if btnp(KEY_Y):
    #         text(10, 20, "Not so fast... First you must solve a riddle. (Press A to continue)", 7)
    #         if btnp(KEY_A):
    #             safe.open_safe()
    #         else:
    #             text(10, 20, "Ok. Sad :'(.", 6)    
    #     else:
    #         text(10, 20, "Very sad :'(", 5)

while True:
    move = False
    attack = False
    px = player_x
    py = player_y
    collision = False
    #pl = (player_x//8, player_y//8)
    cls(0)
    tm.draw(0)
    
    prev_player_x = player_x
    prev_player_y = player_y

    # player movement
    if btn(KEY_RIGHT):
        move = True
        player_x = tm.x_scroll(player_x, 1)
        face_left = False
    elif btn(KEY_LEFT):
        move = True
        player_x = tm.x_scroll(player_x, -1)
        face_left = True
    elif btn(KEY_UP):
        move = True
        player_y = tm.y_scroll(player_y, -1)
    elif btn(KEY_DOWN):
        player_y = tm.y_scroll(player_y, 1)
        move = True
    
    #knife movement
    if btn(KEY_A):
        attack = True
    for safe in safes:
        if player_x <= safe._x + 1 and player_x >= safe._x - 1 and player_y <= safe._y + 1 and player_y >= safe._y - 1: # check for collision
            collision = True
    if (player_x == 4 or player_x == 5 or player_x == 6) and (player_y >= 4 and player_y <= 8):
        collision = True
    if player_x <= 0 or player_y <= 0 or player_x >= 30 or player_y >= 30: 
        if player_x >= 30 and player_y == 15:
            collision = False
        else:
            collision = True
    
    if (player_x == 28 or player_x == 29) and (player_y == 13 or player_y == 14 or player_y == 16 or player_y == 17):
        collision = True

    if collision == True:
        player_x = prev_player_x
        player_y = prev_player_y
        move = False

    if "knife" in player._tools:
        if not attack:
            draw_sprite(player_x,player_y,3)
            if move:
                draw_sprite(player_x,player_y,4)
        else:
            draw_sprite(player_x,player_y,5)
    else:
        if move:
            draw_sprite(player_x,player_y, 2)
        else:
            draw_sprite(player_x,player_y, 1)
    openSafe(safes, player_x, player_y)
    flip()

