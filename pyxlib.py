from pyxel import *
from math import floor


class Tilemap:
    def __init__(self, relative=True, size=8, colkey=0):
        self.x = 0
        self.y = 0
        self.relative = relative
        self.size = size
        self.ss = size ** 2
        self.colkey = colkey

    def get(self, tm, x, y):
        return tilemap(tm).pget(self.x * self.size + x, self.y * self.size + y)

    def set(self, tm, x, y, data):
        return tilemap(tm).pset(self.x * self.size + x, self.y * self.size + y,
                               data)

    def draw(self, tm, colkey=0):
        bltm(0, 0, tm, self.x * self.ss, self.y * self.ss, self.ss, self.ss, self.colkey)


def sprite(x, y, n, m=0, size=8, colkey=0):
    blt(x * size, y * size, 0, n * size, m * size, size, size, colkey)


def mouse_tile_pos(tile_size=8, screen_size=64):
    return floor(mouse_x * size / screen_size), floor(mouse_y * size / screen_size)
