from pyxel import *
import math, random

class Equipment:

    def __init__(self, name, x, y, u=0, v=0) -> None:
        self._name = name # string specify the name of the tool
        self._x = x
        self._y = y
        self.u = u 
        self.v = v

class Worm:
    def __init__(self, x = random.randint(0, 256), y = random.randint(0, 256), life = True) -> None:
        self._x = x
        self._y = y
        self._life = life
        self._chase = False # If chase, run chase() and stop move(); otherwise, run move()

    
    def move_change_loc(self, x_change, y_change):
        self._x += x_change
        self._y += y_change

    def close_to_player(self, player) -> bool:
        if math.sqrt((self._x - player._x) ** 2 + (self._y - player._y) ** 2) < 10:
            return True
        return False
    

    def move(self):
        # Generate a pair of random number (a, b) where a, b \in {0, 1}.
        # For a: 0 - horizontal walk; 1 - vertical walk
        # For b: 0 - -1 step; 1: 1 step
        a, b = (random.randint(0, 1), random.randint(0, 1))
        if a == 0:
            if b == 0:
                self.move_change_loc(0, 3)
            else:
                self.move_change_loc(0, 3)
        else:
            if b == 0:
                self.move_change_loc(3, 0)
            else:
                self.move_change_loc(3, 0)

    
    def chase(self, player):
        if self.close_to_player(player):
            if self._x > player._x:
                self._x -= 1
            elif self._x < player._x:
                self._x += 1
            if self._y > player._y:
                self._y -= 1
            elif self._y < player._y:
                self._y += 1


class Safe: 
    def __init__(self, name, x, y, text) -> None:
        self._name = name
        self._x = x
        self._y = y
        self._text = text

    def open_safe(self, dialogue) -> bool:
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
            
            
    def set_life(self, is_alive):
        self._life = is_alive

    
