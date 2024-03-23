from pyxel import *
from pyxlib import *
init(64, 64, fps=3)
load('my_resource.pyxres')

tm = Tilemap()
x = 1
y = 1
while True:
    px = x
    py = y
    pl = (x//8, y//8)
    cls(0)
    if btn(KEY_RIGHT):
        x += 1
    elif btn(KEY_LEFT):
        x -= 1
    elif btn(KEY_UP):
        y -= 1
    elif btn(KEY_DOWN):
        y += 1
    if tm.get(0, x%8, y%8) == (0, 1) and (x//8, y//8) == pl:
        x = px 
        y = py 
    elif tm.get(0, x%8, y%8) == (1, 1):
        x = 1
        y = 1
    tm.x = x//8
    tm.y = y//8
    sprite(x%8, y%8, 1, 0)
    tm.draw(0)
    flip()

#sdfsd
