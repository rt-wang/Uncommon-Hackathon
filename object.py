from pyxel import *

class Equipment:

    def __init__(self, name, x, y) -> None:
        self._name = name # string specify the name of the tool
        self._x = x
        self._y = y

class Worm:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    
    def move_change_loc(self, x_change, y_change):
        self._x += x_change
        self._y += y_change

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