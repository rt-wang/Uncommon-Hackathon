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
        self._equipment = Equipment() # Contain knife, backpack, and oxygen_tank
        

    # Update the player location by specifying the change of (x, y)
    def move_change_loc(self, x_change, y_change):
        self._x += x_change
        self._y += y_change


    def pickup_tool(self, tool) -> None:
        """
        Pick up a tool and update it in the character. If the player has a 
        backpack, tools can be picked up. 
        Otherwise, no action unless the tool is a knife.

        tool[str]: name of the tool, one of these: "knife, backpack, oxygen_tank"
        """
        assert tool == "knife" or tool == "backpack" or tool == "oxygen_tank"

        if self._equipment._backpack:
            if tool == "knife":
                self._equipment._knife = True
            elif tool == "backpack":
                self._equipment._backpack = True
            else:
                self._equipment._oxygen_tank = True
        elif self._equipment._backpack and tool == "knife":
            self._equipment._knife = True

    
    # Check if the player is alive. If so, return True, and False otherwise.
    def is_alive(self) -> bool:
        if self._health > 0 and self._oxygen > 0 and self._food > 0:
            return True
        else:
            return False
