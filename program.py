from pyxel import *
from background import *
from player import Player
from object import Safe
from object import Equipment
from background import Tilemap, sprite
from object import Worm

init(256, 256, fps=15, title="The Red Planet")
load('astronaut.pyxres')


#test
#from PIL import Image
#img = Image.open("game_over.jpg")
#img = Image.load(game_over.jpg)

#img.show()


tm = Tilemap()
curMap = 0
timeOnMars = 0
timeOxygen = 0
bloodTimer = 0

player = Player(1,1)
player_x = player._x
player_y = player._y
scroll_x = 0
scroll_y = 0

encountered_worm = []

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
    
    elif frame == 6:
        if face_left:
            sprite(player_x, player_y, 4, 10, flip = False)
        else:
            sprite(player_x, player_y, 4, 10, flip = True)

knife = Equipment("knife", 0, 0, 0, 88)
key = Equipment("key", 0, 0, 8, 88)
rations = Equipment("rations", 0, 0, 8, 80)
tank = Equipment("tank", 0, 0, 0, 80)

#test
# player._tools = [knife, key, rations, tank]

safeHouses = [(4,2), (28, 4), (49, 4), (50, 19), (26, 19), (2, 19), (3, 43), (43, 15), (61, 51)]

safe1 = Safe("safe1", 25, 9, "ehewif") # 25 24 27 26 (top left, lower right)
safe2 = Safe("safe2", 4, 25, "awejfio") # 9 26 11 28 # letter is just a read object
safe3 = Safe("safe3", 28, 28, "safe")

safes = [safe1, safe2, safe3]

safe1_visited = False
safe2_visited = False
safe3_visited = False

# code for opening safe, only uncomment after object.py is done
length = 0
print_str = ""
dialogue = 0

def render_text(str):
    rect(19 + tm.scroll_x * 8, 28 + tm.scroll_y * 8, 200 + tm.scroll_x, 10, 0)
    text(20 + tm.scroll_x * 8, 30 + tm.scroll_y * 8, str, 7)

def displayUI(scroll_x, scroll_y, size, health, oxygen):
    # backdrop
    # for i in range(0, 7):
    #     for j in range(0, 4):
    #         blt((scroll_x + 31-i)*size, (scroll_y + j)*size, 0, 8, 24, 8, 8)

    # health
    for i in range(0, health):
        blt((scroll_x + 30-i)*size, (scroll_y + 1) *size, 0, 8, 32, 8, 8,colkey=3)
    
    #oxygen
    for i in range(0, oxygen):
        blt((scroll_x + 30-i)*size, (scroll_y + 2)*size, 0, 8, 40, 8, 8, colkey=3)
    
    # inventory
    # (0, 128)
    for i in range(0, 3):
        blt((scroll_x+31)*size, (scroll_y+29+i)*size, 0, 0, 128 + 8*i, -8, 8, colkey=3)
        blt((scroll_x + 31 - len(player._tools) - 1)*size, (scroll_y+29+i)*size, 0, 0, 128 + 8*i, 8, 8, colkey=3)
    for i in range(len(player._tools)):
        blt((scroll_x + 30-i)*size, (scroll_y + 30)*size, 0, 8, 136, 8, 8, colkey=3)
        blt((scroll_x + 30-i)*size, (scroll_y + 29)*size, 0, 8, 128, 8, 8, colkey=3)
        blt((scroll_x + 30-i)*size, (scroll_y + 31)*size, 0, 8, 128, 8, -8, colkey=3)
        blt((scroll_x + 30-i)*size, (scroll_y + 30)*size, 0, player._tools[i].u, player._tools[i].v, 8, 8, colkey=3)
    


# Initialize worms
worm_frame = 0
worm_lst = []
player_frame = 0

