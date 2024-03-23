from typing import Any
from object import Equipment

class Player:
    # The player class

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
        self._health = 5
        self._oxygen = 5
        self._food = 0
        self._equipment = Equipment() # Contain knife, backpack, and oxygen_tank
        

    def move_change_loc(self, x_change, y_change):
        # Update the player location by specifying the change of (x, y)
        self._x += x_change
        self._y += y_change


    def pickup_tool(self, tool):
        """
        Pick up a tool and update it in the character. If the player has a 
        backpack, tools can be picked up. 
        Otherwise, no action unless the tool is a knife.

        tool[str]: name of the tool
        """
        if self._equipment._backpack:
            if tool == "knife":
                self._equipment._knife = True
        elif self._equipment._backpack and tool == "knife":
            self._equipment._knife = True
