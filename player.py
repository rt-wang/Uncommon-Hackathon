class Player:

    def __init__(self) -> None:
        _health = 5
        _oxygen = 5
        _food = 0
        _x = 0
        _y = 0

    def set_health(self, newHealth):
        _health = newHealth

    def set_oxygen(self, newOxygen):
        _oxygen = newOxygen
    
    def set_food(self, newFood):
        _food = newFood

    def move_change_loc(self, x_change, y_change):
        # Update the player location by specifying the change of (x, y)
        _x += _x + x_change
        _y += _y + y_change
    
    def set_loc(self, new_x, new_y):
        # Set the player location to a new coordinate (new_x, new_y)
        _x, _y = (new_x, new_y)