while True:
    move = False
    attack = False
    px = player_x
    py = player_y
    collision = False
    safe_collision = False
    bed_collision = False
    safe_num = 1
    safe = False


    # check if player is alive
    if not player.is_alive():
        print("player is dead")
        # PUT UP GAME OVER IMAGE/TILEMAP/Whatever
        while True:
            draw_sprite(player_x, player_y, 6)
            render_text("Game Over. Press [Space] to start a new game")
            flip()
            if btn(KEY_SPACE):
                curMap = 0
                timeOnMars = 0
                timeOxygen = 0

                player = Player(1,1)
                player_x = player._x
                player_y = player._y
                tm.scroll_x = 0
                tm.scroll_y = 0

                face_left = False
                door = False
                safe1_visited = False
                safe2_visited = False
                safe3_visited = False

                length = 0
                print_str = ""
                dialogue = 0

                worm_frame = 0
                worm_lst = []
                a_worm = Worm()
                worm_lst.append(a_worm)
                tm.draw(0)
                break
            
            flip()


    #pl = (player_x//8, player_y//8)
    cls(0)
    if not door:
        curMap = 0
        tm.draw(curMap)
    else:
        curMap = 1
        tm.draw(curMap)
    
    prev_player_x = player_x
    prev_player_y = player_y

    # player movement
    if player.is_alive():
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

    player._x = player_x
    player._y = player_y

    #knife movement
    if btn(KEY_A) and "knife" in player.tool_names():
        attack = True

    # room collision
    if not door:
        for safe in safes:
            if player_x <= safe._x + 2 and player_x >= safe._x - 2 and player_y <= safe._y + 2 and player_y >= safe._y - 2:
                safe_collision = True
                if player_x <= safe._x + 1 and player_x >= safe._x - 1 and player_y <= safe._y + 1 and player_y >= safe._y - 1: # check for collision
                    collision = True
                break
            safe_num = safe_num + 1
            if player_x <= safe._x + 1 and player_x >= safe._x - 1 and player_y <= safe._y + 1 and player_y >= safe._y - 1: # check for collision
                collision = True
        if (player_x >= 3 and player_x <= 7) and (player_y >= 3 and player_y <= 9):
            bed_collision = True
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
    else: # in Mars
        if player_x < 0 or player_y < 0 or player_x >= 63 or player_y >= 63: 
            collision = True

        if collision:
            player_x = prev_player_x
            player_y = prev_player_y
            move = False

        # Increase a worm every 4 sec
        if worm_frame % 30 == 0:
            print("made")
            worm = Worm()
            worm_lst.append(worm) # NEED SPECIFY AREA
        
        # Safehouse encounter collision
        for x, y in safeHouses:
            if player_x == x and player_y == y:
                safe = True
                if timeOxygen >= 15:
                    player._oxygen = min(8, player._oxygen+1)
                    timeOxygen = 0
                else:
                    timeOxygen += 1

        worm_frame += 1

        # Encounter worm, press A to kill the worm
        for worm in worm_lst:
            if worm_frame % 7 == 0 and worm._life: # worm speed
                if worm.close_to_player(player):
                    print("close")
                    worm.chase(player)
                    encountered_worm.append(worm)
            
        for worm in encountered_worm:
            worm.draw()
            met, health = worm.encounter_player(player, face_left, attack)
            if met:
                if health == 0:
                    encountered_worm.remove(worm)
                    attack = False
                    print("killed")
                else:
                    if not safe:
                        player._health += health
            if (worm._x, worm._y) in safeHouses:
                    if worm_frame % 5 == 0:
                        if not safe:
                            player._health += health
            if (worm._x and worm._y) in safeHouses:
                encountered_worm.remove(worm)
            

        # Lose oxygen every 5 seconds while on Mars
        timeOnMars += 1
        if timeOnMars >= 75:
            player._oxygen -= 1
            timeOnMars = 0
        if player._oxygen <= 0:
            if bloodTimer >= 30:
                player._health -= 1
                bloodTimer = 0
                print("lost health due to oxygen")
            bloodTimer += 1
        
        # moves player home if they pass by the home door
        if player_x == 1 and player_y == 8:
            door = False
            player_x = 29
            player_y = 15
            


    if bed_collision == True:
        if dialogue == 0:
            print_str = "Would you like to go to sleep? Y/N"
        if btnp(KEY_Y):
            if dialogue <= 1:
                print_str = "Really? There's no time to sleep now."
                dialogue = 1
        if btnp(KEY_N):
            if dialogue <= 1:
                print_str = "Good choice."
                dialogue = 1
    elif safe_collision == True:
        if safe_num == 1 and safe1_visited == False:
            if dialogue == 0:
                print_str = "Would you like to open the safe? Y/N"
            if btnp(KEY_Y):
                if dialogue <= 1:
                    print_str = "Not so quick. (Press K)"
                    dialogue = 1
                if dialogue == 6:
                    print_str = "Correct. As Baby Ben is a baby, he does lie down."
                    #safe number not thought
                    player._tools.append(knife)
                    safe1_visited = True
                    dialogue = 0
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
                    print_str = "Incorrect. Please be better."
        elif safe_num == 2 and safe2_visited == False:
            if dialogue == 0:
                print_str = "Would you like to open the safe? Y/N"
            if btnp(KEY_Y):
                if dialogue <= 1:
                    print_str = "Another riddle awaits..."
                    player._tools.append(key)
                    dialogue = 2
                elif dialogue == 6:
                    print_str = "Dear ----,"
                    dialogue = 7
            if btnp(KEY_K):
                if dialogue == 2:
                    print_str = "There is a letter as well..."
                    dialogue = 3
                elif dialogue == 3:
                    print_str = "Very clearly worn down from reading, "
                    dialogue = 4
                elif dialogue == 4:
                    print_str = "many words are smudged beyond recognition."
                    dialogue = 5
                elif dialogue == 5:
                    print_str= "Would you like to read? (Y/N)"
                    dialogue = 6
                elif dialogue == 7:
                    print_str = "It’s always hot and dusty. I miss home."
                    dialogue = 8
                elif dialogue == 8:
                    print_str = "I miss Martha and Ben so much."
                    dialogue = 9
                elif dialogue == 9:
                    print_str = "It's a lonesome existence, being the -----."
                    dialogue = 10
                elif dialogue == 10:
                    print_str = "I miss everyone. They are probably all -----."
                    dialogue = 11
                elif dialogue == 10:
                    print_str = "I wonder, sometimes, if it's even ------"
                    dialogue = 11   
                elif dialogue == 11:
                    print_str = "I hope you understand when -----"
                    dialogue = 12
                elif dialogue == 12:
                    print_str = "Sincerely, -----"
                    dialogue = 13
                    safe2_visited = True
        elif safe_num == 3 and safe3_visited == False:
            if dialogue == 0:
                print_str = "Would you like to open the safe? Y/N"
            if btnp(KEY_Y):
                if dialogue <= 1:
                    print_str = "Patience child"
                    dialogue = 1
                    player._tools.append(rations)
                    player._tools.append(tank)
                    safe3_visited = True
    else:
        print_str = ""
        dialogue = 0

    # DRAW EVERYTHING

    # Draw player
    if not player.is_alive():
        draw_sprite(player_x, player_y, 6)
    elif "knife" in player.tool_names():
        if not attack:
            if move and player_frame%5 < 3:
                draw_sprite(player_x,player_y,4)
            else:
                draw_sprite(player_x,player_y,3)
        else:
            draw_sprite(player_x,player_y,5)
    else:
        if move and player_frame%5 < 3:
            draw_sprite(player_x,player_y, 2)
        else:
            draw_sprite(player_x,player_y, 1)
    
    # Draw UI
    displayUI(tm.scroll_x, tm.scroll_y, 8, player._health, player._oxygen)
    
    # Draw text
    if print_str != "":
        render_text(print_str)           


    player_frame += 1
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