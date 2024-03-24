from pyxel import *
import math, random

class Equipment:

    def __init__(self, name, x=0, y=0, u=0, v=0) -> None:
        self._name = name # string specify the name of the tool
        self._x = x
        self._y = y
        self.u = u 
        self.v = v

class Worm:
    def __init__(self, life = True) -> None:
        self._x = random.randint(0, 256)
        self._y = random.randint(0, 256)
        self._life = life
        self._chase = False # If chase, run chase() and stop move(); otherwise, run move()
        self.safeHouses = [(4,2), (28, 4), (49, 4), (50, 19), (26, 19), (2, 19), (3, 43), (43, 15), (61, 51)]
    
    #def move_change_loc(self, x_change, y_change):
       # self._x += x_change
        # self._y += y_change

    def close_to_player(self, player) -> bool:
        if (self._x - player._x) < 200 or (self._y - player._y) < 200:
            return True
        return False
    
    def encounter_player(self, player, face_left, attack):
        x_diff = player._x*8 - self._x
        y_diff = player._y*8 - self._y

        if ((0 <= x_diff <= 20) and abs(y_diff) <= 10):
            if face_left and attack:
                self._life = False
            elif abs(x_diff) <= 5 and abs(y_diff) <=5:
                return (True, -1)
            return (True, 0)
        elif ((0 >= x_diff >= - 20) and abs(y_diff) <= 10):
            if (not face_left) and attack:
                self._life = False
            elif abs(x_diff) <= 5 and abs(y_diff) <=5:
                return (True, -1)
            return (True, 0)

        else:
            return (False, 0 )
                

    # def move(self):
    #     # Generate a pair of random number (a, b) where a, b \in {0, 1}.
    #     # For a: 0 - horizontal walk; 1 - vertical walk
    #     # For b: 0 - -1 step; 1: 1 step
    #     a, b = (random.randint(0, 1), random.randint(0, 1))
    #     if a == 0:
    #         if b == 0:
    #             self.move_change_loc(0, 3)
    #         else:
    #             self.move_change_loc(0, -3)
    #     else:
    #         if b == 0:
    #             self.move_change_loc(3, 0)
    #         else:
    #             self.move_change_loc(-3, 0)
    
    def draw(self):
        blt(self._x, self._y, 1, 0, 8, 16, 8, colkey=3)
    
    def chase(self, player):
        x_diff = player._x*8 - self._x
        y_diff = player._y*8 - self._y
        if x_diff != 0:
            if abs(x_diff) >= 8:
                self._x += 8 if x_diff > 0 else -8
            else:
                self._x += 2 if x_diff > 0 else -2

        if y_diff != 0:
            if abs(y_diff) >= 8:
                self._y += 8 if y_diff > 0 else -8
            else:
                self._y += 2 if y_diff > 0 else -2


class Safe: 
    def __init__(self, name, x, y, text) -> None:
        self._name = name
        self._x = x
        self._y = y
        self._text = text        
            
            
    def set_life(self, is_alive):
        self._life = is_alive

    
