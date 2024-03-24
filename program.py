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

safe1 = Safe("knife, tank", 25, 9, "ehewif") # 25 24 27 26 (top left, lower right)
safe2 = Safe("letter, key", 4, 25, "awejfio") # 9 26 11 28 # letter is just a read object
safe3 = Safe("rations, backpack", 28, 28, "rations")

safes = [safe1, safe2, safe3]
# code for opening safe, only uncomment after object.py is done

def display_safe(safes, player_x, player_y):        
    rect(19 + tm.scroll_x * 8, 18 + tm.scroll_y * 8, 150, 10, 0)
    text(20 + tm.scroll_x * 8, 20 + tm.scroll_y * 8, "Would you like to open the safe? Y/N", 7)
    show_message = False
    if btnp(KEY_Y):
        show_message = True

    if show_message == True:
        rect(19 + tm.scroll_x * 8, 18 + tm.scroll_y * 8, 200, 10, 0)
        text(20 + tm.scroll_x * 8, 20 + tm.scroll_y * 8, "Not so fast... (Press A)", 7)
    #   if btnp(KEY_A):
    #             safe.open_safe()
    #         else:
    #             text(10, 20, "Ok. Sad :'(.", 6)    
    #     else:
    #         text(10, 20, "Very sad :'(", 5)

while True:
    move = False
    px = player_x
    py = player_y
    collision = False
    safe_collision = False
    #pl = (player_x//8, player_y//8)
    cls(0)
    
    prev_player_x = player_x
    prev_player_y = player_y

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
    
    for safe in safes:
        if player_x <= safe._x + 2 and player_x >= safe._x - 2 and player_y <= safe._y + 2 and player_y >= safe._y - 2:
            safe_collision = True
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

    tm.draw(0)
    if move:
        draw_sprite(player_x,player_y, 2)
    else:
        draw_sprite(player_x,player_y, 1)
    if safe_collision == True:
        display_safe(safes, player_x, player_y)
    flip()

