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

    def set_life(self, is_alive):
        self._life = is_alive