from typing import Any
from object import Equipment

class Player:

    def __init__(self, x, y, health, oxygen, food) -> None:
        """
        health[int]: 0 is death, and higher value coresponds to more health.
        oxygen[int]
        food[int]
        """
        self._x = x
        self._y = y
        self._health = health
        self._oxygen = oxygen
        self._food = food
        self._tools = []
        

    # Update the player location by specifying the change of (x, y)
    def move_change_loc(self, x_change, y_change):
        self._x += x_change
        self._y += y_change


    def set_tool(self, tool) -> None:
        """
        Pick up a tool and update it in the character. If the player has a 
        backpack, tools can be picked up. 
        Otherwise, no action unless the tool is a knife.

        tool[Equipment]
        """
        assert isinstance(tool, Equipment)

        for each in self._tools:
            if each.name == "backpack":
                self.tools.append(tool)
        if self.tool.name == "knife":
            self._tools.append(tool)

    
    # Check if the player is alive. If so, return True, and False otherwise.
    def is_alive(self) -> bool:
        if self._health > 0 and self._oxygen > 0 and self._food > 0:
            return True
        else:
            return False
