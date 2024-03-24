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
    def __init__(self, x = 0, y = 0, life = True) -> None:
        self._x = random.randint(0, 256)
        self._y = random.randint(0, 256)
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
                self.move_change_loc(0, -3)
        else:
            if b == 0:
                self.move_change_loc(3, 0)
            else:
                self.move_change_loc(-3, 0)
    
    def draw(self):
        blt(self._x, self._y, 1, 0, 8, 16, 8, 3)

    
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
            
            
    def set_life(self, is_alive):
        self._life = is_alive

    
