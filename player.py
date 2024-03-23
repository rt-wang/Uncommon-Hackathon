class Player:
    # The player class

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
        self._health = 5
        self._oxygen = 5
        self._food = 0
        self._equipment = Equipment()
        

    def move_change_loc(self, x_change, y_change):
        # Update the player location by specifying the change of (x, y)
        self._x += x_change
        self._y += y_change

    def has_oxygen_tank(self, oxygen_tank):
        if oxygen_tank:
            self._oxygen = 5