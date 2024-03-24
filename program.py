from pyxel import *
from background import *
from player import Player
from object import Safe
from object import Equipment, FixHanger
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

fixHanger = 0
# make sure no repeat pick ups
oneNail = 0
oneWood = 0
oneOil = 0

hanger = False
hanger_visited = False

player = Player(1,1)
player_x = player._x
player_y = player._y
scroll_x = 0
scroll_y = 0

encountered_worm = []

face_left = False
door = False

ending = False
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

nail = Equipment("nail", 0, 14, 8, 96)
oil = Equipment("oil", 40, 0, 0, 96)
wood = Equipment("wood", 55, 0, 0, 104)


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
    for i in range(0, 3):
        blt((scroll_x+31)*size, (scroll_y+29+i)*size, 0, 0, 128 + 8*i, -8, 8, colkey=3)
        blt((scroll_x + 31 - len(player._tools) - 1)*size, (scroll_y+29+i)*size, 0, 0, 128 + 8*i, 8, 8, colkey=3)
    for i in range(len(player._tools)):
        blt((scroll_x + 30-i)*size, (scroll_y + 30)*size, 0, 8, 136, 8, 8, colkey=3)
        blt((scroll_x + 30-i)*size, (scroll_y + 29)*size, 0, 8, 128, 8, 8, colkey=3)
        blt((scroll_x + 30-i)*size, (scroll_y + 31)*size, 0, 8, 128, 8, -8, colkey=3)
        blt((scroll_x + 30-i)*size, (scroll_y + 30)*size, 0, player._tools[i].u, player._tools[i].v, 8, 8, colkey=3)



