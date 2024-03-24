from pyxel import *
from background import *
from player import Player
from background import Tilemap, sprite
from object import Worm
init(256, 256, fps=15)
load('astronaut.pyxres')

tm = Tilemap()
player = Player()
player_x = player._x
player_y = player._y

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
def openSafe(safe, player):
    for pos in safe_pos: # dont for each position in the safe positions
        if player.run_into_obj(): # check for collision
# NEED UPDATE            player.set_tool(safe._tool) # sets the tool that has been picked up from safe
# NEED UPDATE            text(safe.x, safe.y, safe.text, 7) # displays text where the safe is opened
            return True
        else:
            return False

# Initialize worms
worm_lst = []
for i in range(5):
    worm = Worm()
    worm_lst.append(worm)


while True:
    # Worm movement
    for worm in worm_lst:
        if not worm._chase:
            worm.move()
        else:
            worm.chase()
        if worm._life:
            blt(worm._x, worm._y, 2, 0, 0, 8, 8)

    # Worm collide
    


    move = False
    px = player_x
    py = player_y
    #pl = (player_x//8, player_y//8)
    cls(0)

    # Encounter worm, press F to kill the worm
    for worm in worm_lst:
        if player.encounter_worm(worm):
            if btn(KEY_F):
                worm._life = False
            else:
                player._health -= 1

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

