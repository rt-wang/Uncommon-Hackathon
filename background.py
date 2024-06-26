from pyxel import *
class Tilemap:
    def __init__(self, relative=True, size=32, colkey=0):
        self.x = 0
        self.y = 0
        self.relative = relative
        self.size = size
        self.ss = size ** 2
        self.colkey = colkey
        self.scroll_x = 0
        self.scroll_y = 0
        self.scroll_border_rightx = size * .75
        self.scroll_border_leftx = size * .25
        self.scroll_border_upy = size * .75
        self.scroll_border_downy = size * .25

    def get(self, tm, x, y):
        return tilemap(tm).pget(self.x * self.size + x, self.y * self.size + y)

    def set(self, tm, x, y, data):
        return tilemap(tm).pset(self.x * self.size + x, self.y * self.size + y, data)
    
    def draw(self, tm, colkey=3):
        camera(self.scroll_x*8, self.scroll_y*8)
        bltm(0, 0, tm, self.x * self.ss, self.y * self.ss, self.ss, self.ss, self.colkey)

    def x_scroll(self, player_x, player_x_speed):
        player_x += player_x_speed
        if player_x_speed > 0 and player_x - self.scroll_x > self.scroll_border_rightx:
            self.scroll_x += player_x_speed
            return player_x
        elif player_x_speed < 0 and player_x - self.scroll_x < self.scroll_border_leftx:
            self.scroll_x += player_x_speed
            return player_x
        return player_x
    
    def y_scroll(self, player_y, player_y_speed):
        player_y += player_y_speed
        if player_y_speed > 0 and player_y - self.scroll_y > self.scroll_border_upy:
            self.scroll_y += player_y_speed
            return player_y
        elif player_y_speed < 0 and player_y - self.scroll_y < self.scroll_border_downy:
            self.scroll_y += player_y_speed
            return player_y
        return player_y


def sprite(x, y, n, m=0, size=8, colkey=0):
    blt(x * size, y * size, 0, n * size, m * size, size, size, colkey) # redraws sprite at new location


def sprite(x, y, n, m, size=8, colkey=3, flip = False):
    if not flip:
        blt(x * size, y * size, 0, n * size, m * size, -size*2, size*2, colkey) # redraws sprite at new location
    else:
        blt(x * size, y * size, 0, n * size, m * size, size*2, size*2, colkey) # redraws sprite at new location

def sprite_2(x, y, n, m, size = 8, colkey=3, flip = False):
    if not flip:
        blt(x * size, y * size, 0, n , m, 22, 16, colkey) # redraws sprite at new location
    else:
        blt(x * size, y * size, 0, n , m, -22, 16, colkey)


def mouse_tile_pos(tile_size=8, screen_size=64):
    return floor(mouse_x * size / screen_size), floor(mouse_y * size / screen_size)

