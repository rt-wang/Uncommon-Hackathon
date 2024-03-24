from typing import Any
from object import Equipment, Worm

class Player:

    def __init__(self, x = 0, y = 0, health = 3, oxygen = 5, food = True) -> None:
        """
        health[int]: 0 is death, and higher value coresponds to more health.
        oxygen[int]
        food[int]
        tools[List]: a list of Equipment objects
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
            else:
                if tool._name == "knife":
                    self._tools.append(tool)

    
    # Check if the player is alive. If so, return True, and False otherwise.
    def is_alive(self) -> bool:
        if self._health > 0:
            return True
        else:
            return False


    # Return the list of tool names
    def tool_names(self) -> list:
        lst = [tool._name for tool in self._tools]
        return lst

    # Encounter an object
    def run_into_obj(self, obj):
        if self._x == obj._x and self._y == obj._y:
            return True
        return False

    
    # Encounter a worm
    def encounter_worm(self, worm):
        return self.run_into_obj(worm)
    