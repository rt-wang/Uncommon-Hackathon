from pyxel import *
from background import *
from player import Player
from object import Safe
from object import Equipment
from background import Tilemap, sprite
from object import Worm

init(256, 256, fps=15)
load('astronaut.pyxres')

tm = Tilemap()
curMap = 0

player = Player(1,1)
#player._tools.append("knife") # temp
player_x = 1
player_y = 1
scroll_x = 0
scroll_y = 0

face_left = False
door = False

def draw_sprite(player_x, player_y, frame):
    if frame == 1:
        sprite(player_x, player_y, 0,0, flip=face_left)
        
    elif frame == 2:
        sprite(player_x, player_y, 2,0, flip=face_left)
        
    elif frame == 3:
        sprite(player_x, player_y, 2,2, flip=face_left)
        
    elif frame == 4:
        sprite(player_x, player_y, 4,2, flip=face_left)
        
    elif frame == 5:
        if face_left:
            sprite_2(player_x, player_y, 28, 48, flip = False)
        else:
            sprite_2(player_x, player_y, 28, 48, flip = True)

knife = Equipment("knife", 0, 0, 0, 88)
key = Equipment("key", 0, 0, 8, 88)
rations = Equipment("rations", 0, 0, 8, 80)

#test
player._tools = [knife, key, rations]


safe1 = Safe("knife, tank", 25, 9, "ehewif") # 25 24 27 26 (top left, lower right)
safe2 = Safe("letter, key", 4, 25, "awejfio") # 9 26 11 28 # letter is just a read object
safe3 = Safe("rations, backpack", 28, 28, "rations")

safes = [safe1, safe2, safe3]
# code for opening safe, only uncomment after object.py is done
length = 0
print_str = ""
dialogue = 0

def render_text(str):
    rect(19 + tm.scroll_x * 8, 18 + tm.scroll_y * 8, 180 + tm.scroll_x, 10, 0)
    text(20 + tm.scroll_x * 8, 20 + tm.scroll_y * 8, str, 7)

def displayUI(scroll_x, scroll_y, size, health, oxygen):
    # backdrop
    # for i in range(0, 7):
    #     for j in range(0, 4):
    #         blt((scroll_x + 31-i)*size, (scroll_y + j)*size, 0, 8, 24, 8, 8)

    # health
    for i in range(0, health):
        blt((scroll_x + 30-i)*size, (scroll_y + 1) *size, 0, 8, 32, 8, 8)
    
    #oxygen
    for i in range(0, oxygen):
        blt((scroll_x + 30-i)*size, (scroll_y + 2)*size, 0, 8, 40, 8, 8)
    
    # inventory
    for i in range(len(player._tools)):
        blt((scroll_x + 30-i)*size, (scroll_y + 30)*size, 0, player._tools[i].u, player._tools[i].v, 8, 8)



# Initialize worms
worm_lst = []
for i in range(100):
    worm = Worm()
    worm_lst.append(worm)

worm_frame = 0


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
    if not door:
        tm.draw(curMap)
    else:
        curMap = 1
        tm.draw(curMap)
    
    prev_player_x = player_x
    prev_player_y = player_y

    # Encounter worm, press F to kill the worm
    for worm in worm_lst:
        if player.encounter_worm(worm):
            if btn(KEY_F):
                worm._life = False
                worm_lst.remove(worm)
            else:
                player._health -= 1

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

    if player_x == 31 and (player_y == 15 or player_y == 16):
        door = True

    if collision == True:
        player_x = prev_player_x
        player_y = prev_player_y
        move = False

    if "knife" in player.tool_names():
        if not attack:
            if move:
                draw_sprite(player_x,player_y,4)
            else:
                draw_sprite(player_x,player_y,3)
        else:
            draw_sprite(player_x,player_y,5)
    else:
        if move:
            draw_sprite(player_x,player_y, 2)
        else:
            draw_sprite(player_x,player_y, 1)

    displayUI(tm.scroll_x, tm.scroll_y, 8, player._health, 5)


    # Worm movement
    for worm in worm_lst:
        if not worm._chase and worm_frame%5 == 0:
            worm.move()
        else:
            worm.chase(player)
        if worm._life:
            worm.draw()
            
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
        
    if print_str != "":
        render_text(print_str)           

    worm.chase(player)
    if worm._life:
        blt(worm._x, worm._y, 2, 0, 8, 16, 8, 3)

    worm_frame += 1

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