# Game start screen
while True:
    cls(0)
    blt(0, 12, 2, 0, 32, 256, 256)
    flip()
    if btnp(KEY_SPACE):
        break

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
    encountered_worm = []


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
                encountered_worm = []
                a_worm = Worm()
                worm_lst.append(a_worm)
                tm.draw(0)
                break
            
            flip()


    #pl = (player_x//8, player_y//8)
    cls(0)
    if not door:
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
            player_x = 1
            player_y = 10
            tm.scroll_x = 0
            tm.scroll_y = 0

        if collision == True:
            player_x = prev_player_x
            player_y = prev_player_y
            move = False
    else: # in Mars
        if "tank" not in player.tool_names():
            player._oxygen = 0
            player._health = 0

        if (player_x == 1) and (player_y == 8):
            door = False
            curMap = 0
            player_x = 29
            player_y = 15
            tm.scroll_x = 0
            tm.scroll_y = 0
        # fixHanger
        # nail
        if (player_x == 0 or player_x == 1) and (player_y == 14 or player_y == 15):    
            collision = True
            if hanger_visited == True:
                fixHanger += 1
                if oneNail == 0:
                    player._tools.append(nail)
                oneNail += 1
        # oil
        if (player_x == 40 or player_x == 41 or player_x == 42) and (player_y == 0 or player_y == 1):    
            if hanger_visited == True:
                fixHanger += 1
                collision = True
                if oneOil == 0:
                    player._tools.append(oil)
                oneOil += 1
        #wood
        if (player_x == 55 or player_x == 56) and (player_y == 0 or player_y == 1):    
            if hanger_visited == True:
                fixHanger += 1
                collision = True
                if oneWood == 0:
                    player._tools.append(wood)
                oneWood += 1
        
        if fixHanger == 3:
            hanger = True
        
        
        if (player_x >= 20 and player_x <= 23) or (player_y >= 0 and player_y <= 3):
            hanger_visited = True
            # if btnp(KEY_K):
            #     if dialogue == 0:
            #         render_text("It seems like there is a broken hanger")
            #         dialogue = 1
            #     if dialogue == 1:
            #         render_text("Perhaps there are materials to fix it nearby")
            #         dialogue = 0
            # if hanger == True:
            #     render_text("Do you want to fly away? (Y/N)")

        # border
        if player_x < 0 or player_y < 0 or player_x >= 63 or player_y >= 63: 
            collision = True

        if collision:
            player_x = prev_player_x
            player_y = prev_player_y
            move = False

        # Increase a worm every 4 sec
        if worm_frame % 30 == 0 and len(worm_lst) <= 10:
            print("made")
            worm = Worm()
            worm_lst.append(worm) # NEED SPECIFY AREA
        
        # Safehouse encounter collision
        for x, y in safeHouses:
            if player_x == x and player_y == y:
                safe = True
                if timeOxygen >= 15:
                    player._oxygen = min(5, player._oxygen+1)
                    timeOxygen = 0
                else:
                    timeOxygen += 1

        worm_frame += 1

        # Encounter worm, press A to kill the worm
        for worm in worm_lst:
            if worm_frame % 7 == 0 and worm._life: # worm speed
                worm.chase(player) 
            if worm.close_to_player(player) and worm._life:
                # print("close")
                encountered_worm.append(worm)
            
        for worm in encountered_worm:
            worm.draw()
            met, health = worm.encounter_player(player, face_left, attack)
            if met:
                if health == 0:
                    # encountered_worm.remove(worm)
                    worm_lst.remove(worm)
                    attack = False
                    print("killed")
                else:
                    if worm_frame % 3 == 0:
                        if not safe:
                            player._health += health
            if (worm._x and worm._y) in safeHouses:
                # encountered_worm.remove(worm)
                print('died to safe house')
                worm_lst.remove(worm)
            

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
            

    if (player_x >= 48 and player_x <= 52) and (player_y >= 0 and player_y <= 5):
            # reached the statue
            collision = True
            if dialogue == 0:
                print_str = "Read the plaque. (Y/N)"
                dialogue = 1
            if btnp(KEY_Y):
                if dialogue == 1:
                    print_str = "There was never a choice to make."
                    dialogue = 6
            if btnp(KEY_K):
                # if dialogue == 2:
                #     print_str = "I came to Mars to give humanity hope."
                #     dialogue = 3
                # elif dialogue == 3:
                #     print_str = "I end my journey as the last hope of humanity."
                #     dialogue = 10
                # elif dialogue == 4:
                #     print_str = "We were told it might finally be the end for Earth a year before"
                #     dialogue = 5
                # elif dialogue == 5:
                #     print_str = "Everyone went back in hopes of protecting the world"
                #     dialogue = 6
                if dialogue == 6:
                    print_str = "We needed someone to stay behind."
                    dialogue = 7
                elif dialogue == 7:
                    print_str = "Just in case the world really ended."
                    dialogue = 8
                elif dialogue == 8:
                    print_str = "I didn't want to"
                    dialogue = 9
                elif dialogue == 9:
                    print_str = "but there was no one else who knew what I did."
                    dialogue = 10
                elif dialogue == 10:
                    print_str = "I never said goodbye to Martha"
                    dialogue = 11
                elif dialogue == 11:
                    print_str = "and I never got to say hello to Ben"
                    dialogue = 12
                elif dialogue == 12:
                    print_str = "I always have that temptation"
                    dialogue = 13
                elif dialogue == 13:
                    print_str = "to go back to Earth."
                    dialogue = 14
                elif dialogue == 14:
                    print_str = "Just to see that it's really gone"
                    dialogue = 15
                elif dialogue == 15:
                    print_str = "Because I know it is, but I don't KNOW."
                    dialogue = 16
                elif dialogue == 16:
                    print_str = "I stay, though, for the last of humanity"
                    dialogue = 20
                # elif dialogue == 17:
                #     print_str = "And sometimes I wonder, is it worth it?"
                #     dialogue = 18
                # elif dialogue == 18:
                #     print_str = "They'll live their lives trapped in a suit"
                #     dialogue = 19
                # elif dialogue == 19:
                #     print_str = "They won't know ice cream or candy"
                #     dialogue = 20
                elif dialogue == 20:
                    print_str = "They won't know the small joys of life as we do"
                    dialogue = 21
                elif dialogue == 21:
                    print_str = "But, I'll make sure they still know joy."
                    dialogue = 22
                elif dialogue == 22:
                    print_str = "So I watch the last light go out on Earth"
                    dialogue = 23
                elif dialogue == 23:
                    print_str = "And I stayed here. Alive. Living."
                    dialogue = 24
                elif dialogue == 24:
                    print_str = "Sincerely, -----"
                    dialogue = 25
    elif bed_collision == True:
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
                dialogue = 1
            if btnp(KEY_Y):
                if dialogue == 1:
                    print_str = "Another riddle awaits..."
                    dialogue = 14
                elif dialogue == 6:
                    print_str = "Dear ----,"
                    dialogue = 7
                elif dialogue == 16:
                    print_str = "Correct, T-H-A-T!"
                    player._tools.append(key)
                    dialogue = 2
            if btnp(KEY_N):
                if dialogue == 16:
                    print_str = "Try again."
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
                elif dialogue == 14:
                    print_str = "Mississipi is a pretty hard word to spell."
                    dialogue = 15
                elif dialogue == 15:
                    print_str = "Can you spell that without 'I's and 'S's? Y/N"
                    dialogue = 16
                
        elif safe_num == 3 and safe3_visited == False:
            if dialogue == 0:
                print_str = "Would you like to open the safe? Y/N"
                dialogue = 1
            if btnp(KEY_Y):
                if dialogue == 1:
                    print_str = "My wife, Martha, is from Mississipi"
                    dialogue = 2
            if btnp(KEY_K):
                if dialogue == 2:
                    print_str = "I miss her quite a bit."
                    dialogue = 3
                elif dialogue == 3:
                    print_str = "She's always loved puzzles."
                    dialogue = 4
                elif dialogue == 4:
                    print_str = "So I've started making them as well"
                    dialogue = 5
                elif dialogue == 5:
                    print_str = "Answer me this, what comes once in a minute"
                    dialogue = 6
                elif dialogue == 6:
                    print_str = "twice in a moment"
                    dialogue = 7
                elif dialogue == 7:
                    print_str = "but NEVER in a thousand years?"
                    dialogue = 8
                elif dialogue == 8:
                    print_str = "1. M"
                    dialogue = 9
                elif dialogue == 9:
                    print_str = "2. A"
                    dialogue = 10
                elif dialogue == 10:
                    print_str = "3. R"
                    dialogue = 11
                elif dialogue == 11:
                    print_str = "4. T"
                    dialogue = 12
                elif dialogue  == 12:
                    print_str = "5. H"
                    dialogue = 13
                elif dialogue == 13:
                    print_str = "6. A"
                    dialogue = 14
                elif dialogue == 14:
                    print_str = "oops I repeated that one, didn't I?"
                    dialogue = 15
                elif dialogue == 15:
                    print_str = "Type your answer (1, 2, 3, 4, 5)"
                    dialogue = 16
            if dialogue == 16:
                if btnp(KEY_1):
                    print_str = "Correct!"
                    player._tools.append(rations)
                    player._tools.append(tank)
                    safe3_visited = True
                elif btnp(KEY_2) or btnp(KEY_3) or btnp(KEY_4) or btnp(KEY_5) or btnp(KEY_6):
                    print_str = "No. No. No."
                    
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