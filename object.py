from pyxel import *
import math, random

class Equipment:

    def __init__(self, name, x, y) -> None:
        self._name = name # string specify the name of the tool
        self._x = x
        self._y = y

class Worm:
    def __init__(self, x, y, life = True) -> None:
        self._x = x
        self._y = y
        self._life = life

    
    def move_change_loc(self, x_change, y_change):
        self._x += x_change
        self._y += y_change

    def close_to_player(self, player) -> bool:
        if math.sqrt((self._x - player._x) ** 2 + (self._y - player._y) ** 2) < 6:
            return True
        return False
    

    def move(self):
        # Generate a pair of random number (a, b) where a, b \in {0, 1}.
        # For a: 0 - horizontal walk; 1 - vertical walk
        # For b: 0 - -1 step; 1: 1 step
        a, b = (random.randint(0, 1), random.randint(0, 1))
        if a == 0:
            self.move_change_loc(b)
        else:
            self.move_change_loc(b)


class Safe: 
    def __init__(self, name, x, y, text) -> None:
        self._name = name
        self._x = x
        self._y = y
        self._text = text

    def open_safe(self) -> bool:
        text(self._x, self._y, "Would you like to open the safe?", 2)
        if btnp(KEY_Y):
            text(self._x, self._y, "correct", 8)
            return True
        else:
            return False
<<<<<<< HEAD

=======
        
>>>>>>> 04934b53800e4211c3e222d5fd91329caf18e381
    def set_life(self, is_alive):
        self._life = is_alive

    
