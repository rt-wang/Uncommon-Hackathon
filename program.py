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

safe1 = Safe("knife, tank", 25, 9, "ehewif") # 25 24 27 26 (top left, lower right)
safe2 = Safe("letter, key", 4, 25, "awejfio") # 9 26 11 28 # letter is just a read object
safe3 = Safe("rations, backpack", 28, 28, "rations")

safes = [safe1, safe2, safe3]
# code for opening safe, only uncomment after object.py is done
length = 0
print_str = ""
dialogue = 0

def render_text(str):
    rect(19 + tm.scroll_x * 8, 18 + tm.scroll_y * 8, 237 + tm.scroll_x, 10, 0)
    text(20 + tm.scroll_x * 8, 20 + tm.scroll_y * 8, str, 7)

def display_safe(safe_num):        
    if btnp(KEY_Y):
        return True

while True:
    move = False
    attack = False
    px = player_x
    py = player_y
    collision = False
    safe_collision = False
    safe_num = 0
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
        if player_x <= safe._x + 2 and player_x >= safe._x - 2 and player_y <= safe._y + 2 and player_y >= safe._y - 2:
            safe_collision = True
            safe_num = safe_num - 1 # which safe it is
        safe_num = safe_num + 1
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

    if safe_collision == True:
        if dialogue == 0:
            print_str = "Would you like to open the safe? Y/N"
        if btnp(KEY_Y):
            if dialogue <= 1:
                print_str = "Not so quick. (Press K)"
                dialogue = 1
            if dialogue == 6:
                print_str = "Correct. As Baby Ben is a baby, he does lie down."
        if btnp(KEY_K):
            if dialogue <= 2:
                print_str = "A good astronaut remembers details..."
                dialogue = 3
            elif dialogue <= 3:
                print_str = "Baby Ben lies."
                dialogue = 4
            elif dialogue <= 4:
                print_str = "Baby Ben does not lie."
                dialogue = 5
            elif dialogue <= 5:
                print_str = "Does Baby Ben lie? Y/N"
                dialogue = 6
        if btnp(KEY_N):
            if dialogue == 6:
                print_str = "Incorrect. One item has been lost. Permanently."
            
            
    else:
        print_str = ""

    render_text(print_str)           
    flip()
    
# Plan for the safe
'''
1. collision
2. do you want to open the safe (Y/N)
3. if yes is picked, give a riddle (multiple choice)
4. if correct answer picked, open safe, and items can be taken and added to inventory
    5. for each item, player is asked do they want the item?
    6. if they say yes, they are given options based on the item and their inventory
        a. if they do not yet have a backpack, to take one item, you must get rid of another
        b. for each item (post backpack), you can store item (if knife, rations, and key), use item, or leave item
            c. for letter, using item means reading it
            d. for rations, using item means eating it (so its gone)
'''

