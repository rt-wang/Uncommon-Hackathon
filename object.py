class Equipment:

    def __init__(self, oxygen_tank, knife, backpack) -> None:
        # Boolean var
        self._oxygen_tank = oxygen_tank
        self._knife = knife
        self._backpack = backpack


class Worm:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    
    def move_change_loc(self, x_change, y_change):
        self._x += x_change
        self._y += y_change